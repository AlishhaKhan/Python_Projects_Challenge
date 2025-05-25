import streamlit as st
import random  
import string

# --- Function to generate password ---
def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters  # a-z + A-Z

    if use_digits:
        characters += string.digits    # 0-9

    if use_special_chars:
        characters += string.punctuation  # !@#$%^&*()...

    if not characters:
        return "Please select at least one character type."

    return ''.join(random.choice(characters) for _ in range(length))


# --- Streamlit App Layout ---
st.set_page_config("Password Generator", page_icon="🔐")
st.title("🔐 Password Generator")

length = st.slider("Password Length", min_value=8, max_value=32, value=12)

use_digits = st.checkbox("Include Digits", value=True)
use_special = st.checkbox("Include Special Characters", value=True)

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"Generated Password: `{password}`")

    st.markdown("---")
    st.markdown("Built with ❤️ by [Alisha Khan](https://github.com/AlishhaKhan)")
