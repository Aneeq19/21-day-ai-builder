"""Streamlit UI for DentalVerify AI."""

import streamlit as st

from dental_ai import analyze_verification

st.set_page_config(
    page_title="DentalVerify AI",
    page_icon="🦷",
    layout="wide",
)

st.title("🦷 DentalVerify AI")
st.caption("AI-powered preparation assistant for structured dental insurance verification")

st.info(
    "Educational portfolio demo using fictional data only. This app prepares a "
    "verification workflow; it does not verify benefits or replace payer confirmation."
)

with st.expander("How it works", expanded=False):
    st.markdown(
        """
        1. Enter **fictional** patient, plan, and procedure details.
        2. Gemini checks what information is missing.
        3. The app creates a verification checklist and payer questions.
        4. Staff still confirm all eligibility and benefits directly with the payer.
        """
    )

with st.form("verification_form"):
    st.subheader("Demo patient & insurance details")
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
        "Generate verification plan",
        type="primary",
        use_container_width=True,
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
            with st.spinner("Preparing checklist..."):
                result = analyze_verification(record)

            st.success("Verification preparation plan generated")
            st.subheader("Summary")
            st.write(result.get("summary", ""))

            left, right = st.columns(2)
            with left:
                st.markdown("### Missing information")
                missing = result.get("missing_information", [])
                if missing:
                    for item in missing:
                        st.write(f"• {item}")
                else:
                    st.write("• No obvious missing fields detected from the demo input.")

                st.markdown("### Verification checklist")
                for item in result.get("verification_checklist", []):
                    st.write(f"• {item}")

            with right:
                st.markdown("### Questions for payer")
                for item in result.get("questions_for_payer", []):
                    st.write(f"• {item}")

                st.markdown("### Next action")
                st.write(result.get("next_action", ""))

            st.warning(
                result.get(
                    "disclaimer",
                    "Confirm all eligibility and benefits directly with the payer.",
                )
            )

            with st.expander("Raw structured AI output"):
                st.json(result)

        except Exception as exc:
            st.error(f"Unable to generate the plan: {exc}")
            st.caption("Check the Gemini API configuration and try again.")

st.divider()
st.caption(
    "Built by Aneeq • Python • Streamlit • Google Gemini API | "
    "Benefits must always be confirmed directly with the payer."
)
