import streamlit as st


# ─────────────────────────────────────────────
#  inject_css()  —  Full page + widget styling
# ─────────────────────────────────────────────

def inject_css():

    st.set_page_config(
        layout="centered"
    )
    st.markdown("""
    <style>

    /* -------------------------
       Background
    ------------------------- */
    .stApp {
        background: linear-gradient(
            135deg,
            #0f172a,
            #1e293b,
            #334155
        );
    }

    /* -------------------------
       Text Input
    ------------------------- */
    .stTextInput > div > div > input {
        background-color: rgba(255,255,255,0.08);
        color: white;
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 10px;
        padding: 12px;
    }

    .stTextInput > div > div > input:focus {
        border: 1px solid #4f46e5;
        box-shadow: 0 0 10px rgba(79,70,229,0.4);
    }

    /* Placeholder */
    .stTextInput input::placeholder {
        color: #cbd5e1;
    }

    /* -------------------------
       Password Input
    ------------------------- */
    .stTextInput input[type="password"] {
        color: white;
    }

    /* -------------------------
       Button
    ------------------------- */
    .stButton > button {
        width: 100%;
        background: #4f46e5;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px;
        font-weight: 600;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background: #4338ca;
        transform: translateY(-2px);
    }

    .stButton > button:active {
        transform: translateY(0px);
    }

    /* -------------------------
       Labels
    ------------------------- */
    label {
        color: white !important;
        font-weight: 500;
    }

    .stDeployButton {
    display: none;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    .main .block-container {
        padding-top: 1rem;
    }

    /* =====================================================
       MAIN CONTAINER
    ===================================================== */
    .main-container {
        padding: 2rem;
        border-radius: 22px;
        background: linear-gradient(
            145deg,
            rgba(255,255,255,0.03),
            rgba(255,255,255,0.01)
        );
        border: 1px solid rgba(255,255,255,0.08);
        backdrop-filter: blur(10px);
        margin-bottom: 2rem;
    }

    /* =====================================================
       HERO SECTION
    ===================================================== */
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 10px;
        color: white;
    }

    .hero-subtitle {
        color: #9ca3af;
        font-size: 3rem;
        margin-bottom: 2rem;
    }

    .highlight {
        color: #8b5cf6;
    }

    </style>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  header()  —  JARVIS HUD-style header
# ─────────────────────────────────────────────
def header():
    
    st.markdown("""
    <div class="main-container">
        <div class="hero-title">
            Access your <span class="highlight">personalized</span>
        </div>
        <div class="hero-subtitle">
             AI environment
        </div>
    </div>
    """, unsafe_allow_html=True)