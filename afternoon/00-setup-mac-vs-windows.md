# 💻 Setup Guide — Mac vs Windows

> 📄 **Two formats, same content.** This Markdown version renders nicely here on
> GitHub. There's also a styled **`00-setup-mac-vs-windows.html`** in this folder —
> double-click it to open the prettier version in your web browser. Keep the two in
> sync if you edit either.

**Read this before the building guide if you're setting up your own laptop.**
The workshop tools work the same on both Mac and Windows, but the *exact*
commands and clicks differ. This guide gives you **two columns — pick yours and
ignore the other.**

> 🍎 = **macOS** (Apple laptops/desktops)  🪟 = **Windows** (PC laptops/desktops)
>
> **Not sure which you have?** 🍎 Apple menu in the top-left corner = Mac.
> 🪟 a Start button / Windows logo in the bottom-left = Windows.

---

## 🔑 The cheat sheet (keep this handy)

These are the differences you'll bump into all day. The rest of this guide
explains each one.

| Thing | 🍎 macOS | 🪟 Windows |
|---|---|---|
| Terminal app | **Terminal** (or iTerm) | **PowerShell** (recommended) or Command Prompt |
| The "modifier" key in shortcuts | **Cmd** (⌘) | **Ctrl** |
| Open terminal in VS Code | `` Cmd+` `` | `` Ctrl+` `` |
| Python command | `python3` and `pip3` | `python` and `pip` |
| Turn on the virtual environment | `source venv/bin/activate` | `venv\Scripts\activate` |
| Folder separator in paths | forward slash `/` | backslash `\` |
| Set an environment variable | `export NAME="value"` | `$env:NAME="value"` (PowerShell) |
| Home folder | `~` (e.g. `~/Desktop`) | `%USERPROFILE%` (e.g. `%USERPROFILE%\Desktop`) |

> 💡 **Why `python3` on Mac but `python` on Windows?** Macs historically shipped
> an old Python 2 as `python`, so the modern one is `python3`. On Windows the
> installer registers it as plain `python`. If one doesn't work, try the other —
> that's the single most common "it's not working" cause.

---

# Part 1 — Install the tools

You need three free tools: **VS Code** (the editor), **Python** (the language),
and **Git** (for GitHub). Install them in this order.

## 1.1 — VS Code

VS Code is the program you'll write code in.

### 🍎 macOS
1. Go to **[code.visualstudio.com](https://code.visualstudio.com)** and click **Download for Mac**.
2. Open the downloaded `.zip` — it becomes **Visual Studio Code.app**.
3. **Drag it into your Applications folder** (important — don't run it from Downloads).
4. Open it from Applications (or press `Cmd+Space`, type "Visual Studio Code", Enter).

### 🪟 Windows
1. Go to **[code.visualstudio.com](https://code.visualstudio.com)** and click **Download for Windows**.
2. Run the downloaded installer (`VSCodeUserSetup-….exe`).
3. ✅ On the setup screens, **check the box "Add to PATH"** and **"Add 'Open with Code' action"** — these make life easier later.
4. Finish, then open VS Code from the Start menu.

## 1.2 — Python

### 🍎 macOS
The cleanest option for beginners:
1. Go to **[python.org/downloads](https://www.python.org/downloads/)** and click the big **Download Python 3.x** button.
2. Open the `.pkg` installer and click through (defaults are fine).
3. Verify — open **Terminal** (`Cmd+Space`, type "Terminal") and run:
   ```bash
   python3 --version
   ```
   You should see `Python 3.x.x`.

### 🪟 Windows
1. Go to **[python.org/downloads](https://www.python.org/downloads/)** and click **Download Python 3.x**.
2. Run the installer, and on the **first screen** ✅ **check the box that says
   "Add python.exe to PATH"** at the bottom. **This is the #1 thing Windows
   beginners forget**, and skipping it causes "python is not recognized" errors.
3. Click **"Install Now"**, finish.
4. Verify — open **PowerShell** (right-click Start → "Windows PowerShell") and run:
   ```powershell
   python --version
   ```
   You should see `Python 3.x.x`.

> 🪟 ⚠️ **If you forgot the "Add to PATH" checkbox:** the easiest fix is to
> re-run the installer, choose **Modify**, and tick the PATH option — or just
> uninstall Python and reinstall, being careful to check the box this time.

## 1.3 — Git (needed for GitHub)

Git is the tool that talks to GitHub. (You can do a lot on the GitHub website
without it — see the [GitHub primer](04-github-basics-primer.md) — but installing
Git unlocks the full workflow.)

### 🍎 macOS
Macs can install Git with one command. Open **Terminal** and run:
```bash
xcode-select --install
```
A dialog pops up — click **Install**. (This installs Apple's developer command-line
tools, which include Git.) Verify with:
```bash
git --version
```

### 🪟 Windows
1. Go to **[git-scm.com/download/win](https://git-scm.com/download/win)** — the download starts automatically.
2. Run the installer. The defaults are fine for beginners — just keep clicking **Next**.
   - It also installs **Git Bash**, a Mac-style terminal, and **Git Credential Manager**, which handles your GitHub sign-in for you.
3. Verify — open a **new** PowerShell window and run:
   ```powershell
   git --version
   ```

> 🪟 💡 **Line endings (you can ignore this, but here's why it exists):** the Git
> for Windows installer asks about "line endings." The default
> (*"Checkout Windows-style, commit Unix-style"*) is correct — leave it. It quietly
> prevents a common Mac↔Windows formatting mismatch in shared files.

---

# Part 2 — Using the tools (the differences that bite)

Once everything's installed, here are the per-OS specifics for the workshop.
The [building guide](02-step-by-step-guide.html) walks through the actual steps;
this section is the **Mac-vs-Windows translation** for each one.

## 2.1 — Opening a terminal inside VS Code
- 🍎 Press `` Cmd+` `` (the key above Tab), or menu **Terminal → New Terminal**.
- 🪟 Press `` Ctrl+` ``, or menu **Terminal → New Terminal**.
- 🪟 On Windows, VS Code's terminal usually opens **PowerShell** by default — that's
  what we recommend. You can tell it's PowerShell because the prompt starts with `PS`.

## 2.2 — Telling VS Code which Python to use ("select interpreter")
After you create your virtual environment (next step), point VS Code at it so it
uses the right Python:
1. Press `Cmd+Shift+P` (🍎) / `Ctrl+Shift+P` (🪟) to open the **Command Palette**.
2. Type **"Python: Select Interpreter"** and press Enter.
3. Choose the one that has **`venv`** in its name (your project's environment).

This step is the same idea on both systems — only the shortcut key differs.

## 2.3 — Create & activate the virtual environment
A virtual environment ("venv") is a private toolbox of packages for this project.

### 🍎 macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

### 🪟 Windows (PowerShell)
```powershell
python -m venv venv
venv\Scripts\activate
```

✅ **Both:** when it works, your prompt shows `(venv)` at the start.

> 🪟 ⚠️ **If Windows says "running scripts is disabled on this system"** when you
> activate, run this once, then try again:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```
> (This permits scripts you create locally — a normal, safe setting for development.)

## 2.4 — Install the packages (same on both)
```bash
pip install -r requirements.txt
```
> If `pip` isn't found, try `pip3` (🍎) or `python -m pip install -r requirements.txt` (🪟).

## 2.5 — Set your API key (for running locally in the terminal)
This makes the key available for the current terminal session.

- 🍎 macOS / Linux:
  ```bash
  export ANTHROPIC_API_KEY="sk-ant-your-real-key-here"
  ```
- 🪟 Windows — PowerShell:
  ```powershell
  $env:ANTHROPIC_API_KEY="sk-ant-your-real-key-here"
  ```
- 🪟 Windows — Command Prompt:
  ```cmd
  set ANTHROPIC_API_KEY=sk-ant-your-real-key-here
  ```

> 💡 **A friendlier option for beginners:** instead of the command above, put the
> key in a `.env` file in your project (the workshop app reads it automatically).
> See the [completed project README](../completed-project/README.md). The `.env`
> approach works identically on Mac and Windows.

## 2.6 — Run the app (same on both)
```bash
streamlit run app.py
```
Your browser opens to `http://localhost:8501`.

---

# Part 3 — GitHub (per-OS notes)

The [GitHub primer](04-github-basics-primer.md) and
[deployment guide](03-streamlit-cloud-deployment-guide.md) cover GitHub in full.
Here are the only real Mac-vs-Windows differences:

| Step | 🍎 macOS | 🪟 Windows |
|---|---|---|
| Installing Git | `xcode-select --install` (see 1.3) | Git for Windows installer (see 1.3) |
| Signing in on first `git push` | A browser window opens; sign in to GitHub | **Git Credential Manager** opens a browser; sign in once and it remembers you |
| The "no-command-line" path | Drag-and-drop upload on github.com works the same | Same — github.com in any browser |

> ✅ **Easiest for everyone, both OSes:** you can do the entire workshop's GitHub
> work in your **web browser** (upload by drag-and-drop, edit with the pencil icon).
> No terminal required. The primer explains this path.

---

# Part 4 — Claude Code (optional / for the curious) 🤖

**Claude Code** is a separate, free tool: an AI coding assistant that runs in your
terminal and can read, write, and run code in your project for you. It's **not
required** to build or deploy the workshop app — but if you want to try it, here's
the Mac-vs-Windows setup.

> 🧭 **Workshop app vs. Claude Code — don't mix them up.** The app you build uses
> the **Anthropic API** (your `sk-ant-…` key) from Python. **Claude Code** is a
> standalone assistant you talk to in the terminal. Different tools, both made by
> Anthropic.

## 4.1 — Install Claude Code

### 🍎 macOS *(needs macOS 13 or newer)*
Open **Terminal** and run:
```bash
curl -fsSL https://claude.ai/install.sh | bash
```
*(Prefer Homebrew? `brew install --cask claude-code` also works.)*

### 🪟 Windows *(needs 64-bit Windows 10 or newer)*
Open **PowerShell** (right-click Start → "Windows PowerShell") and run:
```powershell
irm https://claude.ai/install.ps1 | iex
```
- After it finishes, **close and reopen PowerShell** so it recognizes the new `claude` command.
- *(Optional but nice: installing [Git for Windows](https://git-scm.com/download/win) first gives Claude Code a Bash shell to work in.)*

> 🪟 ⚠️ **`irm` is not recognized?** You're in **Command Prompt**, not PowerShell.
> PowerShell's prompt starts with `PS`. Close the window and open *Windows
> PowerShell* instead.

## 4.2 — Start it
In any project folder, just type:
```
claude
```
- 🍎 Run this in **Terminal**.
- 🪟 Run this in **PowerShell** (or Command Prompt, or Windows Terminal).

The first time, it opens your browser to **sign in** — log in with your
Claude.ai account and you're ready. (You can also authenticate with an API key by
setting `ANTHROPIC_API_KEY`, exactly like in §2.5.)

## 4.3 — Using Claude Code inside VS Code
1. Open the Extensions panel: `Cmd+Shift+X` (🍎) / `Ctrl+Shift+X` (🪟).
2. Search **"Claude Code"** and click **Install**.
3. A few handy shortcuts differ by OS:

| Action | 🍎 macOS | 🪟 Windows |
|---|---|---|
| Toggle the Claude panel | `Cmd+Esc` | `Ctrl+Esc` |
| Insert an @-mention of the current file/selection | `Option+K` | `Alt+K` |
| Command Palette (then type "Claude Code") | `Cmd+Shift+P` | `Ctrl+Shift+P` |

## 4.4 — Common "command not found" fix
If your terminal says `claude: command not found` (🍎) or `claude is not
recognized` (🪟) right after installing, the tool installed correctly but your
terminal can't see it yet:
- 🍎 **macOS:** add it to your PATH, then reopen Terminal:
  ```bash
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
  source ~/.zshrc
  ```
- 🪟 **Windows:** the simplest fix is to **restart your computer** (Windows reads
  the PATH at startup). Then open a fresh PowerShell and run `claude --version`.

---

# 🆘 Quick troubleshooting by symptom

| You see… | 🍎 macOS fix | 🪟 Windows fix |
|---|---|---|
| `python: command not found` / `not recognized` | Use `python3` | Re-run the Python installer and ✅ check "Add to PATH" |
| `pip: command not found` | Use `pip3` or `python3 -m pip …` | Use `python -m pip …` |
| `(venv)` never appears | Use `source venv/bin/activate` | Use `venv\Scripts\activate`; if blocked, run the `Set-ExecutionPolicy` command in §2.3 |
| `git: command not found` | `xcode-select --install` | Install Git for Windows (§1.3) |
| `claude: command not found` | Add `~/.local/bin` to PATH (§4.4) | Restart the computer (§4.4) |
| Shortcut in a guide doesn't work | Replace **Ctrl** with **Cmd** | Replace **Cmd** with **Ctrl** |

---

*CSPD 2026 • Agentic AI for STEM Teachers • Grand Canyon University*
