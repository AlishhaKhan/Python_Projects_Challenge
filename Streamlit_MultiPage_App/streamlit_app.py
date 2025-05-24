import streamlit as st

# --- Page Setup ---
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon="😊",
    default=True,
)
project_1_page = st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    icon="📊",
)
project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chatbot",
    icon="🤖",
)

# --- Page Navigation --- [Without Section]
# page = st.navigation(pages=[about_page, project_1_page, project_2_page])

# Navigation Setup --- [With Section]
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)

# --- Sharred on all pages ---
st.logo("assets/codingisfun_logo.png")
st.sidebar.text("Made with ❤ by Alisha")

# --- Run Navigation ---
pg.run()  # <- This is the correct variable
