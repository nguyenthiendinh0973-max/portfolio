# HƯỚNG DẪN DEPLOY CHATBOT PORTFOLIO VỚI GOOGLE APPS SCRIPT

Dự án Portfolio của bạn đã được thiết kế sẵn sàng với đầy đủ các file:
- **`index.html`**: Trang Portfolio hiện đại với UI công nghệ tối ưu, hiển thị ma trận toàn bộ kỹ năng từ CV và widget Chatbot AI ở góc phải.
- **`Code.gs`**: Mã nguồn Google Apps Script đóng vai trò backend webhook, tiếp nhận tin nhắn và gọi mô hình Gemini AI trả lời dựa trên file tri thức.
- **`knowledge_base.txt`**: File cơ sở dữ liệu tri thức được trích xuất và mở rộng từ CV của bạn.

---

### BƯỚC 1: LẤY GEMINI API KEY (HOÀN TOÀN MIỄN PHÍ)
1. Truy cập: [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Đăng nhập bằng tài khoản Google của bạn và bấm **Create API key**.
3. Copy API Key được cấp.

---

### BƯỚC 2: TẠO FILE KNOWLEDGE BASE TRÊN GOOGLE DRIVE
1. Truy cập Google Drive ([drive.google.com](https://drive.google.com)).
2. Tải file `knowledge_base.txt` (nằm trong thư mục dự án) lên Google Drive của bạn.
3. Nhấp chuột phải vào file trên Drive -> Chọn **Chia sẻ (Share)** -> Đổi quyền truy cập thành **"Bất kỳ ai có đường liên kết" (Anyone with the link)** với quyền Xem.
4. Lấy **File ID** từ thanh địa chỉ trình duyệt:
   - Link có dạng: `https://drive.google.com/file/d/1a2B3c4D_xyz.../view`
   - File ID chính là đoạn mã ở giữa `.../d/` và `/view`: `1a2B3c4D_xyz...`

*(Lưu ý: Nếu không muốn dùng Google Drive, hệ thống trong `Code.gs` đã tích hợp sẵn dữ liệu CV dự phòng, bạn có thể để trống biến `DRIVE_FILE_ID`).*

---

### BƯỚC 3: DEPLOY BACKEND TRÊN GOOGLE APPS SCRIPT
1. Truy cập [script.google.com](https://script.google.com) và bấm **Dự án mới (New Project)**.
2. Xóa code mặc định trong file `Code.gs`, mở file `Code.gs` trong thư mục dự án này, copy toàn bộ nội dung và dán vào.
3. Sửa 2 dòng đầu trong `Code.gs`:
   ```javascript
   const GEMINI_API_KEY = "DÁN_GEMINI_API_KEY_CỦA_BẠN_VÀO_ĐÂY";
   const DRIVE_FILE_ID = "DÁN_DRIVE_FILE_ID_VÀO_ĐÂY"; // (hoặc để rỗng "")
   ```
4. Bấm **Lưu (Ctrl + S)**.
5. Ở góc trên bên phải, bấm nút **Triển khai (Deploy)** -> **Tùy chọn triển khai mới (New deployment)**.
6. Thiết lập thông số:
   - Loại triển khai: Nhấp vào biểu tượng bánh răng ⚙️ -> Chọn **Ứng dụng web (Web app)**.
   - Mô tả: `Portfolio Chatbot API`.
   - Thực thi dưới dạng (Execute as): **Tôi (Me - your_email@gmail.com)**.
   - Ai có quyền truy cập (Who has access): **Bất kỳ ai (Anyone)** *(Rất quan trọng để frontend có thể gọi API)*.
7. Bấm **Triển khai (Deploy)**. Nếu Google yêu cầu cấp quyền (Authorize Access), chọn tài khoản của bạn -> Bấm *Advanced* -> Chọn *Go to Untitled project (unsafe)* -> Bấm *Allow*.
8. Copy đường dẫn **URL ứng dụng web (Web App URL)** có dạng:
   `https://script.google.com/macros/s/AKfycb.../exec`

---

### BƯỚC 4: KẾT NỐI VÀO TRANG PORTFOLIO (index.html)
1. Mở file `index.html`.
2. Tìm đến dòng có biến `APPS_SCRIPT_URL` (khoảng dòng 400):
   ```javascript
   const APPS_SCRIPT_URL = "DÁN_URL_WEB_APP_TỪ_BƯỚC_3_VÀO_ĐÂY";
   ```
3. Lưu file lại.
4. Mở trực tiếp file `index.html` trên trình duyệt để thưởng thức portfolio cùng Chatbot AI!
