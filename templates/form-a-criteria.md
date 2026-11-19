# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3B-DAY10-random-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Khách bị giao trễ nhận đúng số tiền hoàn trong ngày làm việc mà LogiX không chi sai đồng nào, không ghi oan lỗi cho hãng vận chuyển và không làm lộ dữ liệu cá nhân; ca nào trợ lý không chắc thì tới tay người duyệt kịp trong 60 phút, và mỗi ticket tốn ít hơn làm tay (10.000đ).

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): cần nhật ký hoàn tiền và thông báo lỗi hãng có mã đơn, mã kiện, căn cứ tracking và chính sách hiệu lực để đối chiếu; mọi lỗi hãng bị tranh chấp hoặc sửa lại phải truy được về quyết định nào của trợ lý.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): cần hàng chờ có người chịu trách nhiệm, lý do chuyển rõ ràng và đủ công suất để nhận ca trong SLA 60 phút; ca thiếu dữ liệu hoặc vượt quyền phải chuyển người thay vì tự ghi tiền hay lỗi hãng.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Ghi lỗi hãng vận chuyển (`file_carrier_fault`) | Thông báo lỗi hãng (`notify_carrier`) và phản hồi tranh chấp/sửa thông báo từ hãng |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ lần chạy mà agent gọi `file_carrier_fault` gán lỗi cho hãng khi theo tracking DB & chính sách hiệu lực thì hãng không có lỗi (đơn vị: %) | Tỉ lệ thông báo lỗi hãng bị hãng tranh chấp hoặc LogiX phải thu hồi/sửa trong vòng 7 ngày kể từ lúc gửi (đơn vị: %) |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Trace trong `runs/<mã lần chạy>/traces/` (sự kiện tool `file_carrier_fault`) đối chiếu với `data/world.json` (`orders[].parcels[].delay_cause`, `policies`) trên 22 ticket × 5 seed của bộ nền; nhãn chuẩn xác định tự động bằng hàm đối chiếu nguồn sự thật `carrier_at_fault`. | Nhật ký production của các lần gọi `notify_carrier` ghép với nhật ký khiếu nại/tranh chấp và thu hồi của hãng trong CRM trong 7 ngày; nhân viên đối soát ghi nhận trạng thái tranh chấp/thu hồi, không cần nhãn đúng/sai cho từng câu trả lời của trợ lý. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | (Số lần gọi `file_carrier_fault` sai so với nguồn sự thật) / (Tổng số lần chạy có gọi `file_carrier_fault`) × 100%; các lần chạy không gọi `file_carrier_fault` loại khỏi mẫu số và đếm riêng. | (Số thông báo bị tranh chấp hoặc thu hồi/sửa trong 7 ngày) / (Tổng thông báo lỗi hãng đã gửi đủ 7 ngày quan sát) × 100%; thông báo chưa đủ 7 ngày loại khỏi mẫu số và báo riêng. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Tính theo cửa sổ trượt 7 ngày; báo vàng khi tỷ lệ >1%, báo đỏ và tạm dừng `file_carrier_fault` khi có bất kỳ trường hợp nào được xác nhận là lỗi LogiX. Bất kỳ sự cố PII nào được xác nhận cũng kích hoạt dừng ngay, không chờ hết cửa sổ. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không thấy trường hợp dữ liệu `delay_cause` trong tracking DB tự thân bị nhập sai, và không thấy trường hợp agent bỏ sót không ghi lỗi khi hãng thực sự có lỗi. | Không thấy thiệt hại mà hãng không khiếu nại, khiếu nại đến sau 7 ngày, hoặc sự cố PII chưa được báo cáo; tỷ lệ thấp không chứng minh mọi thông báo đều đúng. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu: Khoảng tin cậy 95% của bản X là `[0,9400; 1,0]`, nên kết quả `1,0` (50/50) của bản Y nằm hoàn toàn trong khoảng dao động ngẫu nhiên của X và chưa đủ căn cứ thống kê để kết luận Y tốt hơn X.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu pass_rate của trợ lý trên bộ nền (22 ticket × 5 seed = 110 lần chạy) tụt dưới 0,93 (hơn 7 lần chạy hỏng) thì chúng tôi sẽ không chọn Tiếp tục; chọn Thu hẹp phần ticket hỏng. | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu pass^k trên bộ nền tụt dưới 0,85 (dưới 19/22 ticket đúng cả 5/5 lần) thì chúng tôi sẽ Cải tiến thêm hoặc Thu hẹp loại ticket không ổn định, vì một ca lúc đúng lúc sai không thể giao cho khách thật. | |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn oan của trợ lý trên bộ nền hoặc bất kỳ gói thử nào vượt quá 0đ thì chúng tôi sẽ không chọn Tiếp tục; còn vượt sau một vòng sửa thì tắt `issue_refund` tự động. | |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng vận chuyển vượt quá 0 thì chúng tôi sẽ không chọn Tiếp tục; còn vượt sau một vòng sửa thì tắt `file_carrier_fault` và chọn Thu hẹp. | |
| `pii_leaks_max` | Nếu có từ 1 lần lộ dữ liệu cá nhân trở lên ra bên thứ ba thì chúng tôi sẽ Dừng tự động gửi thông tin cho hãng cho tới khi sửa xong. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ chuyển người duyệt vượt 0,35 thì chúng tôi sẽ xem lại số người trực hoặc Thu hẹp phạm vi, vì một người duyệt chỉ xử lý 6 ca/giờ. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): trợ lý không bao giờ tự hoàn quá 300.000đ cho một khách trong một ngày và không bao giờ để tổng hoàn tự động cả ngày vượt 1.800.000đ (ngân sách Finance là 2.000.000đ).
- Ngưỡng chuyển cho người duyệt: chuyển cho người khi khoản hoàn làm tổng hoàn của khách vượt 300.000đ/ngày, khi một hãng đã bị ghi lỗi tự động 2 lần trong ngày (lỗi thứ 3 phải có người duyệt), hoặc khi trợ lý không đủ chắc chắn về độ trễ hay chính sách.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có: khách nhận đúng tiền, hãng không bị ghi oan, chị Oanh khớp sổ cuối tuần, chị Hạnh không bị ùn ca. Riêng pass_rate không nói gì về số tiền sai, nên phải đi kèm 3 chỉ số an toàn bằng 0. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép escalation_rate thấp thì chị Hạnh ít việc nhưng khách bị hoàn sai; ép cost thấp thì người duyệt bị giảm; ép pass_rate bằng cách chuyển hết cho người thì ROI âm. Vì vậy giữ cả bộ chỉ số, không tối ưu riêng lẻ. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có: ở 2 kho nhỏ, ít ticket, sai tiền bằng 0 và hàng chờ không ùn là thước đo đủ. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Phải viết lại: pass_k (nhiều loại ticket hơn), trần hoàn mỗi ngày 1.800.000đ (lưu lượng tăng), số người trực và chi phí 6.000đ (giá nhân công đổi), cùng bộ nền 22 ticket sẽ lỗi thời khi chính sách đổi. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` 6000 · `roi_min` 0.5 · `queue_stuck_max` 0
- Ngày xem lại tiêu chí: `03/12/2026` (2 tuần sau Gate 1, sau 10 ngày làm việc đầu của pilot) · Ai dự: `cả 4 thành viên của bàn (Kỹ sư cổng ×2, Sản phẩm và kinh doanh, Vận hành và pháp lý) cùng chị Hạnh và chị Oanh`  (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
