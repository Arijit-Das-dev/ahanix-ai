import streamlit as st


st.set_page_config(
    page_title="PromptLab",
    layout="centered"
)


def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* APP BACKGROUND WITH ANIMATED GRADIENT */
    .stApp {
        background: linear-gradient(135deg, #0a0118 0%, #1a0b2e 25%, #2d1b4e 50%, #1a0b2e 75%, #0a0118 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        color: white;
        font-family: 'Inter', sans-serif;
    }
    
    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* FLOATING PARTICLES */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(138, 43, 226, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 80% 70%, rgba(75, 0, 130, 0.15) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }

    /* GLASS CARD */
    .glass-card {
        position: relative;
        background: linear-gradient(135deg, rgba(20, 20, 40, 0.85) 0%, rgba(10, 10, 25, 0.9) 100%);
        border-radius: 32px;
        padding: 60px 70px;
        border: 1px solid rgba(147, 51, 234, 0.3);
        box-shadow:
            0 8px 32px rgba(138, 43, 226, 0.4),
            0 0 100px rgba(147, 51, 234, 0.2),
            inset 0 0 80px rgba(147, 51, 234, 0.05);
        backdrop-filter: blur(20px);
        max-width: 1200px;
        margin: 30px auto;
        transition: all 0.4s ease;
        overflow: hidden;
    }
    
    /* DECORATIVE ORBS */
    .glass-card .orb {
        position: absolute;
        border-radius: 50%;
        filter: blur(60px);
        opacity: 0.3;
        pointer-events: none;
        animation: float 8s ease-in-out infinite;
    }
    
    .glass-card .orb-1 {
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, #8b5cf6, transparent);
        top: -50px;
        right: -50px;
    }
    
    .glass-card .orb-2 {
        width: 180px;
        height: 180px;
        background: radial-gradient(circle, #d946ef, transparent);
        bottom: -40px;
        left: -40px;
        animation-delay: -4s;
    }
    
    @keyframes float {
        0%, 100% { transform: translate(0, 0) scale(1); }
        33% { transform: translate(20px, -20px) scale(1.1); }
        66% { transform: translate(-15px, 15px) scale(0.9); }
    }
                
    /* TITLE WITH GRADIENT */
    .hero-title {
        font-size: 58px;
        font-weight: 700;
        line-height: 1.15;
        margin-bottom: 24px;
        background: linear-gradient(135deg, #ffffff 0%, #e0d4ff 50%, #c4b5fd 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.02em;
        position: relative;
        z-index: 1;
    }
    
    .hero-title .accent {
        background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    /* USER GUIDE TEXT */
    .hero-sub {
        font-size: 17px;
        color: #d4d4ff;
        line-height: 1.8;
        margin-top: 20px;
        opacity: 0.95;
        position: relative;
        z-index: 1;
    }
    
    .hero-sub p {
        margin: 14px 0;
        padding-left: 8px;
        border-left: 3px solid rgba(167, 139, 250, 0.4);
        transition: all 0.3s ease;
    }
    
    .hero-sub p:hover {
        border-left-color: rgba(167, 139, 250, 0.8);
        transform: translateX(5px);
        color: #ffffff;
    }

    /* BUTTON */
    .stButton > button {
        background: linear-gradient(135deg, #8b5cf6 0%, #d946ef 100%);
        color: white;
        border: none;
        border-radius: 16px;
        padding: 16px 40px;
        font-size: 16px;
        font-weight: 600;
        box-shadow: 
            0 0 30px rgba(139, 92, 246, 0.6),
            0 4px 20px rgba(217, 70, 239, 0.4);
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        white-space: nowrap;
        min-height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s ease;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }

    .stButton > button:hover {
        box-shadow: 
            0 0 50px rgba(139, 92, 246, 0.9),
            0 8px 30px rgba(217, 70, 239, 0.6);
        transform: translateY(-3px);
    }
    
    /* DIVIDER */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(167, 139, 250, 0.5), transparent);
        margin: 50px 0;
    }
    
    /* SECTION HEADER */
    h2, h3 {
        color: #e0d4ff !important;
        font-weight: 600 !important;
        position: relative;
        padding-left: 20px;
    }
    
    h2::before, h3::before {
        content: '';
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 5px;
        height: 70%;
        background: linear-gradient(180deg, #8b5cf6, #d946ef);
        border-radius: 3px;
    }
    
    /* SELECTBOX STYLING */
    div[data-baseweb="select"] > div {
        background: rgba(30, 20, 50, 0.6) !important;
        border: 1.5px solid rgba(167, 139, 250, 0.4) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        transition: all 0.3s ease !important;
    }
    
    div[data-baseweb="select"] > div:hover {
        border-color: rgba(167, 139, 250, 0.7) !important;
        box-shadow: 0 0 20px rgba(167, 139, 250, 0.3) !important;
    }
    
    div[data-baseweb="select"] span {
        color: #ffffff !important;
        font-weight: 500 !important;
    }
    
    
    /* INFO BOX */
    .stAlert {
        background: rgba(139, 92, 246, 0.1) !important;
        border: 1px solid rgba(167, 139, 250, 0.3) !important;
        border-radius: 14px !important;
        color: #d4d4ff !important;
    }
    
    /* FEATURE BADGES */
    .feature-badge {
        display: inline-block;
        background: rgba(167, 139, 250, 0.15);
        border: 1px solid rgba(167, 139, 250, 0.3);
        border-radius: 20px;
        padding: 8px 18px;
        margin: 6px 8px 6px 0;
        font-size: 13px;
        color: #c4b5fd;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .feature-badge:hover {
        background: rgba(167, 139, 250, 0.25);
        border-color: rgba(167, 139, 250, 0.5);
        transform: translateY(-2px);
    }        
        
    /* SCROLLBAR */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(10, 10, 25, 0.5);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #8b5cf6, #d946ef);
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #a78bfa, #ec4899);
    }
    </style>
    """, unsafe_allow_html=True)

# Landing Page 1
def landing_section1():
    st.markdown("""
    <div class="glass-card">
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>
        <div class="hero-title">
            Welcome to<br><span class="accent">Jarvis PromptLab</span>
        </div>
        <div class="hero-sub">
            Turn your ideas into powerful, structured AI prompts.<br>
            Describe what you need and let AI generate production-ready prompts instantly.<br>
            Built for creators, developers, and anyone leveraging AI effectively.
        </div>
        <div style="margin-top: 35px; position: relative; z-index: 1;">
            <span class="feature-badge">🧠 Prompt Intelligence</span>
            <span class="feature-badge">⚡ Instant Prompt Generation</span>
            <span class="feature-badge">📦 Structured Output</span>
            <span class="feature-badge">🎯 Use-case Optimized</span>
            <span class="feature-badge">✨ AI Refinement Engine</span>
            <span class="feature-badge">🚀 Production Ready</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    return st.button("🚀 Get Started")

def render_promptlab_home():

    st.markdown("""
    <style>
    .glass-wrapper {
        display: flex;
        justify-content: center;
        gap: 25px;
        margin-top: 20px;
        flex-wrap: wrap;
    }

    .glass-card-mini {
        width: 220px;
        padding: 25px;
        border-radius: 18px;
        background: rgba(30,30,50,0.5);
        backdrop-filter: blur(12px);
        border:1px solid rgba(255,255,255,0.08);
        box-shadow: 0 8px 30px rgba(0,0,0,0.4);
        color:#d4d4ff;
        font-size:14px;
        line-height:1.6;
        text-align:center;
        transition: all 0.35s ease;
        animation: fadeUp 0.8s ease forwards;
        opacity: 0;
    }

    .glass-card-mini:nth-child(1) { animation-delay: 0.1s; }
    .glass-card-mini:nth-child(2) { animation-delay: 0.3s; }
    .glass-card-mini:nth-child(3) { animation-delay: 0.5s; }

    .glass-card-mini:hover {
        transform: translateY(-6px);
        box-shadow: 0 12px 40px rgba(139,92,246,0.4);
    }

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .promptlab-title {
        font-size: 56px;
        font-weight: 700;
        text-align: center;
        letter-spacing: -1px;

        background: linear-gradient(270deg, #a78bfa, #ec4899, #7c3aed, #c4b5fd);
        background-size: 600% 600%;

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        animation: gradientMove 6s ease infinite, fadeUp 1s ease forwards;
        opacity: 0;
    }

    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    </style>
    <!-- 🔥 REMOVE BIG TOP SPACE -->
    <div style="text-align:center; margin-top:10px;">  
        <h1 style="
            font-size:42px;
            font-weight:700;
            background: linear-gradient(135deg,#ffffff,#c4b5fd);
            -webkit-background-clip:text;
            -webkit-text-fill-color:transparent;
            margin-bottom:15px;
        ">           
        <div class="promptlab-title">
         PromptLab
        </div>        
         </h1>
        <div class="glass-wrapper">
            <div class="glass-card-mini">
                🧠 Generate structured, production-ready prompts instantly.
            </div>
            <div class="glass-card-mini">
                ⚡ Turn simple ideas into powerful AI instructions.
            </div>
            <div class="glass-card-mini">
                🚀 Build better workflows with optimized prompts.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)