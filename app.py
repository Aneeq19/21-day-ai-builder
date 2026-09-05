"""Streamlit UI for the Dental Verification Prep Assistant."""

import streamlit as st

from dental_ai import analyze_verification

st.set_page_config(page_title="Dental Verification Prep AI", page_icon="🦷", layout="centered")

st.title("🦷 Dental Verification Prep AI")
st.caption("21-Day AI Builder • Fictional demo data only")

st.info(
    "This demo prepares a verification checklist. It does not verify insurance "
    "benefits or replace payer confirmation. Do not enter real patient information."
)

with st.form("verification_form"):
    st.subheader("Demo patient & insurance details")
    patient_name = st.text_input("Patient name", value="John Demo")
    dob = st.text_input("Date of birth", value="01/01/1995")
    insurance_company = st.text_input("Insurance company", value="Demo Dental Plan")
    member_id = st.text_input("Member ID", value="DEMO12345")
    group_number = st.text_input("Group number", value="GRP001")
    procedure = st.text_input("Procedure / service", value="Crown")
    notes = st.text_area("Notes", value="New patient; office wants a pre-visit verification checklist.")
    submitted = st.form_submit_button("Generate verification plan", type="primary")

if submitted:
    record = {
        "patient_name": patient_name,
        "dob": dob,
        "insurance_company": insurance_company,
        "member_id": member_id,
        "group_number": group_number,
        "procedure": procedure,
        "notes": notes,
    }

    try:
        with st.spinner("Preparing checklist..."):
            result = analyze_verification(record)

        st.success("Verification preparation plan generated")
        st.subheader("Summary")
        st.write(result.get("summary", ""))

        left, right = st.columns(2)
        with left:
            st.markdown("### Missing information")
            for item in result.get("missing_information", []):
                st.write(f"• {item}")
            st.markdown("### Verification checklist")
            for item in result.get("verification_checklist", []):
                st.write(f"• {item}")

        with right:
            st.markdown("### Questions for payer")
            for item in result.get("questions_for_payer", []):
                st.write(f"• {item}")
            st.markdown("### Next action")
            st.write(result.get("next_action", ""))

        st.warning(result.get("disclaimer", "Confirm all benefits directly with the payer."))
        with st.expander("Raw structured AI output"):
            st.json(result)

    except Exception as exc:
        st.error(str(exc))
