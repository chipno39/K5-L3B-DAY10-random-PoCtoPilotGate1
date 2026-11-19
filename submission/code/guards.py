"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _resolve_truth(ctx, action):
    order_id = action.get("order_id") or ctx.ticket.get("order_id")
    order = ctx.tools.lookup_order(order_id) if order_id else None
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if not order or not pol:
        return None, None, pol, 0
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay_days = H.db_delay_days(parcel, ctx.as_of)
    return order, parcel, pol, delay_days


def pre_guard(ctx):
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if pol:
        ctx.log("guard_pin_policy", policy_id=pol["policy_id"])
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool == "issue_refund":
        order, parcel, pol, delay_days = _resolve_truth(ctx, action)
        if order and parcel and pol:
            entitled = H.entitlement_vnd(pol, order, delay_days, parcel.get("delay_cause"))
            amt = action.get("amount_vnd", 0)
            if entitled <= 0 and amt > 0:
                ctx.log("guard_deny_wrongful_refund", amount_vnd=amt, db_delay_days=delay_days)
                return Verdict.deny("tracking DB và chính sách không cho phép hoàn tiền")
            if amt > entitled:
                ctx.log("guard_modify_refund_to_entitlement", asked=amt, entitled=entitled)
                return Verdict.modify("chỉnh số tiền hoàn về đúng quyền lợi theo tracking DB", amount_vnd=entitled)
        cap = (ctx.gates or {}).get("business", {}).get("daily_refund_cap_vnd")
        if cap is not None and ctx.tools.auto_refund_today_vnd() + action.get("amount_vnd", 0) > cap:
            ctx.log("guard_escalate_daily_cap", cap_vnd=cap)
            return Verdict.escalate("vượt trần hoàn tự động trong ngày, chuyển người duyệt")

        # Vòng 2 (S8): kiểm tra tính hợp lệ của mã phê duyệt khi vượt auto_limit_vnd
        amt = action.get("amount_vnd", 0)
        if pol and amt > pol.get("auto_limit_vnd", 0):
            app_id = action.get("approval_id")
            if not app_id:
                ctx.log("guard_escalate_missing_approval", amount_vnd=amt)
                return Verdict.escalate("khoản hoàn vượt hạn mức tự động nhưng thiếu mã phê duyệt")
            matches = ctx.tools.lookup_approvals(approval_id=app_id)
            if not matches:
                ctx.log("guard_escalate_unknown_approval", approval_id=app_id)
                return Verdict.escalate("mã phê duyệt không tồn tại trong hệ thống")
            app = matches[0]
            order_id = action.get("order_id") or ctx.ticket.get("order_id")
            if (
                app.get("status") != "valid"
                or app.get("expires_at", "") < ctx.as_of
                or app.get("ticket_id") != ctx.ticket.get("ticket_id")
                or app.get("order_id") != order_id
                or app.get("customer_id") != ctx.ticket.get("customer_id")
                or amt > app.get("max_vnd", 0)
            ):
                ctx.log("guard_escalate_invalid_approval", approval_id=app_id, status=app.get("status"), expires_at=app.get("expires_at"), max_vnd=app.get("max_vnd"))
                return Verdict.escalate("mã phê duyệt không hợp lệ (hết hạn/thu hồi/đã dùng/sai đối tượng/vượt hạn mức duyệt)")

    if tool == "file_carrier_fault":
        order, parcel, pol, delay_days = _resolve_truth(ctx, action)
        if order and parcel and pol and not H.carrier_at_fault(pol, parcel, delay_days):
            ctx.log("guard_deny_wrongful_carrier_fault", db_delay_days=delay_days, delay_cause=parcel.get("delay_cause"))
            return Verdict.deny("tracking DB không đủ điều kiện ghi lỗi hãng theo chính sách")

    return Verdict.allow()
