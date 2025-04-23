import streamlit as st
import streamlit.components.v1 as components

# MUST be the first Streamlit command!
st.set_page_config(page_title="Multi-Agent Chat – Connexus AI", layout="wide")

# Then apply custom styling (like removing top padding, watermark)
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
        }
        .logo-watermark {
            position: absolute;
            top: 180px;
            left: 50%;
            transform: translateX(-50%);
            opacity: 0.08;
            z-index: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("💬 Multi-Agent Chat – Connexus AI")

# Tabs
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
          window.onload = () => {
            ChatWidget.initializeChatWidget();
          };
        </script>
    """, height=400)

with tabs[1]:
    st.subheader("Abe – Info Receptionist")
    # 🔽 Insert watermark image here
    st.markdown(f"""
        <img src="data:image/png;base64,{st.image('/mnt/data/47508700-ced9-4950-a70f-944ab2d2ecb0.png', use_column_width=False).image_to_bytes().decode('utf-8')}"
             class="logo-watermark" />
    """, unsafe_allow_html=True)

    components.html("""
        <script src="https://connexusai.pages.dev/chat-widget.js"
          integrity="vC9YPpJCP1QqkOQ9kePoXmywFRS4mksl4NjUesvWKelztotJiBII+WJuR6TYolgu%"
          data-source-id="Ai-001-HonestAbe_InfoReceptionist_Prototype"
          data-agent-id="agent_4783654b2ef711860c963b7b22"
          data-agent-name="Abe"
          data-div-id="Abe-connexUS">
        </script>
        <script>
          window.onload = () => {
            ChatWidget.initializeChatWidget();
          };
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
          window.onload = () => {
            ChatWidget.initializeChatWidget();
          };
        </script>
    """, height=400)
