from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Jasser Hedhli"
PAGE_ICON = ":wave:"
NAME = "Jasser Hedhli"
DESCRIPTION = """
Software Developer | Data Scientist | GenAI Enthusiast
"""
EMAIL = "jesserhedhli@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/jasser-hedhli",
    "GitHub": "https://github.com/JasserHedhli",
}

PROJECTS = {
    "🏆 LangGraph Agent UI - LangChain & Gradio": "Customizable System Prompts: Tailor your AI agent to specific use cases",
    "🏆 Travel Itinerary Planner - LangChain & Gradio": "Create a personalized day trip itinerary based on your preferred destination and interests ",
    "🏆 Invoice Data Extraction Tool - GeminiAPI & Streamlit": "Extract, store data on SQLite and Ineract with it",
    "🏆 Customer Support System - Langchain & Gradio": "Categorizes queries, analyzes sentiment, and provides automated responses ",
    "🏆 Smart Glasses - OCR & YOLOv4 & gTTs": "Object detection, emotion detection, floor detection, read a book, voice assistant ",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Experienced in data science, machine learning, deep learning and software development.
- ✔️ Proficient in Python, TensorFlow, Streamlit, and SQL.
- ✔️ Expertise in developing interactive dashboards and AI-driven applications.
- ✔️ Good understanding of statistical principles and their respective applications
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, Java, SQL, JavaScript, R
- 📊 Data Visualization: Power BI, Streamlit, Gradio, Matplotlib
- 📚 ML/DL: TensorFlow, scikit-learn, KMeans, RandomForest, SOM
- 🗄️ Databases: SQLite, SSMS, MongoDB, Cassandra
- ☁️ Cloud & DevOps: Docker, Microsoft Azure, MLOps (ZenML)
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Scientist | Sherpa Engineering MENA**")
st.write("07/2024 - 08/2024 - Present")
st.write(
    """
- ► Optimized thermal comfort in electric vehicles using machine learning.
- ► Developed a web app for deployment using Docker and automated model creation with MLOps (ZenML).
- ► Created KMeans and SOM models for vehicle thermal analysis.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Scientist | STB Bank**")
st.write("07/2023 - Hybrid")
st.write(
    """
- ► Developed a Power BI dashboard for cash prediction with 90% accuracy (XGBRegressor).
- ► Performed branch clustering using KMeans.
- ► Built an interactive Python interface combining BI and predictive analytics for cash management simulation.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Artificial Intelligence Programmer | Québec Training Center**")
st.write("06/2023 - Remote")
st.write(
    """
- ► Completed a summer internship at Quebec Training Center focusing on facial emotion recognition.
- ► Developed a project utilizing Python, TensorFlow, DeepFace, OpenCV, and the MobileNetv2 model.
- ► Implemented a voice assistant to verbally convey detected emotions.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Data Scientist | BNA Bank**")
st.write("02/2022 - 04/2022 - Hybrid")
st.write(
    """
- ► Led credit forecasting and risk assessment using supervised machine learning.
- ► Developed a real-time credit risk evaluation app using Streamlit with SQLite for database management.
- ► Designed dashboards with Power BI and performed ETL processes with SSIS.
"""
)

# --- JOB 5
st.write('\n')
st.write("🚧", "**Data Scientist | STB Bank**")
st.write("07/2021 - Hybrid")
st.write(
    """
- ► Led a project on real estate price prediction in Tunisia, involving data collection from major websites using Selenium.
- ► Developed a Flask web application to showcase forecasts generated by various machine learning models.
- ► Provided decision-makers with valuable insights for evaluating real estate investment opportunities.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
