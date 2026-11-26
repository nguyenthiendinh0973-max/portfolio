import re
import os
import subprocess
import pypdf
import pypdfium2 as pdfium
from PIL import Image

import test_modern_template

with open(r'd:\1\slides\build_cvs.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Replace get_css() with get_modern_css()
new_css = test_modern_template.get_modern_css()
pattern_css = r'def get_css\(\):.*?return """.*?"""'
code = re.sub(pattern_css, f'def get_css():\n    return """{new_css}"""', code, count=1, flags=re.DOTALL)

# 2. Update generate_vi_html: header title and badges
code = code.replace(
    '<div class="cand-role">Lập Trình Viên · Full-Stack, ERP &amp; Tự Động Hóa IoT</div>',
    '<div class="cand-role">Kỹ Sư Phần Mềm · Full-Stack Web, ERP &amp; Tự Động Hóa IoT</div>'
)
code = code.replace(
    '<span class="badge-tag highlight">★ Làm chủ độc lập dự án A–Z (Phân tích → Triển khai → Bảo trì)</span>',
    '<span class="badge-tag highlight">★ Độc lập làm chủ dự án A–Z (Phân tích → Triển khai → Vận hành)</span>'
)

# 3. Update footer text to clean modern style in VI
code = code.replace(
    'NGUYỄN THIÊN ĐỊNH · CHUYÊN VIÊN LẬP TRÌNH (FULL-STACK, ERP &amp; IoT)',
    'NGUYỄN THIÊN ĐỊNH · HỒ SƠ ỨNG VIÊN LẬP TRÌNH VIÊN'
)

# 4. Update footer text to clean modern style in EN
code = code.replace(
    'NGUYEN THIEN DINH · SOFTWARE DEVELOPER (FULL-STACK, ERP &amp; IoT)',
    'NGUYEN THIEN DINH · SOFTWARE DEVELOPER RESUME'
)

with open(r'd:\1\slides\build_cvs.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_cvs.py updated with modern design successfully!")
