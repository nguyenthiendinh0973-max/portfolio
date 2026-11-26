import os
import subprocess
import tempfile

workspace = r"d:\1\slides"
chrome_bin = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

CV_VARIANTS = [
    {
        "filename": "CV Nguyễn Thiên Định - Kỹ Sư Phần Mềm Full-Stack & IoT.pdf",
        "doc_title": "CV Nguyễn Thiên Định - Kỹ Sư Phần Mềm Full-Stack &amp; IoT",
        "role": "Kỹ Sư Phần Mềm Full-Stack Web, ERP &amp; Tự Động Hóa IoT",
        "summary": (
            "Kỹ sư Kỹ thuật Phần mềm với gần 2 năm kinh nghiệm thực chiến, có năng lực độc lập làm chủ toàn bộ vòng đời các dự án lớn: "
            "từ phân tích yêu cầu, thiết kế kiến trúc, lập trình Full-Stack đến đóng gói installer, triển khai server production và bảo trì dài hạn. "
            "Thành thạo phát triển các hệ thống Dashboard quản trị doanh nghiệp với Laravel, PHP, Node.js, ReactJS, Tailwind CSS &amp; Bootstrap, "
            "WordPress &amp; tối ưu SEO; chuyên sâu tối ưu hóa cơ sở dữ liệu (+25% tốc độ truy vấn), tự động hóa vận hành với Google Apps Script "
            "và tích hợp thiết bị phần cứng IoT (MQTT/ESP32/C#.NET). Từng tích hợp thành công Mascot 3D tương tác + Audio sinh động trên Web. "
            "Sở hữu chứng chỉ TOEIC 745 (IIG Vietnam), sẵn sàng đảm nhận vai trò Full-Stack/ERP Developer hoặc Onboard dự án mới."
        ),
    },
    {
        "filename": "CV Nguyễn Thiên Định - Nhân Viên Website.pdf",
        "doc_title": "CV Nguyễn Thiên Định - Nhân Viên Website",
        "role": "Nhân Viên Website",
        "summary": (
            "Kỹ sư Kỹ thuật Phần mềm với gần 2 năm kinh nghiệm thực chiến trong phát triển, quản trị và tối ưu hóa hệ thống Website doanh nghiệp. "
            "Thành thạo xây dựng giao diện chuẩn Responsive (HTML5/CSS3, Tailwind CSS, Bootstrap 5, ReactJS, jQuery/AJAX), phát triển Backend "
            "(PHP/Laravel, Node.js/Express), quản trị và tùy biến WordPress (CMS) kết hợp tối ưu Technical &amp; On-page SEO. "
            "Có kinh nghiệm cấu hình VPS Linux, Nginx SSL, tối ưu tốc độ tải trang, quản trị cơ sở dữ liệu MySQL/SQL Server (+25% tốc độ truy vấn), "
            "tích hợp Mascot 3D tương tác + Audio trên Web và tự động hóa quy trình với Google Apps Script. "
            "Sở hữu chứng chỉ TOEIC 745 (IIG Vietnam), sẵn sàng Onboard ngay cho vị trí Nhân Viên Website."
        ),
    },
]


def get_css():
    return """
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

  :root {
    --navy: #0f172a;
    --blue: #0284c7;
    --text-main: #0f172a;
    --text-body: #334155;
    --text-muted: #475569;
    --border: #cbd5e1;
    --border-light: #e2e8f0;
    --bg-soft: #f8fafc;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  @page {
    size: A4;
    margin: 9mm 11mm;
  }

  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    color: var(--text-body);
    background-color: #ffffff;
    line-height: 1.32;
    font-size: 7.8pt;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  .page {
    width: 100%;
    background: #ffffff;
  }

  /* HEADER */
  .header {
    margin-bottom: 6px;
  }

  .cand-name {
    font-size: 20pt;
    font-weight: 800;
    color: var(--navy);
    letter-spacing: -0.01em;
    line-height: 1.1;
    text-transform: uppercase;
  }

  .cand-role {
    font-size: 10pt;
    font-weight: 700;
    color: var(--blue);
    margin-top: 2px;
    margin-bottom: 5px;
  }

  .highlights {
    display: flex;
    flex-wrap: wrap;
    gap: 3px 14px;
    font-size: 7.7pt;
    font-weight: 600;
    color: var(--navy);
    margin-bottom: 5px;
  }

  .hl-item {
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }

  .hl-sq {
    color: var(--blue);
    font-size: 8pt;
    line-height: 1;
  }

  .header-divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 4px 0;
  }

  .contact-bar {
    display: flex;
    flex-wrap: wrap;
    gap: 2px 14px;
    font-size: 7.7pt;
    color: var(--text-body);
  }

  .contact-bar strong {
    color: var(--navy);
    font-weight: 700;
  }

  .contact-bar a {
    color: var(--text-body);
    text-decoration: none;
  }

  /* SUMMARY BOX */
  .summary-box {
    background: var(--bg-soft);
    border-left: 3px solid var(--blue);
    padding: 6px 9px;
    margin: 6px 0 8px 0;
    font-size: 7.65pt;
    line-height: 1.36;
    color: var(--text-body);
  }

  .summary-box strong {
    color: var(--navy);
    font-weight: 700;
  }

  /* TWO-COLUMN BODY */
  .main-grid {
    display: grid;
    grid-template-columns: 31% 1fr;
    gap: 14px;
    align-items: start;
  }

  .section-h {
    font-size: 8.6pt;
    font-weight: 800;
    color: var(--navy);
    text-transform: uppercase;
    letter-spacing: 0.02em;
    border-bottom: 1.5px solid var(--navy);
    padding-bottom: 2px;
    margin-bottom: 6px;
  }

  .sidebar-block {
    margin-bottom: 9px;
  }

  /* EDUCATION */
  .edu-school {
    font-size: 8pt;
    font-weight: 700;
    color: var(--navy);
  }

  .edu-major {
    font-size: 7.7pt;
    font-weight: 600;
    color: var(--blue);
    margin-top: 1px;
  }

  .edu-time {
    font-size: 7.4pt;
    color: var(--text-muted);
    margin-bottom: 3px;
  }

  .clean-list {
    list-style: none;
    padding-left: 0;
  }

  .clean-list li {
    position: relative;
    padding-left: 9px;
    margin-bottom: 2.5px;
    font-size: 7.55pt;
    line-height: 1.32;
  }

  .clean-list li::before {
    content: "•";
    position: absolute;
    left: 0;
    top: 0;
    color: var(--navy);
    font-weight: 700;
  }

  /* CERTIFICATE BOX */
  .cert-box {
    border: 1px solid var(--border);
    border-radius: 3px;
    padding: 5px 7px;
    background: #ffffff;
  }

  .cert-title {
    font-size: 8pt;
    font-weight: 700;
    color: var(--navy);
  }

  .cert-org {
    font-size: 7.4pt;
    font-weight: 600;
    color: var(--blue);
    margin-bottom: 2px;
  }

  .cert-desc {
    font-size: 7.4pt;
    line-height: 1.32;
    color: var(--text-body);
  }

  /* SKILL MATRIX (TEXT-BASED ATS-FRIENDLY) */
  .skill-group {
    margin-bottom: 5.5px;
  }

  .skill-group-title {
    font-size: 7.7pt;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 1px;
  }

  .skill-group-items {
    font-size: 7.45pt;
    line-height: 1.32;
    color: var(--text-body);
  }

  /* EXPERIENCE */
  .exp-item {
    margin-bottom: 7px;
  }

  .exp-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 8px;
  }

  .exp-role {
    font-size: 8.3pt;
    font-weight: 700;
    color: var(--navy);
  }

  .exp-date {
    font-size: 7.6pt;
    font-weight: 700;
    color: var(--blue);
    white-space: nowrap;
  }

  .exp-company {
    font-size: 7.4pt;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    margin-bottom: 4px;
  }

  .sub-proj {
    border-left: 2px solid var(--border);
    padding: 3px 0 3px 7px;
    margin-bottom: 4px;
    background: #ffffff;
  }

  .sub-proj-h {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 8px;
  }

  .sub-proj-title {
    font-size: 7.75pt;
    font-weight: 700;
    color: var(--navy);
  }

  .sub-proj-date {
    font-size: 7.25pt;
    color: var(--text-muted);
    white-space: nowrap;
  }

  .sub-proj-tech {
    font-size: 7.3pt;
    font-weight: 600;
    color: var(--blue);
    margin: 1px 0;
  }

  .sub-proj-desc {
    font-size: 7.45pt;
    line-height: 1.32;
    color: var(--text-body);
  }

  /* FEATURED PROJECTS TABLE */
  .proj-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.4pt;
    margin-top: 2px;
  }

  .proj-table thead th {
    background: var(--navy);
    color: #ffffff;
    font-weight: 700;
    text-align: left;
    padding: 4px 6px;
    font-size: 7.45pt;
  }

  .proj-table tbody td {
    padding: 4px 6px;
    border-bottom: 1px solid var(--border-light);
    vertical-align: top;
    line-height: 1.3;
  }

  .proj-table tbody tr:nth-child(even) td {
    background: var(--bg-soft);
  }

  .proj-name {
    font-weight: 700;
    color: var(--navy);
    width: 28%;
  }

  .proj-res {
    font-weight: 700;
    color: var(--blue);
    white-space: nowrap;
    width: 18%;
  }
"""


def generate_html(variant):
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>{variant['doc_title']}</title>
  <style>{get_css()}</style>
</head>
<body>
  <div class="page">

    <!-- HEADER -->
    <header class="header">
      <div class="cand-name">NGUYỄN THIÊN ĐỊNH</div>
      <div class="cand-role">{variant['role']}</div>
      <div class="highlights">
        <span class="hl-item"><span class="hl-sq">▪</span> Độc lập làm chủ dự án A–Z (Phân tích – Triển khai – Vận hành)</span>
        <span class="hl-item"><span class="hl-sq">▪</span> TOEIC 745 (IIG Vietnam)</span>
        <span class="hl-item"><span class="hl-sq">▪</span> Gần 2 năm kinh nghiệm thực chiến</span>
        <span class="hl-item"><span class="hl-sq">▪</span> Sẵn sàng Onboard ngay (On-site / Remote)</span>
      </div>
      <hr class="header-divider">
      <div class="contact-bar">
        <span><strong>Điện thoại:</strong> 0854 243 828</span>
        <span><strong>Email:</strong> nguyenthiendinh.dev@gmail.com</span>
        <span><strong>Portfolio:</strong> <a href="https://nguyenthiendinh0973-max.github.io/portfolio/">nguyenthiendinh0973-max.github.io/portfolio</a></span>
        <span><strong>Địa chỉ:</strong> Ninh Kiều, TP. Cần Thơ</span>
      </div>
    </header>

    <!-- SUMMARY -->
    <div class="summary-box">
      <strong>Tóm Tắt Năng Lực &amp; Mục Tiêu Nghề Nghiệp:</strong> {variant['summary']}
    </div>

    <!-- MAIN 2-COLUMN BODY -->
    <div class="main-grid">

      <!-- LEFT SIDEBAR -->
      <aside>
        <div class="sidebar-block">
          <div class="section-h">HỌC VẤN</div>
          <div class="edu-school">ĐH Kỹ Thuật – Công Nghệ Cần Thơ</div>
          <div class="edu-major">Kỹ Sư Kỹ Thuật Phần Mềm</div>
          <div class="edu-time">2019 – 2024</div>
          <ul class="clean-list">
            <li>Tốt nghiệp loại <strong>Khá</strong>.</li>
            <li>Độc lập làm chủ toàn bộ vòng đời phát triển phần mềm (Full-Cycle Engineering) cho các hệ thống lớn.</li>
          </ul>
        </div>

        <div class="sidebar-block">
          <div class="section-h">CHỨNG CHỈ &amp; NGOẠI NGỮ</div>
          <div class="cert-box">
            <div class="cert-title">TOEIC 745 Điểm</div>
            <div class="cert-org">Do IIG Vietnam cấp</div>
            <div class="cert-desc">Đọc hiểu tài liệu kỹ thuật chuyên sâu; giao tiếp và phối hợp làm việc hiệu quả trong môi trường quốc tế.</div>
          </div>
        </div>

        <div class="sidebar-block">
          <div class="section-h">MA TRẬN KỸ NĂNG</div>
          <div class="skill-group">
            <div class="skill-group-title">Frontend &amp; UI Engineering</div>
            <div class="skill-group-items">ReactJS, Tailwind CSS, Bootstrap 5, jQuery, AJAX, JavaScript ES6+, HTML5/CSS3, Technical &amp; On-page SEO</div>
          </div>
          <div class="skill-group">
            <div class="skill-group-title">Backend &amp; RESTful API</div>
            <div class="skill-group-items">PHP / Laravel, Node.js / Express, WordPress (CMS), C#.NET, RESTful API, JWT, SSO / RBAC, WebSockets</div>
          </div>
          <div class="skill-group">
            <div class="skill-group-title">Cơ Sở Dữ Liệu &amp; Tối Ưu</div>
            <div class="skill-group-items">MySQL, SQL Server, Tối ưu Query (+25%), Stored Procedures, Data Migration</div>
          </div>
          <div class="skill-group">
            <div class="skill-group-title">IoT, Tự Động Hóa &amp; 3D Web</div>
            <div class="skill-group-items">ESP32 / MQTT, Modbus, C# WinForms/WPF, Google Apps Script, Mascot 3D + Audio, SpeechAce AI</div>
          </div>
          <div class="skill-group">
            <div class="skill-group-title">Mobile &amp; Bảo Mật Ứng Dụng</div>
            <div class="skill-group-items">Flutter, Dart, Riverpod, GoRouter, Drift (SQLite), Argon2id, AES-256-GCM, Biometric Auth</div>
          </div>
          <div class="skill-group">
            <div class="skill-group-title">Hạ Tầng, DevOps &amp; Khác</div>
            <div class="skill-group-items">Git, GitHub PR, Docker căn bản, VPS Linux / Nginx SSL, CI/CD, QA/QC</div>
          </div>
        </div>
      </aside>

      <!-- RIGHT MAIN -->
      <main>
        <div class="section-h">KINH NGHIỆM LÀM VIỆC THỰC CHIẾN</div>

        <div class="exp-item">
          <div class="exp-header">
            <div class="exp-role">Lập Trình Viên (Full-Stack &amp; IoT)</div>
            <div class="exp-date">01/2025 – 04/2026</div>
          </div>
          <div class="exp-company">CÔNG TY CỔ PHẦN ĐẦU TƯ GIÁO DỤC GENIUS OPENWIDE GLOBAL</div>

          <div class="sub-proj">
            <div class="sub-proj-h">
              <div class="sub-proj-title">1. EduPortal Enterprise Workspace System</div>
              <div class="sub-proj-date">01/2025 – 10/2025</div>
            </div>
            <div class="sub-proj-tech">Flutter · Express · MySQL · WebSockets · SSO</div>
            <div class="sub-proj-desc">Cổng giáo dục &amp; điều hành nội bộ tích hợp SSO + RBAC phân quyền bảo mật, Chat/Helpdesk real-time qua WebSockets, đóng gói ứng dụng Windows Installer và trực tiếp triển khai hạ tầng máy chủ production.</div>
          </div>

          <div class="sub-proj">
            <div class="sub-proj-h">
              <div class="sub-proj-title">2. Học Liệu Số &amp; Tích Hợp Thanh Toán / Phần Cứng</div>
              <div class="sub-proj-date">11/2025 – 01/2026</div>
            </div>
            <div class="sub-proj-tech">Node.js · ESP32 · MQTT · VNPay/Stripe · Docker</div>
            <div class="sub-proj-desc">Xây dựng Backend đa vai trò, tích hợp cổng thanh toán VNPay / Stripe qua Webhook bảo mật, kết nối thiết bị ESP32 qua MQTT in hóa đơn tự động theo sự kiện đơn hàng, cấu hình máy chủ VPS Linux / Nginx SSL và CI/CD với Codemagic.</div>
          </div>

          <div class="sub-proj">
            <div class="sub-proj-h">
              <div class="sub-proj-title">3. Hệ Thống Thi Tiếng Anh Đa Nền Tảng</div>
              <div class="sub-proj-date">01/2026 – 04/2026</div>
            </div>
            <div class="sub-proj-tech">Flutter Desktop · Audio DSP · SpeechAce AI · Excel</div>
            <div class="sub-proj-desc">Phát triển app thi PC + Web Admin Dashboard chấm thi nói, tích hợp bộ xử lý âm thanh Audio DSP + SpeechAce AI nhận diện phát âm, ngân hàng đề thi đa dạng và xuất báo cáo Excel tự động – <strong>tiết kiệm 80% thời gian tổng hợp kết quả</strong>.</div>
          </div>
        </div>

        <div class="exp-item">
          <div class="exp-header">
            <div class="exp-role">Lập Trình Viên Module &amp; Tối Ưu CSDL</div>
            <div class="exp-date">06/2024 – 10/2024</div>
          </div>
          <div class="exp-company">TRUNG TÂM GDNN ĐÀO TẠO &amp; SÁT HẠCH LÁI XE CHIẾN THẮNG</div>
          <ul class="clean-list">
            <li>Phát triển các module chức năng quản lý cốt lõi: hồ sơ học viên, điều phối lịch sát hạch và hệ thống trích xuất báo cáo kiểm định.</li>
            <li>Tối ưu hóa CSDL MySQL, tái cấu trúc (refactor) các câu query phức tạp giúp giảm thời gian phản hồi và nâng cao hiệu năng hệ thống.</li>
            <li>Thực hiện quy trình QA/QC: kiểm thử chức năng, tái hiện lỗi, lập log tracking và trực tiếp sửa lỗi (bug fixing) toàn hệ thống.</li>
            <li>Quản lý mã nguồn Git chuyên nghiệp: chiến lược phân nhánh (branching strategy), tạo Pull Request và giải quyết merge conflict.</li>
          </ul>
        </div>

        <div class="exp-item">
          <div class="exp-header">
            <div class="exp-role">Kỹ Sư Phần Mềm Tự Do (Freelance &amp; Dự Án Kỹ Thuật)</div>
            <div class="exp-date">06/2023 – Hiện tại</div>
          </div>
          <div class="exp-company">LÀM VIỆC TỰ DO / DỰ ÁN KỸ THUẬT &amp; THIẾT BỊ NGOẠI VI</div>
          <ul class="clean-list">
            <li>Tích hợp thiết bị ngoại vi vào hệ thống tự động: kết nối cảm biến đo lường, vi điều khiển (ESP32/Arduino) và PLC qua giao thức MQTT, WebSockets, Modbus phục vụ thu thập telemetry theo thời gian thực.</li>
            <li>Phát triển phần mềm ứng dụng Desktop PC (C#.NET WinForms / WPF) điều khiển thiết bị, hiển thị đồ thị kỹ thuật real-time; phát triển Web Dashboard (Node.js, PHP/Laravel, ReactJS, Tailwind/Bootstrap) giám sát từ xa.</li>
            <li>Tích hợp thành công Mascot 3D tương tác Web + Hiệu ứng âm thanh sinh động (Audio DSP).</li>
            <li>Hạ tầng &amp; bảo mật: cấu hình và quản trị máy chủ VPS Linux, cài đặt chứng chỉ SSL/Nginx, tối ưu hóa tốc độ tải trang web.</li>
          </ul>
        </div>

        <div class="section-h" style="margin-top: 6px;">DỰ ÁN TIÊU BIỂU &amp; SẢN PHẨM BÀN GIAO</div>
        <table class="proj-table">
          <thead>
            <tr>
              <th>Sản Phẩm / Dự Án</th>
              <th>Mô Tả Giải Pháp</th>
              <th>Kết Quả</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="proj-name">EduPortal Enterprise Workspace</td>
              <td>Cổng giáo dục tích hợp SSO/RBAC, Chat/Helpdesk real-time qua WebSockets, đóng gói Windows Installer.</td>
              <td class="proj-res">Production</td>
            </tr>
            <tr>
              <td class="proj-name">Hệ Thống Thi Nói SpeechAce AI</td>
              <td>Ứng dụng thi PC + Web Admin, tích hợp Audio DSP và SpeechAce AI chấm điểm Speaking tự động.</td>
              <td class="proj-res">Tiết kiệm 80%</td>
            </tr>
            <tr>
              <td class="proj-name">In Hóa Đơn Tự Động ESP32 &amp; VNPay</td>
              <td>Backend đa vai trò, webhook thanh toán trực tuyến, vi điều khiển ESP32 kích hoạt máy in qua MQTT.</td>
              <td class="proj-res">Hoàn thành</td>
            </tr>
            <tr>
              <td class="proj-name">Google Apps Script &amp; Query Optimizer</td>
              <td>Tự động hóa đồng bộ Google Sheets, tối ưu hóa truy vấn Database, Stored Procedures &amp; Indexing.</td>
              <td class="proj-res">+25% Speedup</td>
            </tr>
            <tr>
              <td class="proj-name">SafeVault — Quản Lý Mật Khẩu Offline</td>
              <td>App Flutter (Riverpod, GoRouter, Drift SQLite) mã hóa Argon2id + AES-256-GCM, DEK 256-bit, sinh trắc học, dashboard fl_chart.</td>
              <td class="proj-res"><a href="https://drive.google.com/uc?export=download&id=1uzp6S8bmiWwCOBTlz0uot1TRg6oWT4Dc">Tải App</a></td>
            </tr>
          </tbody>
        </table>
      </main>

    </div>
  </div>
</body>
</html>
"""


def main():
    for variant in CV_VARIANTS:
        output_pdf = os.path.join(workspace, variant["filename"])
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tmp:
            tmp.write(generate_html(variant))
            tmp_html = tmp.name

        try:
            if os.path.exists(output_pdf):
                try:
                    os.remove(output_pdf)
                except PermissionError:
                    print(f"Notice: {variant['filename']} is currently open in a PDF viewer, skipped.")
                    continue
            cmd = [
                chrome_bin,
                "--headless=new",
                "--disable-gpu",
                "--no-sandbox",
                f"--print-to-pdf={output_pdf}",
                "--no-pdf-header-footer",
                tmp_html,
            ]
            subprocess.run(cmd, check=True)
            print(f"Generated: {output_pdf} ({os.path.getsize(output_pdf)} bytes)")
        finally:
            if os.path.exists(tmp_html):
                os.remove(tmp_html)


if __name__ == "__main__":
    main()
