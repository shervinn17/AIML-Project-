import streamlit as st
import requests

st.title("🧠 Mental Health Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_input = st.text_input("You:", "")
if st.button("Send") and user_input:
    response = requests.post("http://localhost:5000/chat", json={"message": user_input})
    bot_message = response.json().get("response")
    st.session_state["messages"].append(("You", user_input))
    st.session_state["messages"].append(("Bot", bot_message))

for sender, msg in st.session_state["messages"]:
    st.write(f"**{sender}:** {msg}")
