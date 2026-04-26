import streamlit as st
import Frontend.F_Editor as ui 
from mistralai.client import Mistral
from DB.EditorDB import save_user_code, save_user_query
from Backend.Config.settings import settings
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

            save_user_code(user_id=userId, user_code=code)

            root_dir = os.path.abspath(
                        os.path.join(os.path.dirname(__file__), "..", "..")
                    )
            prompt_path = os.path.join(root_dir, "Prompt", "codePrompt1.txt")

            with open(prompt_path, "r", encoding="utf-8") as f:
                prompt1 = f.read()

            final_prompt1 = f"{prompt1}\nUser: {code}\nAssistant:"
            # Initialize client
            with Mistral(api_key=settings.MISTRAL_API_KEY) as mistral:
                completion_ = mistral.chat.complete(
                    model="mistral-small-latest",
                    messages=[
                        {"role": "user", "content": final_prompt1}
                    ],
                    stream=False
                )

            # Extract result
            result1 = completion_.choices[0].message.content

            # Send to UI
            ui.output_box(result1)
    
    with col_chat:

        user_input, send = ui.ai_chat_input()

        if send:

            save_user_query(user_id=userId, user_query=user_input)
            
            root_dir = os.path.abspath(
                        os.path.join(os.path.dirname(__file__), "..", "..")
                    )
            prompt_path = os.path.join(root_dir, "Prompt", "codePrompt2.txt")

            with open(prompt_path, "r", encoding="utf-8") as f:
                prompt2 = f.read()
            
            final_prompt2 = f"{prompt2}\nUser: {user_input}\nAssistant:"
            
            with Mistral(api_key=settings.MISTRAL_API_KEY) as mistral:
                completion_ = mistral.chat.complete(
                    model="mistral-small-latest",
                    messages=[
                        {"role": "user", "content": final_prompt2}
                    ],
                    stream=False
                )

            result2 = completion_.choices[0].message.content
            
            ui.output_box(result2)