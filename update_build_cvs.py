import re
import os

with open(r'd:\1\slides\build_cvs.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update get_css()
new_css_func = '''def get_css():
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
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    color: var(--text-main);
    background-color: #cbd5e1;
    line-height: 1.34;
    font-size: 8.35pt;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  /* TOP ACTION BAR */
  .top-action-bar {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: #0f172a;
    color: white;
    padding: 8px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
  }
  .top-action-bar .brand-title {
    font-size: 13px;
    font-weight: 700;
    color: #e2e8f0;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .top-action-bar .actions {
    display: flex;
    gap: 8px;
    align-items: center;
  }
  .top-action-bar a, .top-action-bar button {
    background: #4f46e5;
    color: white;
    border: none;
    padding: 6px 14px;
    border-radius: 6px;
    font-size: 11.5px;
    font-weight: 600;
    cursor: pointer;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    transition: all 0.2s;
  }
  .top-action-bar a:hover, .top-action-bar button:hover {
    background: #4338ca;
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
    height: 297mm;
    margin: 15px auto;
    background: #ffffff;
    box-shadow: 0 10px 30px rgba(0,0,0,0.12);
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
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
      page-break-after: avoid;
    }
  }

  /* HEADER BLOCK */
  .cv-header {
    background: linear-gradient(135deg, #090e17 0%, #161938 55%, #0d1322 100%);
    color: white;
    padding: 13px 22px 11px 22px;
    border-bottom: 2.5px solid #4f46e5;
    flex-shrink: 0;
  }
  .cv-header-grid {
    display: flex;
    align-items: center;
    gap: 15px;
  }
  .avatar-wrap {
    width: 72px;
    height: 72px;
    border-radius: 12px;
    overflow: hidden;
    border: 2px solid rgba(255,255,255,0.9);
    box-shadow: 0 4px 12px rgba(0,0,0,0.35);
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
    font-size: 17.5pt;
    font-weight: 800;
    letter-spacing: -0.3px;
    line-height: 1.1;
    color: #ffffff;
    text-transform: uppercase;
  }
  .cand-role {
    font-size: 9.2pt;
    font-weight: 700;
    color: #a5b4fc;
    letter-spacing: 0.2px;
    margin-top: 1.5px;
  }
  .header-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
    margin-top: 4px;
  }
  .badge-tag {
    font-size: 6.9pt;
    font-weight: 600;
    padding: 1.5px 5.5px;
    border-radius: 3.5px;
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    color: #e2e8f0;
    display: inline-flex;
    align-items: center;
    gap: 3px;
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
    gap: 10px;
    margin-top: 5px;
    padding-top: 5px;
    border-top: 1px solid rgba(255,255,255,0.12);
    font-size: 7.4pt;
    color: #cbd5e1;
  }
  .contact-item {
    display: inline-flex;
    align-items: center;
    gap: 3.5px;
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
    width: 10.5px;
    height: 10.5px;
    color: #818cf8;
    flex-shrink: 0;
  }

  /* TWO COLUMN BODY */
  .cv-body {
    display: grid;
    grid-template-columns: 65mm 1fr;
    flex: 1;
    min-height: 0;
  }

  /* SIDEBAR (LEFT) */
  .sidebar {
    background: #f8fafc;
    border-right: 1.5px solid var(--border-light);
    padding: 10px 10px 8px 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  /* MAIN CONTENT (RIGHT) */
  .main-content {
    padding: 10px 13px 8px 13px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: #ffffff;
  }

  /* SECTION HEADINGS */
  .section-h {
    display: flex;
    align-items: center;
    gap: 4.5px;
    font-size: 8pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.35px;
    color: var(--primary);
    padding-bottom: 2px;
    border-bottom: 1.5px solid var(--primary);
    margin-bottom: 3.5px;
  }
  .section-h svg {
    width: 11px;
    height: 11px;
    color: var(--accent);
  }

  /* SIDEBAR CARDS */
  .side-card {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 5px;
    padding: 4px 6.5px;
    margin-bottom: 2.5px;
  }
  .side-card-title {
    font-size: 7.6pt;
    font-weight: 700;
    color: var(--primary);
    line-height: 1.2;
  }
  .side-card-sub {
    font-size: 6.8pt;
    color: var(--text-light);
    margin-top: 1px;
    font-weight: 500;
  }
  .side-card-desc {
    font-size: 6.8pt;
    color: var(--text-muted);
    margin-top: 1.5px;
    line-height: 1.28;
  }

  /* SKILL GROUP */
  .skill-group {
    margin-bottom: 3px;
  }
  .skill-group-title {
    font-size: 7.1pt;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 1.5px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .skill-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 2.5px;
  }
  .skill-pill {
    font-size: 6.4pt;
    font-weight: 500;
    padding: 1px 4px;
    border-radius: 3px;
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
    padding: 4.5px 8px;
    border-radius: 0 4px 4px 0;
    font-size: 7.3pt;
    color: #334155;
    line-height: 1.32;
  }
  .summary-box strong {
    color: #0f172a;
  }

  /* TIMELINE ITEM */
  .exp-item {
    margin-bottom: 4.5px;
  }
  .exp-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 1px;
  }
  .exp-role {
    font-size: 8pt;
    font-weight: 700;
    color: #0f172a;
  }
  .exp-period {
    font-size: 6.7pt;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    color: var(--accent);
    background: var(--accent-subtle);
    padding: 0.5px 4px;
    border-radius: 3px;
    border: 1px solid rgba(99, 102, 241, 0.2);
    white-space: nowrap;
  }
  .exp-company {
    font-size: 7pt;
    font-weight: 700;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.2px;
    margin-bottom: 1.5px;
  }
  .exp-bullets {
    list-style: none;
    padding-left: 0;
  }
  .exp-bullets li {
    font-size: 7pt;
    color: #334155;
    margin-bottom: 1.5px;
    position: relative;
    padding-left: 8px;
    line-height: 1.28;
  }
  .exp-bullets li::before {
    content: "▪";
    position: absolute;
    left: 0;
    color: var(--accent);
    font-size: 6.8pt;
    line-height: 1;
    top: 1px;
  }

  .subproject-box {
    background: #f8fafc;
    border-left: 2px solid var(--accent);
    border-top: 1px solid #f1f5f9;
    border-right: 1px solid #f1f5f9;
    border-bottom: 1px solid #f1f5f9;
    border-radius: 0 4px 4px 0;
    padding: 2.5px 5px;
    margin-top: 1.5px;
    margin-bottom: 2px;
  }
  .subproject-title {
    font-size: 7pt;
    font-weight: 700;
    color: #1e1b4b;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .subproject-desc {
    font-size: 6.7pt;
    color: #475569;
    margin-top: 1px;
    line-height: 1.24;
  }
  .tech-inline {
    font-size: 6.4pt;
    font-family: 'JetBrains Mono', monospace;
    color: #4f46e5;
    font-weight: 600;
  }

  /* KEY PROJECT GRID */
  .proj-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3.5px;
  }
  .proj-card {
    background: #f8fafc;
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 3.5px 5.5px;
  }
  .proj-h {
    font-size: 7pt;
    font-weight: 700;
    color: var(--primary);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .proj-tag {
    font-size: 5.8pt;
    font-weight: 700;
    padding: 0.5px 2.5px;
    border-radius: 2px;
    background: var(--emerald-subtle);
    color: var(--emerald);
    border: 0.5px solid rgba(5, 150, 105, 0.3);
  }
  .proj-desc {
    font-size: 6.5pt;
    color: #475569;
    margin-top: 1px;
    line-height: 1.22;
  }

  /* FOOTER */
  .cv-footer {
    background: #0f172a;
    color: #94a3b8;
    padding: 4px 18px;
    font-size: 6.6pt;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255,255,255,0.12);
    flex-shrink: 0;
  }
  .cv-footer a {
    color: #a5b4fc;
    text-decoration: none;
    font-weight: 600;
  }
"""'''

pattern_css = r'def get_css\(\):.*?return """.*?"""'
code = re.sub(pattern_css, new_css_func, code, count=1, flags=re.DOTALL)

# 2. Add footer in generate_vi_html
vi_footer_html = """        </div>

      </main>

    </div>

    <!-- FOOTER BAR -->
    <footer class="cv-footer">
      <div>NGUYỄN THIÊN ĐỊNH · CHUYÊN VIÊN LẬP TRÌNH (FULL-STACK, ERP &amp; IoT)</div>
      <div>
        <a href="https://nguyenthiendinh0973-max.github.io/portfolio/" target="_blank">nguyenthiendinh0973-max.github.io/portfolio</a>
        &nbsp;•&nbsp; 0854 243 828 &nbsp;•&nbsp; nguyenthiendinh.dev@gmail.com
      </div>
    </footer>

  </div>

</body>
</html>\"\"\""""

pattern_vi_end = r'        </div>\s*</main>\s*</div>\s*</div>\s*</body>\s*</html>"""'
code = re.sub(pattern_vi_end, vi_footer_html, code, count=1)

# 3. Add footer in generate_en_html
en_footer_html = """        </div>

      </main>

    </div>

    <!-- FOOTER BAR -->
    <footer class="cv-footer">
      <div>NGUYEN THIEN DINH · SOFTWARE DEVELOPER (FULL-STACK, ERP &amp; IoT)</div>
      <div>
        <a href="https://nguyenthiendinh0973-max.github.io/portfolio/" target="_blank">nguyenthiendinh0973-max.github.io/portfolio</a>
        &nbsp;•&nbsp; (+84) 854 243 828 &nbsp;•&nbsp; nguyenthiendinh.dev@gmail.com
      </div>
    </footer>

  </div>

</body>
</html>\"\"\""""

code = re.sub(pattern_vi_end, en_footer_html, code, count=1)

# 4. In copies_vi list, ensure CV_NguyenThienDinh_A4_Chuan.pdf is added
if 'CV_NguyenThienDinh_A4_Chuan.pdf' not in code:
    code = code.replace(
        'copies_vi = [',
        'copies_vi = [\n    os.path.join(workspace, "CV_NguyenThienDinh_A4_Chuan.pdf"),'
    )

with open(r'd:\1\slides\build_cvs.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_cvs.py updated successfully!")
