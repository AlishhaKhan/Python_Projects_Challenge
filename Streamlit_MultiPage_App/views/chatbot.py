import streamlit as st
import random

# --- Set Page Title ---
st.title("Chatbot")
st.write("Welcome! Ask me anything and I'll try my best to help you.")

# --- Initialize Session State for Chat ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Enhanced Rule-Based Bot Logic with Language Detection ---
def get_bot_response(user_input):
    user_input = user_input.lower()

    english_greetings = ["hello", "hi", "hey"]
    roman_greetings = ["salam", "assalamualaikum", "kia hal hai", "kaise ho", "kese ho"]
    english_identity = ["who are you", "what's your name"]
    roman_identity = ["tumhara naam", "tum kon ho"]
    english_how_are_you = ["how are you", "how’s it going"]
    roman_how_are_you = ["kaise ho", "kesi ho", "kya haal hai", "kia haal chaal"]
    english_farewell = ["bye", "goodbye", "see you"]
    roman_farewell = ["khuda hafiz", "allah hafiz", "milte hain"]
    english_thanks = ["thank", "thanks", "thank you"]
    roman_thanks = ["shukriya", "meharbani"]
    english_jokes = ["joke", "funny", "laugh"]
    roman_jokes = ["mazaq", "chutkula"]

    def is_roman(text):
        return any(word in text for word in roman_greetings + roman_identity + roman_how_are_you + roman_farewell + roman_thanks + roman_jokes)

    is_roman_input = is_roman(user_input)

    if any(word in user_input for word in english_greetings + roman_greetings):
        return random.choice([
            "Hello! 👋 How can I help you today?" if not is_roman_input else "Salaam! 👋 Kya haal hain?",
            "Hey there! 😄" if not is_roman_input else "Kese ho? 😄",
            "Welcome! How’s your day going?" if not is_roman_input else "Khair maqdam! Din kaisa guzra?"
        ])

    elif any(word in user_input for word in english_identity + roman_identity):
        return "I'm Ellie, Alisha's chatbot assistant 🤖" if not is_roman_input else "Main Ellie hoon, Alisha ki chatbot assistant 🤖"

    elif any(word in user_input for word in english_how_are_you + roman_how_are_you):
        return random.choice([
            "I'm doing great, thank you! How about you? 😊" if not is_roman_input else "Main theek hoon, shukriya! Aap sunao? 😊",
            "All good here! Need any help today?" if not is_roman_input else "Sab fit! Aaj kis cheez mein madad chahiye?"
        ])

    elif "project" in user_input:
        return "You can view all projects in the 'Projects' section from the sidebar! 📁" if not is_roman_input else "Projects sidebar mein 'Projects' section mein milenge 📁"

    elif any(word in user_input for word in english_jokes + roman_jokes):
        return random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛" if not is_roman_input else "Programmers dark mode q pasand karte hain? Kyunke light bugs ko attract karti hai! 🐛",
            "Knock knock! Who's there? AI. AI who? AI am just a bot 😅" if not is_roman_input else "Knock knock! Kon hai? AI. AI kon? AI sirf ek bot hai 😅"
        ])

    elif any(word in user_input for word in english_thanks + roman_thanks):
        return "You're welcome! 😊" if not is_roman_input else "Koi baat nahi! 😊"

    elif any(word in user_input for word in english_farewell + roman_farewell):
        return random.choice([
            "Goodbye! Have a nice day 😊" if not is_roman_input else "Allah Hafiz! Khush raho 😊",
            "See you later! 👋" if not is_roman_input else "Phir milte hain! 👋"
        ])

    else:
        return "I'm still learning 🧠. Could you try asking that another way?" if not is_roman_input else "Main abhi seekh rahi hoon 🧠. Zara aur asaan tareeqay se poochho?"

# --- User Input Form ---
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", "")
    submit = st.form_submit_button("Send")

# --- Handle Submission ---
if submit and user_input:
    bot_response = get_bot_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

# --- Display Chat History ---
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")
