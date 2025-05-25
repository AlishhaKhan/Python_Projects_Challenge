from pathlib import Path
import streamlit as st
from PIL import Image

# --- Path Settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- General Settings ---
PAGE_TITLE = "Digital CV | Alisha Khan"
PAGE_ICON = ":wave:"
NAME = "Alisha Khan"
DESCRIPTION = "Full Stack Developer | AI Enthusiast | Cloud-Native App Developer"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/alishakhan/",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
    "Youtube": "https://www.youtube.com",
}
PROJECTS = {
    "🏆 Data Visualization": "https:/github.com",
    "🏆 AI Chatbot Development": "https://github.com",
    "🏆 Web Application Development": "https://github.com",
    "🏆 Secure Data Encryption": "https://github.com",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- Load CSS, Pdf & Profile Pic ---
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic_image = Image.open(profile_pic)

# --- Hero Section ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic_image, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📪", "alisha@example.com")  # Add your email here

# --- Social Media Links ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Experience & Qualifications ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - **AI Agentic Engineer** (2025 - Present)
    - **Cloud-Native App Development** (2023 - 2024)
    - **Bachelor of ADP in Economics** from University of Karachi (2019 - 2023)
    """
)

# --- Expertise Section ---
st.write("#")
st.subheader("Expertise")
st.write(
     """
    - Strong hands-on experience and knowledge in Python, machine learning, and AI.
    - Good understanding of multiple programming languages.
    - Proficient in data analysis, model building, and deployment.
    - Excellent problem-solving skills with a focus on AI-driven solutions.
    """
)

# --- Skills Section ---
st.write("#")
st.subheader("Skills")
st.write(
       """
    - **Programming Languages**: Python, Next.JS, TypeScript
    - **Machine Learning**: Scikit-learn, TensorFlow, Keras
    - **Data Visualization**: Matplotlib, Seaborn, Plotly
    - **Tools & Technologies**: Git, Docker, Streamlit, Vercel
    - **Soft Skills**: Problem-solving, Communication, Teamwork
    """
)

# --- Work History ---
st.write("#")
st.subheader("Work History")
st.write("---")
  
# Job
st.write("Full Stack Developer at XYZ Corp")
st.write("Jan 2023 - Present")
st.write(
    """
    - Developed and maintained web applications using Next.JS and TypeScript.
    - Collaborated with cross-functional teams to deliver high-quality software solutions.
    - Implemented RESTful APIs and integrated third-party services.
    """
)



# Projects & Accomplishments
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"- [{project}]({link})") 