import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Configure page
st.set_page_config(
    page_title="Pneumonia & Immunization CBME Module",
    page_icon="🏥",
    layout="wide",
    menu_items={
        'About': """
        Pneumonia Treatment & Immunization CBME Module
        Developed by Dr. Siddalingaiah H S
        For MBBS Phase 3 Part 1 Medical Students
        """
    }
)

# Custom CSS
st.markdown("""
<style>
.st-emotion-cache-1jicfl2 {padding-top: 1rem;}
.st-emotion-cache-1inwz65 {width: 100% !important;}
.big-font {font-size: 24px !important;}
.medium-font {font-size: 18px !important;}
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.title("🏥 Pneumonia Treatment & Immunization")
        st.subheader("CBME Module for MBBS Phase 3 Part 1")
    with col3:
        st.markdown("**Version:** 1.0")
        st.markdown(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}")

    # Navigation
    menu = st.sidebar.radio("Navigation", [
        "🏠 Dashboard",
        "📖 Curriculum",
        "🧪 Clinical Cases",
        "📊 Practice MCQs",
        "🛡️ Vaccination Hub",
        "📝 Assessment",
        "📋 Resources"
    ])

    # Attribution
    st.sidebar.markdown("---")
    st.sidebar.markdown("**👨‍⚕️ Developed by:**")
    st.sidebar.markdown("Dr. Siddalingaiah H S")
    st.sidebar.markdown("hssling@yahoo.com")
    st.sidebar.markdown("+91-8941087719")

    # Navigation Content
    if menu == "🏠 Dashboard":
        show_dashboard()
    elif menu == "📖 Curriculum":
        show_curriculum()
    elif menu == "🧪 Clinical Cases":
        show_cases()
    elif menu == "📊 Practice MCQs":
        show_mcqs()
    elif menu == "🛡️ Vaccination Hub":
        show_vaccines()
    elif menu == "📝 Assessment":
        show_assessment()
    elif menu == "📋 Resources":
        show_resources()

def show_dashboard():
    st.header("📈 Module Overview")

    # Statistics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Chapters", "15", "+100%")
    with col2:
        st.metric("Clinical Cases", "8", "+125%")
    with col3:
        st.metric("MCQ Questions", "150+", "+200%")
    with col4:
        st.metric("Vaccines Covered", "2", "PN & INF")

    st.markdown("---")

    # Learning Objectives
    st.subheader("🎯 Learning Objectives")
    objectives = [
        "Master evidence-based pneumonia treatment protocols",
        "Understand pneumococcal and influenza vaccination strategies",
        "Develop clinical skills for pneumonia diagnosis",
        "Strengthen immunization implementation skills",
        "Achieve competency in vaccine safety management"
    ]

    for obj in objectives:
        st.checkbox(obj, value=True, disabled=True)

    # Progress Tracking
    st.markdown("---")
    st.subheader("📊 Learning Progress")

    # Mock progress data
    progress_data = pd.DataFrame({
        'Topic': ['Diagnosis', 'Treatment', 'Prevention', 'Vaccination', 'Assessment'],
        'Progress': [85, 70, 60, 45, 30]
    })

    for idx, row in progress_data.iterrows():
        col1, col2 = st.columns([3, 2])
        with col1:
            st.write(f"{row['Topic']}")
        with col2:
            st.progress(row['Progress'] / 100)
            st.write(f"{row['Progress']}%")

def show_curriculum():
    st.header("📚 Curriculum Structure")

    # Curriculum tabs
    tab1, tab2, tab3 = st.tabs(["Unit 1: Core Concepts", "Unit 2: Management", "Unit 3: Prevention"])

    with tab1:
        st.subheader("Core Pneumonia Concepts (Chapters 1-6)")
        chapters = [
            "1. Epidemiology & Pathophysiology",
            "2. Pneumonia Classification",
            "3. Clinical Diagnosis & Assessment",
            "4. Radiological Diagnosis",
            "5. Microbiological Diagnosis",
            "6. Antibiotic Treatment Guidelines"
        ]
        for chapter in chapters:
            if st.button(chapter, key=f"ch{chapter[:1]}"):
                st.info(f"Content for {chapter} would be displayed here.")

    with tab2:
        st.subheader("Management & Treatment (Chapters 7-8)")
        chapters = [
            "7. Severe & Complicated Pneumonia",
            "8. Supportive Care & Adjunct Therapies"
        ]
        for chapter in chapters:
            if st.button(chapter, key=f"ch{chapter[:1]}"):
                st.info(f"Content for {chapter} would be displayed here.")

    with tab3:
        st.subheader("Prevention & Vaccination (Chapters 9-15)")
        chapters = [
            "9. Prevention Strategies",
            "10. Pneumococcal Vaccination",
            "11. Influenza Vaccination",
            "12. Immunization Implementation",
            "13. Coverage & Monitoring",
            "14. Vaccine Safety & AEFIs",
            "15. Program Evaluation"
        ]
        for chapter in chapters:
            if st.button(chapter, key=f"ch{chapter[:2].strip()}"):
                st.info(f"Content for {chapter} would be displayed here.")

def show_cases():
    st.header("🧪 Clinical Case Studies")

    case_list = [
        "Community-Acquired Pneumonia in Adult",
        "Severe Pneumonia in Pediatric Patient",
        "Nosocomial Pneumonia Management",
        "Pneumococcal Vaccine Failure Case",
        "Influenza Season Outbreak Response",
        "Multi-drug Resistant Organism",
        "COPD Exacerbation with Pneumonia",
        "Immunocompromised Patient Case"
    ]

    selected_case = st.selectbox("Select Clinical Case:", case_list)

    if selected_case:
        st.subheader(f"📋 {selected_case}")

        if selected_case == "Community-Acquired Pneumonia in Adult":
            st.markdown("""
            **Patient Profile:**
            - 45-year-old male
            - Fever, cough, chest pain, dyspnea
            - Smoker, occasional alcohol use

            **Clinical Findings:**
            - Temperature: 101.5°F, HR: 95 bpm, RR: 22/min
            - Chest auscultation: Rales in right lower zone
            - CXR: Consolidation right lower lobe
            """)

            # Management options
            st.markdown("**Management Options:**")
            tx_options = [
                "Amoxicillin 500mg TID for 7 days",
                "Azithromycin 500mg Day 1, then 250mg for 4 days",
                "Ceftriaxone IV + Azithromycin IV",
                "Home management with NSAIDs"
            ]

            choice = st.radio("Choose treatment:", tx_options)
            if st.button("Submit Answer"):
                if "Azithromycin" in choice or choice.startswith("Amoxicillin"):
                    st.success("✅ Correct! Appropriate antibiotic choice")
                else:
                    st.error("❌ Consider respiratory fluoroquinolone or azithromycin/azithromycin regimen")

def show_mcqs():
    st.header("📊 Practice MCQs")

    # Sample MCQs
    mcq_data = [
        {
            "question": "What is the most common bacterial cause of community-acquired pneumonia?",
            "options": ["Streptococcus pneumoniae", "Haemophilus influenzae", "Moraxella catarrhalis", "Chlamydia pneumoniae"],
            "correct": 0,
            "explanation": "Streptococcus pneumoniae accounts for 30-50% of CAP cases in adults"
        },
        {
            "question": "Which antibiotic is first-line for outpatient CAP treatment?",
            "options": ["Ciprofloxacin", "Amoxicillin", "Vancomycin", "Linezolid"],
            "correct": 1,
            "explanation": "Amoxicillin is the first-line choice for outpatient CAP treatment"
        },
        {
            "question": "When should pneumococcal vaccination be given to adults?",
            "options": ["Birth", "2 months", "≥65 years or high-risk conditions", "Monthly"],
            "correct": 2,
            "explanation": "PPSV23 is recommended for adults ≥65 or those with certain medical conditions"
        }
    ]

    for i, mcq in enumerate(mcq_data):
        st.subheader(f"Question {i+1}:")
        st.write(mcq["question"])

        answer = st.radio(f"Select answer for Q{i+1}:", mcq["options"], key=f"q{i}")

        if st.button(f"Check Answer {i+1}", key=f"check{i}"):
            if mcq["options"].index(answer) == mcq["correct"]:
                st.success("✅ Correct!")
            else:
                st.error("❌ Incorrect")
            st.info(f"**Explanation:** {mcq['explanation']}")

def show_vaccines():
    st.header("🛡️ Vaccination Hub")

    vaccine_tabs = st.tabs(["Pneumococcal", "Influenza", "Guidelines"])

    with vaccine_tabs[0]:
        st.subheader("💉 Pneumococcal Vaccination")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            **Vaccine Types:**
            - PCV13 (Conjugate vaccine)
            - PPSV23 (Polysaccharide vaccine)

            **Target Groups:**
            - Children <2 years
            - Adults ≥65 years
            - Immunocompromised patients
            """)

        with col2:
            st.markdown("""
            **Schedule:**
            - PCV: 2, 4, 6 months
            - PPSV23: Single dose ≥65
            - Sequential: PCV13 then PPSV23

            **Coverage Goal:** 90%+
            """)

        if st.button("View Pneumococcal Guidelines", key="pcv-guidelines"):
            st.info("Detailed pneumococcal immunization guidelines would open here.")

    with vaccine_tabs[1]:
        st.subheader("🦠 Influenza Vaccination")

        st.markdown("""
        **Influenza Vaccine Types:**
        - Trivalent (3 strains)
        - Quadrivalent (4 strains)

        **Annual Vaccination:**
        - October-November (Northern Hemisphere)
        - April-May (Southern Hemisphere)

        **Target Groups:**
        - All age groups ≥6 months
        - Priority: Elderly, healthcare workers, pregnant women
        """)

        if st.button("View Influenza Guidelines", key="flu-guidelines"):
            st.info("Detailed influenza immunization guidelines would open here.")

    with vaccine_tabs[2]:
        st.subheader("📋 National Immunization Guidelines")
        st.info("Ministry of Health vaccination guidelines and WHO recommendations for pneumonia prevention.")

        if st.button("Download IPL and Coverage Guidelines"):
            st.warning("📁 Guidelines document would be downloaded.")

def show_assessment():
    st.header("📝 Competency Assessment")

    st.markdown("### 🏆 CBME Competencies Assessment")

    competencies = [
        "Clinical Diagnosis of Pneumonia",
        "Antibiotic Stewardship",
        "Vaccination Counseling",
        "Adverse Event Management",
        "Program Monitoring & Evaluation"
    ]

    assessment_data = {}
    for competency in competencies:
        assessment_data[competency] = st.selectbox(
            f"Rate your competency in: {competency}",
            ["Needs Improvement", "Developing", "Proficient", "Mastery"],
            key=f"assess_{competency.replace(' ', '_').lower()}"
        )

    if st.button("Submit Self-Assessment"):
        st.success("✅ Assessment Submitted Successfully!")

        # Display assessment results
        proficient_or_mastery = sum(1 for rating in assessment_data.values()
                                   if rating in ["Proficient", "Mastery"])

        st.metric(f"Core Competencies Achieved", f"{proficient_or_mastery}/{len(competencies)}")

        if proficient_or_mastery >= 4:
            st.balloons()
            st.success("🎉 Excellent! You have achieved competency in Pneumonia Management!")

def show_resources():
    st.header("📋 Resources & References")

    st.subheader("📚 Key References")

    references = [
        "WHO Pneumonia Treatment Guidelines 2023",
        "Indian Academy of Pediatrics Guidelines",
        "Ministry of Health Universal Immunization Program",
        "ATS/IDSA Community-Acquired Pneumonia Guidelines",
        "National Technical Advisory Group on Immunization (NTAGI)"
    ]

    for ref in references:
        st.markdown(f"- 📖 {ref}")

    st.markdown("---")

    st.subheader("🔗 Useful Links")

    links = [
        ("CDC Pneumonia Guidelines", "https://www.cdc.gov/pneumonia/"),
        ("WHO Immunization", "https://www.who.int/immunization"),
        ("MoHFW Immunization", "https://mohfw.gov.in/universal-immunization-programme")
    ]

    for title, url in links:
        st.markdown(f"- 🔗 [{title}]({url})")

    st.markdown("---")

    st.subheader("🛠️ Tools & Calculators")

    if st.button("CURB-65 Calculator"):
        st.info("OPEN → PORT Score: 0-1 points = Home care, 2 points = Hospital care, ≥3 points = ICU admission")

    if st.button("Vaccination Schedule Planner"):
        st.info("Interactive vaccination schedule planner tool")

if __name__ == "__main__":
    main()
