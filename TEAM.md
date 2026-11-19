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
