import streamlit as st
from utils.ai_helper import get_ai_response

st.set_page_config(page_title="Quiz Generator", page_icon="📊")

st.title("📊 Quiz Generator")
st.markdown("Generate custom quizzes for your STEM class with an answer key.")
st.markdown("---")

# ── TODO 5 (completed): The system prompt ──
system_prompt = """You are an expert STEM curriculum designer creating quizzes
and assessments for high school students.

QUIZ CREATION RULES:
1. Generate exactly the number of questions requested.
2. Mix question types:
   - Multiple choice (4 options labeled A-D, with exactly one correct answer)
   - True/False (with brief justification in the answer key)
   - Short answer (1-3 sentences expected)
3. Order questions from easiest to most challenging.
4. Make every question clear and unambiguous.
5. Align difficulty and vocabulary to the specified grade level.
6. Include real-world applications and critical thinking questions,
   not just rote memorization.

OUTPUT FORMAT:
- Title the quiz with the topic and grade level
- Number each question clearly
- After ALL questions, include a clearly labeled ANSWER KEY section
- In the answer key, provide the correct answer AND a brief explanation
  for each question (1-2 sentences explaining WHY it's correct)
- At the end, list which standards or key concepts each question addresses

IMPORTANT: Never include inappropriate, biased, or culturally insensitive
content. Questions should be inclusive and accessible to all students."""


# ── TODO 6 (completed): The user interface ──

# Settings in two columns
col1, col2 = st.columns(2)
with col1:
    subject = st.selectbox(
        "Subject", ["Biology", "Chemistry", "Physics", "Math", "Engineering", "Other"]
    )
    num_questions = st.slider("Number of questions", min_value=3, max_value=20, value=10)
with col2:
    grade = st.selectbox("Grade Level", ["9th", "10th", "11th", "12th", "AP"])
    difficulty = st.selectbox(
        "Difficulty Mix", ["Mostly Easy", "Balanced", "Mostly Challenging"]
    )

# Topic input
topic = st.text_input(
    "Quiz Topic",
    placeholder="e.g., Photosynthesis, Newton's Laws, Quadratic Equations",
)

# Optional extra instructions
extra = st.text_area(
    "Additional instructions (optional)",
    height=100,
    placeholder="e.g., Focus on real-world applications, include diagram descriptions...",
)

# Generate button
if st.button("📊 Generate Quiz", type="primary"):
    if topic.strip():
        user_message = f"""Create a quiz with the following specifications:
- Subject: {subject}
- Topic: {topic}
- Grade Level: {grade}
- Number of Questions: {num_questions}
- Difficulty Mix: {difficulty}"""
        if extra.strip():
            user_message += f"\n- Additional Instructions: {extra}"

        with st.spinner("Generating your quiz..."):
            quiz_text = get_ai_response(system_prompt, user_message)

        if quiz_text:
            st.markdown("### Your Quiz")
            st.markdown(quiz_text)
            st.download_button(
                "📥 Download Quiz",
                quiz_text,
                file_name=f"{topic}_quiz.txt",
                mime="text/plain",
            )
        else:
            st.error("Could not generate quiz. Check your API key and try again.")
    else:
        st.warning("Please enter a quiz topic.")

st.markdown("---")
st.caption("Tip: Be specific with your topic for better questions!")
