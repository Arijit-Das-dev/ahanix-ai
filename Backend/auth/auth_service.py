import streamlit as st
from supabase import Client, create_client
from Backend.Config.settings import settings


class Authentication:

    def __init__(self):
        self.supabase_url = settings.SUPABASE_URL
        self.supabase_key = settings.SUPABASE_KEY

        self.supabase: Client = create_client(
            self.supabase_url,
            self.supabase_key
        )

    # -------------------------
    # SIGN UP
    # -------------------------
    def sign_up(self, email: str, password: str):

        if not email or not password:
            st.warning("Please fill all fields.")
            return None

        try:
            user = self.supabase.auth.sign_up(
                {
                    "email": email,
                    "password": password
                }
            )

            return user

        except Exception as e:
            st.error(f"Registration failed: {str(e)}")
            return None

    # -------------------------
    # SIGN IN
    # -------------------------
    def sign_in(self, email: str, password: str):

        if not email or not password:
            st.warning("Please fill all fields.")
            return None

        try:
            user = self.supabase.auth.sign_in_with_password(
                {
                    "email": email,
                    "password": password
                }
            )

            return user

        except Exception as e:
            st.error(f"Login failed: {str(e)}")
            return None

    # -------------------------
    # SIGN OUT
    # -------------------------
    def sign_out(self):

        try:
            self.supabase.auth.sign_out()

            st.session_state.user_email = None
            st.session_state.logged_in = False

            st.success("Logged out successfully.")
            st.rerun()

        except Exception as e:
            st.error(f"Logout failed: {str(e)}")

    # -------------------------
    # MAIN APP
    # -------------------------
    def main_app(self, user_email):

        st.title("Welcome Page")

        st.success(f"Welcome, {user_email}")

        st.divider()

        if st.button("Logout", use_container_width=True):
            self.sign_out()

    # -------------------------
    # AUTH SCREEN
    # -------------------------
    def auth_screen(self):

        st.title("🔐 JARVIS Authentication")

        # Initialize auth mode
        if "auth_mode" not in st.session_state:
            st.session_state.auth_mode = "signin"

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Sign In", use_container_width=True):
                st.session_state.auth_mode = "signin"

        with col2:
            if st.button("Sign Up", use_container_width=True):
                st.session_state.auth_mode = "signup"

        st.divider()

        email = st.text_input("Email Address")

        password = st.text_input(
            "Password",
            type="password"
        )

        # ---------------------
        # SIGN UP UI
        # ---------------------
        if st.session_state.auth_mode == "signup":

            if st.button("Create Account", use_container_width=True):

                user = self.sign_up(
                    email=email,
                    password=password
                )

                if user:
                    st.success(
                        "Registration successful. Check your email for verification."
                    )

        # ---------------------
        # SIGN IN UI
        # ---------------------
        else:

            if st.button("Login", use_container_width=True):

                user = self.sign_in(
                    email=email,
                    password=password
                )

                if user and user.user:

                    st.session_state.user_email = user.user.email
                    st.session_state.logged_in = True

                    st.success(
                        f"Welcome back, {user.user.email}"
                    )

                    st.rerun()