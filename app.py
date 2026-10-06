import streamlit as st
import pandas as pd
import datetime
import qrcode
import io
import base64
import random
import json
import hadrami_extensions as ext

# حقن وتفعيل الهوية المرئية والوضع الداكن/المضيء وتنسيق التقارير في كامل البرنامج
ext.inject_premium_theme_and_graphics_engine()

# ====================================================================
# 1. تهيئة النواة المحاسبية الفوق-مؤسسية الكبرى وقواعد البيانات اللامحدودة
# ====================================================================
if 'app_name' not in st.session_state:
    st.session_state.app_name = "دفتر الحضرمي ERP - الإصدار العالمي الفوق-مطلق رقم 1"
if 'owner_name' not in st.session_state:
    st.session_state.owner_name = "مجموعة الحضرمي المالية والصناعية القابضة"
if 'company_logo' not in st.session_state:
    st.session_state.company_logo = None
if 'theme_selection' not in st.session_state:
    st.session_state.theme_selection = "SAP Business One Theme (الأزرق الملكي)"

if 'warehouses_db' not in st.session_state:
    st.session_state.warehouses_db = ["مستودع مكة المركزي - بضائع الحج", "مستودع المدينة المنورة - بضائع العمرة", "مستودع خط الإنتاج والتصنيع"]

if 'audit_trail_log' not in st.session_state:
    st.session_state.audit_trail_log = pd.DataFrame([
        {"التاريخ والوقت": str(datetime.datetime.now()), "المستخدم": "System", "العملية المنفذة": "تأسيس النواة البرمجية العالمية ومحاكاة الشاشات الكبرى للـ SAP & Onyx Pro", "الأثر الهيكلي": "مستقر وأمن آلياً ✅"}
    ])

if 'employees_db' not in st.session_state:
    st.session_state.employees_db = pd.DataFrame([
        {"الرقم الوظيفي": "EMP-001", "الاسم": "أحمد المحاسب المالي", "القسم": "المالية", "الراتب الأساسي": 10000.0, "بدل السكن": 2500.0, "بدل مواصلات": 1000.0, "التأمينات (GOSI)": 1000.0, "أيام الغياب": 0, "ساعات الإضافي": 15},
        {"الرقم الوظيفي": "EMP-002", "الاسم": "عمر مشرف كاشير POS", "القسم": "التشغيل", "الراتب الأساسي": 6000.0, "بدل السكن": 1500.0, "بدل مواصلات": 500.0, "التأمينات (GOSI)": 600.0, "أيام الغياب": 0, "ساعات الإضافي": 20}
    ])

if 'bom_db' not in st.session_state:
    st.session_state.bom_db = {
        "حقائب ومستلزمات الحج الفاخرة": [
            {"المادة الخام": "جلد طبيعي / قماش معالج", "الكمية المطلوبة": 1.5, "التكلفة التقديرية للمادة (SAR)": 15.0},
            {"المادة الخام": "أحزمة وإكسسوارات معدنية", "الكمية المطلوبة": 4.0, "التكلفة التقديرية للمادة (SAR)": 2.0}
        ]
    }

if 'inventory_db' not in st.session_state:
    st.session_state.inventory_db = pd.DataFrame([
        {"كود الصنف": "SKU-100", "المستودع": "مستودع مكة المركزي - بضائع الحج", "بيان المنتج": "حقائب ومستلزمات الحج الفاخرة", "النوع": "منتج جاهز", "إجمالي الوارد": 600, "إجمالي المنصرف": 100, "الكمية الحالية": 500, "تكلفة الوحدة": 45.0, "سعر البيع": 85.0, "تاريخ الانتهاء": "2028-12-31"},
        {"كود الصنف": "RAW-01", "المستودع": "مستودع خط الإنتاج والتصنيع", "بيان المنتج": "جلد طبيعي / قماش معالج", "النوع": "مادة خام", "إجمالي الوارد": 3000, "إجمالي المنصرف": 500, "الكمية الحالية": 2500, "تكلفة الوحدة": 15.0, "سعر البيع": 0.0, "تاريخ الانتهاء": "2027-02-15"}
    ])

if 'partners_equity' not in st.session_state:
    st.session_state.partners_equity = pd.DataFrame([
        {"اسم الشريك": "الشريك الأول - الحضرمي", "رأس المال المدخل": 400000.0, "نسبة الحصة (%)": 40.0, "المسحوبات": 0.0},
        {"اسم الشريك": "الشريك الثاني - باوزير", "رأس المال المدخل": 300000.0, "نسبة الحصة (%)": 30.0, "المسحوبات": 0.0},
        {"اسم الشريك": "الشريك الثالث - البار", "رأس المال المدخل": 200000.0, "نسبة الحصة (%)": 20.0, "المسحوبات": 0.0},
        {"اسم الشريك": "الشريك الرابع - العمودي", "رأس المال المدخل": 100000.0, "نسبة الحصة (%)": 10.0, "المسحوبات": 0.0}
    ])

if 'users_db' not in st.session_state:
    st.session_state.users_db = pd.DataFrame([
        {
            "اسم المستخدم": "admin", "كلمة المرور": "حضرمي2026", 
            "البريد الإلكتروني": "admin@hadrami-erp.com", "رقم الهاتف": "+966500000000",
            "الدور": "Super Admin", "المخزن المتاح": "كافة المخازن",
            "صلاحية_العمليات": True, "صلاحية_التقارير": True, "صلاحية_التبويبات_الحساسة": True
        }
    ])

if 'company_info' not in st.session_state:
    st.session_state.company_info = {
        "vat_number": "300000000000003",
        "national_address": "طريق الملك عبد العزيز، الأبراج التجارية، الرياض، المملكة العربية السعودية",
        "phone": "+966500000000",
        "license_number": "LIC-2026-9982",
        "fiscal_year": "2026"
    }

if 'journal' not in st.session_state:
    st.session_state.journal = pd.DataFrame([
        {"رقم القيد": 1, "التاريخ": datetime.date.today(), "كود الحساب": 110201, "اسم الحساب": "الأصول المتداولة - البنوك - حساب بنك الراجحي جاري (SAR)", "البيان والشرح التفصيلي": "رصيد نقدية بنكي جاري افتتاحي معتمد للمنشأة", "المستودع": "كافة المخازن", "مركز التكلفة": "الإدارة العامة - الرياض", "مدين (SAR)": 500000.0, "دائن (SAR)": 0.0, "المسؤول": "System"}
    ])

if 'offline_pos_queue' not in st.session_state: st.session_state.offline_pos_queue = []
if 'current_user' not in st.session_state: st.session_state.current_user = None
if 'user_allowed_wh' not in st.session_state: st.session_state.user_allowed_wh = "كافة المخازن"
if 'cost_centers' not in st.session_state: st.session_state.cost_centers = ["فرع مكة المكرمة - موسم الحج", "فرع مكة المكرمة - موسم العمرة", "الإدارة العامة - الرياض"]
if 'currencies' not in st.session_state: st.session_state.currencies = {"SAR": 1.0, "USD": 3.75, "EUR": 4.00}
if 'otp_generated' not in st.session_state: st.session_state.otp_generated = None
if 'temp_user_login' not in st.session_state: st.session_state.temp_user_login = None

if 'coa' not in st.session_state:
    st.session_state.coa = {
        110101: {"name": "الأصول المتداولة - النقدية بالصندوق الرئيسي (كاش)", "type": "أصول", "category": "أصول متداولة"},
        110201: {"name": "الأصول المتداولة - البنوك - حساب بنك الراجحي جاري (SAR)", "type": "أصول", "category": "أصول متداولة"},
        110203: {"name": "الأصول المتداولة - حساب وسيط شبكة مدى والفيزا ونقاط البيع", "type": "أصول", "category": "أصول متداولة"},
        110301: {"name": "الأصول المتداولة - مخزون المنتجات التامة والجاهزة للبيع", "type": "أصول", "category": "أصول متداولة"},
        110302: {"name": "الأصول المتداولة - مخزون المواد الخام والأولية للتصنيع", "type": "أصول", "category": "أصول متداولة"},
        110401: {"name": "الأصول المتداولة - ذمم العملاء والبعثات والشركات الزميلة", "type": "أصول", "category": "أصول متداولة"},
        210101: {"name": "الالتزامات المتداولة - ذمم الموردين والمقاولين التجاريين", "type": "التزامات", "category": "الالتزامات المتداولة"},
        210201: {"name": "الالتزامات المتداولة - حساب أمانات ضريبة المخرجات VAT 15%", "type": "التزامات", "category": "الالتزامات المتداولة"},
        210301: {"name": "الالتزامات المتداولة - مخصص ومستحقات هيئة الزكاة والضريبة والجمارك", "type": "التزامات", "category": "الالتزامات المتداولة"},
        210401: {"name": "الالتزامات المتداولة - حساب الأجور والرواتب المستحقة للموظفين", "type": "التزامات", "category": "الالتزامات المتداولة"},
        310101: {"name": "حقوق الملكية - رأس المال المدفوع - جاري الشركاء الموحد", "type": "حقوق ملكية", "category": "حقوق الملكية"},
        410101: {"name": "إيرادات النشاط - عوائد عقود ومبيعات موسم الحج والعمرة", "type": "إيرادات", "category": "إيرادات والنشاط"},
        510101: {"name": "التكاليف المباشرة - تكلفة استهلاك المواد الخام والتشغيل الصناعي", "type": "تكاليف", "category": "تكلفة المبيعات"},
        610101: {"name": "مصروفات عمومية - نفقات الأجور ورواتب الكادر الإداري والعمومي", "type": "مصروفات", "category": "مصروفات تشغيلية"}
    }

if st.session_state.current_user is None:
    st.title(f"🏛️ تسجيل الدخول الآمن - {st.session_state.app_name}")
    if st.session_state.otp_generated is None:
        with st.form("بوابة تسجيل الدخول الأولى"):
            u_input = st.text_input("اسم المستخدم الإداري المعرّف:")
            p_input = st.text_input("كلمة المرور السرية للحساب:", type="password")
            if st.form_submit_button("🔓 طلب رمز المصادقة (OTP)"):
                match = st.session_state.users_db[(st.session_state.users_db["اسم المستخدم"] == u_input) & (st.session_state.users_db["كلمة المرور"] == p_input)]
                if not match.empty:
                    st.session_state.otp_generated = str(random.randint(100000, 999999))
                    st.session_state.temp_user_login = match.iloc
                    st.rerun()
                else: st.error("❌ خطأ حرج: بيانات الدخول المدخلة غير صحيحة.")
    else:
        st.info(f"📲 تم إرسال رسالة نصية SMS تحتوي على الـ OTP إلى جوالك الخاص: ({st.session_state.temp_user_login['رقم الهاتف']})")
        st.code(f"🔓 [لوحة المحاكاة العالمية لشبكة الجوال]: الرمز السري الحالي هو: {st.session_state.otp_generated}")
        with st.form("التحقق من صحة الشخص"):
            otp_in = st.text_input("أدخل رمز التأكيد المؤلف من 6 خانات لتأكيد الهوية:")
            if st.form_submit_button("🛡️ فتح شاشات الـ ERP"):
                if otp_in == st.session_state.otp_generated:
                    u_data = st.session_state.temp_user_login
                    st.session_state.current_user = u_data["اسم المستخدم"]
                    st.session_state.user_allowed_wh = u_data["المخزن المتاح"]
                    st.session_state.otp_generated = None
                    st.rerun()
                else: st.error("❌ الرمز المدخل غير مطابق لرسالة التأكيد.")
    st.stop()

selected_color = "#1B365D"
st.markdown(f"""
    <style>
    .reportview-container .main .block-container{{ direction: rtl; text-align: right; }}
    div.stButton > button:first-child {{ background-color: {selected_color}; color: white; border-radius: 6px; font-weight: bold; width: 100%; border: none; height: 42px; }}
    .sidebar .sidebar-content {{ direction: rtl; text-align: right; background-color: #1F2937; }}
    h1, h2, h3, h4 {{ color: {selected_color}; text-align: right; font-family: 'Segoe UI', sans-serif; font-weight: 700; }}
    .stTabs [data-baseweb="tab"] {{ font-size: 13px; font-weight: bold; color: {selected_color}; }}
    </style>
    """, unsafe_allow_html=True)

def generate_zatca_qr(seller_name, vat_reg_num, timestamp, total_amt, vat_amt):
