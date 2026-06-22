# 🐙 GitHub Basics — A Primer for Complete Beginners

**Read this before the deployment guide if "GitHub" is a new word to you.**
No experience assumed. By the end you'll understand what GitHub is, the handful
of words people throw around (repo, commit, push…), and how to actually do the
few things you need for this workshop.

> 🕐 **Time:** ~15 minutes to read. You do **not** need to memorize anything —
> come back and look things up when you need them.

---

## 1. The one-sentence version

> **Git** is a tool that tracks the history of your files. **GitHub** is a website
> that stores those files online so you can back them up and share them.

That's genuinely it. Everything else is detail.

A useful comparison:

| If you've used… | Then GitHub is like… |
|---|---|
| Google Docs | …the cloud where your document lives — but for code, with a full "version history" |
| Dropbox / Google Drive | …a shared folder in the cloud — but built specifically for code projects |
| "Track Changes" in Word | …that, but you decide exactly when to save a snapshot, and every snapshot is kept forever |

---

## 2. Why teachers should care

You need GitHub for this workshop for **one practical reason**: Streamlit Cloud
(the free service that puts your app on the internet) reads your code **from
GitHub**. So the path to a shareable app is:

```
Your computer  →  GitHub (stores the code)  →  Streamlit Cloud (runs the app)  →  Public link
```

Beyond the workshop, GitHub is also:
- A **free backup** of your work (your laptop dies; your code is safe)
- A way to **share** lesson tools with other teachers (send a link, not a zip file)
- A place to **find** thousands of free education projects to learn from or reuse

---

## 3. The vocabulary (the words people use)

You'll see these terms everywhere. Here's what each one actually means, in plain
language. **Skim it now; refer back as needed.**

| Term | Plain-English meaning | Everyday analogy |
|---|---|---|
| **Repository** ("repo") | A project folder that GitHub is tracking | A labeled folder for one project |
| **Commit** | A saved snapshot of your files at one moment, with a short note | Clicking "Save" + writing what you changed |
| **Push** | Upload your commits from your computer to GitHub | "Sync to cloud" / "Upload" |
| **Pull** | Download the latest version from GitHub to your computer | "Sync from cloud" / "Download" |
| **Clone** | Make a copy of an online repo onto your computer | "Download a copy I can work on" |
| **Fork** | Make **your own copy** of *someone else's* repo, under your account | "Copy this to my account so I can change it" |
| **Branch** | A separate line of work, so you can experiment without breaking the main version | A draft copy you can throw away |
| **`main`** | The default, primary branch — the "official" version | The master document |
| **Remote** | The online location your code is linked to (usually GitHub) | The address of your cloud folder |
| **README** | A file (`README.md`) that describes the project; GitHub shows it on the front page | The cover page / instructions |
| **`.gitignore`** | A list of files Git should **never** upload (like secret keys) | A "do not pack" list |
| **Commit message** | The short note you write describing a commit | The label on a saved version |

> 💡 **The two you'll use most often: commit (save a snapshot) and push (upload it).**

---

## 4. The mental model (how it fits together)

```
   YOUR COMPUTER                          GITHUB (the website)
   ─────────────                          ────────────────────
   your project folder                    your repository
        │                                       ▲
        │  1. commit  (save a snapshot)         │
        ▼                                       │
   saved snapshots  ───────  2. push  ─────────►│  (now backed up & shareable)
                                                │
   your project folder  ◄──── 3. pull ──────────┘  (get the latest changes back)
```

1. You **commit** to save a snapshot on your computer.
2. You **push** to upload those snapshots to GitHub.
3. If you (or a collaborator) changed things on GitHub, you **pull** to bring them down.

For this workshop you mostly do **commit → push**. That's the whole loop.

---

## 5. Two ways to use GitHub — pick what's comfortable

You do **not** have to use the command line. There are three ways in, from
easiest to most technical:

### Option A — The website (easiest, nothing to install) ⭐ recommended for beginners
Do everything in your web browser at [github.com](https://github.com):
- Create a repo with a button
- Upload files by **dragging and dropping** them onto the page
- Edit a file by clicking the **pencil ✏️ icon**, then "Commit changes"

This is exactly what the [deployment guide](03-streamlit-cloud-deployment-guide.md)
uses. **If you're nervous, use this.**

### Option B — GitHub Desktop (a friendly app, no commands)
Download [desktop.github.com](https://desktop.github.com). A point-and-click app
with buttons for **Commit** and **Push**. A nice middle ground: real Git, no typing.

### Option C — The command line (terminal)
Type commands like `git add`, `git commit`, `git push`. Most powerful, but the
steepest. You only need this if you want it — the cheat sheet is in §7.

---

## 6. The two things you'll actually do this workshop

### Thing 1 — Get your finished app onto GitHub
Create a new repo, then upload your project files. (Full step-by-step, website
version, is in the [deployment guide §2](03-streamlit-cloud-deployment-guide.md).)

### Thing 2 — Make a change later and update it
Fixed a typo or improved a prompt? Either:
- **Website:** open the file on GitHub → pencil ✏️ → edit → **Commit changes**, or
- **Desktop/CLI:** commit your change, then push it.

Streamlit Cloud notices the new version and **automatically redeploys** within a
minute or two. That's the magic: GitHub is the source of truth, and your live app
always runs the latest version.

---

## 7. Command-line cheat sheet (only if you chose Option C)

You can ignore this whole section if you're using the website or GitHub Desktop.

> 💻 **First, install Git** — `xcode-select --install` on a Mac, or the Git for
> Windows installer on Windows. Step-by-step for both is in the
> [Setup Guide — Mac vs Windows](00-setup-mac-vs-windows.html) (Part 1.3).

```bash
# One time, on a new computer — tell Git who you are
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Start tracking a project folder you already have
cd path/to/your/project
git init                      # turn this folder into a repo
git add -A                    # stage ALL your files for the next snapshot
git commit -m "First version" # save the snapshot, with a note
git branch -M main            # name the main branch "main"

# Connect it to your empty GitHub repo and upload
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main       # upload (push) to GitHub

# Day-to-day after that
git add -A                    # stage your changes
git commit -m "Describe what changed"
git push                      # upload them

# Bring down changes made on GitHub
git pull

# See what's changed / what's staged
git status

# Copy an existing repo onto your computer
git clone https://github.com/SOMEONE/THEIR-REPO.git
```

> 💡 **Writing good commit messages:** describe *what changed*, briefly.
> "Fix typo in quiz prompt" is great. "stuff" or "asdf" is not helpful when you're
> looking back in six months.

---

## 8. ⚠️ The one rule you must never break

**Never put secrets — like your Anthropic API key — into a file you commit to GitHub.**

A public repo can be read by *anyone* on the internet. A leaked API key is like a
leaked credit card: someone can find it and run up charges. This is why every
project here includes a **`.gitignore`** file that lists `.env` and
`secrets.toml` — those hold your key and must stay on your computer only.

**If you ever think you committed a key:**
1. Go to [console.anthropic.com](https://console.anthropic.com) → API Keys → **delete (revoke)** that key immediately.
2. Create a new one.
3. Make sure it's only in your local `.env` / Streamlit Secrets, never in code.

The deployment guide is built so this can't happen if you follow it — the key
goes in Streamlit's private **Secrets** box, not in your code.

---

## 9. Frequently asked questions

**Do I need to install anything to use GitHub?**
No — the website does everything. Install GitHub Desktop or Git only if you want
the app or command-line workflow.

**Is my code visible to everyone?**
If the repo is **public**, yes — anyone can read the code (but not your secret
key, which is never in the code). You can also make repos **private** (visible
only to you and people you invite). Free Streamlit Cloud needs a public repo.

**What's the difference between Git and GitHub again?**
Git is the tool on your computer that tracks changes. GitHub is the website that
hosts your repos online. You can use Git without GitHub, but for sharing and
deploying, you want both.

**What's the difference between "clone" and "fork"?**
**Clone** = download a copy to your computer. **Fork** = make your own copy of
*someone else's* repo under *your* GitHub account (then you can clone your fork).
Fork when you want to build on someone else's project.

**I made a mistake — can I undo it?**
Almost always, yes. Every commit is a saved snapshot, so you can go back. This is
the whole point of Git — it's a safety net. Ask a facilitator if you're stuck.

**Where do I get help?**
- GitHub's own guides: [docs.github.com/get-started](https://docs.github.com/en/get-started)
- A facilitator at the workshop
- The [deployment guide](03-streamlit-cloud-deployment-guide.md) for the exact steps

---

## ✅ You're ready

You now know what GitHub is, the words people use, and the two things you'll do
(commit and push). Head to the
**[deployment guide](03-streamlit-cloud-deployment-guide.md)** to put your app on
the internet.

---

*CSPD 2026 • Agentic AI for STEM Teachers • Grand Canyon University*
