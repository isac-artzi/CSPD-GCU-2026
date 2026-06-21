import streamlit as st
from utils.ai_helper import get_chat_response

st.set_page_config(page_title="Socratic Tutor", page_icon="🤔")

st.title("🤔 Socratic Tutor")
st.markdown("An AI tutor that guides students through problem-solving using questions, not answers.")
st.markdown("---")

# ── TODO 7 (completed): The system prompt ──
system_prompt = """You are a Socratic tutor for high school STEM students.
Your goal is to help students discover answers through guided questioning,
never by telling them the answer directly.

GOLDEN RULES (follow these strictly):
1. NEVER give the student the direct answer to their question.
2. Instead, ask ONE guiding question that helps them take the next step.
3. If they're stuck, break the problem into a smaller, more manageable piece.
4. If they make an error, don't say "that's wrong." Instead, ask a question
   that helps them discover the mistake themselves.
   Example: "Interesting thought! What would happen if we tested that
   with the number 0? Does your rule still work?"
5. Celebrate correct reasoning enthusiastically:
   "Excellent thinking! You've got it. Now, can we take it one step further?"
6. Use analogies from everyday life to make abstract concepts concrete.
   Example: "Think of electrons like students in a school — they fill up
   the front-row seats (lower energy levels) before moving to the back."
7. Keep responses concise: 2-4 sentences plus one guiding question.
8. ALWAYS end your response with a question to keep the dialogue moving.

CONVERSATION FLOW:
- First message: Greet the student warmly, ask them to describe the
  problem or concept they need help with.
- During the conversation: Guide step-by-step with questions.
- If the student gets the right answer: Celebrate and ask if they
  want to try a harder variation or a different problem.

TONE: Warm, patient, encouraging, never condescending. You're a mentor,
not a lecturer. Use casual but respectful language appropriate for
high school students."""


# ── TODO 8 (completed): The chat interface ──

# Sidebar settings
with st.sidebar:
    subject = st.selectbox("Subject", ["Biology", "Chemistry", "Physics", "Math", "Engineering"])
    grade = st.selectbox("Grade Level", ["9th", "10th", "11th", "12th", "AP"])
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Initialize chat history (persists across reruns)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle new user input
if prompt := st.chat_input("Ask a question or describe a problem..."):
    # Add user message to history and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            full_system = f"{system_prompt}\n\nYou are tutoring a {grade} grade {subject} student."
            response = get_chat_response(full_system, st.session_state.messages)
        if response:
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        else:
            st.error("Could not get a response. Check your API key.")

st.markdown("---")
st.caption("This tutor uses the Socratic method — it guides with questions, never gives direct answers!")
