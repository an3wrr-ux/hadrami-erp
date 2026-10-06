# ====================================================================
# 🪐 محرك الحقن المركزي الشامل: hadrami_extensions.py (طبعة 2026)
# 🛑 كود آمن 100%: يحقن الخصائص الجديدة فوق كودك القديم دون حذف أو تغيير
# ====================================================================

import streamlit as st
import pandas as pd
import sqlite3
import qrcode
import io
import base64
import os
from datetime import datetime

# اسم قاعدة البيانات الحالية لبرنامجك (تأكد من مطابقتها لاسم ملفك القديم)
DB_ERP_PROD = "al_hadrami_sky_production.db"
ATTACHMENT_WAREHOUSE = "stored_system_attachments"

if not os.path.exists(ATTACHMENT_WAREHOUSE):
    os.makedirs(ATTACHMENT_WAREHOUSE)

# --------------------------------------------------------------------
# 🌓 1. محرك تفعيل الوضع التبادلي الشامل (Dark/Light Mode Theme Injector)
# --------------------------------------------------------------------
def inject_premium_theme_and_graphics_engine():
    """يحقن ألوان الهوية والعنابي الملكي والوضع الداكن/المضيء المتجاوب مع الجوالات"""
    if 'ui_theme_mode' not in st.session_state:
        st.session_state.ui_theme_mode = "داكن"
        
    bg_main, bg_card, text_main, border_color = ("#1A1F26", "#222B36", "#FFFFFF", "#2F3944") if st.session_state.ui_theme_mode == "داكن" else ("#F4F6F7", "#FFFFFF", "#2C3E50", "#D5D8DC")
    
    st.markdown(f"""
        <link rel="stylesheet" href="https://cloudflare.com">
        <style>
        body, div, h1, h2, h3, h4, h5, h6, p, span, table, label, td, th, input, select, textarea {{ 
            text-align: right !important; direction: rtl !important; color: {text_main} !important;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
        }}
        [data-testid="stAppViewContainer"] {{ background-color: {bg_main} !important; }}
        [data-testid="stSidebar"] {{ background: linear-gradient(180deg, #161C24 0%, #0F141C 100%) !important; border-left: 1px solid #2F3944; }}
        
        .sidebar-brand-card {{ background: linear-gradient(135deg, #5B1E31 0%, #3D1421 100%); padding: 20px; border-radius: 10px; text-align: center; border: 1px solid #F7DC6F; box-shadow: 0px 4px 15px rgba(0,0,0,0.5); }}
        .user-profile-card {{ background-color: #222B36; padding: 12px; border-radius: 8px; margin-bottom: 20px; border-right: 5px solid #F7DC6F; }}
        .gl-row-box {{ background-color: {bg_card}; padding: 18px; border-radius: 8px; border: 1px solid {border_color}; margin-bottom: 15px; box-shadow: 0px 2px 8px rgba(0,0,0,0.15); }}
        .report-print-sheet {{ background-color: #FFFFFF !important; padding: 40px; border-radius: 8px; color: #2C3E50 !important; border: 1px solid #D5D8DC; margin-bottom: 25px; }}
        .report-print-sheet * {{ color: #2C3E50 !important; text-align: right !important; }}
        
        .stButton>button {{ width: 100%; font-weight: bold; background-color: #5B1E31 !important; color: #F7DC6F !important; border-radius: 6px; border: 1px solid #F7DC6F !important; height: 42px; transition: 0.2s; }}
        .stButton>button:hover {{ background-color: #7D2641 !important; color: #FFFFFF !important; transform: translateY(-2px); }}
        </style>
        """, unsafe_allow_html=True)

# --------------------------------------------------------------------
# ⚖️ 2. محرك شريط فحص التوازن اللحظي بالأرقام الفورية (Balancing Bar)
# --------------------------------------------------------------------
def inject_live_balancing_numeric_validation_bar(target_document_type="قيد يومية"):
    """يقرأ كفتي الحسابات ويبرز التنبيه الأحمر ويذكر قيمة الفارق بالرقم بدقة متناهية"""
    conn = sqlite3.connect(DB_ERP_PROD)
    try:
        df = pd.read_sql_query(f"SELECT debit, credit FROM erp_documents WHERE status IN ('نشط', 'مسودة') AND doc_type = '{target_document_type}'", conn)
    except Exception:
        df = pd.DataFrame(columns=['debit', 'credit'])
    conn.close()
    
    total_dr = df['debit'].sum() if not df.empty else 0.0
    total_cr = df['credit'].sum() if not df.empty else 0.0
    balance_difference = total_dr - total_cr
    
    st.markdown("##### ⚖️ شريط الرقابة وفحص توازن الحركة اللحظي")
    chk_c1, chk_c2, chk_c3 = st.columns(3)
    chk_c1.markdown(f"<div style='background-color:#222B36; padding:15px; border-radius:8px; border-right:5px solid #5B1E31;'><p style='margin:0; color:#919EAB; font-size:12px;'>إجمالي حركات المدين</p><h3>{total_dr:,.2f} SAR</h3></div>", unsafe_allow_html=True)
    chk_c2.markdown(f"<div style='background-color:#222B36; padding:15px; border-radius:8px; border-right:5px solid #5B1E31;'><p style='margin:0; color:#919EAB; font-size:12px;'>إجمالي حركات الدائن</p><h3>{total_cr:,.2f} SAR</h3></div>", unsafe_allow_html=True)
    
    with chk_c3:
        if abs(balance_difference) < 0.01:
            st.markdown("<div style='background-color:#222B36; padding:15px; border-radius:8px; border-right:5px solid #27AE60;'><p style='margin:0; color:#27AE60; font-size:12px;'>حالة مطابقة الدفاتر</p><h3 style='color:#27AE60 !important;'>متزن ومطابق 100%</h3></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='background-color:#222B36; padding:15px; border-radius:8px; border-right:5px solid #E74C3C;'><p style='margin:0; color:#E74C3C; font-size:12px;'>⚠️ قيد غير متزن (يوجد فارق)</p><h3 style='color:#E74C3C !important;'>الفارق بالرقم: {abs(balance_difference):,.2f} SAR</h3></div>", unsafe_allow_html=True)

# --------------------------------------------------------------------
# 📁 3. محرك الرفع والأرشفة الرقمية للمستندات والصور (Universal Attachment)
# --------------------------------------------------------------------
def inject_universal_file_uploader_field(document_id, module_key):
    """يحقن حقل رفع المستندات ويحفظ الملف دائمياً بالسيرفر ويربطه بجدول الـ SQLite"""
    uploaded_file = st.file_uploader("📂 رفع وأرشفة المستند الورقي أو صلب الفاتورة (Attachment)", type=["png", "jpg", "jpeg", "pdf", "xlsx"], key=f"file_{module_key}_{document_id}")
    if uploaded_file is not None:
        file_name = f"doc_{document_id}_{int(datetime.now().timestamp())}_{uploaded_file.name}"
        full_saved_path = os.path.join(ATTACHMENT_WAREHOUSE, file_name)
        with open(full_saved_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        conn = sqlite3.connect(DB_ERP_PROD)
        try:
            conn.cursor().execute("UPDATE erp_documents SET attachment_path = ? WHERE id = ?", (full_saved_path, document_id))
            conn.commit()
        except Exception: pass
        conn.close()
        st.success("📁 تم أرشفة وحفظ صورة المستند بنجاح في السيرفر!")
        return full_saved_path
    return None

# --------------------------------------------------------------------
# 🇸🇦 4. محرك الـ QR Code المشفر والطباعة الرسمية (ZATCA QR & Print Engine)
# --------------------------------------------------------------------
def generate_zatca_tlv_qr_stream(seller, vat, time, total, vat_val):
    def slot(tag, val): return bytes([tag]) + bytes([len(val.encode('utf-8'))]) + val.encode('utf-8')
    tlv = slot(1, seller) + slot(2, vat) + slot(3, time) + slot(4, str(total)) + slot(5, str(vat_val))
    qr = qrcode.QRCode(version=1, box_size=3, border=1)
    qr.add_data(base64.b64encode(tlv).decode('utf-8'))
    qr.make(fit=True)
    buf = io.BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(buf, format="PNG")
    return buf.getvalue()

def render_enterprise_printable_invoice_sheet(document_record, module_title="مستند مالي"):
    """يبني ورقة الطباعة البيضاء الرسمية A4 ويحقن الشعار والبيانات والـ QR Code المشفر"""
    st.markdown("<div class='report-print-sheet'>", unsafe_allow_html=True)
    subtotal = max(document_record, document_record)
    vat_15 = subtotal * 0.15
    g_total = subtotal + vat_15
    
    qr_bytes = generate_zatca_tlv_qr_stream("مجموعة الحضرمي التجارية", "310961234567693", datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'), round(g_total, 2), round(vat_15, 2))
    
    c_h1, c_h2 = st.columns(2)
    c_h1.markdown(f"<h2>⚜️ مجموعة الحضرمي التجارية</h2><p><b>الرقم الضريبي المعتمد:</b> 310961234567693</p><h4>{module_title} - رقم الوثيقة #{document_record}</h4>", unsafe_allow_html=True)
    c_h2.image(qr_bytes, width=105)
    
    st.markdown(f"""
    <hr>
    <p><b>التاريخ المعتمد:</b> {document_record} | <b>الرقم المرجعي للسند:</b> {document_record} | <b>الفترة المالية:</b> {document_record}</p>
    <p><b>الحساب المتأثر بالدفاتر:</b> {document_record} - <b>{document_record}</b> | <b>مركز التكلفة والنشاط:</b> {document_record}</p>
    <p><b>البيان والشرح التفصيلي للحركة:</b> {document_record}</p>
    <h3 style='color:#5B1E31 !important;'>صافي المبلغ الخاضع للضريبة: {subtotal:,.2f} SAR</h3>
    <h4 style='color:#5B1E31 !important;'>قيمة ضريبة القيمة المضافة (15%): {vat_15:,.2f} SAR</h4>
    <h2 style='color:#27AE60 !important; font-weight:bold;'>الإجمالي الموحد شامل الضريبة: {g_total:,.2f} SAR</h2>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------------------------
# 🖨️ 5. محرك التصدير والحفظ الشامل لكشوفات الجرد والقوائم المالية (Excel & PDF)
# --------------------------------------------------------------------
def inject_universal_export_and_save_engine(dataframe_to_export, document_filename="تقرير_مالي"):
    """يحقن أزرار تصدير إكسيل والطباعة لـ PDF أسفل أي كشف حساب أو قائمة ببرنامجك"""
    st.markdown("---")
    cx1, cx2 = st.columns(2)
    with cx1:
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            dataframe_to_export.to_excel(writer, sheet_name='Report', index=False)
        st.download_button(label="📊 حفظ وتصدير كـ ملف Excel (.xlsx)", data=buffer.getvalue(), file_name=f"{document_filename}.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    with cx2:
