# 🦷 21-Day AI Builder — Dental Verification Prep AI

A beginner-to-builder sprint focused on shipping a useful AI product, not just watching tutorials.

## Current MVP

**Dental Verification Prep AI** helps a dental front-desk team turn fictional patient/insurance details into a structured preparation checklist for an insurance verification call.

> ⚠️ Educational portfolio demo only. Do not enter real patient data or PHI. The app does **not** verify benefits and must not be treated as payer confirmation.

### What it does

- Collects demo patient, plan and procedure details
- Uses Gemini to identify missing information
- Produces a verification checklist
- Suggests questions to ask the payer
- Returns structured JSON so the output can later power automations or a database
- Never intentionally invents benefit amounts or claims that coverage is verified

## Architecture

```text
Streamlit form (app.py)
        ↓
AI workflow (dental_ai.py)
        ↓
Gemini API
        ↓
Structured JSON
        ↓
Staff-friendly checklist
```

## Run locally

1. Install Python 3.10+.
2. Clone this repository.
3. Install packages:

```bash
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and put your own Gemini API key in `.env`.
5. Never commit `.env` or share the API key.
6. Start the app:

```bash
streamlit run app.py
```

## Project files

- `app.py` — Day 4 web interface
- `dental_ai.py` — Day 3 Gemini + structured-output logic
- `sample_data.json` — fictional test record
- `.env.example` — safe environment-variable template
- `.gitignore` — keeps secrets/local files out of Git
- `requirements.txt` — Python dependencies

## 21-Day progress

- [x] Day 1 — GitHub basics and developer setup
- [x] Day 2 — Python, VS Code and first Gemini API experiment locally
- [x] Day 3 — Structured AI workflow for dental verification preparation
- [x] Day 4 — Streamlit web MVP and safe demo data
- [ ] Day 5 — Test, polish, screenshots and hackathon-ready presentation
- [ ] Day 6+ — Deployment, credential, automation/database, competition and portfolio work

## Why this project?

The goal is to learn the full AI-builder workflow: Python → API → prompting → structured data → frontend → deployment → portfolio.

## Next milestone

Day 5 will focus on testing the app with a real API key, improving reliability and presentation, and preparing proof/screenshots for the portfolio and hackathon submission.
