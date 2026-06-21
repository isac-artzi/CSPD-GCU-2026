import streamlit as st
from utils.ai_helper import get_chat_response

st.set_page_config(page_title="Socratic Tutor", page_icon="🤔")

st.title("🤔 Socratic Tutor")
st.markdown("An AI tutor that guides students through problem-solving using questions, not answers.")
st.markdown("---")

# ──────────────────────────────────────────────
# TODO 7: Write the system prompt for the Socratic Tutor
#
# This is the trickiest prompt! The AI must:
#   - NEVER give direct answers
#   - Ask guiding questions that lead students to discover answers themselves
#   - Break complex problems into smaller, manageable steps
#   - Celebrate correct reasoning and gently redirect mistakes
#   - Adapt to the student's level of understanding
#   - Be patient, encouraging, and never condescending
#
# Example starter:
#   system_prompt = """You are a Socratic tutor for high school STEM students.
#
#   GOLDEN RULES:
#   - NEVER give the student the direct answer
#   - Instead, ask guiding questions that help them discover the answer
#   - If they're stuck, break the problem into smaller pieces
#   - If they make an error, ask a question that helps them see it
#   - Celebrate correct reasoning: "Great thinking! Now let's take it further..."
#   - Use analogies from everyday life when concepts are abstract
#   - Keep responses concise (2-4 sentences plus a guiding question)
#   - Always end your message with a question to keep the dialogue going"""
# ──────────────────────────────────────────────

system_prompt = ""  # ← Write your system prompt here!


# ──────────────────────────────────────────────
# TODO 8: Create the chat interface
#
# Streamlit has built-in chat components! Here's what to add:
#
#   1. Set up the subject selector in the sidebar:
#      with st.sidebar:
#          subject = st.selectbox("Subject", ["Biology", "Chemistry", "Physics", "Math", "Engineering"])
#          grade = st.selectbox("Grade Level", ["9th", "10th", "11th", "12th", "AP"])
#          if st.button("🗑️ Clear Chat"):
#              st.session_state.messages = []
#              st.rerun()
#
#   2. Initialize chat history in session state:
#      if "messages" not in st.session_state:
#          st.session_state.messages = []
#
#   3. Display existing chat messages:
#      for msg in st.session_state.messages:
#          with st.chat_message(msg["role"]):
#              st.markdown(msg["content"])
#
#   4. Handle new user input:
#      if prompt := st.chat_input("Ask a question or describe a problem..."):
#          # Add user message to history
#          st.session_state.messages.append({"role": "user", "content": prompt})
#          with st.chat_message("user"):
#              st.markdown(prompt)
#
#          # Get AI response
#          with st.chat_message("assistant"):
#              with st.spinner("Thinking..."):
#                  # Build the full system prompt with subject context
#                  full_system = f"{system_prompt}\n\nYou are tutoring a {grade} grade {subject} student."
#                  response = get_chat_response(full_system, st.session_state.messages)
#                  if response:
#                      st.markdown(response)
#                      st.session_state.messages.append({"role": "assistant", "content": response})
#                  else:
#                      st.error("Could not get a response. Check your API key.")
# ──────────────────────────────────────────────

# Your chat code goes here!

st.markdown("---")
st.caption("This tutor uses the Socratic method — it guides with questions, never gives direct answers!")
