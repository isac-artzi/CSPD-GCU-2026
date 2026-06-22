# CSPD 2026 — Agentic AI for STEM Teachers (GCU)

Welcome! This repository contains everything for the **CSPD 2026 workshop at Grand
Canyon University**: a full day of learning to build and deploy your own
AI-powered teaching tools — no prior coding experience required.

By the end you will have:
- Built a **STEM AI Toolkit** (a real web app with 3 AI tools) in Python + Streamlit
- Learned the basics of **GitHub** (how to store and share code)
- **Deployed your app to the internet** for free, with a link you can share

> 🔑 **Note on API keys:** This repo contains **no secret keys**. You'll use your
> own Anthropic API key, which stays on your computer (in a git-ignored `.env`
> file) or in Streamlit Cloud's private "Secrets" box — never in the code.

---

## 🗺️ What's in this repo

| Folder / File | What it is |
|---|---|
| `morning/` | Morning session: intro, interactive lesson, practice exercises, and a glossary (open the `.html` files in any web browser) |
| `afternoon/` | Afternoon session: the recap, the **step-by-step building guide**, and the **deployment guide** |
| `starter-project/` | The **starter** app with `TODO`s for you to complete during the workshop |
| `completed-project/` | The **finished** app — your reference if you get stuck, or a ready-to-run version |

### Key documents to open

- 💻 **Setup guide — Mac vs Windows (installing VS Code, Python, Git, Claude Code)** → [`afternoon/00-setup-mac-vs-windows.md`](afternoon/00-setup-mac-vs-windows.md)
- 📘 **Building guide** → `afternoon/02-step-by-step-guide.html`
  *(double-click to open it in your web browser)*
- 🐙 **GitHub basics primer (new to GitHub? start here)** → [`afternoon/04-github-basics-primer.md`](afternoon/04-github-basics-primer.md)
- 🚀 **Deployment guide (GitHub + Streamlit Cloud, for beginners)** → [`afternoon/03-streamlit-cloud-deployment-guide.md`](afternoon/03-streamlit-cloud-deployment-guide.md)
- 📝 **Completed project setup** → [`completed-project/README.md`](completed-project/README.md)

---

## 🏃 Quick start (run the app on your computer)

```bash
cd completed-project
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Add your Anthropic API key — copy `completed-project/.streamlit/secrets.toml.example`
to `.streamlit/secrets.toml` and paste your key in, **or** create a `.env` file with:

```
ANTHROPIC_API_KEY=sk-ant-your-real-key-here
```

Then run:

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## 🌐 Put your app on the internet

Follow the beginner-friendly guide:
**[`afternoon/03-streamlit-cloud-deployment-guide.md`](afternoon/03-streamlit-cloud-deployment-guide.md)**

It walks you through GitHub and Streamlit Community Cloud from scratch — no
command line required — and ends with a public link you can share with colleagues.

**Brand new to GitHub?** Read the
[GitHub basics primer](afternoon/04-github-basics-primer.md) first — it explains
what a repo, commit, and push are, in plain language.

---

## 📄 License

These materials are released under the [MIT License](LICENSE) — you're free to
use, adapt, and share them, including in your own classroom. Attribution is
appreciated but not required.

---

*CSPD 2026 • Agentic AI for STEM Teachers • Grand Canyon University*
*Built with [Streamlit](https://streamlit.io) • Powered by [Claude](https://claude.com)*
