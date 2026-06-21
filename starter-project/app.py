import streamlit as st

st.set_page_config(
    page_title="🔬 STEM AI Toolkit",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🔬 STEM AI Toolkit")
st.markdown("### Your AI-Powered Teaching Assistant")
st.markdown("---")

st.markdown("""
Welcome to your personal STEM AI Toolkit! This app contains three AI-powered tools
designed to help you in your classroom:

**📝 Lab Report Feedback** — Paste a student's lab report and get detailed, constructive feedback based on your rubric.

**📊 Quiz Generator** — Enter a topic and get a custom quiz with answer key, aligned to your grade level.

**🤔 Socratic Tutor** — An AI tutor that guides students through problem-solving using the Socratic method.

👈 **Select a tool from the sidebar to get started!**
""")

st.markdown("---")
st.caption("Built at CSPD 2026 • Powered by Claude AI")
