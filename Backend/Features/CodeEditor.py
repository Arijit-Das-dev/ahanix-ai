import streamlit as st
import Frontend.F_Editor as ui 
from DB.EditorDB import save_user_code, save_user_query
from Backend.Services.modelMistral import modelMistral
import uuid
import os
import sys

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

st.set_page_config(layout="wide")
ui.inject_css()

# ---------- Session variables (TOP) ----------
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

# ---------------- Session State ----------------
if "started" not in st.session_state:
    st.session_state.started = False

userId = st.session_state.user_id

# ---------------- Landing Page ----------------
if not st.session_state.started:
    ui.landing_section1()
    start = ui.landing_section2() # just renders user guide

    # If "Get Started" clicked, update session_state and rerun
    if start:
        st.session_state.started = True
        st.rerun()

else:
    # Editor + chat layout
    col_editor, col_chat = st.columns([5, 4])
    
    with col_editor:
        
        code, submit = ui.code_editor()

        if submit:

            # save user code to DB
            save_user_code(user_id=userId, user_code=code)

            # Extract result from Backend/Services/modelMistral.py
            result_1 = modelMistral.mistralModel1(code1=code)

            # Send to UI
            ui.output_box(result_1)
    
    with col_chat:

        user_input, send = ui.ai_chat_input()

        if send:

            save_user_query(user_id=userId, user_query=user_input)

            result2 = modelMistral.mistralModel2(code2=user_input)
            
            ui.output_box(result2)