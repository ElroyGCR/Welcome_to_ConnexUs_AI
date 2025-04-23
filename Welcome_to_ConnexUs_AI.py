import streamlit as st
import streamlit.components.v1 as components
import base64

# ✅ Must be first
st.set_page_config(page_title="Multi-Agent Chat", layout="wide")

# ✅ THEME SWITCHER (Paste right below ↑)
if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "dark"

theme = st.radio("Choose Theme", ["dark", "light"], index=0 if st.session_state.theme_mode == "dark" else 1)

if theme != st.session_state.theme_mode:
    st.session_state.theme_mode = theme
    st.experimental_rerun()

# ✅ Global tab style (make this part renderable)
st.markdown(
    """
    <style>
    /* Make tab labels bigger + more spacing */
    .stTabs [data-baseweb="tab"] {
        font-size: 20px !important;
        font-weight: 600 !important;
        padding: 12px 24px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Inject light mode styles
if st.session_state.theme_mode == "light":
    st.markdown(
        """
        <style>
        body, .block-container {
            background-color: #f7f7f7 !important;
            color: #222 !important;
        }
        .stTabs [data-baseweb="tab-list"] button {
            background-color: #fff !important;
            color: #111 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
# ✅ Convert new watermark logo to base64
with open("connexus_logo_watermark_triangle.png", "rb") as f:  # use the latest triangle logo you uploaded
    triangle_logo_base64 = base64.b64encode(f.read()).decode("utf-8")

# ✅ Inject responsive triangle logo watermark
st.markdown(
    f"""
    <style>
    .watermark {{
        position: fixed;
        top: 40px;
        left: 50%;
        transform: translateX(-50%);
        height: auto;
        width: 40vw;
        max-width: 750px;
        z-index: 0;
        pointer-events: none;
        background-image: url("data:image/png;base64,{triangle_logo_base64}");
        background-repeat: no-repeat;
        background-position: center;
        background-size: contain;
        opacity: 0.08;
    }}
    </style>
    <div class="watermark"></div>
    """,
    unsafe_allow_html=True
)

# ✅ Top-right logo block
with open("connexus_logo.png", "rb") as f:
    logo_topright = base64.b64encode(f.read()).decode("utf-8")

st.markdown(
    f"""
    <style>
    .top-logo {{
        position: absolute;
        top: 50px;
        right: 20px;
        max-height: 50px;  /* adjust this based on how tall you want it */
        width: auto;
        z-index: 999;
    }}
    </style>
    <img src="data:image/png;base64,{logo_topright}" class="top-logo" />
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .responsive-title {
        font-size: clamp(26px, 3.5vw, 48px);
        font-weight: 700;
        margin-bottom: 16px;
        color: inherit;
    }

    .agent-header {
        font-size: 26px;
        font-weight: 600;
        margin-top: 10px;
        margin-bottom: 10px;
        color: inherit;
    }

    /* Agent tab styling globally */
    .stTabs [data-baseweb="tab"] {
        font-size: 20px !important;
        font-weight: 600 !important;
        padding: 12px 24px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h1 class="responsive-title">
        Pick the V-Rep you would like to speak with
    </h1>
    """,
    unsafe_allow_html=True
)

# ✅ Tabs - this section is now clean
tabs = st.tabs(["🧠 Amber", "🤖 Abe", "🧠 Noah"])

# === AMBER ===
with tabs[0]:
    st.markdown(
    f"""
    <h2 class="agent-header">
        Amber – Ecampus Prototype
    </h2>
    """,
    unsafe_allow_html=True
)
    components.html("""
    <div style="background-color: transparent;">
    <script src="https://connexusai.pages.dev/chat-widget.js"
      integrity="vC9YPpJCP1QqkOQ9kePoXmywFRS4mksl4NjUesvWKelztotJiBII+WJuR6TYolgu%"
      data-source-id="Ai-001-Ecampus_Protoype"
      data-agent-id="agent_d8a88fd3d28d15594dbdc0320b"
      data-agent-name="Amber"
      data-div-id="Amber-connexUS">
    </script>
    <script>
      window.onload = () => {{
        ChatWidget.initializeChatWidget();
        document.body.style.background = "transparent";
      }};
    </script>
    </div>
    """, height=400)

# === ABE ===
with tabs[1]:
    st.markdown(
    f"""
    <h2 class="agent-header">
        Abe – Info Receptionist
    </h2>
    """,
    unsafe_allow_html=True
)
    components.html("""
    <div style="background-color: transparent;">
    <script src="https://connexusai.pages.dev/chat-widget.js"
      integrity="vC9YPpJCP1QqkOQ9kePoXmywFRS4mksl4NjUesvWKelztotJiBII+WJuR6TYolgu%"
      data-source-id="Ai-001-HonestAbe_InfoReceptionist_Prototype"
      data-agent-id="agent_4783654b2ef711860c963b7b22"
      data-agent-name="Abe"
      data-div-id="Abe-connexUS">
    </script>
    <script>
      window.onload = () => {{
        ChatWidget.initializeChatWidget();
        document.body.style.background = "transparent";
      }};
    </script>
    </div>
    """, height=400)

# === NOAH ===
with tabs[2]:
    st.markdown(
    f"""
    <h2 class="agent-header">
        Noah – Home Life Shield
    </h2>
    """,
    unsafe_allow_html=True
)
    components.html("""
    <div style="background-color: transparent;">
    <script src="https://connexusai.pages.dev/chat-widget.js"
      integrity="vC9YPpJCP1QqkOQ9kePoXmywFRS4mksl4NjUesvWKelztotJiBII+WJuR6TYolgu%"
      data-source-id="Ai-001-Noah_HomeLifeShield"
      data-agent-id="agent_b58be8d047b32cb246aa72b900"
      data-agent-name="Noah"
      data-div-id="Noah-connexUS">
    </script>
    <script>
      window.onload = () => {{
        ChatWidget.initializeChatWidget();
        document.body.style.background = "transparent";
      }};
    </script>
    </div>
    """, height=400)
