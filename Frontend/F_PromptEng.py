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
                
    /* underline base */
    .promptlab-title::after {
        content: "";
        position: absolute;
        left: 50%;
        bottom: -6px;
        width: 0%;
        height: 3px;
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        border-radius: 10px;
        transform: translateX(-50%);
        
        /* smooth animation */
        transition: width 0.4s ease;
    }

    /* animate on load */
    .promptlab-title.animate::after {
        width: 60%;
    }

    /* hover effect (expand slightly) */
    .promptlab-title:hover::after {
        width: 80%;
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
        <div class="promptlab-title animate">
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

import streamlit as st


def landingSection2():
    # ── Inject global CSS ──────────────────────────────────────────────────────
    st.markdown(
        """
        <style>
        /* ── Google Fonts ── */
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

        /* ── Reset & base ── */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
            background: transparent !important;
        }
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #05060f 0%, #0d0f2b 35%, #130824 65%, #06030f 100%) !important;
            min-height: 100vh;
        }
        [data-testid="stHeader"] { background: transparent !important; }
        .block-container { padding: 0 !important; max-width: 100% !important; }
        * { box-sizing: border-box; }

        /* ── Noise overlay ── */
        [data-testid="stAppViewContainer"]::before {
            content: "";
            position: fixed; inset: 0; z-index: 0; pointer-events: none;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
            opacity: 0.35;
        }

        /* ── Ambient blobs ── */
        .pl-blob {
            position: absolute; border-radius: 50%; filter: blur(90px);
            pointer-events: none; z-index: 0;
        }

        /* ── Wrapper ── */
        .pl-section {
            position: relative;
            padding: 96px 5vw 120px;
            font-family: 'DM Sans', sans-serif;
            overflow: hidden;
        }

        /* ── Eyebrow ── */
        .pl-eyebrow {
            display: inline-flex; align-items: center; gap: 8px;
            background: rgba(109, 77, 255, 0.12);
            border: 1px solid rgba(109, 77, 255, 0.35);
            border-radius: 100px;
            padding: 6px 16px 6px 10px;
            font-family: 'DM Sans', sans-serif;
            font-size: 12px; font-weight: 500; letter-spacing: 0.08em;
            color: #a78bfa; text-transform: uppercase;
            margin-bottom: 28px;
        }
        .pl-eyebrow-dot {
            width: 7px; height: 7px; border-radius: 50%;
            background: #7c3aed;
            box-shadow: 0 0 8px #7c3aed;
            animation: pulse-dot 2s ease-in-out infinite;
        }
        @keyframes pulse-dot {
            0%,100% { opacity: 1; transform: scale(1); }
            50%      { opacity: 0.5; transform: scale(1.4); }
        }

        /* ── Hero headline ── */
        .pl-hero-title {
            font-family: 'Syne', sans-serif;
            font-size: clamp(40px, 6vw, 84px);
            font-weight: 800;
            line-height: 1.05;
            letter-spacing: -0.03em;
            color: #f0eeff;
            margin: 0 0 10px;
        }
        .pl-hero-title .grad {
            background: linear-gradient(90deg, #a78bfa 0%, #60a5fa 50%, #f472b6 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        /* ── Sub-headline ── */
        .pl-hero-sub {
            font-size: clamp(16px, 1.6vw, 20px);
            font-weight: 300; line-height: 1.7;
            color: rgba(200, 195, 240, 0.65);
            max-width: 560px;
            margin: 22px 0 48px;
        }

        /* ── CTA row ── */
        .pl-cta-row {
            display: flex; align-items: center; gap: 16px;
            flex-wrap: wrap; margin-bottom: 88px;
        }
        .pl-btn-primary {
            display: inline-flex; align-items: center; gap: 9px;
            background: linear-gradient(135deg, #7c3aed, #4f46e5);
            color: #fff; font-family: 'DM Sans', sans-serif;
            font-size: 15px; font-weight: 500;
            padding: 14px 28px; border-radius: 14px;
            border: none; cursor: pointer; text-decoration: none;
            box-shadow: 0 0 32px rgba(124, 58, 237, 0.45),
                        0 2px 8px rgba(0,0,0,0.5);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .pl-btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 0 48px rgba(124, 58, 237, 0.65),
                        0 4px 16px rgba(0,0,0,0.5);
        }
        .pl-btn-ghost {
            display: inline-flex; align-items: center; gap: 8px;
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.1);
            color: rgba(220,215,255,0.75);
            font-family: 'DM Sans', sans-serif;
            font-size: 15px; font-weight: 400;
            padding: 14px 24px; border-radius: 14px;
            cursor: pointer; text-decoration: none;
            transition: background 0.2s, border-color 0.2s;
        }
        .pl-btn-ghost:hover {
            background: rgba(255,255,255,0.08);
            border-color: rgba(167,139,250,0.35);
        }

        /* ── Stats strip ── */
        .pl-stats {
            display: flex; gap: 48px; flex-wrap: wrap;
            border-top: 1px solid rgba(255,255,255,0.06);
            padding-top: 36px; margin-bottom: 96px;
        }
        .pl-stat-item { display: flex; flex-direction: column; gap: 4px; }
        .pl-stat-num {
            font-family: 'Syne', sans-serif;
            font-size: 32px; font-weight: 700;
            background: linear-gradient(90deg, #c4b5fd, #818cf8);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .pl-stat-label {
            font-size: 13px; color: rgba(180,175,220,0.5);
            letter-spacing: 0.04em;
        }

        /* ── Section label ── */
        .pl-section-label {
            font-size: 11px; font-weight: 500; letter-spacing: 0.14em;
            text-transform: uppercase; color: rgba(167,139,250,0.55);
            margin-bottom: 40px;
        }

        /* ── Feature cards grid ── */
        .pl-cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
            margin-bottom: 80px;
        }
        .pl-card {
            background: rgba(255,255,255,0.035);
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 20px;
            padding: 32px 28px;
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            position: relative; overflow: hidden;
            transition: transform 0.25s, border-color 0.25s, box-shadow 0.25s;
        }
        .pl-card::before {
            content: "";
            position: absolute; inset: 0; border-radius: inherit;
            background: radial-gradient(ellipse at 0% 0%, rgba(124,58,237,0.1) 0%, transparent 65%);
            pointer-events: none;
        }
        .pl-card:hover {
            transform: translateY(-4px);
            border-color: rgba(124,58,237,0.3);
            box-shadow: 0 16px 48px rgba(0,0,0,0.4),
                        0 0 0 1px rgba(124,58,237,0.15);
        }
        .pl-card-icon {
            font-size: 28px; margin-bottom: 18px;
            display: flex; align-items: center; justify-content: center;
            width: 52px; height: 52px;
            background: rgba(124, 58, 237, 0.12);
            border: 1px solid rgba(124, 58, 237, 0.2);
            border-radius: 14px;
        }
        .pl-card-title {
            font-family: 'Syne', sans-serif;
            font-size: 17px; font-weight: 700;
            color: #ede9fe; margin-bottom: 10px;
        }
        .pl-card-desc {
            font-size: 14px; line-height: 1.65;
            color: rgba(190,183,235,0.55);
        }
        .pl-card-tag {
            display: inline-block; margin-top: 18px;
            font-size: 11px; letter-spacing: 0.08em;
            text-transform: uppercase; color: #a78bfa;
            background: rgba(124,58,237,0.12);
            border: 1px solid rgba(124,58,237,0.22);
            border-radius: 100px; padding: 3px 10px;
        }

        /* ── How it works timeline ── */
        .pl-timeline {
            display: flex; gap: 0;
            flex-wrap: wrap;
            position: relative;
            margin-bottom: 80px;
        }
        .pl-timeline-step {
            flex: 1; min-width: 200px;
            position: relative; padding: 0 24px 0 0;
        }
        .pl-timeline-step:not(:last-child)::after {
            content: "";
            position: absolute; top: 20px; right: 0;
            width: 24px; height: 1px;
            background: linear-gradient(90deg, rgba(124,58,237,0.5), transparent);
        }
        .pl-step-num {
            font-family: 'Syne', sans-serif;
            font-size: 11px; font-weight: 700; letter-spacing: 0.1em;
            color: #7c3aed; margin-bottom: 12px;
        }
        .pl-step-icon {
            font-size: 22px; margin-bottom: 12px;
        }
        .pl-step-title {
            font-family: 'Syne', sans-serif;
            font-size: 15px; font-weight: 700;
            color: #ede9fe; margin-bottom: 8px;
        }
        .pl-step-desc {
            font-size: 13px; line-height: 1.6;
            color: rgba(180,175,220,0.5);
        }

        /* ── Model compatibility strip ── */
        .pl-models {
            display: flex; align-items: center;
            gap: 12px; flex-wrap: wrap; margin-bottom: 80px;
        }
        .pl-models-label {
            font-size: 12px; letter-spacing: 0.06em; text-transform: uppercase;
            color: rgba(180,175,220,0.4); margin-right: 8px;
        }
        .pl-model-chip {
            display: inline-flex; align-items: center; gap: 6px;
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 100px; padding: 6px 14px;
            font-size: 13px; font-weight: 400;
            color: rgba(210,205,255,0.7);
        }
        .pl-model-dot {
            width: 6px; height: 6px; border-radius: 50%;
        }

        /* ── Testimonial / quote card ── */
        .pl-quote-card {
            background: rgba(124,58,237,0.07);
            border: 1px solid rgba(124,58,237,0.18);
            border-radius: 20px;
            padding: 40px 44px;
            backdrop-filter: blur(12px);
            margin-bottom: 80px;
            position: relative; overflow: hidden;
        }
        .pl-quote-card::before {
            content: "\201C";
            position: absolute; top: -10px; left: 28px;
            font-family: 'Syne', sans-serif;
            font-size: 120px; line-height: 1;
            color: rgba(124,58,237,0.18);
            pointer-events: none;
        }
        .pl-quote-text {
            font-family: 'DM Sans', sans-serif;
            font-size: clamp(17px, 1.8vw, 22px);
            font-weight: 300; font-style: italic;
            line-height: 1.65;
            color: rgba(225,220,255,0.8);
            max-width: 720px;
            position: relative; z-index: 1;
            margin-bottom: 24px;
        }
        .pl-quote-author {
            font-size: 13px; font-weight: 500;
            color: rgba(167,139,250,0.7);
            letter-spacing: 0.04em;
        }

        /* ── CTA bottom banner ── */
        .pl-cta-banner {
            background: linear-gradient(135deg,
                rgba(79,70,229,0.18) 0%,
                rgba(124,58,237,0.22) 50%,
                rgba(236,72,153,0.12) 100%);
            border: 1px solid rgba(124,58,237,0.22);
            border-radius: 24px;
            padding: 56px 52px;
            display: flex; align-items: center; justify-content: space-between;
            flex-wrap: wrap; gap: 32px;
            backdrop-filter: blur(16px);
            position: relative; overflow: hidden;
        }
        .pl-cta-banner::before {
            content: "";
            position: absolute; bottom: -40px; right: -40px;
            width: 280px; height: 280px; border-radius: 50%;
            background: radial-gradient(circle, rgba(124,58,237,0.25), transparent 70%);
            pointer-events: none;
        }
        .pl-cta-banner-title {
            font-family: 'Syne', sans-serif;
            font-size: clamp(24px, 2.8vw, 36px);
            font-weight: 800; color: #f0eeff;
            line-height: 1.15; max-width: 480px;
        }
        .pl-cta-banner-sub {
            font-size: 14px; color: rgba(190,185,235,0.55);
            margin-top: 8px; max-width: 380px; line-height: 1.6;
        }

        /* ── Scroll fade-in animation ── */
        .pl-fade { animation: fadein 0.7s ease both; }
        .pl-fade-d1 { animation-delay: 0.1s; }
        .pl-fade-d2 { animation-delay: 0.2s; }
        .pl-fade-d3 { animation-delay: 0.35s; }
        .pl-fade-d4 { animation-delay: 0.5s; }
        @keyframes fadein {
            from { opacity: 0; transform: translateY(18px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ── Build HTML ─────────────────────────────────────────────────────────────
    html = """
    <div class="pl-section">
        <!-- Ambient blobs -->
        <div class="pl-blob" style="width:600px;height:600px;top:-150px;left:-120px;
            background:radial-gradient(circle, rgba(79,70,229,0.18) 0%, transparent 70%);"></div>
        <div class="pl-blob" style="width:500px;height:500px;top:200px;right:-100px;
            background:radial-gradient(circle, rgba(124,58,237,0.14) 0%, transparent 70%);"></div>
        <div class="pl-blob" style="width:400px;height:400px;bottom:0;left:30%;
            background:radial-gradient(circle, rgba(236,72,153,0.08) 0%, transparent 70%);"></div>
        <!-- ── HERO ── -->
        <div class="pl-fade pl-fade-d1">
            <span class="pl-eyebrow">
                <span class="pl-eyebrow-dot"></span>
                Now in Public Beta · PromptLab v2.0
            </span>
        </div>
        <div class="pl-cta-banner-title">
            <span class="grad"> Jarvis PromptLab</span>
        </div>
        <h1 class="pl-hero-title pl-fade pl-fade-d2">
            The Engine That Makes<br>
            <span class="grad">Every AI Think Clearer</span>
        </h1>
        <p class="pl-hero-sub pl-fade pl-fade-d3">
            PromptLab is a universal prompt engine that crafts precision prompts for any task —
            unlocking the full reasoning power of GPT‑4, Claude, Gemini, Mistral, and beyond.
            Stop fighting your AI. Start orchestrating it.
        </p>
        <!-- ── STATS ── -->
        <div class="pl-stats pl-fade pl-fade-d4">
            <div class="pl-stat-item">
                <span class="pl-stat-num">50 K+</span>
                <span class="pl-stat-label">Prompts Generated</span>
            </div>
            <div class="pl-stat-item">
                <span class="pl-stat-num">12 +</span>
                <span class="pl-stat-label">AI Models Supported</span>
            </div>
            <div class="pl-stat-item">
                <span class="pl-stat-num">3.4×</span>
                <span class="pl-stat-label">Avg Output Quality Lift</span>
            </div>
            <div class="pl-stat-item">
                <span class="pl-stat-num">99.9 %</span>
                <span class="pl-stat-label">Uptime SLA</span>
            </div>
        </div>
        <!-- ── FEATURE CARDS ── -->
        <p class="pl-section-label">Core Capabilities</p>
        <div class="pl-cards-grid">
            <div class="pl-card">
                <div class="pl-card-icon">🎯</div>
                <div class="pl-card-title">Task-Aware Prompt Synthesis</div>
                <div class="pl-card-desc">
                    Describe what you need — PromptLab reverse-engineers the optimal
                    instruction set. Whether it's code review, creative writing, data
                    analysis, or customer support, the engine picks the right structure.
                </div>
                <span class="pl-card-tag">NLP Core</span>
            </div>
            <div class="pl-card">
                <div class="pl-card-icon">🤖</div>
                <div class="pl-card-title">Model-Specific Tuning</div>
                <div class="pl-card-desc">
                    Each AI model has quirks. PromptLab knows them. Prompts are
                    auto-adapted to match the instruction style, token economy, and
                    reasoning patterns of GPT-4, Claude, Gemini, Llama, and more.
                </div>
                <span class="pl-card-tag">Multi-Model</span>
            </div>
            <div class="pl-card">
                <div class="pl-card-icon">🔗</div>
                <div class="pl-card-title">Chain-of-Thought Scaffolding</div>
                <div class="pl-card-desc">
                    Automatically injects reasoning scaffolds — few-shot examples,
                    step-by-step directives, role assignments — so your model thinks
                    deeper before it speaks.
                </div>
                <span class="pl-card-tag">Reasoning</span>
            </div>
            <div class="pl-card">
                <div class="pl-card-icon">📐</div>
                <div class="pl-card-title">Output Format Control</div>
                <div class="pl-card-desc">
                    Need JSON? A markdown table? A numbered list? Specify the shape
                    of your output and PromptLab wires the constraint directly into
                    the prompt — no post-processing hacks needed.
                </div>
                <span class="pl-card-tag">Structured Output</span>
            </div>
            <div class="pl-card">
                <div class="pl-card-icon">🔒</div>
                <div class="pl-card-title">Safety & Guardrail Injection</div>
                <div class="pl-card-desc">
                    Production deployments demand safe outputs. PromptLab weaves in
                    guardrails, refusal clauses, and tone policies invisibly — so
                    your AI stays on-brand and compliant at all times.
                </div>
                <span class="pl-card-tag">Enterprise-ready</span>
            </div>
            <div class="pl-card">
                <div class="pl-card-icon">🔄</div>
                <div class="pl-card-title">Iterative Prompt Optimizer</div>
                <div class="pl-card-desc">
                    Not happy with results? Feed outputs back in. PromptLab's
                    optimizer rewrites the prompt, measures delta, and converges
                    toward peak performance — automatically.
                </div>
                <span class="pl-card-tag">Self-Improving</span>
            </div>
        </div>
        <!-- ── HOW IT WORKS ── -->
        <p class="pl-section-label">How It Works</p>
        <div class="pl-timeline">
            <div class="pl-timeline-step">
                <div class="pl-step-num">STEP 01</div>
                <div class="pl-step-icon">📝</div>
                <div class="pl-step-title">Describe Your Task</div>
                <div class="pl-step-desc">
                    Write a plain-English description of what you want the AI to do.
                    No prompt engineering knowledge required.
                </div>
            </div>
            <div class="pl-timeline-step">
                <div class="pl-step-num">STEP 02</div>
                <div class="pl-step-icon">⚙️</div>
                <div class="pl-step-title">Engine Processes</div>
                <div class="pl-step-desc">
                    PromptLab's NLP core analyzes intent, complexity, and model
                    constraints to assemble the ideal prompt structure.
                </div>
            </div>
            <div class="pl-timeline-step">
                <div class="pl-step-num">STEP 03</div>
                <div class="pl-step-icon">✨</div>
                <div class="pl-step-title">Receive Precision Prompt</div>
                <div class="pl-step-desc">
                    Get a battle-tested, model-ready prompt with role, context,
                    instructions, and output format — one click away.
                </div>
            </div>
            <div class="pl-timeline-step">
                <div class="pl-step-num">STEP 04</div>
                <div class="pl-step-icon">🚀</div>
                <div class="pl-step-title">Deploy & Iterate</div>
                <div class="pl-step-desc">
                    Plug it into any AI API or UI. Refine with feedback loops.
                    Save, version, and share across your team.
                </div>
            </div>
        </div>
        <!-- ── MODEL COMPATIBILITY ── -->
        <div class="pl-models">
            <span class="pl-models-label">Works with</span>
            <span class="pl-model-chip"><span class="pl-model-dot" style="background:#60a5fa;"></span> Gemini 2.5</span>
            <span class="pl-model-chip"><span class="pl-model-dot" style="background:#f59e0b;"></span> Llama 3</span>
            <span class="pl-model-chip"><span class="pl-model-dot" style="background:#f472b6;"></span> Mistral</span>
        </div>
        <!-- ── QUOTE ── -->
        <div class="pl-quote-card">
            <p class="pl-quote-text">
                We cut our prompt iteration cycle from days to minutes. PromptLab doesn't just
                write prompts — it teaches our team what good prompting actually looks like.
                Every model we run is performing measurably better.
            </p>
            <div class="pl-quote-author">— Head of AI, Series-B SaaS · YC W23</div>
        </div>
        <!-- ── BOTTOM CTA ── -->
        <div class="pl-cta-banner">
            <div>
                <div class="pl-cta-banner-title">
                    Ready to unlock your AI's<br>true potential?
                </div>
                <div class="pl-cta-banner-sub">
                    Join 8,000+ engineers and product teams who ship faster with
                    PromptLab-powered workflows. Free tier available, no credit card required.
                </div>
        </div>
    </div>
    """
    
    st.markdown(html, unsafe_allow_html=True)

    col1, col2, col3, col5, col6 = st.columns(5)

    with col3:

        return st.button("Get started")