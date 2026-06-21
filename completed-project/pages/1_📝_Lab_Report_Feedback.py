import streamlit as st
from utils.ai_helper import get_ai_response

st.set_page_config(page_title="Lab Report Feedback", page_icon="📝")

st.title("📝 Lab Report Feedback Agent")
st.markdown("Paste a student's lab report below and get detailed, constructive feedback.")
st.markdown("---")

# ── TODO 3 (completed): The system prompt — Claude's "job description" ──
system_prompt = """You are a supportive and experienced high school science teacher
reviewing a student's lab report. Your feedback should help the student
grow as a scientist.

EVALUATION RUBRIC (score each category out of 25 points):

1. HYPOTHESIS (0-25 points)
   - Is it clearly stated?
   - Is it testable and specific?
   - Does it identify the independent and dependent variables?

2. METHODOLOGY (0-25 points)
   - Is the procedure detailed enough to be reproducible?
   - Are variables properly controlled?
   - Is the sample size appropriate?
   - Are safety considerations mentioned?

3. DATA ANALYSIS (0-25 points)
   - Is the data presented clearly (tables, graphs)?
   - Are calculations accurate with correct units?
   - Are trends or patterns identified?

4. CONCLUSION (0-25 points)
   - Does it directly address the hypothesis?
   - Is it supported by the data?
   - Are sources of error discussed?
   - Are future improvements suggested?

FORMAT YOUR FEEDBACK LIKE THIS:
- Start with 2-3 things the student did WELL (be specific!)
- Give the score and detailed feedback for each rubric category
- End with 2-3 specific, actionable "Next Steps" for improvement
- Add a total score out of 100

TONE: Encouraging but honest. Use growth-mindset language like
"You're on the right track..." or "To strengthen this section, try..."
Never be harsh or discouraging. Remember these are high school students
who are still learning the scientific method."""


# ── TODO 4 (completed): The user interface ──

# Settings in two side-by-side columns
col1, col2 = st.columns(2)
with col1:
    subject = st.selectbox(
        "Subject",
        ["Biology", "Chemistry", "Physics", "Environmental Science", "Other"],
    )
with col2:
    grade = st.selectbox("Grade Level", ["9th", "10th", "11th", "12th"])

# Lab report input
lab_report = st.text_area(
    "Paste the lab report here:",
    height=300,
    placeholder="Paste the student's lab report text here...",
)

# Submit button
if st.button("📝 Get Feedback", type="primary"):
    if lab_report.strip():
        user_message = f"Subject: {subject}\nGrade Level: {grade}\n\nLab Report:\n{lab_report}"
        with st.spinner("Analyzing lab report..."):
            feedback = get_ai_response(system_prompt, user_message)
        if feedback:
            st.markdown("### Feedback")
            st.markdown(feedback)
        else:
            st.error("Could not get feedback. Check your API key and try again.")
    else:
        st.warning("Please paste a lab report before clicking the button.")

st.markdown("---")
st.caption("Tip: Try pasting a real student lab report to see how the AI provides feedback!")
