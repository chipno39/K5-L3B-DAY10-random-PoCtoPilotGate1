# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `random`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-random-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Xuân Đạt | 2A202603958 | Kỹ sư cổng | x |
|   2 | Lương Đức Anh | 2A202603931 | Vận hành & Pháp lý | |
|   3 | Vũ Lương Duy | 2A202603945 | Sản phẩm và kinh doanh |             |
|   4 | Quách Ngọc Huy | 2A202603956 | Kỹ sư cổng |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.


## VuLuongDuy-2A202603945

### Phần việc phụ trách

Vai Sản phẩm và kinh doanh. Phiếu A: mục A1 câu 1.1, mục A4 câu 1.6 (sáu câu tiêu chí, hai câu ranh giới đầu ra, bốn câu soát, ba số `business_ops`, ngày xem lại). Phiếu B: mục B3 (câu 2.3), B7.4 (câu 2.9), B8 (quyết định v1). File: `config/acceptance_criteria.json`, `config/operating_gates.json` mục `business`.

### Đóng góp cụ thể

- Chọn ngưỡng tiêu chí từ `data/world.json` (`ops_limits`, `ops_facts`): pass_rate 0,93, pass_k 0,85, ba chỉ số an toàn bằng 0, chi phí tối đa 6.000đ/ticket, ROI tối thiểu 0,5, số ca ùn tối đa 0; viết `stop_condition` và bốn dòng `decision_rule`.
- Kiểm công thức ROI trong `lab10/ops.py` và sửa ngưỡng chi phí/ROI cho nhất quán trước khi ký.
- Đặt cổng `business`: trần hoàn 1.800.000đ/ngày, ngân sách 1.500đ/ticket, phạm vi pilot HN và HCM (loại HCM-B2B), kèm lý do có số.
- Câu 2.3: bản đồ dữ liệu và ví dụ drift chính sách REFUND-v3 sang v4 ngày 01/12/2026.
- Soát B8 của nhóm: khôi phục câu hỏi mẫu bị mất, thống nhất ngày xem lại tiêu chí 30/11/2026 giữa Phiếu A và B8.

### Bằng chứng

Commit `78fe22b`, `b9b5a5b`, `706d829`, `ccd08b1`, `8153af1`; commit ký tiêu chí `f512b92`; mã lần chạy `R-base-before-20261119-150830-5299ea`, `R-base-prepared-20261119-153943-69a4dd` (Phiếu B mục B0, B8).

### Exit ticket

Học được: ROI trong lab chia cho chi phí chứ không chia cho tiền làm tay, nên phải đọc `lab10/ops.py` trước khi chốt ngưỡng; và tiêu chí ký bằng hash của từng byte nên cả lỗi xuống dòng CRLF cũng làm lệch. Còn chưa chắc: các ngưỡng này (chi phí 6.000đ, ROI 0,5, pass_k 0,85) có còn hợp lý trên gói sự cố và bài kiểm tra ẩn hay không, vì bộ nền đang cho kết quả 1,0.


## NguyenXuanDat-2A202603958

### Phần việc phụ trách

Vai Trưởng nhóm và Kỹ sư cổng 1. Quản lý fork repo, cấu hình Git và `.gitattributes` (chuẩn LF cho file khoá hash); chạy lệnh ký tiêu chí (`lab10.criteria sign`), chốt cổng vòng 1 (`lab10.checkpoint`), fetch và nhận thẻ sự cố `S8`, chạy kiểm tra `lab10.grade`. Phiếu A: A2 câu 1.3 (cột Offline), A3 câu 1.5; Phiếu B: B0 dòng 2–3, B6, B7.1, B8 (cột v1); Phiếu C: C0 dòng 1–2 & 7, C1, C7. File code chính: `lab10/guards.py`.

### Đóng góp cụ thể

- Thiết lập repo nhóm `K5-L3B-DAY10-random-PoCtoPilotGate1`, thêm `.gitattributes` để bảo toàn byte LF cho tiêu chí ký và toàn bộ file khoá trong `MANIFEST.json` trên Windows.
- Code 3 cổng phòng ngừa Vòng 1 trong `lab10/guards.py`: `pre_guard` ghim phiên bản chính sách hiệu lực theo `ctx.as_of`; `write_gate` kiểm tra quyền lợi từ tracking DB (`H.entitlement_vnd`), kiểm tra trần hoàn tự động ngày (`daily_refund_cap_vnd`), và kiểm tra điều kiện quy lỗi hãng (`H.carrier_at_fault`).
- Chốt cổng Vòng 1 (`lab10.checkpoint`, hash `298b9e9d`) đưa bộ nền lên `1.0` ở cả `pass_rate` và `pass_k`, loại bỏ hoàn toàn 20.000đ hoàn sai và 1 lỗi hãng oan ở `T-002@55`.
- Code cổng Vòng 2 (thẻ `S8`) trong `lab10/guards.py`: xác thực toàn diện `approval_id` khi khoản hoàn vượt `auto_limit_vnd` (`status == "valid"`, `expires_at >= ctx.as_of`, khớp `ticket_id`/`order_id`/`customer_id`, `amount_vnd <= max_vnd`), đưa hoàn sai từ 1.140.000đ và lỗi hãng oan từ 5 về 0.

### Bằng chứng

Commit `4f4ba40`, `2052b90`, `f512b92` (Sign acceptance criteria), `e0c2401`, `1e09be0`, `ba96697` (chốt vòng 1), `50b3578` (Nhận thẻ S8), `6082a12`, `c29cb1e`. Mã lần chạy: `R-base-after-20261119-151709-4475da`, `R-base-prepared-20261119-153943-69a4dd`, `R-S8-after-20261119-161239-4fcc2b`, `R-S8-after-20261119-165233-f03b12`, `R-S8-grade-20261119-165234-f03b12` (`PASS-VISIBLE`).

### Exit ticket

Học được: các cổng phòng ngừa ngoài model/prompt dựa trên nguồn sự thật (`tracking`, `policies`, `approvals`) ngăn được lỗi chìm không đảo ngược hiệu quả hơn việc sửa prompt, nhưng an toàn kỹ thuật mới là điều kiện cần — sự cố `S8` cho thấy nếu thiếu giải thích quyết định và quy trình kiểm mẫu để hiệu chỉnh lòng tin thì con người sẽ kiểm tay 100% và làm chi phí vượt làm tay. Còn chưa chắc: tỷ lệ kiểm mẫu 10% hiện tại có đủ để bắt kịp các lỗi cấp phê duyệt hợp lệ về mặt hình thức nhưng sai nghiệp vụ ở quy mô nhiều depot hay không.
