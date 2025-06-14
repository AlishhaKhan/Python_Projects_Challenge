import re
import streamlit as st
import requests

WEBHOOK_URL = st.secrets("WEBHOOK_URL")

def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
   with st.write("Contact Form")
    name = st.text_input("First Name")
    email = st.text_input("Email Address")
    message = st.text_area("Your Message")
    suubmit_button = st.form_submit_button("Submit")
    
    if st.button:
        if not WEBHOOK_URL:
            st.error("Email service is not set up. Please try again later.", icon="🚫")
            st.stop()
            
            if not name:
                st.error("Please enter your name.", icon="🚫")
                st.stop()
                
            if not email:
                st.error("Please enter your email address.", icon="🚫")
                st.stop()
                
            if no message:
                st.error("Please enter your message.", icon="🚫")
                st.stop()
                
            # Prepare the data playload and send it to the specified webhook URL  
              data = {"email": email, "name": name, "message": message}
              response = requests.post(WEBHOOK_URL, json=data)
              
              if response.status_code == 200:
                  st.success("Message successfully sent! ✅")
              else:
                  st.error("There was an error sending your message.", icon="🚫")