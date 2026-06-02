import streamlit as st
from Backend.auth.auth_service import Authentication


# Initialize Authentication
auth = Authentication()


# Initialize session state
if "user_email" not in st.session_state:
    st.session_state.user_email = None

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# Route user
if st.session_state.logged_in and st.session_state.user_email:
    auth.main_app(
        user_email=st.session_state.user_email
    )
else:
    auth.auth_screen()