/**
 * =========================================================================
 * GOOGLE APPS SCRIPT BACKEND CHO CHATBOT PORTFOLIO - NGUYỄN THIÊN ĐỊNH
 * =========================================================================
 * 
 * HƯỚNG DẪN CẤU HÌNH & DEPLOY:
 * 1. Truy cập https://script.google.com -> Tạo "Dự án mới" (New Project).
 * 2. Dán toàn bộ mã nguồn này vào file Code.gs.
 * 3. Điền GEMINI_API_KEY (lấy miễn phí tại https://aistudio.google.com/app/apikey).
 * 4. Tạo một file trên Google Drive (hoặc Google Doc / text) chứa nội dung file 'knowledge_base.txt'.
 *    - Lấy File ID từ đường link Drive: https://drive.google.com/file/d/[DRIVE_FILE_ID]/view
 *    - Gán vào biến DRIVE_FILE_ID bên dưới.
 *    - (Nếu để trống DRIVE_FILE_ID, bot sẽ tự động dùng dữ liệu fallback CV mặc định đã tích hợp sẵn bên dưới).
 * 5. Bấm "Triển khai" (Deploy) -> "Mới" (New deployment).
 *    - Chọn loại: "Ứng dụng web" (Web App).
 *    - Mô tả: Portfolio Chatbot API.
 *    - Thực thi với tư cách: "Tôi" (Me).
 *    - Ai có quyền truy cập: "Bất kỳ ai" (Anyone).
 * 6. Copy URL Web App nhận được và dán vào biến `APPS_SCRIPT_URL` trong file index.html!
 */

// CẤU HÌNH API KEY VÀ FILE KNOWLEDGE BASE TRÊN GOOGLE DRIVE
const GEMINI_API_KEY = "AQ.Ab8RN6JBt6p_HNbjuU7XhfpAfhD0VrhR3FApxLg0LWpaqDZg9Q"; 
const DRIVE_FILE_ID = ""; // Điền ID file text trên Google Drive nếu muốn cập nhật thông tin động từ Drive

// Xử lý yêu cầu GET (phục vụ kiểm tra kết nối)
function doGet(e) {
  return ContentService.createTextOutput(JSON.stringify({
    status: "online",
    message: "Google Apps Script Chatbot API Nguyễn Thiên Định đang hoạt động!",
    timestamp: new Date().toISOString()
  })).setMimeType(ContentService.MimeType.JSON);
}

// Xử lý yêu cầu POST (nhận câu hỏi từ frontend và gọi Gemini AI)
function doPost(e) {
  try {
    let requestData;
    if (e.postData && e.postData.contents) {
      requestData = JSON.parse(e.postData.contents);
    } else {
      requestData = e.parameter;
    }

    const userMessage = requestData.message || requestData.query || "";
    const conversationHistory = requestData.history || [];

    if (!userMessage.trim()) {
      return createCorsResponse({
        success: false,
        reply: "Vui lòng nhập câu hỏi để Định giải đáp nhé!"
      });
    }

    // 1. Đọc nội dung Knowledge Base từ Google Drive hoặc Fallback
    const knowledgeBase = getKnowledgeBaseContent();

    // 2. Xây dựng System Prompt cho Gemini
    const systemPrompt = `Bạn chính là Nguyễn Thiên Định - Kỹ Sư Lập Trình & Tự Động Hóa. Hãy trả lời trực tiếp xưng "mình" hoặc "Định" với người hỏi. Tuyệt đối không nhắc đến từ "AI" hay "trợ lý ảo".
Nhiệm vụ của bạn là giải đáp mọi thắc mắc của nhà tuyển dụng hoặc khách truy cập portfolio về thông tin, kỹ năng, kinh nghiệm, học vấn và phong cách làm việc của Định.

Hãy tuân thủ các nguyên tắc sau:
1. LUÔN TRẢ LỜI DỰA TRÊN DỮ LIỆU CƠ SỞ TRI THỨC (KNOWLEDGE BASE) DƯỚI ĐÂY.
2. Giọng điệu: Thân thiện, tự tin, chuyên nghiệp, khiêm tốn nhưng nêu bật được thế mạnh kỹ thuật của Định.
3. Nếu người dùng hỏi điều gì không có trong cơ sở tri thức, hãy thông báo lịch sự rằng thông tin chưa được cập nhật và mời họ liên hệ trực tiếp với Định qua Email (nguyenthiendinh.dev@gmail.com) hoặc SĐT (0854 243 828).
4. Câu trả lời súc tích, rõ ràng, gạch đầu dòng các kỹ năng / dự án nếu cần để dễ đọc.

--- CƠ SỞ TRI THỨC (CV & PROFILE CỦA NGUYỄN THIÊN ĐỊNH) ---
${knowledgeBase}
------------------------------------------------------------`;

    // 3. Gửi câu hỏi đến Gemini API
    const reply = callGeminiAPI(userMessage, systemPrompt, conversationHistory);

    return createCorsResponse({
      success: true,
      reply: reply
    });

  } catch (err) {
    Logger.log("Lỗi doPost: " + err.toString());
    return createCorsResponse({
      success: false,
      reply: "Xin lỗi, hiện tại bot đang gặp trục trặc kỹ thuật nhỏ: " + err.message
    });
  }
}

/**
 * Đọc nội dung file kiến thức từ Google Drive (nếu cấu hình) hoặc trả về nội dung tĩnh
 */
function getKnowledgeBaseContent() {
  if (DRIVE_FILE_ID && DRIVE_FILE_ID.trim() !== "") {
    try {
      const file = DriveApp.getFileById(DRIVE_FILE_ID.trim());
      return file.getBlob().getDataAsString("UTF-8");
    } catch (e) {
      Logger.log("Không thể đọc file Drive, chuyển sang fallback: " + e.toString());
    }
  }

  // Dữ liệu mặc định từ file CV
  return `
[HỌ VÀ TÊN]: NGUYỄN THIÊN ĐỊNH
[VỊ TRÍ]: CHUYÊN VIÊN LẬP TRÌNH (FULL-STACK / ERP / TỰ ĐỘNG HÓA)
[LIÊN HỆ]: SĐT: 0854 243 828 | Email: nguyenthiendinh.dev@gmail.com | Đ/c: Ninh Kiều, Cần Thơ | Portfolio: https://ln.run/RfYKG
[MỤC TIÊU]: Kỹ sư Kỹ thuật Phần mềm với gần 2 năm kinh nghiệm thực chiến lập trình Web, Desktop & API Doanh nghiệp. Thế mạnh: ReactJS, Node.js, PHP/Laravel, RESTful API và Cơ sở dữ liệu SQL, tối ưu hóa hệ thống ERP/CRM, tự động hóa quy trình sản xuất và vận hành.
[KỸ NĂNG CHUYÊN MÔN]:
- Frontend & UI: ReactJS, Vue.js, Tailwind CSS, JavaScript (ES6+), HTML5/CSS3, Bootstrap
- Backend & API: Node.js (Express), PHP (Laravel), C# (.NET Core), RESTful API, Token/JWT
- Cơ sở dữ liệu: SQL Server, MySQL (Tối ưu hóa Query, Stored Procedure, Data Migration)
- Tự động hóa & IoT: Google Apps Script, MQTT, WebSockets, Tích hợp cảm biến/phần cứng
- Hệ thống & Vận hành: Git, Docker căn bản, Linux CLI, WordPress, IT Helpdesk, Mạng máy tính
- Ngoại ngữ & Khác: Tiếng Anh TOEIC 745 (IIG Vietnam), Đọc hiểu tài liệu kỹ thuật, Thiết kế đa phương tiện
[KINH NGHIỆM LÀM VIỆC]:
1. Lập Trình Viên Full-Stack & Phát Triển Hệ Thống — CÔNG TY CNTT & GIẢI PHÁP SỐ (03/2024 – Hiện tại)
   - Xây dựng dashboard nội bộ (ReactJS, Node.js, Laravel) quản lý dữ liệu real-time.
   - Thiết kế RESTful API xác thực JWT cho Web và Mobile.
   - Xây dựng tool Data Migration giữa SQL Server và MySQL giúp tăng 25% tốc độ truy vấn.
   - Viết kịch bản tự động hóa Google Apps Script đồng bộ Google Sheets và CSDL.
2. Kỹ Sư Lập Trình Hệ Thống & Tự Động Hóa — LÀM VIỆC TỰ DO / DỰ ÁN KỸ THUẬT (Từ khi nghỉ cty cũ đến Hiện nay)
   - Tích hợp thiết bị & phần cứng vào hệ thống tự động: Cảm biến, PLC, bo mạch qua MQTT, WebSockets, Modbus.
   - Phát triển Web & Dashboard giám sát điều khiển từ xa (Node.js, PHP/Laravel, ReactJS, RESTful API).
   - Lập trình ứng dụng Desktop PC (C# .NET) điều khiển thiết bị, vẽ đồ thị telemetry thời gian thực.
   - Phát triển ứng dụng Di Động (Mobile App) theo dõi và điều khiển thiết bị từ xa.
   - Quản trị web, tối ưu máy chủ và hạ tầng IT/CSDL.
3. Nhân Viên IT & Quản Trị Hệ Thống — TT ĐÀO TẠO & SÁT HẠCH LÁI XE CHIẾN THẮNG (09/2022 – 05/2023)
   - Quản trị dữ liệu thi và học viên trên SQL Server, khắc phục sự cố máy tính, mạng LAN/WAN.
   - Quản trị web, thiết kế banner và dựng video truyền thông.
[HỌC VẤN & NĂNG LỰC THỰC CHIẾN]:
- Đại Học Kỹ Thuật - Công Nghệ Cần Thơ: Kỹ Sư Kỹ Thuật Phần Mềm (2019 - 2024), Tốt nghiệp loại Khá.
- Năng lực nổi bật: Độc lập làm chủ toàn bộ vòng đời phát triển dự án quy mô lớn (Solo Full-Cycle Engineering): từ phân tích yêu cầu, thiết kế kiến trúc, lập trình Full-Stack đến đóng gói Windows Installer, triển khai server production và bảo trì dài hạn.
- Tối ưu hóa truy vấn CSDL (+25% tốc độ), tự động hóa Google Apps Script, tích hợp thiết bị IoT (MQTT/ESP32/C# .NET) và Mascot 3D Web tương tác sinh động.
- Chứng chỉ: TOEIC 745 (IIG Vietnam), Chứng chỉ Lập trình Web Full-Stack & Thiết kế đồ họa.
`;
}

/**
 * Gọi Google Gemini API
 */
function callGeminiAPI(prompt, systemInstruction, history) {
  if (!GEMINI_API_KEY || GEMINI_API_KEY === "THAY_BANG_GEMINI_API_KEY_CUA_BAN") {
    // Trả lời cục bộ thông minh nếu chưa điền API Key
    return generateLocalFallbackAnswer(prompt);
  }

  const endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent?key=" + GEMINI_API_KEY;

  // Chuẩn bị danh sách contents gồm lịch sử hội thoại
  const contents = [];

  // Ghép các lượt chat trước (nếu có)
  if (Array.isArray(history) && history.length > 0) {
    history.slice(-6).forEach(msg => {
      contents.push({
        role: msg.role === "user" ? "user" : "model",
        parts: [{ text: msg.text }]
      });
    });
  }

  // Thêm câu hỏi hiện tại
  contents.push({
    role: "user",
    parts: [{ text: prompt }]
  });

  const payload = {
    contents: contents,
    systemInstruction: {
      parts: [{ text: systemInstruction }]
    },
    generationConfig: {
      temperature: 0.4,
      maxOutputTokens: 800
    }
  };

  const options = {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  };

  const response = UrlFetchApp.fetch(endpoint, options);
  const json = JSON.parse(response.getContentText());

  if (json.candidates && json.candidates.length > 0 && json.candidates[0].content) {
    return json.candidates[0].content.parts.map(p => p.text).join("\n");
  } else if (json.error) {
    throw new Error("Gemini API Error: " + json.error.message);
  } else {
    return "Không nhận được phản hồi từ mô hình AI.";
  }
}

/**
 * Phản hồi giả lập thông minh theo từ khóa khi người dùng chưa cấu hình API Key
 */
function generateLocalFallbackAnswer(query) {
  const q = query.toLowerCase();
  if (q.includes("kỹ năng") || q.includes("skill") || q.includes("công nghệ")) {
    return "Nguyễn Thiên Định thành thạo đa dạng kỹ năng: \n- **Frontend**: ReactJS, Vue.js, Tailwind CSS, JavaScript ES6+\n- **Backend**: Node.js, PHP (Laravel), C# (.NET Core), RESTful API, JWT\n- **Database**: SQL Server, MySQL (Tối ưu query, Stored Proc, Data Migration)\n- **Tự động hóa & IoT**: Google Apps Script, MQTT, WebSockets\n- **Ngoại ngữ**: Tiếng Anh TOEIC 745.";
  }
  if (q.includes("kinh nghiệm") || q.includes("dự án") || q.includes("làm việc")) {
    return "Định có gần 2 năm kinh nghiệm thực chiến:\n1. **Lập Trình Viên Full-Stack & Hệ Thống** (03/2024 - Hiện tại): Xây dựng dashboard nội bộ, tối ưu query tăng 25% tốc độ, tự động hóa với Google Apps Script.\n2. **Kỹ Sư Lập Trình Hệ Thống & Tự Động Hóa (Freelance)** (Từ khi nghỉ cty cũ đến Hiện nay): Tích hợp thiết bị vào hệ thống tự động, lập trình Web dashboard, ứng dụng Desktop PC (C# .NET), ứng dụng Di Động (Mobile App), giao thức MQTT/WebSockets/Modbus.\n3. **IT & Hệ Thống** (09/2022 - 05/2023): Quản trị SQL Server, mạng LAN/WAN và web.";
  }
  if (q.includes("học vấn") || q.includes("trường") || q.includes("bằng")) {
    return "Định tốt nghiệp **Kỹ Sư Kỹ Thuật Phần Mềm** tại Trường Đại Học Kỹ Thuật - Công Nghệ Cần Thơ (loại Khá, Đồ án tốt nghiệp đạt 9.0 điểm) cùng chứng chỉ tiếng Anh **TOEIC 745**.";
  }
  if (q.includes("liên hệ") || q.includes("sđt") || q.includes("email") || q.includes("ở đâu")) {
    return "Bạn có thể liên hệ với Định qua:\n- 📱 SĐT: **0854 243 828**\n- ✉ Email: **nguyenthiendinh.dev@gmail.com**\n- 📍 Khu vực: Ninh Kiều, TP. Cần Thơ.";
  }
  return "Chào bạn! Mình là Nguyễn Thiên Định. Bạn có thể hỏi tôi về Kỹ năng chuyên môn, Kinh nghiệm làm việc, Các dự án ERP/Full-Stack hay thông tin liên hệ của Định nhé!";
}

/**
 * Trả về HTTP Response có header CORS cho phép gọi từ bất kỳ website nào
 */
function createCorsResponse(data) {
  return ContentService.createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}
