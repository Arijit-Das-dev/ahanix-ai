import streamlit as st
import uuid
from Backend.Services.modelGemini import modelGemini
import Frontend.F_PromptEng as ui

ui.inject_css()

st.set_page_config(
    page_title="PromptLab",
)

# ---------- Session variables (TOP) ----------
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

# ---------------- Session State ----------------
if "started" not in st.session_state:
    st.session_state.started = False

if "message" not in st.session_state:
    st.session_state.message = []  

userId = st.session_state.user_id

if not st.session_state.started:
    start = ui.landing_section1() # just renders user guide

    # If "Get Started" clicked, update session_state and rerun
    if start:
        st.session_state.started = True
        st.rerun()

else:
    user_input = st.chat_input("Describe your prompt....")  # ← Move this UP

    # Only show welcome if no messages AND no input is being submitted
    if len(st.session_state.message) == 0 and not user_input:
        ui.render_promptlab_home()

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