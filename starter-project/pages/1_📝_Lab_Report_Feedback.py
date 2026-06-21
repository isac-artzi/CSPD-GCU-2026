import streamlit as st
from utils.ai_helper import get_ai_response

st.set_page_config(page_title="Lab Report Feedback", page_icon="📝")

st.title("📝 Lab Report Feedback Agent")
st.markdown("Paste a student's lab report below and get detailed, constructive feedback.")
st.markdown("---")

# ──────────────────────────────────────────────
# TODO 3: Write the system prompt for the Lab Report Feedback Agent
#
# This is the most important part! The system prompt tells Claude HOW to give feedback.
#
# Your system prompt should include:
#   - The AI's role (e.g., "You are an experienced high school science teacher...")
#   - What kind of feedback to give (constructive, encouraging, specific)
#   - A rubric or criteria to evaluate (e.g., hypothesis, methodology, data analysis, conclusion)
#   - The format of the feedback (e.g., start with strengths, then areas for improvement)
#   - Tone guidelines (encouraging but honest, appropriate for high school students)
#
# Example starter (customize this!):
#   system_prompt = """You are a supportive high school science teacher reviewing a student's lab report.
#
#   Evaluate the report on these criteria:
#   1. Hypothesis (clear, testable, specific)
#   2. Methodology (detailed, reproducible, controlled variables)
#   3. Data Analysis (accurate calculations, appropriate graphs, correct units)
#   4. Conclusion (supported by data, addresses hypothesis, discusses errors)
#
#   For each criterion, give a score out of 25 and specific feedback.
#   Always start with what the student did well before suggesting improvements.
#   Use an encouraging, growth-mindset tone.
#   End with 2-3 specific, actionable next steps."""
# ──────────────────────────────────────────────

system_prompt = ""  # ← Write your system prompt here!


# ──────────────────────────────────────────────
# TODO 4: Create the user interface
#
# Add these Streamlit elements:
#   1. A selectbox for the science subject:
#      subject = st.selectbox("Subject", ["Biology", "Chemistry", "Physics", "Environmental Science", "Other"])
#
#   2. A selectbox for grade level:
#      grade = st.selectbox("Grade Level", ["9th", "10th", "11th", "12th"])
#
#   3. A text_area for the lab report:
#      lab_report = st.text_area("Paste the lab report here:", height=300,
#                                 placeholder="Paste the student's lab report text here...")
#
#   4. A button to submit:
#      if st.button("📝 Get Feedback", type="primary"):
#
#   5. Inside the button's if-block:
#      - Check that lab_report is not empty
#      - Build the user_message by combining subject, grade, and lab_report:
#        user_message = f"Subject: {subject}\nGrade: {grade}\n\nLab Report:\n{lab_report}"
#      - Show a spinner: with st.spinner("Analyzing lab report..."):
#      - Call: feedback = get_ai_response(system_prompt, user_message)
#      - Display the feedback: st.markdown(feedback)
#      - If feedback is None, show: st.error("Could not get feedback. Check your API key.")
# ──────────────────────────────────────────────

# Your UI code goes here!

st.markdown("---")
st.caption("Tip: Try pasting a real student lab report to see how the AI provides feedback!")
