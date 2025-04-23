import streamlit as st
import streamlit.components.v1 as components
import base64

# === MUST be first Streamlit call ===
st.set_page_config(page_title="Multi-Agent Chat – Connexus AI", layout="wide")

# === Load logo watermark ===
def get_base64_logo(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = get_base64_logo("connexus_logo_watermark.png")  # Your uploaded logo file

# === Custom CSS ===
st.markdown(f"""
    <style>
        .block-container {{
            padding-top: 1rem;
        }}
        .logo-watermark {{
            position: absolute;
            top: 260px;
            left: 50%;
            transform: translateX(-50%);
            opacity: 0.05;
            z-index: 0;
            width: 280px;
        }}
    </style>
    <img src="data:image/png;base64,{logo_base64}" class="logo-watermark" />
""", unsafe_allow_html=True)

# === Title and Tabs ===
st.title("💬 Multi-Agent Chat – Connexus AI")
tabs = st.tabs(["🧠 Amber", "🤖 Abe", "🧠 Noah"])

with tabs[0]:
    st.subheader("Amber – Ecampus Prototype")
    components.html("""
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
      }};
    </script>
    """, height=400)

with tabs[1]:
    st.subheader("Abe – Info Receptionist")
    components.html("""
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
      }};
    </script>
    """, height=400)

with tabs[2]:
    st.subheader("Noah – Home Life Shield")
    components.html("""
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
      }};
    </script>
    """, height=400)
