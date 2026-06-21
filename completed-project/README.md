# STEM AI Toolkit — Completed Project

This is the **finished** version of the workshop app, with all 8 TODOs completed.
Use it as a reference if you get stuck, or as a ready-to-run app you can deploy.

A multi-page Streamlit app with 3 AI-powered STEM teaching tools:

- **📝 Lab Report Feedback** — Paste a student's lab report and get rubric-based feedback.
- **📊 Quiz Generator** — Enter a topic and get a custom quiz with an answer key.
- **🤔 Socratic Tutor** — A chat tutor that guides students with questions, not answers.

Built at the **CSPD 2026 Workshop: Agentic AI for STEM Teachers**.

---

## Run it locally

### 1. Open a terminal in this folder

### 2. Create and activate a virtual environment

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You'll know it worked when you see `(venv)` at the start of your prompt.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your API key

**Mac/Linux:**
```bash
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

**Windows (Command Prompt):**
```bash
set ANTHROPIC_API_KEY=sk-ant-your-key-here
```

**Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

> **Alternative:** Instead of the command above, copy `.streamlit/secrets.toml.example`
> to `.streamlit/secrets.toml` and paste your key inside. That file is git-ignored
> so it will never be uploaded to GitHub.

### 5. Run the app

```bash
streamlit run app.py
```

It opens automatically at `http://localhost:8501`.

---

## Put it on the internet

To share this app with colleagues via a public link, follow
**`../afternoon/03-streamlit-cloud-deployment-guide.md`** — a step-by-step
guide written for complete beginners.

---

## Project structure

```
completed-project/
├── app.py                          # Home page
├── requirements.txt                # Python dependencies
├── .gitignore                      # Keeps secrets out of GitHub
├── .streamlit/
│   ├── config.toml                 # Theme settings
│   └── secrets.toml.example        # Template for your local API key
├── utils/
│   ├── __init__.py
│   └── ai_helper.py                # Shared AI functions (TODOs 1–2 done)
└── pages/
    ├── 1_📝_Lab_Report_Feedback.py  # TODOs 3–4 done
    ├── 2_📊_Quiz_Generator.py       # TODOs 5–6 done
    └── 3_🤔_Socratic_Tutor.py       # TODOs 7–8 done
```
