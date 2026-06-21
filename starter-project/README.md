# STEM AI Toolkit - Starter Project

A multi-page Streamlit app with 3 AI-powered STEM teaching tools:

- **Lab Report Feedback** - Paste a student's lab report and get detailed, constructive feedback based on your rubric.
- **Quiz Generator** - Enter a topic and get a custom quiz with answer key, aligned to your grade level.
- **Socratic Tutor** - An AI tutor that guides students through problem-solving using the Socratic method.

Built at the **CSPD 2026 Workshop: Agentic AI for STEM Teachers**.

---

## Quick Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd stem-ai-toolkit
```

### 2. Create a virtual environment

**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your API key

**Mac/Linux:**
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

**Windows (Command Prompt):**
```bash
set ANTHROPIC_API_KEY=your-key-here
```

**Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY="your-key-here"
```

### 5. Run the app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## Project Structure

```
stem-ai-toolkit/
├── app.py                          # Home page (complete)
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── config.toml                 # Streamlit theme settings
├── utils/
│   ├── __init__.py
│   └── ai_helper.py                # Shared AI utility (TODOs 1-2)
└── pages/
    ├── 1_📝_Lab_Report_Feedback.py  # Lab report tool (TODOs 3-4)
    ├── 2_📊_Quiz_Generator.py       # Quiz generator (TODOs 5-6)
    └── 3_🤔_Socratic_Tutor.py       # Socratic tutor (TODOs 7-8)
```

## Need Help?

Follow the step-by-step guide provided in the workshop materials, or ask a facilitator!
