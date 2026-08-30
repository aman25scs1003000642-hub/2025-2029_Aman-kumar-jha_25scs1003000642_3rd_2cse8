import streamlit as st
from chatbot import CustomerSupportBot

st.set_page_config(page_title="Customer Support AI", page_icon="", layout="centered")

st.title(" Customer Support AI Chatbot")
st.caption("A Python internship project for automated customer support")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! 👋 I'm your customer support assistant. How can I help you today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_message = st.chat_input("Type your question here...")

if user_message:
    st.session_state.messages.append({"role": "user", "content": user_message})
    with st.chat_message("user"):
        st.write(user_message)

    bot = CustomerSupportBot()
    reply = bot.get_response(user_message)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
