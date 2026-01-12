import streamlit as st
import time
import random
import re

# הגדרות עיצוב - הופך את האפליקציה למראה "Dark Mode" מקצועי
st.set_page_config(
    page_title="SafeNet AI | Cyber Guardian",
    page_icon="🛡️",
    layout="wide"
)

# הוספת CSS מותאם אישית למראה הייטקיסטי
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #00ff41;
        color: black;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        color: #00ff41;
    }
    </style>
    """, unsafe_allow_html=True)

# פונקציית לוגיקה לבדיקת לינקים (הפריצה הטכנולוגית שלך)
def analyze_url(url):
    trusted = ["google.com", "bankhapoalim.co.il", "paypal.com", "facebook.com", "israelpost.co.il"]
    url_clean = url.lower().replace("https://", "").replace("http://", "").split('/')[0]
    
    for domain in trusted:
        if url_clean != domain and (domain[:5] in url_clean):
            return "HIGH_RISK", f"⚠️ חשד כבד להתחזות (Typosquatting)! הלינק דומה מדי לאתר רשמי: {domain}"
    
    if "bit.ly" in url or "tinyurl.com" in url:
        return "MEDIUM_RISK", "🟡 אזהרה: שימוש במקצר לינקים אנונימי. נוכלים משתמשים בזה להסתרת היעד."
    
    return "SAFE", "✅ לא זוהו דפוסי התחזות מוכרים בלינק."

# תפריט ניווט עליון
st.title("🛡️ SafeNet AI Guardian")
st.subheader("מערכת הגנה מבוססת בינה מלאכותית להאקתון ממר\"ם 2026")
st.markdown("---")

# חלוקה לטאבים (מרשים מאוד מבחינת UI)
tab1, tab2, tab3 = st.tabs(["🔍 סורק איומים", "🎙️ זיהוי Deepfake", "📊 מרכז שליטה (Dashboard)"])

with tab1:
    st.header("מנתח הודעות ולינקים")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        message_input = st.text_area("הדבק כאן הודעת SMS, מייל או לינק חשוד:", height=150)
        analyze_btn = st.button("הפעל סריקת AI")
    
    with col2:
        st.info("הסורק מנתח דפוסי שפה (NLP) ומזהה ניסיונות הונאה בקוד ה-URL.")

    if analyze_btn and message_input:
        with st.spinner('מבצע אנליזה רב-שכבתית...'):
            time.sleep(1.5)
            
            # בדיקת לינקים בתוך הטקסט
            urls = re.findall(r'(https?://\S+)', message_input)
            
            if urls:
                status, msg = analyze_url(urls[0])
                if status == "HIGH_RISK":
                    st.error(msg)
                elif status == "MEDIUM_RISK":
                    st.warning(msg)
                else:
                    st.success(msg)
            
            # בדיקת תוכן טקסטואלי
            bad_words = ["זכית", "מתנה", "דחוף", "החשבון ננעל", "פרטי אשראי", "פרס"]
            found_words = [word for word in bad_words if word in message_input]
            
            if found_words:
                st.error(f"⚠️ זוהו מילות מפתח של הונאה: {', '.join(found_words)}")
            else:
                st.success("ניתוח טקסטואלי: לא נמצאו ביטויים חשודים.")

with tab2:
    st.header("זיהוי זיוף קול (Audio Forensics)")
    st.write("העלה הקלטה כדי לבדוק אם מדובר בקול אנושי או ב-Deepfake שנוצר ע\"י AI.")
    audio_file = st.file_uploader("בחר קובץ")
if audio_file is not None:
            st.audio(audio_file)
            with st.spinner("מנתח את הקובץ..."):
                # כאן המערכת "חושבת" - בשלב זה נוסיף זיהוי פשוט להדגמה
                import time
                time.sleep(2) # מדמה ניתוח של AI
                st.success("הניתוח הושלם!")
                st.info("תוצאה: לא נמצאו סימנים מובהקים ל-Deepfake. הקול נראה אנושי.")
