# HW06 – Kiểm thử API

## 1. Thông tin chung

| **Mã bài tập** | **HW06-AI** |
| --- | --- |
| **Thời lượng** | 10 giờ |
| **Hạn nộp** | Vui lòng xem liên kết nộp bài trên Moodle |
| **Hình thức** | Bài tập cá nhân |
| **Nơi nộp** | Moodle (báo cáo) |
| **Giảng viên & Trợ giảng** | TS. Lâm Quang Vũ / TS. Trần Duy Hoàng / ThS. Trần Thị Bích Hạnh / ThS. Trương Phước Lộc / ThS. Hồ Tuấn Thanh |
| **Liên hệ** | lqvu@fit.hcmus.edu.vn / tdhoang@fit.hcmus.edu.vn / ttbhanh@fit.hcmus.edu.vn / tploc@fit.hcmus.edu.vn / hthanh@fit.hcmus.edu.vn |
| **Chính sách AI** | Mở — **bắt buộc** phải có bản khai báo và đính kèm Báo cáo kiểm toán AI |
| **Mức Bloom-AI yêu cầu** | G9.1 → G9.6, tùy theo bài tập (xem phần *Ánh xạ CLO*) |

## 2. Nguyên tắc định hướng

Các nguyên tắc này quy định cách bạn được kỳ vọng làm việc xuyên suốt chuỗi bài tập của học phần. Hãy đọc kỹ trước khi bắt đầu vì bài nộp của bạn sẽ được đánh giá dựa trên các nguyên tắc này.

- **Chiến lược AI-First.** Bạn được yêu cầu áp dụng AI vào các kỹ thuật kiểm thử đã học trên lớp. Tuy nhiên, điều này không có nghĩa là chỉ đưa ra một câu lệnh chung chung như *"hãy tạo tất cả ca kiểm thử API từ đặc tả và chạy chúng"*. Thay vào đó, bạn phải hướng dẫn AI qua từng bước của kỹ thuật đúng như đã được giảng dạy, sử dụng AI như một trợ lý có kỷ luật thay vì một hộp đen.
- **Con người rà soát.** Mọi kết quả do AI tạo ra đều phải được chính bạn, người học, rà soát cẩn thận. Bạn hoàn toàn chịu trách nhiệm về tính chính xác của các kết quả này. Bạn phải thực hiện mọi chỉnh sửa và tinh chỉnh cần thiết — không được nộp nguyên đầu ra thô của AI mà chưa rà soát.
- **Báo cáo kiểm toán AI.** Toàn bộ quá trình sử dụng AI phải được ghi lại trong một nhật ký đầy đủ. Bạn được khuyến khích xây dựng các Agent Skill có thể tự động thực hiện những hoạt động này cho các bài tập tương tự. Nếu **không** sử dụng AI, bạn vẫn phải khai báo rõ điều đó.
- **Tài liệu hóa.** Toàn bộ quá trình làm việc phải được ghi lại ở định dạng văn bản, chẳng hạn như Markdown.
- **Chất lượng quan trọng hơn hoàn thành.** Bài làm không chỉ được chấm dựa trên việc đã hoàn thành hay chưa mà còn dựa trên số lượng và chất lượng của các sản phẩm bàn giao: ca kiểm thử, kiểm toán AI, Postman collection và báo cáo Newman, báo cáo lỗi, thiết kế bộ sinh kiểm thử và các liên kết tham chiếu.

## 3. Chuẩn đầu ra

Sau khi hoàn thành bài tập này, bạn có thể:

- Sử dụng AI để tạo ca kiểm thử API từ đặc tả API của SUT, sau đó kiểm toán và mở rộng chúng.
- Thiết kế kiểm thử API bao phủ phân hoạch miền, chuyển đổi trạng thái, bảo mật và xác thực schema.
- Phát hiện các lỗi AI bỏ sót, đặc biệt là lỗi liên quan đến bảo mật và chuyển đổi trạng thái.
- Thiết kế bộ sinh kiểm thử dựa trên AI cho SUT.
- Thể hiện năng lực Bloom-AI ở các mức **G9.2 (Áp dụng)**, **G9.3 (Phân tích)**, **G9.4 (Cộng tác)** và **G9.5 (Sáng tạo)**.

## 4. Hệ thống được kiểm thử (SUT)

**SUT:** EShop — ứng dụng thương mại điện tử mẫu bằng tiếng Việt, được thiết kế để thực hành kiểm thử.

**Kho mã nguồn:** https://github.com/ttbhanh/eshop-sut

Các chức năng của ứng dụng được tổ chức thành những nhóm sau:

- **Nhóm A — Xác thực, Danh mục và Sản phẩm**
    - FR-01: Đăng ký tài khoản
    - FR-02: Đăng nhập và khóa tài khoản
    - FR-03: Quên mật khẩu và đặt lại mật khẩu (hai bước)
    - FR-04: Quản lý hồ sơ cá nhân
    - FR-05: Danh sách và tìm kiếm sản phẩm
    - FR-06: Xem chi tiết sản phẩm
- **Nhóm B — Giỏ hàng và Thanh toán**
    - FR-07: Giỏ hàng
    - FR-08: Thanh toán
    - FR-09: Mã giảm giá
    - FR-10: Máy trạng thái đơn hàng
    - FR-11: Xem lịch sử đơn hàng (người dùng)
- **Nhóm C — Trang quản trị Web**
    - FR-12: Kiểm soát truy cập
    - FR-13: Bảng điều khiển
    - FR-14: Quản lý danh mục (CRUD)
    - FR-15: Quản lý sản phẩm (CRUD)
    - FR-16: Nhập sản phẩm từ CSV
    - FR-17: Quản lý mã giảm giá (CRUD)
    - FR-18: Quản lý đơn hàng (quản trị viên)
    - FR-19: Quản lý người dùng (quản trị viên)
- **Nhóm D — Ứng dụng di động**

SUT cung cấp một đặc tả API trong kho mã nguồn (`api_specification.md`); hãy tham khảo tài liệu này để biết các endpoint hiện có. Đặc tả cũng quy định các yêu cầu bảo mật **SEC-01–SEC-07**.

## 5. Lựa chọn API

- Chọn **ba (3) API**, mỗi API triển khai một chức năng tương ứng từ **Nhóm A, Nhóm B và Nhóm C** (không sử dụng Nhóm D — ứng dụng di động — vì bài tập này tập trung vào API backend). Tham khảo đặc tả API để tìm các endpoint đứng sau từng chức năng đã chọn.
    - **Nhóm A** — ví dụ: đăng nhập (FR-02) hoặc danh sách/tìm kiếm sản phẩm (FR-05).
    - **Nhóm B** — ví dụ: giỏ hàng (FR-07) hoặc thanh toán/tạo đơn hàng (FR-08, FR-10).
    - **Nhóm C** — ví dụ: thao tác của quản trị viên đối với sản phẩm hoặc đơn hàng có thay đổi trạng thái (FR-15, FR-18).
- Tương tự các bài tập trước, hãy bảo đảm lựa chọn của bạn **không trùng lặp** với các thành viên khác trong nhóm: không có hai thành viên chọn cùng một bộ ba API.

## 6. Yêu cầu

Với mỗi API trong ba API đã chọn, hãy hoàn thành quy trình sau. Ghi lại quá trình trong báo cáo chính và đính kèm các minh chứng bắt buộc. Hãy ôn lại các bài giảng liên quan đến kiểm thử API trước khi bắt đầu.

1. **Sinh bằng AI.** Cung cấp đặc tả API của SUT cho một công cụ AI và điều khiển công cụ đó — theo từng bước, không dùng một câu lệnh chung chung duy nhất — để tạo các ca kiểm thử cho API (mục tiêu **≥ 35 ca cho mỗi API**). Các ca kiểm thử phải bao phủ: **phân hoạch miền** trên mọi tham số (ví dụ: định dạng email, độ phức tạp mật khẩu, giá > 0), **chuyển đổi trạng thái** (FR-10: pending → confirmed → shipping → delivered, cùng các quy tắc hủy), **bảo mật** (SEC-01–SEC-07, ví dụ: SQL injection, IDOR, leo thang đặc quyền) và **xác thực schema** (cấu trúc phản hồi khớp chính xác với đặc tả).
2. **Kiểm toán (con người rà soát).** Gắn nhãn cho từng ca kiểm thử do AI tạo là **VALID / INVALID / INCOMPLETE** kèm lý do, đồng thời sửa các ca không hợp lệ hoặc chưa đầy đủ. Bạn hoàn toàn chịu trách nhiệm về các ca kiểm thử cuối cùng.
3. **Mở rộng.** Tự bổ sung **ít nhất năm** ca kiểm thử mà AI đã bỏ sót — đặc biệt xoay quanh bảo mật và chuyển đổi trạng thái — và giải thích *vì sao* AI bỏ sót chúng (chất lượng câu lệnh, giới hạn mô hình hoặc đặc điểm của API).
4. **Thực thi.** Chạy các ca kiểm thử bằng Postman + Newman (hoặc Karate / RestAssured). Mọi request phải có header `X-Student-Id: {StudentID}` (ví dụ: thông qua pre-request script). Xuất báo cáo Newman / HTML.
5. **Báo cáo lỗi.** Báo cáo mọi lỗi thực sự bạn tìm thấy — bao gồm các lỗi AI bỏ sót — trong cả báo cáo Markdown và trang GitHub Issues của bạn, mỗi issue phải đính kèm ảnh chụp màn hình.

Ngoài ra, các yêu cầu kỹ thuật sau áp dụng cho toàn bộ bộ kiểm thử:

- **Khai thác hợp lý nhiều tính năng Postman nhất có thể** — ví dụ: workspace, collection, biến, environment, chạy theo dữ liệu (Collection Runner với tệp dữ liệu), monitor và mock server. **Liệt kê các tính năng Postman bạn đã sử dụng trong báo cáo.** *(Người dùng Karate / RestAssured cần cung cấp các tính năng công cụ tương đương.)*
- **Tích hợp vào CI/CD.** Thêm các ca kiểm thử API vào một pipeline CI/CD cho SUT (ví dụ: chạy Newman trong GitHub Actions thuộc kho mã nguồn của bạn), đồng thời viết một **báo cáo CI/CD** ngắn mô tả cấu hình pipeline và hai lần chạy bên dưới, kèm ảnh chụp màn hình và liên kết. Cung cấp **hai commit mẫu**: một commit có lần chạy pipeline cho thấy **tất cả** ca kiểm thử API đều đạt, và một commit có lần chạy pipeline cho thấy **một** ca kiểm thử thất bại.

## 7. Agent Skill

- Đối với mức Sáng tạo (G9.5), hãy thiết kế một **bộ sinh kiểm thử API dựa trên AI** cho SUT: khi nhận đặc tả API, nó tự động tạo ra các ca kiểm thử. Cung cấp một **sơ đồ tự vẽ** và **mã giả** của thiết kế. ("Tự vẽ" nghĩa là bạn tự đưa ra các quyết định thiết kế; có thể dùng bất kỳ công cụ vẽ sơ đồ nào, nhưng bản thân sơ đồ không được do AI tạo ra.)
- Bạn được khuyến khích triển khai nó dưới dạng một Agent Skill có thể tái sử dụng và nộp video minh họa (liên kết YouTube) cho thấy skill tạo kiểm thử cho một API.

## 8. Công cụ được phép và mức Bloom-AI

Bạn có thể sử dụng các công cụ sau và phải khai báo chúng trong Báo cáo kiểm toán AI:

- Bất kỳ công cụ AI nào bạn chọn (ví dụ: ChatGPT, Claude, Gemini, Copilot, Cursor).
- Postman + Newman (mặc định) hoặc Karate / RestAssured (thay thế).
- Tùy chọn: các công cụ kiểm thử LLM (Promptfoo, DeepEval, Ragas).

Mức Bloom-AI bắt buộc cho bài tập này là **G9.2 (Áp dụng)**, **G9.3 (Phân tích)**, **G9.4 (Cộng tác)** và **G9.5 (Sáng tạo)**.

## 9. Báo cáo kiểm toán AI (Phụ lục bắt buộc)

Đính kèm Báo cáo kiểm toán AI dưới dạng phụ lục. Sử dụng nội dung của các Mẫu AI được cung cấp nếu cần.

- Nếu không sử dụng AI, hãy khai báo: *"Tôi không sử dụng bất kỳ sự hỗ trợ nào của AI trong bài tập này."*
- Nếu có sử dụng AI, hãy khai báo: *"Tôi sử dụng các công cụ AI cho những tác vụ sau,"* và bao gồm các thông tin sau cho mỗi lượt tương tác:
    - Tên công cụ AI
    - Ngày và giờ
    - Câu lệnh của bạn
    - Đầu ra của AI

Để đơn giản hóa quá trình này, bạn được khuyến khích tạo một skill hoặc rule tự động trích xuất các thông tin trên sau một phiên làm việc với AI.

## 10. Phê bình AI (200–300 từ, bắt buộc)

Viết một đoạn văn dài 200–300 từ để phê bình AI. Trả lời các câu hỏi sau: AI đã sai, thiên lệch hoặc thiếu sót ở đâu? Vì sao AI không phát hiện được vấn đề? Bạn đã học được nguyên tắc gì về việc cộng tác với AI trong bài tập này?

Sử dụng nội dung của các Mẫu AI được cung cấp nếu cần.

## 11. Các ràng buộc chống gian lận bằng AI

Bài tập này dựa trên các minh chứng thực thi có thật và có thể truy nguồn. Những nội dung sau không được AI tạo ra hoặc giả mạo, và trợ giảng sẽ xác minh chúng trong quá trình chấm bài:

- Header `X-Student-Id: {StudentID}`, được minh chứng bằng ảnh chụp console từ pre-request script của bạn.
- Đầu ra lần chạy Newman, trong đó hostname khớp với môi trường triển khai của bạn (`localhost` / `127.0.0.1` được chấp nhận).
- Sơ đồ bộ sinh kiểm thử AI, bắt buộc phải tự vẽ — do bạn thiết kế, không được AI trực tiếp tạo ra.

## 12. Nhật ký commit Git

- Tạo một commit Git mới cho mỗi bước của quy trình (ví dụ: sinh, kiểm toán, mở rộng và thực thi cho từng API).
- Cung cấp nhật ký commit Git ở định dạng tệp văn bản.

## 13. Vấn đáp

**30% sinh viên** được chọn ngẫu nhiên có thể được mời tham gia buổi vấn đáp kéo dài 5–7 phút trong tuần sau hạn nộp để giải thích cách họ hoàn thành bài tập này.

## 14. Quy định nộp bài

- **Định dạng tên tệp:** `<StudentID>_HW06_AI_API_<SelfAssessedGrade>.zip`
    - *SelfAssessedGrade:* số có 3 chữ số trong khoảng [000, 100].
    - *Ví dụ:* `25127001_HW06_AI_API_090.zip`
- **Nội dung bắt buộc trong tệp `.zip`:**
    - Báo cáo chính (Markdown + PDF), bao gồm báo cáo kiểm thử API và nội dung kiểm toán AI.
    - Liên kết kho GitHub công khai (collection, script và báo cáo).
    - Postman collection (`.json`) và báo cáo Newman (HTML), cùng danh sách các tính năng Postman đã sử dụng.
    - Báo cáo CI/CD ngắn: cấu hình pipeline và hai lần chạy pipeline mẫu (một lần tất cả đều đạt, một lần có một ca kiểm thử thất bại), kèm ảnh chụp màn hình và liên kết.
    - Các ca kiểm thử dạng Excel và bản tổng kết kiểm thử.
    - Sơ đồ và mã giả của bộ sinh kiểm thử AI (PNG / Mermaid + `.md` / `.py`).
    - Tùy chọn: đặc tả API được chuyển đổi sang OpenAPI (`.yaml` / `.json`); nếu do AI tạo, cũng phải kiểm toán nội dung này.
    - Báo cáo lỗi, kèm ảnh chụp các lỗi trên trang GitHub Issues.
    - Bài Phê bình AI và Báo cáo kiểm toán AI (Markdown + PDF).
    - Nhật ký commit Git (tệp văn bản).
    - Tệp `README.md` chứa bảng tự đánh giá (bên dưới) và báo cáo tổng kết kiểm thử: số API; số ca kiểm thử được tạo, bổ sung, thực thi, đạt và thất bại; cùng số lượng lỗi.
    - Mọi tài liệu hỗ trợ khác.
- Nộp lên Moodle. Về hạn nộp, hãy xem liên kết nộp bài.

## 15. Mẫu đánh giá

| **STT** | **Tiêu chí** | **Điểm** | **Điểm tự đánh giá** |
| --- | --- | --- | --- |
| **1** | API 1 — quy trình đầy đủ (sinh + kiểm toán + mở rộng + thực thi + lỗi) | 30 |  |
| **2** | API 2 — quy trình đầy đủ (cùng tiêu chí) | 30 |  |
| **3** | API 3 — quy trình đầy đủ (cùng tiêu chí) | 30 |  |
| **4** | Agent Skill (bộ sinh kiểm thử dựa trên AI) | 10 |  |
|  | **Tổng cộng** | **100** |  |

## 16. Tài liệu tham khảo

- Giáo trình ISTQB Foundation Level (phiên bản mới nhất).
- Hardman, P. (2025). *A Post-AI Learning Taxonomy.*
- Fuster Rabella, M. (2025). *OECD Education Working Paper No. 338.*
- Anthropic (2025). *Building Reliable AI Test Agents* — blog kỹ thuật.
- Tài liệu DeepEval & Promptfoo — các framework kiểm thử LLM.

## 17. Các quy định khác

- **Không chấp nhận** nộp trễ.
- Thiếu bất kỳ tài liệu bắt buộc nào sẽ bị **0 điểm**.
- Sao chép giữa các sinh viên — **bao gồm cả câu lệnh** — khiến **cả hai bên bị 0 điểm**.
