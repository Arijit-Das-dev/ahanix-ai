import streamlit as st
from Backend.Services.modelGemini import modelGemini


st.set_page_config(page_title="Prompt Lab", layout="centered")

if "message" not in st.session_state:
    st.session_state.message = []

user_input = st.chat_input("Ask anything....")  # ← Move this UP

# Only show welcome if no messages AND no input is being submitted
if len(st.session_state.message) == 0 and not user_input:
    st.markdown("## Prompt Lab")
    st.markdown("Hi there! How can I help you?")

for i in st.session_state.message:
    with st.chat_message(i["role"]):
        st.markdown(i["msg"])

if user_input:

    st.session_state.message.append({
        "role": "user",
        "msg": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking...."):
            ai_response = modelGemini.askGemini(query=user_input)
            st.markdown(ai_response)

    st.session_state.message.append({
        "role": "assistant",
        "msg": ai_response
    })