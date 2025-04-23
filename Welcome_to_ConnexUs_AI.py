import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Multi-Agent Chat Demo", layout="wide")
st.title("💬 Multi-Agent Chat – Connexus AI")

# Create tabs
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
