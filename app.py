"""Streamlit UI for DentalVerify AI."""

import streamlit as st
from dental_ai import analyze_verification

st.set_page_config(page_title="DentalVerify AI", page_icon="🦷", layout="wide")

st.title("🦷 DentalVerify AI")
st.markdown("#### Turn dental insurance intake into a structured verification-prep plan")
st.caption("Built by Aneeq • 21-Day AI Builder • Hackathon Edition")

m1, m2, m3 = st.columns(3)
m1.metric("Workflow", "Intake → Checklist")
m2.metric("AI Engine", "Gemini")
m3.metric("Output", "Structured JSON")

st.info(
    "🔒 Privacy-first demo: use fictional data only. DentalVerify AI prepares the "
    "verification workflow; eligibility and benefits must always be confirmed with the payer."
)

with st.expander("✨ What DentalVerify AI does", expanded=False):
    st.markdown(
        """
- Detects missing intake information before a verification call
- Builds a structured verification checklist
- Generates targeted questions for the insurance payer
- Recommends the next workflow action
- Returns structured output that can support future automation

**Important:** it does not claim coverage, eligibility, copays, deductibles, frequencies,
or benefit amounts are verified.
        """
    )

with st.form("verification_form"):
    st.subheader("1 · Enter fictional demo information")
    col1, col2 = st.columns(2)
    with col1:
        patient_name = st.text_input("Patient name", value="John Demo")
        dob = st.text_input("Date of birth", value="01/01/1995")
        insurance_company = st.text_input("Insurance company", value="Demo Dental Plan")
        member_id = st.text_input("Member ID", value="DEMO12345")
    with col2:
        group_number = st.text_input("Group number", value="GRP001")
        procedure = st.text_input("Procedure / service", value="Crown")
        notes = st.text_area(
            "Notes",
            value="New patient; office wants a pre-visit verification checklist.",
        )

    submitted = st.form_submit_button(
        "✨ Generate verification plan", type="primary", use_container_width=True
    )

if submitted:
    record = {
        "patient_name": patient_name.strip(),
        "dob": dob.strip(),
        "insurance_company": insurance_company.strip(),
        "member_id": member_id.strip(),
        "group_number": group_number.strip(),
        "procedure": procedure.strip(),
        "notes": notes.strip(),
    }

    if not any(record.values()):
        st.error("Enter at least one fictional detail before generating a plan.")
    else:
        try:
            with st.spinner("Gemini is preparing the verification workflow..."):
                result = analyze_verification(record)

            st.success("✓ Verification preparation plan generated")
            st.subheader("2 · AI-generated verification plan")

            st.markdown("### 📋 Summary")
            st.write(result.get("summary", ""))

            left, right = st.columns(2)
            with left:
                st.markdown("### 🔎 Missing information")
                missing = result.get("missing_information", [])
                if missing:
                    for item in missing:
                        st.write(f"• {item}")
                else:
                    st.write("✓ No obvious missing fields detected from the demo input.")

                st.markdown("### ✅ Verification checklist")
                checklist = result.get("verification_checklist", [])
                for item in checklist:
                    st.write(f"• {item}")

            with right:
                st.markdown("### ☎️ Questions for payer")
                questions = result.get("questions_for_payer", [])
                for item in questions:
                    st.write(f"• {item}")

                st.markdown("### ➜ Recommended next action")
                st.write(result.get("next_action", ""))

            st.warning(
                "⚠️ "
                + result.get(
                    "disclaimer",
                    "Confirm all eligibility and benefits directly with the payer.",
                )
            )

            with st.expander("Developer view · structured JSON"):
                st.json(result)

        except Exception as exc:
            st.error(f"Unable to generate the plan: {exc}")
            st.caption(
                "Check the Gemini API configuration and deployment secrets, then try again."
            )

st.divider()
st.markdown("### 🚀 Built for practical AI workflow automation")
st.caption(
    "Python • Streamlit • Google Gemini API • GitHub | "
    "Educational portfolio demo — never enter real patient information or PHI."
)
