import streamlit as st
from utils.ai_helper import get_ai_response

st.set_page_config(page_title="Quiz Generator", page_icon="📊")

st.title("📊 Quiz Generator")
st.markdown("Generate custom quizzes for your STEM class with an answer key.")
st.markdown("---")

# ──────────────────────────────────────────────
# TODO 5: Write the system prompt for the Quiz Generator
#
# Your system prompt should tell Claude to:
#   - Generate educational quiz questions
#   - Include a mix of question types (multiple choice, short answer, true/false)
#   - Align questions to the specified grade level
#   - Vary difficulty (some easy, some medium, some challenging)
#   - Always include a complete answer key with explanations
#   - Format the output clearly with numbering
#
# Example starter:
#   system_prompt = """You are an expert STEM curriculum designer creating assessments.
#
#   When asked to create a quiz:
#   1. Generate the requested number of questions
#   2. Mix question types: multiple choice (4 options), true/false, and short answer
#   3. Order from easiest to hardest
#   4. After all questions, provide a complete ANSWER KEY with brief explanations
#   5. Align to the specified grade level and standards
#   6. Make questions clear and unambiguous"""
# ──────────────────────────────────────────────

system_prompt = ""  # ← Write your system prompt here!


# ──────────────────────────────────────────────
# TODO 6: Create the user interface
#
# Add these Streamlit elements:
#   1. Two columns for settings:
#      col1, col2 = st.columns(2)
#      with col1:
#          subject = st.selectbox("Subject", ["Biology", "Chemistry", "Physics", "Math", "Engineering", "Other"])
#          num_questions = st.slider("Number of questions", min_value=3, max_value=20, value=10)
#      with col2:
#          grade = st.selectbox("Grade Level", ["9th", "10th", "11th", "12th", "AP"])
#          difficulty = st.selectbox("Difficulty Mix", ["Mostly Easy", "Balanced", "Mostly Challenging"])
#
#   2. A text input for the topic:
#      topic = st.text_input("Quiz Topic", placeholder="e.g., Photosynthesis, Newton's Laws, Quadratic Equations")
#
#   3. An optional text area for additional instructions:
#      extra = st.text_area("Additional instructions (optional)", height=100,
#                            placeholder="e.g., Focus on real-world applications, include diagrams descriptions...")
#
#   4. A button to generate:
#      if st.button("📊 Generate Quiz", type="primary"):
#
#   5. Inside the button's if-block:
#      - Check that topic is not empty
#      - Build the user_message combining all settings
#      - Show spinner, call get_ai_response, display result
#      - Add a download button for the quiz text:
#        st.download_button("📥 Download Quiz", quiz_text, file_name=f"{topic}_quiz.txt")
# ──────────────────────────────────────────────

# Your UI code goes here!

st.markdown("---")
st.caption("Tip: Be specific with your topic for better questions!")
