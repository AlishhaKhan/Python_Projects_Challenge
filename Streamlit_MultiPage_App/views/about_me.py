import os
import streamlit as st

# --- Contact Dialog using st.dialog ---
@st.dialog("Contact Me")
def show_contact_form():
    st.write("### Contact Form")
    st.text_input("First Name")
    st.text_input("Email")
    st.text_area("Message")
    if st.button("Send"):
        st.success("Message sent! ✅")

# --- Profile Image Safe Load ---
image_path = "assets/profile_image.png"
if os.path.exists(image_path):
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(image_path, width=230)
else:
    st.warning("⚠️ Profile image not found. Please add it to the `assets` folder.")
    col1, col2 = st.columns(2, gap="small")  # Still render layout

# --- Textual Info ---
with col2:
    st.title("Alisha Khan", anchor=False)
    st.subheader("Full Stack Developer | Machine Learning Engineer | AI Enthusiast")
    st.write(
        "Welcome to my portfolio! Here, you can explore my projects, skills, and experiences "
        "in the field of data science and machine learning."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()
        
# --- Experience & Qualifications ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - Strong hands-on experience and knowledge in Python, machine learning, and AI.
    - Good understanding of multiple programming languages.
    - Proficient in data analysis, model building, and deployment.
    """
)

# --- Skills ---
st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    - **Programming Languages**: Python, Next.JS, TypeScript
    - **Machine Learning**: Scikit-learn, TensorFlow, Keras
    - **Data Visualization**: Matplotlib, Seaborn, Plotly
    - **Tools & Technologies**: Git, Docker, Streamlit, Vercel
    - **Soft Skills**: Problem-solving, Communication, Teamwork
    """
)
