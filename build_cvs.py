import os
import base64
import subprocess
import shutil

workspace = r"d:\1\slides"
avatar_path = os.path.join(workspace, "avatar.jpg")

with open(avatar_path, "rb") as f:
    avatar_b64 = base64.b64encode(f.read()).decode("utf-8")

# Common CSS
def get_css():
    return """
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

  :root {
    --primary: #0f172a;
    --primary-light: #1e293b;
    --accent: #4338ca;
    --accent-light: #6366f1;
    --accent-subtle: #eef2ff;
    --emerald: #047857;
    --emerald-subtle: #ecfdf5;
    --text-main: #0f172a;
    --text-muted: #334155;
    --text-light: #64748b;
    --border: #cbd5e1;
    --border-light: #e2e8f0;
    --bg-card: #f8fafc;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: var(--text-main);
    background-color: #cbd5e1;
    line-height: 1.42;
    font-size: 8.8pt;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  /* TOP ACTION BAR (Hidden on Print) */
  .top-action-bar {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: #0f172a;
    color: white;
    padding: 10px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
  }
  .top-action-bar .brand-title {
    font-size: 14px;
    font-weight: 700;
    color: #e2e8f0;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .top-action-bar .actions {
    display: flex;
    gap: 10px;
    align-items: center;
  }
  .top-action-bar a, .top-action-bar button {
    background: #4f46e5;
    color: white;
    border: none;
    padding: 7px 15px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s;
  }
  .top-action-bar a:hover, .top-action-bar button:hover {
    background: #4338ca;
    transform: translateY(-1px);
  }
  .top-action-bar .btn-secondary {
    background: #334155;
  }
  .top-action-bar .btn-secondary:hover {
    background: #475569;
  }
  .top-action-bar .btn-emerald {
    background: #059669;
  }
  .top-action-bar .btn-emerald:hover {
    background: #047857;
  }

  /* A4 PAGE CONTAINER */
  .a4-page {
    width: 210mm;
    min-height: 297mm;
    margin: 20px auto;
    background: #ffffff;
    box-shadow: 0 10px 30px rgba(0,0,0,0.12);
    position: relative;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  @page {
    size: A4 portrait;
    margin: 0;
  }

  @media print {
    html, body {
      width: 210mm !important;
      height: 297mm !important;
      margin: 0 !important;
      padding: 0 !important;
      background: white !important;
      overflow: hidden !important;
    }
    .top-action-bar {
      display: none !important;
    }
    .a4-page {
      margin: 0 !important;
      box-shadow: none !important;
      width: 210mm !important;
      height: 297mm !important;
      max-height: 297mm !important;
      page-break-after: avoid !important;
      page-break-inside: avoid !important;
      overflow: hidden !important;
    }
  }

  /* HEADER BLOCK */
  .cv-header {
    background: linear-gradient(135deg, #090e17 0%, #161938 55%, #0d1322 100%);
    color: white;
    padding: 22px 26px 18px 26px;
    border-bottom: 3.5px solid #4f46e5;
  }
  .cv-header-grid {
    display: flex;
    align-items: center;
    gap: 20px;
  }
  .avatar-wrap {
    width: 84px;
    height: 84px;
    border-radius: 16px;
    overflow: hidden;
    border: 2.5px solid rgba(255,255,255,0.9);
    box-shadow: 0 6px 16px rgba(0,0,0,0.35);
    flex-shrink: 0;
    background: #1e293b;
  }
  .avatar-wrap img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
  }
  .header-info {
    flex: 1;
  }
  .cand-name {
    font-size: 20pt;
    font-weight: 800;
    letter-spacing: -0.4px;
    line-height: 1.15;
    color: #ffffff;
    text-transform: uppercase;
  }
  .cand-role {
    font-size: 10pt;
    font-weight: 700;
    color: #a5b4fc;
    letter-spacing: 0.3px;
    margin-top: 2px;
  }
  .header-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 7px;
  }
  .badge-tag {
    font-size: 7.3pt;
    font-weight: 600;
    padding: 2.5px 7.5px;
    border-radius: 5px;
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    color: #e2e8f0;
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }
  .badge-tag.highlight {
    background: rgba(99, 102, 241, 0.35);
    border-color: rgba(165, 180, 252, 0.6);
    color: #ffffff;
  }
  .badge-tag.emerald {
    background: rgba(16, 185, 129, 0.25);
    border-color: rgba(52, 211, 153, 0.5);
    color: #a7f3d0;
  }

  /* CONTACT BAR */
  .contact-bar {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 9px;
    padding-top: 9px;
    border-top: 1px solid rgba(255,255,255,0.12);
    font-size: 7.8pt;
    color: #cbd5e1;
  }
  .contact-item {
    display: inline-flex;
    align-items: center;
    gap: 4.5px;
  }
  .contact-item a {
    color: #cbd5e1;
    text-decoration: none;
  }
  .contact-item a:hover {
    color: #a5b4fc;
    text-decoration: underline;
  }
  .contact-item svg {
    width: 12px;
    height: 12px;
    color: #818cf8;
    flex-shrink: 0;
  }

  /* TWO COLUMN BODY */
  .cv-body {
    display: grid;
    grid-template-columns: 69mm 1fr;
    flex: 1;
    min-height: 0;
  }

  /* SIDEBAR (LEFT) */
  .sidebar {
    background: #f8fafc;
    border-right: 1.5px solid var(--border-light);
    padding: 14px 13px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  /* MAIN CONTENT (RIGHT) */
  .main-content {
    padding: 14px 18px;
    display: flex;
    flex-direction: column;
    gap: 11px;
    background: #ffffff;
  }

  /* SECTION HEADINGS */
  .section-h {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 8.8pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--primary);
    padding-bottom: 3.5px;
    border-bottom: 1.8px solid var(--primary);
    margin-bottom: 6px;
  }
  .section-h svg {
    width: 12.5px;
    height: 12.5px;
    color: var(--accent);
  }

  /* SIDEBAR CARDS */
  .side-card {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 7px;
    padding: 7px 9px;
    margin-bottom: 4px;
  }
  .side-card-title {
    font-size: 8.3pt;
    font-weight: 700;
    color: var(--primary);
    line-height: 1.25;
  }
  .side-card-sub {
    font-size: 7.2pt;
    color: var(--text-light);
    margin-top: 1.5px;
    font-weight: 500;
  }
  .side-card-desc {
    font-size: 7.2pt;
    color: var(--text-muted);
    margin-top: 3px;
    line-height: 1.35;
  }
  .side-card-badge {
    display: inline-block;
    font-size: 6.8pt;
    font-weight: 700;
    padding: 1px 5px;
    border-radius: 3.5px;
    background: var(--accent-subtle);
    color: var(--accent);
    margin-top: 2.5px;
    border: 1px solid rgba(99, 102, 241, 0.25);
  }

  /* SKILL GROUP */
  .skill-group {
    margin-bottom: 6.5px;
  }
  .skill-group-title {
    font-size: 7.6pt;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 2.5px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .skill-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 3px;
  }
  .skill-pill {
    font-size: 6.8pt;
    font-weight: 500;
    padding: 1.5px 5.5px;
    border-radius: 3.5px;
    background: #ffffff;
    border: 1px solid #cbd5e1;
    color: #1e293b;
    font-family: 'JetBrains Mono', monospace;
  }
  .skill-pill.core {
    background: var(--accent-subtle);
    border-color: rgba(99, 102, 241, 0.4);
    color: #312e81;
    font-weight: 700;
  }
  .skill-pill.green {
    background: var(--emerald-subtle);
    border-color: rgba(16, 185, 129, 0.4);
    color: #064e3b;
    font-weight: 700;
  }

  /* SUMMARY BOX */
  .summary-box {
    background: #f8fafc;
    border-left: 3px solid var(--accent);
    padding: 7px 10px;
    border-radius: 0 6px 6px 0;
    font-size: 7.8pt;
    color: #334155;
    line-height: 1.42;
  }
  .summary-box strong {
    color: #0f172a;
  }

  /* TIMELINE ITEM */
  .exp-item {
    margin-bottom: 9px;
  }
  .exp-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 1px;
  }
  .exp-role {
    font-size: 8.8pt;
    font-weight: 700;
    color: #0f172a;
  }
  .exp-period {
    font-size: 7.2pt;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    color: var(--accent);
    background: var(--accent-subtle);
    padding: 1px 5.5px;
    border-radius: 3.5px;
    border: 1px solid rgba(99, 102, 241, 0.2);
    white-space: nowrap;
  }
  .exp-company {
    font-size: 7.6pt;
    font-weight: 700;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    margin-bottom: 3.5px;
  }
  .exp-bullets {
    list-style: none;
    padding-left: 0;
  }
  .exp-bullets li {
    font-size: 7.6pt;
    color: #334155;
    margin-bottom: 3px;
    position: relative;
    padding-left: 10px;
    line-height: 1.36;
  }
  .exp-bullets li::before {
    content: "▪";
    position: absolute;
    left: 0;
    color: var(--accent);
    font-size: 7.5pt;
    line-height: 1;
    top: 1px;
  }

  .subproject-box {
    background: #f8fafc;
    border-left: 2.5px solid var(--accent);
    border-top: 1px solid #f1f5f9;
    border-right: 1px solid #f1f5f9;
    border-bottom: 1px solid #f1f5f9;
    border-radius: 0 5px 5px 0;
    padding: 4px 7px;
    margin-top: 3.5px;
    margin-bottom: 4px;
  }
  .subproject-title {
    font-size: 7.6pt;
    font-weight: 700;
    color: #1e1b4b;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .subproject-desc {
    font-size: 7.1pt;
    color: #475569;
    margin-top: 1.5px;
    line-height: 1.32;
  }
  .tech-inline {
    font-size: 6.8pt;
    font-family: 'JetBrains Mono', monospace;
    color: #4f46e5;
    font-weight: 600;
  }

  /* KEY PROJECT GRID */
  .proj-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
  }
  .proj-card {
    background: #f8fafc;
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 5.5px 7px;
  }
  .proj-h {
    font-size: 7.6pt;
    font-weight: 700;
    color: var(--primary);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .proj-tag {
    font-size: 6.2pt;
    font-weight: 700;
    padding: 0.8px 3.5px;
    border-radius: 2.5px;
    background: var(--emerald-subtle);
    color: var(--emerald);
    border: 0.8px solid rgba(5, 150, 105, 0.3);
  }
  .proj-desc {
    font-size: 6.9pt;
    color: #475569;
    margin-top: 2px;
    line-height: 1.28;
  }

  /* FOOTER */
  .cv-footer {
    background: #090e17;
    color: #94a3b8;
    padding: 5px 20px;
    font-size: 6.8pt;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255,255,255,0.08);
  }
  .cv-footer a {
    color: #a5b4fc;
    text-decoration: none;
    font-weight: 600;
  }
"""

def generate_vi_html():
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CV Nguyễn Thiên Định - Lập Trình Viên (Full-Stack &amp; IoT)</title>
  <style>
    {get_css()}
  </style>
</head>
<body>

  <!-- TOP ACTION BAR -->
  <div class="top-action-bar">
    <div class="brand-title">
      <span>📄 CV NGUYỄN THIÊN ĐỊNH</span>
      <span style="font-size: 11px; color: #a5b4fc;">• Full-Stack, ERP & Tự Động Hóa IoT</span>
    </div>
    <div class="actions">
      <button onclick="window.print()" class="btn-emerald">
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
        In / Lưu PDF (Ctrl + P)
      </button>
      <a href="CV_NguyenThienDinh_LapTrinhVien.pdf" download="CV_NguyenThienDinh_LapTrinhVien.pdf" class="btn-primary">
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
        Tải PDF Trực Tiếp
      </a>
      <a href="cv_en.html" class="btn-secondary">
        🌐 Switch to English (EN)
      </a>
      <a href="index.html" class="btn-secondary">
        ← Về Portfolio
      </a>
    </div>
  </div>

  <!-- A4 PAGE WRAPPER -->
  <div class="a4-page">
    
    <!-- HEADER -->
    <header class="cv-header">
      <div class="cv-header-grid">
        <div class="avatar-wrap">
          <img src="data:image/jpeg;base64,{avatar_b64}" alt="Nguyễn Thiên Định">
        </div>
        <div class="header-info">
          <h1 class="cand-name">Nguyễn Thiên Định</h1>
          <div class="cand-role">Lập Trình Viên · Full-Stack, ERP &amp; Tự Động Hóa IoT</div>
          
          <div class="header-badges">
            <span class="badge-tag highlight">★ Làm chủ độc lập dự án A–Z (Phân tích → Triển khai → Bảo trì)</span>
            <span class="badge-tag emerald">✓ TOEIC 745 (IIG Vietnam)</span>
            <span class="badge-tag">⚡ Gần 2 năm kinh nghiệm thực chiến</span>
            <span class="badge-tag">📍 Sẵn sàng Onboard ngay (On-site / Remote)</span>
          </div>

          <div class="contact-bar">
            <div class="contact-item">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              <span>0854 243 828</span>
            </div>
            <div class="contact-item">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              <a href="mailto:nguyenthiendinh.dev@gmail.com">nguyenthiendinh.dev@gmail.com</a>
            </div>
            <div class="contact-item">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
              <a href="https://nguyenthiendinh0973-max.github.io/portfolio/" target="_blank">nguyenthiendinh0973-max.github.io/portfolio</a>
            </div>
            <div class="contact-item">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              <span>Ninh Kiều, TP. Cần Thơ</span>
            </div>
          </div>
        </div>
      </div>
    </header>

    <!-- BODY -->
    <div class="cv-body">
      
      <!-- SIDEBAR (LEFT) -->
      <aside class="sidebar">
        
        <!-- HỌC VẤN -->
        <div>
          <div class="section-h">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
            <span>Học Vấn</span>
          </div>
          <div class="side-card">
            <div class="side-card-title">ĐH Kỹ Thuật - Công Nghệ Cần Thơ</div>
            <div class="side-card-sub">Kỹ Sư Kỹ Thuật Phần Mềm (2019 – 2024)</div>
            <div class="side-card-desc">
              • Tốt nghiệp loại <strong>Khá</strong>.<br>
              • Độc lập làm chủ toàn bộ vòng đời phát triển phần mềm (Full-Cycle Engineering) cho các hệ thống lớn.
            </div>
          </div>
        </div>

        <!-- CHỨNG CHỈ -->
        <div>
          <div class="section-h">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
            <span>Chứng Chỉ & Ngoại Ngữ</span>
          </div>
          <div class="side-card">
            <div class="side-card-title">TOEIC 745 Điểm</div>
            <div class="side-card-sub">Do IIG Vietnam cấp</div>
            <div class="side-card-desc">
              Đọc hiểu tài liệu kỹ thuật chuyên sâu; giao tiếp và phối hợp làm việc hiệu quả trong môi trường quốc tế.
            </div>
          </div>
        </div>

        <!-- BỘ KỸ NĂNG KỸ THUẬT -->
        <div>
          <div class="section-h">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
            <span>Ma Trận Kỹ Năng</span>
          </div>

          <div class="skill-group">
            <div class="skill-group-title">
              <span>Frontend & UI Engineering</span>
            </div>
            <div class="skill-pills">
              <span class="skill-pill core">ReactJS</span>
              <span class="skill-pill core">Tailwind CSS</span>
              <span class="skill-pill core">Bootstrap 5</span>
              <span class="skill-pill">jQuery</span>
              <span class="skill-pill">AJAX</span>
              <span class="skill-pill">JavaScript ES6+</span>
              <span class="skill-pill">HTML5/CSS3</span>
            </div>
          </div>

          <div class="skill-group">
            <div class="skill-group-title">
              <span>Backend & RESTful API</span>
            </div>
            <div class="skill-pills">
              <span class="skill-pill core">PHP / Laravel</span>
              <span class="skill-pill core">Node.js / Express</span>
              <span class="skill-pill">C# .NET</span>
              <span class="skill-pill core">RESTful API</span>
              <span class="skill-pill">JWT</span>
              <span class="skill-pill">SSO / RBAC</span>
              <span class="skill-pill">WebSockets</span>
            </div>
          </div>

          <div class="skill-group">
            <div class="skill-group-title">
              <span>Cơ Sở Dữ Liệu & Tối Ưu</span>
            </div>
            <div class="skill-pills">
              <span class="skill-pill green">MySQL</span>
              <span class="skill-pill green">SQL Server</span>
              <span class="skill-pill core">Tối ưu Query (+25%)</span>
              <span class="skill-pill">Stored Proc</span>
              <span class="skill-pill">Data Migration</span>
            </div>
          </div>

          <div class="skill-group">
            <div class="skill-group-title">
              <span>IoT, Tự Động Hóa & 3D Web</span>
            </div>
            <div class="skill-pills">
              <span class="skill-pill green">Google Apps Script</span>
              <span class="skill-pill green">Mascot 3D + Audio</span>
              <span class="skill-pill core">ESP32 / MQTT</span>
              <span class="skill-pill">Modbus</span>
              <span class="skill-pill">C# WinForms/WPF</span>
              <span class="skill-pill">SpeechAce AI</span>
            </div>
          </div>

          <div class="skill-group">
            <div class="skill-group-title">
              <span>Hạ Tầng, DevOps & Khác</span>
            </div>
            <div class="skill-pills">
              <span class="skill-pill">Git / GitHub PR</span>
              <span class="skill-pill">Docker căn bản</span>
              <span class="skill-pill">VPS Linux / Nginx SSL</span>
              <span class="skill-pill">CI/CD</span>
              <span class="skill-pill">QA/QC</span>
            </div>
          </div>

        </div>

      </aside>

      <!-- MAIN CONTENT (RIGHT) -->
      <main class="main-content">
        
        <!-- TÓM TẮT NĂNG LỰC -->
        <div>
          <div class="section-h">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            <span>Tóm Tắt Năng Lực & Mục Tiêu Nghề Nghiệp</span>
          </div>
          <div class="summary-box">
            Kỹ sư Kỹ thuật Phần mềm với <strong>gần 2 năm kinh nghiệm thực chiến</strong>, có năng lực <strong>độc lập làm chủ toàn bộ vòng đời các dự án lớn: từ phân tích yêu cầu, thiết kế kiến trúc, lập trình Full-Stack đến đóng gói installer, triển khai server production và bảo trì dài hạn</strong>. Thành thạo phát triển các hệ thống Dashboard quản trị doanh nghiệp với <strong>Laravel, PHP, Node.js, ReactJS, Tailwind CSS &amp; Bootstrap</strong>; chuyên sâu tối ưu hóa cơ sở dữ liệu (<strong>+25% tốc độ truy vấn</strong>), tự động hóa vận hành với <strong>Google Apps Script</strong> và tích hợp thiết bị phần cứng <strong>IoT (MQTT / ESP32 / C# .NET)</strong>. Từng tích hợp thành công <strong>Mascot 3D tương tác + Audio sinh động</strong> trên Web. Sở hữu chứng chỉ <strong>TOEIC 745</strong> (IIG Vietnam), sẵn sàng đảm nhận vai trò Full-Stack / ERP Developer hoặc Onboard dự án mới.
          </div>
        </div>

        <!-- KINH NGHIỆM LÀM VIỆC THỰC CHIẾN -->
        <div>
          <div class="section-h">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
            <span>Kinh Nghiệm Làm Việc Thực Chiến</span>
          </div>

          <!-- Mốc 1: Genius Openwide Global -->
          <div class="exp-item">
            <div class="exp-header">
              <span class="exp-role">Lập Trình Viên (Full-Stack &amp; IoT)</span>
              <span class="exp-period">01/2025 – 04/2026</span>
            </div>
            <div class="exp-company">CÔNG TY CỔ PHẦN ĐẦU TƯ GIÁO DỤC GENIUS OPENWIDE GLOBAL</div>

            <!-- Sub 1 -->
            <div class="subproject-box">
              <div class="subproject-title">
                <span>1. EduPortal Enterprise Workspace System (01–10/2025)</span>
                <span class="tech-inline">Flutter · Express · MySQL · WebSockets · SSO</span>
              </div>
              <div class="subproject-desc">
                Cổng giáo dục &amp; điều hành nội bộ tích hợp <strong>SSO + RBAC phân quyền bảo mật</strong>, Chat/Helpdesk real-time qua WebSockets, đóng gói ứng dụng <strong>Windows Installer</strong> và trực tiếp triển khai hạ tầng máy chủ production.
              </div>
            </div>

            <!-- Sub 2 -->
            <div class="subproject-box">
              <div class="subproject-title">
                <span>2. Học Liệu Số &amp; Tích Hợp Thanh Toán / Phần Cứng (11/2025–01/2026)</span>
                <span class="tech-inline">Node.js · ESP32 · MQTT · VNPay/Stripe · Docker</span>
              </div>
              <div class="subproject-desc">
                Xây dựng Backend đa vai trò, tích hợp cổng thanh toán <strong>VNPay / Stripe</strong> qua Webhook bảo mật, kết nối thiết bị <strong>ESP32 qua MQTT</strong> in hóa đơn tự động theo sự kiện đơn hàng, cấu hình máy chủ VPS Linux / Nginx SSL và CI/CD với Codemagic.
              </div>
            </div>

            <!-- Sub 3 -->
            <div class="subproject-box">
              <div class="subproject-title">
                <span>3. Hệ Thống Thi Tiếng Anh Đa Nền Tảng (01–04/2026)</span>
                <span class="tech-inline">Flutter Desktop · Audio DSP · SpeechAce AI · Excel</span>
              </div>
              <div class="subproject-desc">
                Phát triển app thi PC + Web Admin Dashboard chấm thi nói, tích hợp bộ xử lý âm thanh <strong>Audio DSP + SpeechAce AI</strong> nhận diện phát âm, ngân hàng đề thi đa dạng và xuất báo cáo Excel tự động — <strong style="color: #047857;">tiết kiệm 80% thời gian tổng hợp kết quả</strong>.
              </div>
            </div>
          </div>

          <!-- Mốc 2: Chiến Thắng -->
          <div class="exp-item">
            <div class="exp-header">
              <span class="exp-role">Lập Trình Viên Module &amp; Tối Ưu CSDL</span>
              <span class="exp-period">06/2024 – 10/2024</span>
            </div>
            <div class="exp-company">TRUNG TÂM GDNN ĐÀO TẠO &amp; SÁT HẠCH LÁI XE CHIẾN THẮNG</div>
            <ul class="exp-bullets">
              <li>Phát triển các module chức năng quản lý cốt lõi: hồ sơ học viên, điều phối lịch sát hạch và hệ thống trích xuất báo cáo kiểm định.</li>
              <li>Tối ưu hóa CSDL MySQL, tái cấu trúc (refactor) các câu query phức tạp giúp giảm thời gian phản hồi và nâng cao hiệu năng hệ thống.</li>
              <li>Thực hiện quy trình QA/QC: kiểm thử chức năng, tái hiện lỗi, lập log tracking và trực tiếp sửa lỗi (bug fixing) toàn hệ thống.</li>
              <li>Quản lý mã nguồn Git chuyên nghiệp: chiến lược phân nhánh (branching strategy), tạo Pull Request và giải quyết merge conflict.</li>
            </ul>
          </div>

          <!-- Mốc 3: Freelance -->
          <div class="exp-item" style="margin-bottom: 0;">
            <div class="exp-header">
              <span class="exp-role">Kỹ Sư Phần Mềm Tự Do (Freelance &amp; Dự Án Kỹ Thuật)</span>
              <span class="exp-period">06/2023 – Hiện tại</span>
            </div>
            <div class="exp-company">LÀM VIỆC TỰ DO / DỰ ÁN KỸ THUẬT &amp; THIẾT BỊ NGOẠI VI</div>
            <ul class="exp-bullets">
              <li>Tích hợp thiết bị ngoại vi vào hệ thống tự động: kết nối cảm biến đo lường, vi điều khiển (ESP32/Arduino) và PLC qua giao thức <strong>MQTT, WebSockets, Modbus</strong> phục vụ thu thập telemetry theo thời gian thực.</li>
              <li>Phát triển phần mềm ứng dụng Desktop PC (<strong>C# .NET WinForms / WPF</strong>) điều khiển thiết bị, hiển thị đồ thị kỹ thuật real-time; phát triển Web Dashboard (<strong>Node.js, PHP/Laravel, ReactJS, Tailwind/Bootstrap</strong>) giám sát từ xa.</li>
              <li>Tích hợp thành công <strong>Mascot 3D tương tác Web + Hiệu ứng âm thanh sinh động</strong> (Audio DSP).</li>
              <li>Hạ tầng &amp; bảo mật: cấu hình và quản trị máy chủ VPS Linux, cài đặt chứng chỉ SSL/Nginx, tối ưu hóa tốc độ tải trang web.</li>
            </ul>
          </div>

        </div>

        <!-- DỰ ÁN TIÊU BIỂU -->
        <div>
          <div class="section-h">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            <span>Dự Án Tiêu Biểu &amp; Sản Phẩm Bàn Giao</span>
          </div>
          <div class="proj-grid">
            <div class="proj-card">
              <div class="proj-h">
                <span>EduPortal Enterprise Workspace</span>
                <span class="proj-tag">✓ Production</span>
              </div>
              <div class="proj-desc">Cổng giáo dục tích hợp SSO/RBAC, Chat/Helpdesk real-time qua WebSockets, đóng gói Windows Installer.</div>
            </div>
            <div class="proj-card">
              <div class="proj-h">
                <span>In Hóa Đơn Tự Động ESP32 &amp; VNPay</span>
                <span class="proj-tag">✓ Hoàn thành</span>
              </div>
              <div class="proj-desc">Backend đa vai trò, webhook thanh toán trực tuyến, vi điều khiển ESP32 kích hoạt máy in qua MQTT.</div>
            </div>
            <div class="proj-card">
              <div class="proj-h">
                <span>Hệ Thống Thi Nói SpeechAce AI</span>
                <span class="proj-tag">Tiết kiệm 80%</span>
              </div>
              <div class="proj-desc">Ứng dụng thi PC + Web Admin, tích hợp Audio DSP và SpeechAce AI chấm điểm Speaking tự động.</div>
            </div>
            <div class="proj-card">
              <div class="proj-h">
                <span>Google Apps Script &amp; Query Optimizer</span>
                <span class="proj-tag">+25% Speedup</span>
              </div>
              <div class="proj-desc">Tự động hóa đồng bộ Google Sheets ↔ Database, tối ưu hóa truy vấn Stored Procedures &amp; Indexing.</div>
            </div>
          </div>
        </div>

      </main>

    </div>

  </div>

</body>
</html>"""

def generate_en_html():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Resume - Nguyen Thien Dinh | Software Developer (Full-Stack &amp; IoT)</title>
  <style>
    {get_css()}
  </style>
</head>
<body>

  <!-- TOP ACTION BAR -->
  <div class="top-action-bar">
    <div class="brand-title">
      <span>📄 RESUME: NGUYEN THIEN DINH</span>
      <span style="font-size: 11px; color: #a5b4fc;">• Software Developer · Full-Stack &amp; IoT Automation</span>
    </div>
    <div class="actions">
      <button onclick="window.print()" class="btn-emerald">
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
        Print / Save PDF (Ctrl + P)
      </button>
      <a href="CV_NguyenThienDinh_SoftwareDeveloper.pdf" download="CV_NguyenThienDinh_SoftwareDeveloper.pdf" class="btn-primary">
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
        Download PDF Directly
      </a>
      <a href="cv.html" class="btn-secondary">
        🇻🇳 Chuyển sang Tiếng Việt (VI)
      </a>
      <a href="index.html" class="btn-secondary">
        ← Back to Portfolio
      </a>
    </div>
  </div>

  <!-- A4 PAGE WRAPPER -->
  <div class="a4-page">
    
    <!-- HEADER -->
    <header class="cv-header">
      <div class="cv-header-grid">
        <div class="avatar-wrap">
          <img src="data:image/jpeg;base64,{avatar_b64}" alt="Nguyen Thien Dinh">
        </div>
        <div class="header-info">
          <h1 class="cand-name">Nguyen Thien Dinh</h1>
          <div class="cand-role">Software Developer · Full-Stack, ERP &amp; IoT Automation</div>
          
          <div class="header-badges">
            <span class="badge-tag highlight">★ Full-Lifecycle Ownership: Requirements → Deployment → Maintenance</span>
            <span class="badge-tag emerald">✓ TOEIC 745 (IIG Vietnam)</span>
            <span class="badge-tag">⚡ ~2 Years Practical Experience</span>
            <span class="badge-tag">📍 Available for On-site / Remote / Hybrid</span>
          </div>

          <div class="contact-bar">
            <div class="contact-item">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              <span>(+84) 0854 243 828</span>
            </div>
            <div class="contact-item">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              <a href="mailto:nguyenthiendinh.dev@gmail.com">nguyenthiendinh.dev@gmail.com</a>
            </div>
            <div class="contact-item">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
              <a href="https://nguyenthiendinh0973-max.github.io/portfolio/" target="_blank">nguyenthiendinh0973-max.github.io/portfolio</a>
            </div>
            <div class="contact-item">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              <span>Can Tho City, Vietnam</span>
            </div>
          </div>
        </div>
      </div>
    </header>

    <!-- BODY -->
    <div class="cv-body">
      
      <!-- SIDEBAR (LEFT) -->
      <aside class="sidebar">
        
        <!-- EDUCATION -->
        <div>
          <div class="section-h">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
            <span>Education</span>
          </div>
          <div class="side-card">
            <div class="side-card-title">Can Tho Univ. of Technology (CTUT)</div>
            <div class="side-card-sub">B.S. in Software Engineering (2019 – 2024)</div>
            <div class="side-card-desc">
              • Graduated with <strong>Good standing</strong>.<br>
              • Proven ability to independently lead large-scale systems: end-to-end delivery from requirements to production maintenance.
            </div>
          </div>
        </div>

        <!-- CERTIFICATIONS -->
        <div>
          <div class="section-h">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
            <span>Credentials & Languages</span>
          </div>
          <div class="side-card">
            <div class="side-card-title">TOEIC 745 Certificate</div>
            <div class="side-card-sub">Issued by IIG Vietnam</div>
            <div class="side-card-desc">
              Fluent comprehension of deep technical documentation; confident business communication and agile collaboration.
            </div>
          </div>
        </div>

        <!-- TECHNICAL SKILLSET -->
        <div>
          <div class="section-h">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
            <span>Technical Skill Matrix</span>
          </div>

          <div class="skill-group">
            <div class="skill-group-title">
              <span>Frontend & UI Engineering</span>
            </div>
            <div class="skill-pills">
              <span class="skill-pill core">ReactJS</span>
              <span class="skill-pill core">Tailwind CSS</span>
              <span class="skill-pill core">Bootstrap 5</span>
              <span class="skill-pill">jQuery</span>
              <span class="skill-pill">AJAX</span>
              <span class="skill-pill">JavaScript ES6+</span>
              <span class="skill-pill">HTML5/CSS3</span>
            </div>
          </div>

          <div class="skill-group">
            <div class="skill-group-title">
              <span>Backend & RESTful APIs</span>
            </div>
            <div class="skill-pills">
              <span class="skill-pill core">PHP / Laravel</span>
              <span class="skill-pill core">Node.js / Express</span>
              <span class="skill-pill">C# .NET</span>
              <span class="skill-pill core">RESTful API</span>
              <span class="skill-pill">JWT</span>
              <span class="skill-pill">SSO / RBAC</span>
              <span class="skill-pill">WebSockets</span>
            </div>
          </div>

          <div class="skill-group">
            <div class="skill-group-title">
              <span>Databases & Optimization</span>
            </div>
            <div class="skill-pills">
              <span class="skill-pill green">MySQL</span>
              <span class="skill-pill green">SQL Server</span>
              <span class="skill-pill core">Query Tuning (+25%)</span>
              <span class="skill-pill">Stored Proc</span>
              <span class="skill-pill">Data Migration</span>
            </div>
          </div>

          <div class="skill-group">
            <div class="skill-group-title">
              <span>IoT, Automation & 3D Web</span>
            </div>
            <div class="skill-pills">
              <span class="skill-pill green">Google Apps Script</span>
              <span class="skill-pill green">3D Mascot + Audio</span>
              <span class="skill-pill core">ESP32 / MQTT</span>
              <span class="skill-pill">Modbus</span>
              <span class="skill-pill">C# WinForms/WPF</span>
              <span class="skill-pill">SpeechAce AI</span>
            </div>
          </div>

          <div class="skill-group">
            <div class="skill-group-title">
              <span>DevOps, Infrastructure & Tools</span>
            </div>
            <div class="skill-pills">
              <span class="skill-pill">Git / GitHub PR</span>
              <span class="skill-pill">Docker basics</span>
              <span class="skill-pill">VPS Linux / Nginx SSL</span>
              <span class="skill-pill">CI/CD</span>
              <span class="skill-pill">QA/QC</span>
            </div>
          </div>

        </div>

      </aside>

      <!-- MAIN CONTENT (RIGHT) -->
      <main class="main-content">
        
        <!-- EXECUTIVE SUMMARY -->
        <div>
          <div class="section-h">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            <span>Executive Summary & Professional Profile</span>
          </div>
          <div class="summary-box">
            Software Engineer with <strong>nearly 2 years of hands-on experience</strong> and proven capability to <strong>independently lead large-scale software systems: from requirements analysis, system architecture, Full-Stack engineering to packaging installers, server deployments, and long-term maintenance</strong>. Extensive experience architecting enterprise administration dashboards with <strong>Laravel, PHP, Node.js, ReactJS, Tailwind CSS &amp; Bootstrap</strong>; database query optimization (<strong>+25% query speedup</strong>); workflow automation via <strong>Google Apps Script</strong> and hardware integration with <strong>IoT (MQTT / ESP32 / C# .NET)</strong>. Proven record implementing interactive <strong>3D Web Mascots + Live Audio DSP</strong>. Certified with <strong>TOEIC 745</strong> (IIG Vietnam).
          </div>
        </div>

        <!-- PROFESSIONAL WORK EXPERIENCE -->
        <div>
          <div class="section-h">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
            <span>Professional Work Experience</span>
          </div>

          <!-- Role 1: Genius Openwide Global -->
          <div class="exp-item">
            <div class="exp-header">
              <span class="exp-role">Software Engineer (Full-Stack &amp; IoT)</span>
              <span class="exp-period">01/2025 – 04/2026</span>
            </div>
            <div class="exp-company">GENIUS OPENWIDE GLOBAL EDUCATION INVESTMENT JSC</div>

            <!-- Sub 1 -->
            <div class="subproject-box">
              <div class="subproject-title">
                <span>1. EduPortal Enterprise Workspace System (01–10/2025)</span>
                <span class="tech-inline">Flutter · Express · MySQL · WebSockets · SSO</span>
              </div>
              <div class="subproject-desc">
                Architected internal education &amp; administration hub with <strong>SSO + RBAC role-based authorization</strong>, real-time Chat/Helpdesk via WebSockets, packaged <strong>Windows Installer</strong>, and managed production server deployments.
              </div>
            </div>

            <!-- Sub 2 -->
            <div class="subproject-box">
              <div class="subproject-title">
                <span>2. Digital Learning &amp; Payment / Hardware Integration (11/2025–01/2026)</span>
                <span class="tech-inline">Node.js · ESP32 · MQTT · VNPay/Stripe · Docker</span>
              </div>
              <div class="subproject-desc">
                Engineered multi-role Backend, integrated online payments via secure <strong>VNPay / Stripe Webhooks</strong>, connected <strong>ESP32 over MQTT</strong> for automated invoice receipt printing on order events, configured Linux VPS with Nginx SSL, and established Codemagic CI/CD pipelines.
              </div>
            </div>

            <!-- Sub 3 -->
            <div class="subproject-box">
              <div class="subproject-title">
                <span>3. Cross-Platform English Speaking Examination System (01–04/2026)</span>
                <span class="tech-inline">Flutter Desktop · Audio DSP · SpeechAce AI · Excel</span>
              </div>
              <div class="subproject-desc">
                Developed PC desktop examination app &amp; Web Admin Dashboard, integrating <strong>Audio DSP + SpeechAce AI API</strong> for pronunciation evaluation, dynamic question banks, and automated Excel reporting — <strong style="color: #047857;">saving 80% manual aggregation time</strong>.
              </div>
            </div>
          </div>

          <!-- Role 2: Chien Thang -->
          <div class="exp-item">
            <div class="exp-header">
              <span class="exp-role">Module Developer &amp; Database Tuning Engineer</span>
              <span class="exp-period">06/2024 – 10/2024</span>
            </div>
            <div class="exp-company">CHIEN THANG DRIVER TRAINING &amp; TESTING VOCATIONAL EDUCATION CENTER</div>
            <ul class="exp-bullets">
              <li>Engineered core modules for student profiles, examination scheduling, and certification reporting.</li>
              <li>Tuned MySQL databases, refactoring complex queries to significantly reduce server latency and improve throughput.</li>
              <li>Conducted QA/QC testing: functional test scripts, bug replication, issue logging, and direct codebase bug fixes.</li>
              <li>Maintained professional Git workflows: branching models, code review Pull Requests, and merge conflict resolution.</li>
            </ul>
          </div>

          <!-- Role 3: Freelance -->
          <div class="exp-item" style="margin-bottom: 0;">
            <div class="exp-header">
              <span class="exp-role">Freelance Software &amp; IoT Automation Engineer</span>
              <span class="exp-period">06/2023 – Present</span>
            </div>
            <div class="exp-company">INDEPENDENT CONTRACTOR / TECHNICAL &amp; HARDWARE PROJECTS</div>
            <ul class="exp-bullets">
              <li>Integrated peripherals into automated systems: connected measurement sensors, MCUs (ESP32/Arduino), and PLCs via <strong>MQTT, WebSockets, Modbus</strong> for real-time telemetry streaming.</li>
              <li>Built PC Desktop applications (<strong>C# .NET WinForms / WPF</strong>) for hardware telemetry and charting; developed Web Dashboards (<strong>Node.js, PHP/Laravel, ReactJS, Tailwind/Bootstrap</strong>) for remote equipment monitoring.</li>
              <li>Successfully integrated <strong>Interactive 3D Web Mascot + Live Audio DSP sound effects</strong>.</li>
              <li>Infrastructure: managed Linux VPS instances, installed Nginx SSL certificates, optimized page load speeds.</li>
            </ul>
          </div>

        </div>

        <!-- KEY DELIVERABLES -->
        <div>
          <div class="section-h">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            <span>Key Project Deliverables</span>
          </div>
          <div class="proj-grid">
            <div class="proj-card">
              <div class="proj-h">
                <span>EduPortal Enterprise Workspace</span>
                <span class="proj-tag">✓ Production</span>
              </div>
              <div class="proj-desc">Internal enterprise hub with SSO/RBAC, real-time WebSockets chat, and Windows Installer deployment.</div>
            </div>
            <div class="proj-card">
              <div class="proj-h">
                <span>Automated Hardware Invoice Printer</span>
                <span class="proj-tag">✓ Completed</span>
              </div>
              <div class="proj-desc">Multi-role backend, online payment webhooks, triggering ESP32 thermal receipt printer via MQTT.</div>
            </div>
            <div class="proj-card">
              <div class="proj-h">
                <span>SpeechAce AI Speaking Exam App</span>
                <span class="proj-tag">80% Time Saved</span>
              </div>
              <div class="proj-desc">Desktop PC + Web Admin with Audio DSP &amp; SpeechAce AI for automatic speech assessment &amp; Excel reports.</div>
            </div>
            <div class="proj-card">
              <div class="proj-h">
                <span>Google Apps Script &amp; Query Tuning</span>
                <span class="proj-tag">+25% Speedup</span>
              </div>
              <div class="proj-desc">Google Sheets ↔ Database two-way sync, Stored Procedure optimization &amp; index tuning.</div>
            </div>
          </div>
        </div>

      </main>

    </div>

  </div>

</body>
</html>"""

# Write HTML files
cv_vi_path = os.path.join(workspace, "cv.html")
cv_en_path = os.path.join(workspace, "cv_en.html")

with open(cv_vi_path, "w", encoding="utf-8") as f:
    f.write(generate_vi_html())
print(f"Generated {cv_vi_path}")

with open(cv_en_path, "w", encoding="utf-8") as f:
    f.write(generate_en_html())
print(f"Generated {cv_en_path}")

# Run Chrome headless to render PDFs
chrome_bin = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
pdf_vi = os.path.join(workspace, "CV_NguyenThienDinh_LapTrinhVien.pdf")
pdf_en = os.path.join(workspace, "CV_NguyenThienDinh_SoftwareDeveloper.pdf")

import time

def safe_copy(src, dst):
    for attempt in range(5):
        try:
            shutil.copy2(src, dst)
            print(f"Copied to: {os.path.basename(dst)}")
            return
        except Exception as e:
            time.sleep(0.5)
    print(f"Warning: could not update {os.path.basename(dst)} (file may be open in viewer)")

def render_pdf(html_path, out_pdf):
    temp_pdf = out_pdf + ".tmp.pdf"
    if os.path.exists(temp_pdf):
        try:
            os.remove(temp_pdf)
        except Exception:
            pass
    cmd = [
        chrome_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        f"--print-to-pdf={temp_pdf}",
        "--no-pdf-header-footer",
        html_path
    ]
    print(f"Rendering {out_pdf}...")
    subprocess.run(cmd, check=True)
    safe_copy(temp_pdf, out_pdf)
    if os.path.exists(temp_pdf):
        try:
            os.remove(temp_pdf)
        except Exception:
            pass
    if os.path.exists(out_pdf):
        size = os.path.getsize(out_pdf)
        print(f"Success! {out_pdf} size: {size} bytes")

render_pdf(cv_vi_path, pdf_vi)
render_pdf(cv_en_path, pdf_en)

# Copy to professional application names & maintain backward compatibility
copies_vi = [
    os.path.join(workspace, "CV - Nguyễn Thiên Định - Lập Trình Viên.pdf"),
    os.path.join(workspace, "CV_NguyenThienDinh_Executive.pdf"),
    os.path.join(workspace, "CV_NguyenThienDinh_v2.pdf"),
    os.path.join(workspace, "CV_NguyenThienDinh_Pro.pdf"),
    os.path.join(workspace, "CV_NguyenThienDinh.pdf"),
    os.path.join(workspace, "CV Nguyễn Thiên Định - Chuyên Viên Lập Trình.pdf")
]
for target in copies_vi:
    safe_copy(pdf_vi, target)

copies_en = [
    os.path.join(workspace, "CV_NguyenThienDinh_Executive_EN.pdf")
]
for target in copies_en:
    safe_copy(pdf_en, target)

print("All tasks completed successfully!")
