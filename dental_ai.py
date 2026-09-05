"""Core AI logic for the 21-Day AI Builder dental verification demo.

Educational demo only. Use fictional/dummy patient data; do not enter real PHI.
"""

import json
import os
from typing import Any

from dotenv import load_dotenv
from google import genai

load_dotenv()

SYSTEM_INSTRUCTION = """
You are an assistant for a US dental front-desk team preparing an insurance
verification call. You do NOT claim that benefits are verified and you do NOT
make clinical decisions. Your job is to organize the information supplied,
identify missing information, and create a concise verification checklist.
Return ONLY valid JSON with these keys:
summary, missing_information, verification_checklist, questions_for_payer,
next_action, disclaimer.
Each value except summary, next_action and disclaimer must be a JSON array of
short strings. Never invent coverage, eligibility, copays, deductibles,
frequency limitations, waiting periods, or benefit amounts. If information is
unknown, say it must be verified with the payer.
""".strip()


def build_prompt(patient: dict[str, str]) -> str:
    """Turn the form fields into a clear model request."""
    return f"""{SYSTEM_INSTRUCTION}

Prepare a verification plan for this FICTIONAL demo record:
Patient name: {patient.get('patient_name') or 'Not provided'}
Date of birth: {patient.get('dob') or 'Not provided'}
Insurance company: {patient.get('insurance_company') or 'Not provided'}
Member ID: {patient.get('member_id') or 'Not provided'}
Group number: {patient.get('group_number') or 'Not provided'}
Procedure/service: {patient.get('procedure') or 'Not provided'}
Notes: {patient.get('notes') or 'None'}

Remember: this is preparation for verification, not proof of benefits.
"""


def analyze_verification(patient: dict[str, str]) -> dict[str, Any]:
    """Ask Gemini for a structured verification plan."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Copy .env.example to .env and add your key."
        )

    model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model,
        contents=build_prompt(patient),
    )

    text = (response.text or "").strip()
    if text.startswith("```"):
        text = text.removeprefix("```json").removeprefix("```")
        text = text.removesuffix("```").strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise RuntimeError("The model did not return valid JSON. Please try again.") from exc
