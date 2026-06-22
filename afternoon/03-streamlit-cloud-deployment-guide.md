# 🚀 Putting Your App on the Internet
## A Beginner's Guide to Streamlit Community Cloud

**For teachers who have never coded, never used GitHub, and never deployed anything.**
That's totally fine — this guide assumes you know *nothing*. Read it top to bottom and
follow along. By the end you'll have a real web link you can email to a colleague.

> ⏱️ **Time needed:** about 20–30 minutes the first time.
> 💵 **Cost:** $0. Everything here is free.
> 🐙 **Never used GitHub?** Read the
> [GitHub basics primer](04-github-basics-primer.md) first (~15 min) — it explains
> the words used below (repo, commit, push) in plain language.

---

## 📖 First, the big picture (read this — it makes everything else make sense)

Right now your app only runs on **your** computer. When you close your laptop, the app
turns off. "Deploying" means putting a copy of your app on a computer that's always on,
out on the internet, so anyone with the link can use it — like publishing a document to
the web instead of keeping it on your desktop.

To do this for free we use **three free services**. Here's what each one is, in plain English:

| Service | What it really is | Your everyday analogy |
|---|---|---|
| **GitHub** | A website that stores your code files | A cloud folder (like Google Drive) — but for code |
| **Streamlit Community Cloud** | A free host that *runs* your app | The "always-on computer" that shows your app to the world |
| **Anthropic Console** | Where your AI key lives | The "ID card" that lets your app talk to Claude |

**The flow:** You upload your code to **GitHub** → **Streamlit Cloud** reads it from GitHub
and runs it → you give it your **Anthropic key** so the AI works → you get a public link. 🎉

> 🔑 **The single most important rule in this whole guide:**
> **NEVER let your API key end up on GitHub.** Your key is like a credit card — anyone
> who finds it can spend money with it. We'll handle the key in a special, safe place
> (Streamlit's "Secrets" box), *not* in your code. This guide is built so you can't
> mess this up if you follow it.

---

## ✅ Before you start — a 2-minute checklist

You need three things. Don't worry if you don't have them yet; links are below.

- [ ] **Your finished app folder** on your computer (the `completed-project` folder, or
      your own copy where all the TODOs are done and the app runs locally).
- [ ] **An email address** you can check (for signing up).
- [ ] **Your Anthropic API key** — the secret code starting with `sk-ant-...` that you
      received at the workshop. (If you lost it, see *"Where do I get an API key?"* at the bottom.)

---

# Part 1 — Create your free accounts

## Step 1.1 — Create a GitHub account

1. Go to **https://github.com/signup**
2. Enter your email, make a password, and pick a username.
   - 💡 Your username becomes part of your app's web address, so pick something simple
     and professional (e.g., `jsmith-science`, not `xX_coolteacher_Xx`).
3. Verify your email when GitHub sends you a confirmation.

That's it. You now have a free place to store code. **You do not need to install anything.**

## Step 1.2 — Create a Streamlit Community Cloud account

1. Go to **https://share.streamlit.io**
2. Click **"Continue with GitHub"** (this is the easy path — it links the two accounts so
   they can talk to each other).
3. A screen will ask you to **"Authorize Streamlit."** Click the green **Authorize** button.
   - This is normal and safe. You're telling GitHub: *"It's okay for Streamlit to read my
     code so it can run my app."*

Done. Both accounts now exist and are connected. ✨

---

# Part 2 — Get your code onto GitHub (the no-command-line way)

There are two ways to do this. **Method A uses only your web browser — no typing
commands. We strongly recommend it for beginners.**

## ⭐ Method A — Upload through the website (recommended, no commands)

### Step 2.1 — Make a new, empty repository

A "repository" (or "repo") is just GitHub's word for a project folder.

1. Go to **https://github.com/new**
2. **Repository name:** type `stem-ai-toolkit`
3. **Description** (optional): "My AI teaching toolkit"
4. Choose **Public**.
   - ℹ️ *"Public" means people can see the code, not that they can see your API key —
     your key is never in the code.* Public is required for the free Streamlit tier.
5. **Leave every checkbox unchecked** (don't add a README, .gitignore, or license —
   your folder already has what it needs).
6. Click the green **"Create repository"** button.

### Step 2.2 — Upload your files

On the page that appears, find the link that says **"uploading an existing file"**
(it's in the small text near the top). Click it.

1. Open your `completed-project` folder on your computer in a file window
   (Finder on Mac, File Explorer on Windows).
2. **Select everything inside the folder** (Ctrl+A on Windows, Cmd+A on Mac) and
   **drag it onto the GitHub upload page.**

   > ⚠️ **Drag the *contents*, not the folder itself.** GitHub should show
   > `app.py`, `requirements.txt`, the `pages` folder, the `utils` folder, and the
   > `.streamlit` folder. If you only see one folder named `completed-project`, you
   > dragged the wrong thing — remove it and drag the files from *inside* instead.

3. Scroll down and click the green **"Commit changes"** button. ("Commit" just means "save.")

### Step 2.3 — Confirm your key is NOT there (10-second safety check)

Look at your list of files on GitHub. You should see `app.py`, `requirements.txt`, etc.

- ✅ **Good:** You do **not** see a file called `secrets.toml`.
- 🚨 **Stop if:** you see a file named `secrets.toml`. Click it → click the trash/delete
  icon → commit the deletion. That file contains your key and must never be on GitHub.
  (The included `.gitignore` is designed to prevent this, but always double-check.)

**🎉 Your code is now on GitHub. Skip Method B and go to Part 3.**

---

## Method B — Using Git commands (only if you already know/want the terminal)

<details>
<summary>Click to expand — for users comfortable with a terminal</summary>

From inside your project folder:

```bash
git init
git add -A
git commit -m "Complete STEM AI Toolkit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/stem-ai-toolkit.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Because the project includes a
`.gitignore` that lists `.streamlit/secrets.toml`, your key won't be uploaded — but
run `git status` before committing to be sure no secrets are staged.
</details>

---

# Part 3 — Deploy the app on Streamlit Cloud

This is the fun part. You'll turn your GitHub code into a live website.

### Step 3.1 — Start a new app

1. Go to **https://share.streamlit.io**
2. Click the **"Create app"** button (sometimes labeled **"New app"**), near the top right.
3. If asked, choose **"Deploy a public app from GitHub."**

### Step 3.2 — Tell Streamlit where your code is

You'll see a short form. Fill it in like this:

| Field | What to put |
|---|---|
| **Repository** | Pick `your-username/stem-ai-toolkit` from the dropdown |
| **Branch** | `main` (it's usually filled in already) |
| **Main file path** | `app.py` |
| **App URL** (optional) | Customize the end of your web address if you like |

> 💡 If your repository doesn't show up in the dropdown, click the
> **"Manage app permissions"** / refresh link, or just wait a few seconds and reload —
> GitHub and Streamlit sometimes take a moment to sync.

### Step 3.3 — Add your secret API key (THE important step) 🔑

**Do not click Deploy yet.** First:

1. Click **"Advanced settings…"** (a small link on the deploy form).
2. Find the **"Secrets"** box — a large empty text area.
3. Paste **exactly this one line**, replacing the placeholder with your real key:

   ```toml
   ANTHROPIC_API_KEY = "sk-ant-your-real-key-here"
   ```

   - Keep the quotation marks `" "`.
   - Your real key starts with `sk-ant-`. Paste the whole thing between the quotes.
   - This box is private and encrypted. It is **not** part of your GitHub code, so this
     is the safe place for your key. ✅

4. Click **"Save"** to close the Advanced settings.

### How the secret actually reaches your app 🔌

It's worth understanding *why* that one line makes the AI work — it's the link
between your key and the code, and the #1 source of "why won't it work?" problems.

Inside the app, the file `utils/ai_helper.py` asks Streamlit for the key by name:

```python
api_key = st.secrets.get("ANTHROPIC_API_KEY", None)   # looks up the name "ANTHROPIC_API_KEY"
```

`st.secrets` is Streamlit's built-in, private vault. Whatever you paste into the
**Secrets** box becomes available to your code through `st.secrets`. So:

> ⚠️ **The name on the left must match exactly.** The Secrets box says
> `ANTHROPIC_API_KEY` and the code asks for `ANTHROPIC_API_KEY`. If you rename one
> (a typo, lowercase, extra spaces), they stop matching and the app can't find the
> key — even though the key itself is perfectly valid. This is the most common
> deployment mistake.

```
   Secrets box on Streamlit Cloud          Your code
   ─────────────────────────────          ─────────────────────────────────
   ANTHROPIC_API_KEY = "sk-ant-…"  ─────►  st.secrets["ANTHROPIC_API_KEY"]
        (the name must be identical on both sides)
```

You do **not** edit any code to make this work — the app is already written to read
`st.secrets`. You only provide the value, in the Secrets box.

#### Running locally? Same key, two easy options

When you run the app on **your own computer** (not Streamlit Cloud), there's no
online Secrets box — so the app reads the key one of two ways instead. Pick either:

**Option 1 — a local secrets file** (mirrors how Cloud works). In your project,
create the file `.streamlit/secrets.toml` and put the same line in it:

```toml
ANTHROPIC_API_KEY = "sk-ant-your-real-key-here"
```

There's a ready-made template at `.streamlit/secrets.toml.example` — copy it,
rename the copy to `secrets.toml`, and paste your key in.

**Option 2 — a `.env` file** (what we used in the workshop). Create a file named
`.env` with:

```
ANTHROPIC_API_KEY=sk-ant-your-real-key-here
```

> 🔑 **Both files are already in `.gitignore`**, so neither one is ever uploaded to
> GitHub. Your local key stays on your computer; the Cloud key stays in the Secrets
> box. The same code works in all three places without any changes.

### Step 3.4 — Deploy!

Click the big **"Deploy"** button.

You'll see a screen with messages scrolling by (it's installing Streamlit and Anthropic —
the same thing `pip install` did on your computer). ☕ This takes **2–5 minutes the first
time.** It's normal. Don't close the tab.

When it finishes, **your app appears, live on the web!**

### Step 3.5 — Get and share your link

Your app now has a public address like:

```
https://stem-ai-toolkit.streamlit.app
```

Copy it from your browser's address bar and email it to a colleague. They can use all
three tools right in their browser — **no installation needed on their end.** 🥳

---

# 🛠️ When something goes wrong (it's okay — this is normal)

Deployment rarely works perfectly the first time for anyone. Here are the issues you're
most likely to hit, in plain language, with fixes.

### "I clicked Deploy and got a red error / the app says 'Oh no.'"

Click **"Manage app"** (bottom-right corner of your app) to open the **logs** — the
running diary of what your app is doing. Scroll to the bottom and read the **last few
red lines**. They almost always name the exact problem. Match it to one below.

### `ModuleNotFoundError: No module named 'anthropic'` (or 'streamlit')

Streamlit didn't know it needed to install that package.
- **Fix:** Make sure a file named exactly `requirements.txt` is in your repository, and
  that it contains these two lines:
  ```
  streamlit>=1.35.0
  anthropic>=0.30.0
  ```
- After fixing on GitHub, your app will usually redeploy automatically.

### The app loads, but a tool shows "AI request failed" or "Could not get feedback"

This is almost always the **API key**.
- **Fix:** In your live app, click **"Manage app" → "Settings" → "Secrets"** and confirm
  the line is there and correct:
  ```toml
  ANTHROPIC_API_KEY = "sk-ant-..."
  ```
  Common mistakes: missing quotes, a typo, an extra space, or pasting only part of the key.
  Fix it, click **Save**, then **"Reboot app"** from the Manage menu.
- Still failing? Your key may be expired or out of credit. See the API key section below.

### "The pages in the sidebar are missing!"

Streamlit only knows about pages it can find.
- **Fix:** On GitHub, confirm there's a `pages` folder containing your three `.py` files.
  If you accidentally uploaded the files loose (not inside a `pages` folder), delete them
  and re-upload keeping the folder structure.

### My repository doesn't appear in Streamlit's dropdown

- **Fix:** Reload the deploy page. If it's still missing, click your avatar (top-right) →
  **"Settings"** → make sure Streamlit has permission to see your GitHub repos, or
  re-run the "Authorize Streamlit" step from Part 1.

### I accidentally uploaded my API key to GitHub! 😱

Don't panic, but act:
1. **Treat the key as compromised.** Go to the Anthropic Console and **delete (revoke)
   that key**, then create a new one.
2. Update the new key in Streamlit's **Secrets** box (not in your code).
3. Delete the `secrets.toml` file from your GitHub repo.

This is exactly why we keep keys in the Secrets box — so this can't happen if you follow
the guide.

### My app went to sleep / shows "This app has gone to sleep"

Free apps nap after a period of no use. Just click the **"Wake up"** button — it comes
back in a few seconds. Nothing is broken.

---

# 🔄 How to update your app later

Made an improvement (new tool, better prompt)? Updating is easy:

1. Edit the file. The simplest way without commands: open the file on GitHub in your
   browser, click the **pencil ✏️ icon**, make your change, and click **"Commit changes."**
2. Streamlit **automatically notices and redeploys** within a minute or two. Refresh
   your app to see the update.

That's the magic of this setup: GitHub is the source of truth, and Streamlit always runs
the latest version.

---

# ❓ Frequently asked questions

**Is this really free?**
Yes. GitHub public repos and Streamlit Community Cloud are free. You only pay for the
AI usage through Anthropic (and the workshop key may cover that — ask your facilitator).

**Will my students see my code or my API key?**
They see your *app*, not your code or key. The code is technically public on GitHub
(but harmless), and the key lives only in the private Secrets box.

**Is my app private? Can I limit who uses it?**
The free tier gives a public link — anyone with the link can open it. For classroom use
that's usually fine (share the link only with your class). Streamlit also offers ways to
restrict access by inviting specific Google/email accounts via "Settings → Sharing."

**Can lots of students use it at the same time?**
The free tier has modest limits (good for a class, not a whole school at once). If it
feels slow under heavy use, that's the resource limit — see https://streamlit.io/cloud.

**Where do I get an API key?** *(if you lost the workshop one)*
1. Go to **https://console.anthropic.com**, sign in (or sign up).
2. In the left menu, click **"API Keys."**
3. Click **"Create Key,"** give it a name, and **copy it immediately** — you can't see it
   again later. Store it somewhere safe (a password manager is ideal).
4. New accounts need credit added under **"Billing"** before the key will work. The
   workshop tools cost only a fraction of a cent per use.

**What's the difference between this and the key I `export`ed on my laptop?**
Same key, different home. On your laptop it lived in an environment variable or a local
`secrets.toml`. On Streamlit Cloud it lives in the online Secrets box. The app code
(`utils/ai_helper.py`) is written to read from whichever one is available — so it just
works in both places.

---

# 🎓 You did it!

You took code from your laptop, stored it on GitHub, ran it on a cloud server, and
published a working AI app to the internet — the exact same workflow professional
software teams use. Share that link with pride.

---

*CSPD 2026 • Agentic AI for STEM Teachers • Afternoon Session*
*Built with Streamlit • Powered by Claude AI*
