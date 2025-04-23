import streamlit as st
import streamlit.components.v1 as components
import base64

# ✅ Must be first
st.set_page_config(page_title="Multi-Agent Chat", layout="wide")

# ✅ Convert logo to base64 for CSS watermark
with open("connexus_logo_watermark.png", "rb") as f:
    data_uri = base64.b64encode(f.read()).decode("utf-8")
    logo_url = f"data:image/png;base64,{data_uri}"

# ✅ Inject CSS (watermark + spacing + transparent containers)
st.markdown(
    f"""
    <style>
    .block-container {{
        padding-top: 1rem !important;
    }}
    .watermark {{
        position: fixed;
        top: 40px;
        left: 50%;
        transform: translateX(-50%);
        height: 625px;
        width: 700px;
        z-index: 0;
        pointer-events: none;
        background-image: url("{logo_url}");
        background-repeat: no-repeat;
        background-position: center center;
        background-size: contain;
        opacity: 0.15;
    }}
    section.main > div {{
        background-color: transparent !important;
    }}
    </style>
    <div class="watermark"></div>
    """,
    unsafe_allow_html=True
)

# ✅ Page title and tabs
st.title("💬 Multi-Agent Chat")
tabs = st.tabs(["🧠 Amber", "🤖 Abe", "🧠 Noah"])

# === AMBER ===
with tabs[0]:
    st.subheader("Amber – Ecampus Prototype")
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
    st.subheader("Abe – Info Receptionist")
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
    st.subheader("Noah – Home Life Shield")
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
