import streamlit as st 
import streamlit.components.v1 as components
import base64

# ✅ Set Streamlit config
st.set_page_config(page_title="Multi-Agent Chat", layout="wide")

# ✅ Load images
with open("connexus_logo_watermark.png", "rb") as f:
    triangle_logo_base64 = base64.b64encode(f.read()).decode("utf-8")

with open("connexus_logo.png", "rb") as f:
    logo_topright_base64 = base64.b64encode(f.read()).decode("utf-8")

# ✅ Inject layout and styles (adjusted tabs and watermark size)
st.markdown(
    f"""
    <style>
    .block-container {{
        padding-top: 3rem !important;
        position: relative;
        background-image: url("data:image/png;base64,{triangle_logo_base64}");
        background-repeat: no-repeat;
        background-position: center 240px;
        background-size: 45%;
    }}

    .top-logo {{
        position: absolute;
        top: 30px;
        right: 20px;
        max-height: 40px;
        width: auto;
        z-index: 999;
    }}

    .responsive-title {{
        font-size: clamp(26px, 3.5vw, 48px);
        font-weight: 700;
        margin-top: 140px;
        margin-bottom: 16px;
        color: inherit;
    }}

    .agent-header {{
        font-size: 32px;
        font-weight: 600;
        margin-top: 10px;
        margin-bottom: 10px;
        color: inherit;
    }}

    .stTabs [data-baseweb="tab"] {{
        font-size: 36px !important;
        font-weight: 700 !important;
        padding: 16px 28px !important;
    }}
    </style>

    <img src="data:image/png;base64,{logo_topright_base64}" class="top-logo" />
    """,
    unsafe_allow_html=True
)

# ✅ Title
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
