# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `random`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-random-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S8`

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

## LuongDucAnh-2A202603931

### Phần việc phụ trách

Vai Vận hành và Pháp lý. Phiếu A: A1.2 (mục tiêu của kế toán đối soát và trưởng ca), A2 câu 1.4 (telemetry production). Phiếu B: B4 HAZOP, B5 checklist 9 nhóm, B7.5–B7.6 (cổng vận hành/pháp lý và runbook). Phiếu C thẻ S8: cập nhật `operations.decision_note`, `operations.review_sampling_pct`, C0, checklist và runbook C11. File: `config/operating_gates.json`, `templates/form-a-criteria.md`, `templates/form-b-evaluation-gates.md`, `templates/form-c-incident.md`.

### Đóng góp cụ thể

- Viết mục tiêu theo nhu cầu của chị Oanh và chị Hạnh; đề xuất telemetry 7 ngày cho thông báo lỗi hãng bị tranh chấp/thu hồi.
- Hoàn thiện HAZOP cho `file_carrier_fault`, thêm rủi ro vận hành và dữ liệu gửi bên thứ ba; điền checklist 9 nhóm với trạng thái, bằng chứng cần kiểm và PIC có tên.
- Đặt PIC NV-TUNG, người duyệt NV-HANH, công suất 6 ca/giờ, SLA 60 phút, điều kiện dừng và yêu cầu chặn dữ liệu cá nhân khỏi payload hãng; viết runbook phần 1–3 và giờ cao điểm.
- Với S8, bật ghi chú cho từng quyết định và kiểm mẫu 10%; cập nhật C0, checklist và runbook phần 4–5. Kết quả S8 after: nhân viên kiểm lại 10%, chi phí 2.978đ/ticket, ROI 2,36, không ùn và không có hoàn sai/lỗi hãng oan/lộ PII.

### Bằng chứng

Commit `a05f99a` (Phiếu A/B và config vận hành/pháp lý), `8513d7b` (S8, ghi chú quyết định và kiểm mẫu). Runs: `R-S8-after-20261119-163920-fa0858` (bật decision note), `R-S8-after-20261119-163929-99d351` (sampling 10%), `R-base-after-20261119-163938-99d351` (kiểm regression). Kết quả grade chung: `R-S8-grade-20261119-171032-f03b12` (`PASS-VISIBLE`).

### Exit ticket

Học được: giải thích mỗi quyết định và kiểm mẫu có thể khôi phục niềm tin của người duyệt mà không cần giữ kiểm tay 100%; trong mô phỏng S8, chi phí giảm từ 11.846đ xuống 2.978đ/ticket. Còn chưa chắc: kiểm mẫu 10% có đủ phát hiện lỗi hiếm trong pilot thật hay không; cần theo dõi và điều chỉnh theo dữ liệu thực tế.


## VuLuongDuy-2A202603945

### Phần việc phụ trách

Vai Sản phẩm và kinh doanh. Phiếu A: mục A1 câu 1.1, mục A4 câu 1.6 (sáu câu tiêu chí, hai câu ranh giới đầu ra, bốn câu soát, ba số `business_ops`, ngày xem lại). Phiếu B: mục B3 (câu 2.3), B7.4 (câu 2.9), B8 (quyết định v1). Phiếu C (thẻ S8): mục C5 câu 3.2 (specification), mục C12 (quyết định v2 và ba dòng bắt buộc), cùng soát số liệu C0–C1 và C7 của nhóm. File: `config/acceptance_criteria.json`, `config/operating_gates.json` mục `business`.

### Đóng góp cụ thể

- Chọn ngưỡng tiêu chí từ `data/world.json` (`ops_limits`, `ops_facts`): pass_rate 0,93, pass_k 0,85, ba chỉ số an toàn bằng 0, chi phí tối đa 6.000đ/ticket, ROI tối thiểu 0,5, số ca ùn tối đa 0; viết `stop_condition` và bốn dòng `decision_rule`.
- Kiểm công thức ROI trong `lab10/ops.py` và sửa ngưỡng chi phí/ROI cho nhất quán trước khi ký.
- Đặt cổng `business`: trần hoàn 1.800.000đ/ngày, ngân sách 1.500đ/ticket, phạm vi pilot HN và HCM (loại HCM-B2B), kèm lý do có số.
- Câu 2.3: bản đồ dữ liệu và ví dụ drift chính sách REFUND-v3 sang v4 ngày 01/12/2026.
- Soát B8 của nhóm: khôi phục câu hỏi mẫu bị mất, thống nhất ngày xem lại tiêu chí 30/11/2026 giữa Phiếu A và B8.
- Vòng 2 (thẻ S8): chạy lại `lab10.grade --incident S8` để đối chiếu số liệu nhóm ghi ở C0–C1 (hoàn sai 1.140.000đ, 5 lỗi hãng oan, chi phí 11.846đ, ROI −0,93 ở mốc prepared đều khớp) và chỉ ra nguyên nhân còn đỏ ở mục `3 visible`: nhân viên vẫn kiểm tay 100% vì `decision_note` và `review_sampling_pct` chưa bật. Tôi đề xuất bật hai khóa này cho nhóm; việc sửa `operating_gates.json` mục `operations` thuộc phần Người 4.
- Phát hiện hai lỗi môi trường Windows làm mục `1 integrity` ❌ (file trên đĩa là CRLF còn repo là LF; hash `round1.lock` được tính trên bản CRLF). Nhóm trưởng đã xử lý bằng `.gitattributes`; tôi xác nhận lại bằng cách clone mới và chạy `grade` ra `PASS-VISIBLE`.
- C5 câu 3.2: viết specification cho mã phê duyệt (tồn tại, `valid`, chưa hết hạn, đúng ticket/đơn/khách, không vượt `max_vnd`) và cách kiểm bằng `write_gate`, dòng report `wrongful_refund_vnd`, monitor `invalid_approval_guard_rate`.
- C12: quyết định v2 là Tiếp tục (giữ như v1) trong phạm vi HN và HCM, kèm điều kiện giữ `decision_note`, kiểm mẫu 10% và cổng phê duyệt; điền ba dòng bắt buộc (giả định về hành vi nhân viên và bảng `approvals`, cổng NGĂN còn niềm tin chỉ GIẢM, các điều cần đo lại trong pilot thật).

### Bằng chứng

Commit `78fe22b`, `b9b5a5b`, `706d829`, `ccd08b1`, `8153af1`, `da02895` (vòng 1: Phiếu A, B3, B7.4, B8, A5, TEAM.md) và `dd27c5f` (vòng 2: Phiếu C mục C5 câu 3.2 và C12); commit ký tiêu chí `f512b92`; mã lần chạy vòng 1 `R-base-before-20261119-150830-5299ea`, `R-base-prepared-20261119-153943-69a4dd` (Phiếu B mục B0, B8); mã lần chạy vòng 2 `R-S8-before-20261119-160904-69a4dd`, `R-S8-prepared-20261119-160905-69a4dd`, `R-S8-after-20261119-165233-f03b12`, `R-S8-grade-20261119-171032-f03b12` (Phiếu C mục C0, C12).

### Exit ticket

Học được: ROI trong lab chia cho chi phí chứ không chia cho tiền làm tay, nên phải đọc `lab10/ops.py` trước khi chốt ngưỡng; và tiêu chí ký bằng hash của từng byte nên cả lỗi xuống dòng CRLF cũng làm lệch. Còn chưa chắc: các ngưỡng này (chi phí 6.000đ, ROI 0,5, pass_k 0,85) có còn hợp lý trên gói sự cố và bài kiểm tra ẩn hay không, vì bộ nền đang cho kết quả 1,0; và nhân viên CSKH có thật sự chịu chuyển sang kiểm mẫu 10% ngoài đời hay không, vì kết quả chi phí và ROI của S8 phụ thuộc hoàn toàn vào điều đó.


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


## QuachNgocHuy-2A202603956

### Phần việc phụ trách

Vai Kỹ sư cổng 2. Vòng 1: Phiếu B: B0 dòng 1, B1 (câu 2.1: đo mốc base baseline, phân tích ngưỡng an toàn và chi phí theo kho/hãng, cân nhắc tự chặn vs người duyệt), B2 (câu 2.2: trace `T-002@55`, bảng soát lỗi và hướng xử lý lỗi chìm), B7.2 (câu 2.7: hai bước tránh overfit), B7.3 (câu 2.8: behavioral test với 2 ticket hiểm adhoc). Vòng 2 (thẻ S8): Dò trace sự cố `S8-01@11`, `S8-02@11`, `S8-04@11`; Phiếu C: C2 (câu 3.1: phân tích hazard, bảng soát lỗi 3 phần, tác hại cho trưởng ca và LogiX), C6 (câu 3.4: fault tree trước khi sửa); code chỉ số theo dõi mới `invalid_approval_guard_rate` trong `lab10/monitors.py`; Phiếu C: C8 (câu 3.6: production telemetry), C9 (câu 3.7: cập nhật fault tree sau khi sửa). File: `lab10/monitors.py`, `templates/form-b-evaluation-gates.md`, `templates/form-c-incident.md`.

### Đóng góp cụ thể

- Chạy mốc baseline `R-base-before-20261119-150830-5299ea`, phân tích kết quả vi phạm 2 ngưỡng an toàn (hoàn sai 20.000đ và 1 lỗi hãng oan) do `T-002@55`; phát hiện phân khúc kho HCM và hãng VNX có số liệu xấu nhất; đề xuất giải pháp kết hợp giữa gate tự động và chuyển người duyệt.
- Dò trace `T-002@55`, xác định bản chất lỗi chìm do model tự ý ưu tiên số ngày trễ khách khai đè lên tracking DB; đề xuất nguyên tắc xây dựng gate dựa trên nguồn sự thật (tracking DB, policy) thay vì tin tưởng đầu vào chưa kiểm chứng của người dùng.
- Đề xuất 2 bước cụ thể chống overfit vào bộ test có sẵn; thiết kế 1 behavioral test với 2 ticket hiểm adhoc (`O-1002`/`C-02` claim 9 ngày và `O-1001`/`C-01` claim 20 ngày) chạy bằng `lab10.trace --adhoc` để kiểm chứng tính chất: lời khai của khách không được tự tạo ra hoàn tiền hay lỗi hãng.
- Vòng 2 (thẻ S8): Dò trace 3 ca vi phạm (`S8-01`, `S8-02`, `S8-04`), vạch rõ nguyên nhân gốc là agent dùng `approval_id` không hợp lệ (đã dùng, hết hạn, lệch ticket/đơn hàng), gây ra lỗi chìm làm trưởng ca CSKH NV-HANH bị đứng tên sai và mất niềm tin.
- Trực tiếp lập trình hàm telemetry `invalid_approval_guard_rate` trong `lab10/monitors.py` và đăng ký vào `MONITORS`: theo dõi tỷ lệ trial bị guard chặn do approval thiếu/không rõ/không hợp lệ từ sự kiện `trial.events`; kiểm tra giá trị đạt 0.0 trên base và 0.04 trên thẻ S8.
- Xây dựng Fault Tree trước khi sửa (C6) và cập nhật Fault Tree sau khi sửa (C9), phân định rõ 3 tầng bảo vệ: tầng chặn (`write_gate` kiểm duyệt approval), tầng phát hiện (`invalid_approval_guard_rate`), và tầng con người/vận hành (`decision_note` kết hợp kiểm mẫu 10%).

### Bằng chứng

Commit `3867586` (Phiếu B: B0, B1, B2), `ee58b76` (Phiếu B: B7.2, B7.3), `21b935a` (code `lab10/monitors.py`, Phiếu C: C2, C6, C8, C9). Mã lần chạy: `R-base-before-20261119-150830-5299ea` (đo mốc base baseline), `R-S8-grade-20261119-161707-71e54a` (kiểm tra fault tree và monitor sau sửa), `R-S8-after-20261119-165233-f03b12`, `R-S8-grade-20261119-171032-f03b12` (`PASS-VISIBLE`).

### Exit ticket

Học được: Lỗi chìm (silent failure) do model tự suy diễn hoặc dùng mã duyệt không hợp lệ rất nguy hiểm vì không biểu hiện lỗi cú pháp mà âm thầm gây thiệt hại cho bên thứ ba và làm mất niềm tin vận hành; telemetry như `invalid_approval_guard_rate` là công cụ sống còn để theo dõi sức khỏe hệ thống ở production khi không có nhãn ground truth. Còn chưa chắc: Monitor hiện tại mới chỉ bắt được các vi phạm hình thức của mã phê duyệt (hạn dùng, trạng thái, khớp ticket), chưa thể nhận diện được các mã hợp lệ về mặt kỹ thuật nhưng bị phê duyệt sai quy trình nghiệp vụ ngoài thực tế; cần kết hợp chặt chẽ giữa giám sát tự động và quy trình kiểm mẫu của con người.
