# 🦷 DentalVerify AI

**AI-powered preparation assistant for structured dental insurance verification.**

🌐 **Live demo:** https://21-day-ai-builder-byaneeq.streamlit.app/

DentalVerify AI is the product built during my 21-Day AI Builder sprint. It turns fictional dental patient/insurance intake information into a structured verification-preparation workflow for front-desk staff.

> ⚠️ **Portfolio/educational demo only.** Do not enter real patient data or PHI. The app does not verify eligibility or benefits and is not payer confirmation.

## The problem

Dental insurance verification involves collecting plan information, spotting missing details, and preparing many repetitive questions before contacting a payer. Missing information can slow the workflow down.

## The solution

DentalVerify AI uses Google Gemini to transform fictional intake details into:

- missing-information checks
- a structured verification checklist
- questions to ask the payer
- a recommended next action
- machine-readable JSON for future automation

The model is explicitly instructed not to invent coverage, eligibility, copays, deductibles, waiting periods, frequency limitations, or benefit amounts.

## How it works

```text
Streamlit form
     ↓
Python AI workflow
     ↓
Gemini API
     ↓
Structured JSON
     ↓
Staff-friendly verification-prep plan
```

## Tech stack

- Python
- Streamlit
- Google Gemini API
- python-dotenv
- Git & GitHub
- Streamlit Community Cloud

## Run locally

```bash
git clone https://github.com/Aneeq19/21-day-ai-builder.git
cd 21-day-ai-builder
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, add your own Gemini API key, then run:

```bash
streamlit run app.py
```

Never commit `.env` or API keys.

## Project files

- `app.py` — Streamlit web interface
- `dental_ai.py` — Gemini prompting and structured-output logic
- `sample_data.json` — fictional test record
- `.env.example` — safe environment-variable template
- `.gitignore` — excludes secrets/local files
- `requirements.txt` — Python dependencies

## 21-Day Builder progress

- [x] GitHub + developer setup
- [x] Python + Gemini API
- [x] Structured dental verification workflow
- [x] Streamlit MVP
- [x] Local testing with fictional data
- [x] Public Streamlit deployment
- [x] GitHub Student Developer Pack
- [x] Hackathon registrations
- [ ] Demo video
- [ ] Hackathon submission
- [ ] Portfolio case study

## Hackathon pitch

**DentalVerify AI helps dental-office staff prepare insurance verification more consistently by converting intake information into a structured checklist and payer-question workflow with AI.**

## Roadmap

Potential next steps include saved verification cases, exportable reports, configurable office checklists, audit-friendly workflow history, and integrations designed with appropriate privacy/security controls.

---

Built as part of a practical 21-Day AI Builder sprint: **learn → build → test → deploy → present**.
