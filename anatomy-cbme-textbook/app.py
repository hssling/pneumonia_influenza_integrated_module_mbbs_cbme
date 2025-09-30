#!/usr/bin/env python3
"""
CBME Human Anatomy Textbook - Interactive Streamlit Application
A revolutionary competency-based medical education platform
"""

import streamlit as st
import pandas as pd
import json
import os
from pathlib import Path
import time
from datetime import datetime

# Configure Streamlit
st.set_page_config(
    page_title="🩺 CBME Human Anatomy Textbook",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define paths
ROOT_DIR = Path(__file__).parent
DRAFTS_DIR = ROOT_DIR / "drafts"
EXPORT_DIR = ROOT_DIR / "export"
MCQ_DIR = ROOT_DIR / "mcq_bank"

# Load chapter navigation data
CHAPTERS = {
    "1": {"title": "Basic Concepts in Anatomy", "file": "chapter1_basic_concepts_anatomy.md", "icon": "🧬"},
    "2": {"title": "Histology & Cellular Anatomy", "file": "chapter2_histology_cellular_anatomy.md", "icon": "🔬"},
    "3": {"title": "Skeletal System", "file": "chapter3_skeletal_system.md", "icon": "🦴"},
    "4": {"title": "Muscular System", "file": "chapter4_muscular_system.md", "icon": "💪"},
    "5": {"title": "Cardiovascular System", "file": "chapter5_cardiovascular_system.md", "icon": "❤️"},
    "6": {"title": "Respiratory System", "file": "chapter6_respiratory_system.md", "icon": "🫁"},
    "7": {"title": "Nervous System", "file": "chapter7_nervous_system.md", "icon": "🧠"},
    "8": {"title": "Digestive System", "file": "chapter8_digestive_system.md", "icon": "🍽️"},
    "9": {"title": "Urinary System", "file": "chapter9_urinary_system.md", "icon": "🫘"},
    "10": {"title": "Reproductive System", "file": "chapter10_reproductive_system.md", "icon": "👶"},
    "11": {"title": "Endocrine System", "file": "chapter11_endocrine_system.md", "icon": "🦋"},
    "12": {"title": "Integumentary System", "file": "chapter12_integumentary_system.md", "icon": "🛡️"},
    "13": {"title": "Special Senses", "file": "chapter13_special_senses.md", "icon": "👁️"},
    "14": {"title": "Lymphatic System", "file": "chapter14_lymphatic_system.md", "icon": "🔵"},
    "15": {"title": "Radiological Anatomy", "file": "chapter15_radiological_anatomy.md", "icon": "📡"},
    "16": {"title": "Developmental Anatomy", "file": "chapter16_developmental_anatomy.md", "icon": "👶"},
    "17": {"title": "Clinical & Applied Anatomy", "file": "chapter17_clinical_and_applied_anatomy.md", "icon": "🏥"},
    "18": {"title": "Anatomy in Clinical Practice", "file": "chapter18_anatomy_in_clinical_practice.md", "icon": "⚕️"}
}

def load_chapter_content(chapter_id):
    """Load and return chapter content"""
    chapter = CHAPTERS[chapter_id]
    chapter_file = DRAFTS_DIR / chapter["file"]

    try:
        with open(chapter_file, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"# {chapter['icon']} {chapter['title']}\n\n**Content loading...**"

def create_navigation_sidebar():
    """Create the navigation sidebar with chapter selection"""
    st.sidebar.title("🏥 CBME Anatomy Textbook")

    # User info section
    with st.sidebar.container():
        st.markdown("---")
        st.markdown("### 🎓 Student Progress")
        progress = st.sidebar.progress(75)
        st.sidebar.caption("18 of 18 chapters completed")
        st.markdown("---")

    # Chapter navigation
    st.sidebar.markdown("## 📚 Chapters")

    # Foundation chapters
    st.sidebar.markdown("### 🧬 Foundation")
    foundation_chapters = ["1", "2"]

    for chap_id in foundation_chapters:
        chap = CHAPTERS[chap_id]
        if st.sidebar.button(f"{chap['icon']} Ch. {chap_id}: {chap['title']}"):
            st.session_state.selected_chapter = chap_id
            st.rerun()

    # Major systems
    st.sidebar.markdown("### 🫀 Major Systems")
    major_systems = ["3", "4", "5", "6", "7"]

    for chap_id in major_systems:
        chap = CHAPTERS[chap_id]
        if st.sidebar.button(f"{chap['icon']} Ch. {chap_id}: {chap['title']}"):
            st.session_state.selected_chapter = chap_id
            st.rerun()

    # Other systems
    st.sidebar.markdown("### 🔬 Other Systems")
    other_systems = ["8", "9", "10", "11", "12", "13", "14"]

    for chap_id in other_systems:
        chap = CHAPTERS[chap_id]
        if st.sidebar.button(f"{chap['icon']} Ch. {chap_id}: {chap['title']}"):
            st.session_state.selected_chapter = chap_id
            st.rerun()

    # Advanced chapters
    st.sidebar.markdown("### ⚕️ Advanced Topics")
    advanced_chapters = ["15", "16", "17", "18"]

    for chap_id in advanced_chapters:
        chap = CHAPTERS[chap_id]
        if st.sidebar.button(f"{chap['icon']} Ch. {chap_id}: {chap['title']}"):
            st.session_state.selected_chapter = chap_id
            st.rerun()

    # Tools section
    st.sidebar.markdown("---")
    st.sidebar.markdown("## 🛠️ Tools")

    # Assessment tool
    if st.sidebar.button("📝 MCQ Assessment"):
        st.session_state.current_page = "assessment"
        st.rerun()

    # Progress tracking
    if st.sidebar.button("📊 Progress Dashboard"):
        st.session_state.current_page = "progress"
        st.rerun()

    # Search tool
    if st.sidebar.button("🔍 Chapter Search"):
        st.session_state.current_page = "search"
        st.rerun()

    # Help & Resources
    st.sidebar.markdown("---")
    st.sidebar.markdown("## 📋 Help & Resources")

    with st.sidebar.expander("👩‍🏫 Instructor Guide"):
        st.write("Complete teaching strategies and assessment frameworks")

    with st.sidebar.expander("📚 Download Textbook"):
        st.write("Access compiled publications in multiple formats")

    with st.sidebar.expander("💡 Study Tips"):
        st.markdown("""
        - **Active Learning**: Use diagrams to connect structures
        - **Clinical Correlation**: Link anatomy to patient presentations
        - **Regular Assessment**: Take quizzes after each chapter
        - **OSCE Practice**: Focus on practical examinations
        """)

def create_main_content():
    """Create the main content area based on current selection"""

    # Initialize session state
    if 'selected_chapter' not in st.session_state:
        st.session_state.selected_chapter = "1"
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "chapters"

    # Handle different pages
    if st.session_state.current_page == "chapters":
        display_chapter_content()
    elif st.session_state.current_page == "assessment":
        display_assessment_page()
    elif st.session_state.current_page == "progress":
        display_progress_page()
    elif st.session_state.current_page == "search":
        display_search_page()

def display_chapter_content():
    """Display the selected chapter content"""

    chapter_id = st.session_state.selected_chapter
    chapter = CHAPTERS[chapter_id]

    # Chapter header
    col1, col2, col3 = st.columns([1, 4, 1])

    with col1:
        st.markdown(f"# {chapter['icon']}")
        st.caption(f"Chapter {chapter_id}")

    with col2:
        st.title(chapter["title"])

    with col3:
        # Reading progress (simulated)
        progress_val = int(chapter_id) / 18
        st.progress(progress_val)
        st.caption("75% Complete")

    # Content tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📖 Content", "🎯 Key Points", "📝 Quick Quiz", "🗣️ Discussion"])

    with tab1:
        st.markdown("---")
        content = load_chapter_content(chapter_id)

        # Basic content processing for better display
        # Convert headers, code blocks, etc.
        processed_content = content.replace("#", "##")  # Adjust header levels

        st.markdown(processed_content)

    with tab2:
        st.markdown("### 🎯 Key Learning Objectives")

        # Extract or generate key points based on chapter
        key_points = generate_key_points(chapter_id)
        for point in key_points:
            st.markdown(f"✅ {point}")

    with tab3:
        st.markdown("### 📝 Chapter Quiz")
        create_chapter_quiz(chapter_id)

    with tab4:
        st.markdown("### 🗣️ Discussion & Questions")

        # Discussion forum (mockup)
        st.text_area("Share your questions or insights:", height=100)
        if st.button("Post Question"):
            st.success("Question posted! Faculty will respond shortly.")

        # Sample discussions
        st.markdown("**Recent Discussions:**")
        st.info("💡 How does the histological structure of skeletal muscle correlate with its function?")
        st.success("📖 Great question! The highly organized myofibril arrangement provides the contractile strength needed for movement.")

def generate_key_points(chapter_id):
    """Generate key learning points for each chapter"""
    key_points_db = {
        "1": [
            "Understand CBME framework and progressive competency development",
            "Identify anatomical planes, positions, and directional terms",
            "Describe basic tissue types and their functions",
            "Apply anatomical terminology in clinical contexts"
        ],
        "2": [
            "Identify four basic tissue types and their subtypes",
            "Understand cellular organization in histological structures",
            "Describe epithelial tissue classification and functions",
            "Analyze tissue relationships in organ systems"
        ],
        "3": [
            "Classify bone types and understand skeletal structure",
            "Describe bone development and growth processes",
            "Identify major bones and their anatomical features",
            "Understand joint classification and articulation"
        ],
        "5": [
            "Describe heart chambers and valve functions",
            "Trace blood flow through cardiac circuits",
            "Understand coronary circulation and cardiac conduction",
            "Apply cardiac anatomy to clinical assessment"
        ],
        "7": [
            "Distinguish between central and peripheral nervous systems",
            "Describe neuron structure and synaptic transmission",
            "Understand brain regions and their functions",
            "Apply neurological anatomy to clinical practice"
        ]
    }

    if chapter_id in key_points_db:
        return key_points_db[chapter_id]
    else:
        return [
            "Master fundamental anatomical concepts",
            "Understand structure-function relationships",
            "Apply knowledge to clinical scenarios",
            "Develop competency-based learning skills"
        ]

def create_chapter_quiz(chapter_id):
    """Create interactive quiz for the current chapter"""

    # Sample questions (in real app, these would be loaded from MCQ files)
    quiz_questions = {
        "1": [
            {
                "question": "Which CBME phase focuses on demonstrating clinical skills in workplace settings?",
                "options": ["Knowledge Phase (KP)", "Skills Phase (SP)", "Patient Care Phase (PC)", "Attitude Phase (AP)"],
                "correct": 2,
                "explanation": "The Patient Care Phase (PC) involves demonstrating competencies in actual clinical environments under supervision."
            },
            {
                "question": "The anatomical position is characterized by all of the following EXCEPT:",
                "options": ["Standing erect", "Palms facing posteriorly", "Feet slightly apart", "Eyes facing forward"],
                "correct": 1,
                "explanation": "In the anatomical position, palms face anteriorly/forward, not posteriorly."
            }
        ],
        "2": [
            {
                "question": "Which tissue type provides the lowest resistance to passage of substances?",
                "options": ["Stratified squamous epithelium", "Simple squamous epithelium", "Transitional epithelium", "Pseudostratified columnar epithelium"],
                "correct": 1,
                "explanation": "Simple squamous epithelium is thin and allows rapid diffusion of substances."
            }
        ]
    }

    if chapter_id in quiz_questions:
        questions = quiz_questions[chapter_id]
    else:
        st.info("Full MCQ assessment available in the dedicated assessment section.")
        return

    # Quiz logic
    if f'quiz_{chapter_id}' not in st.session_state:
        st.session_state[f'quiz_{chapter_id}'] = {'answers': [None] * len(questions), 'submitted': False}

    quiz_state = st.session_state[f'quiz_{chapter_id}']

    correct_answers = sum(1 for i, q in enumerate(questions)
                         if quiz_state['answers'][i] is not None and quiz_state['answers'][i] == q['correct'])

    st.write(f"**Score: {correct_answers}/{len(questions)} questions correct**")

    for i, question in enumerate(questions):
        st.markdown(f"**{i+1}. {question['question']}**")

        # Radio button selection
        options = [f"{chr(65+j)}) {opt}" for j, opt in enumerate(question['options'])]
        choice = st.radio(f"question_{i}_{chapter_id}",
                         options,
                         key=f"q_{chapter_id}_{i}",
                         label_visibility="collapsed")

        if choice:
            selected_index = ord(choice[0]) - ord('A')
            quiz_state['answers'][i] = selected_index

        # Show explanation after answering
        if quiz_state['answers'][i] is not None:
            if quiz_state['answers'][i] == question['correct']:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Incorrect. {question['explanation']}")

        st.markdown("---")

    # Submit button
    if st.button("📊 Check All Answers", key=f"submit_{chapter_id}"):
        quiz_state['submitted'] = True
        score = sum(1 for i, q in enumerate(questions)
                   if quiz_state['answers'][i] == q['correct'])
        percentage = (score / len(questions)) * 100

        if percentage >= 70:
            st.success(f"🎉 Excellent! You scored {percentage:.1f}% ({score}/{len(questions)})")
        elif percentage >= 50:
            st.warning(f"📚 Good effort! {percentage:.1f}% ({score}/{len(questions)}) - Review before proceeding.")
        else:
            st.error(f"📖 Time for review. {percentage:.1f}% ({score}/{len(questions)}) - Consider revisiting the chapter.")

def display_assessment_page():
    """Display the comprehensive assessment page"""

    st.title("📝 CBME Anatomy Assessment Center")
    st.markdown("Test your anatomical knowledge across all systems")

    # Assessment options
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎯 Competency Assessment")
        st.markdown("""
        **Levels Available:**
        - Level KS1: Basic Knowledge
        - Level KS2: Applied Knowledge
        - Level KS3: Advanced Integration

        **Topics Covered:**
        - Gross Anatomy
        - Histology & Embryology
        - Clinical Correlations
        """)

        if st.button("🚀 Start Full Assessment"):
            st.info("Full assessment module will be available in next update.")

    with col2:
        st.subheader("📊 Progress Tracking")
        st.markdown("""
        **Your Statistics:**
        - Chapters Completed: 18/18
        - Questions Answered: 75+
        - Average Score: 85%
        - Study Streak: 14 days
        """)

        # Progress visualization
        progress_data = {
            "Systems": ["Skeletal", "Muscular", "Cardiovascular", "Respiratory", "Nervous", "Digestive"],
            "Score": [92, 88, 90, 85, 95, 82]
        }

        st.bar_chart(pd.DataFrame(progress_data).set_index("Systems"))

    # Study recommendations
    st.subheader("📚 Personalized Study Recommendations")

    with st.expander("🔍 Your Learning Gaps"):
        st.markdown("""
        **Areas for Improvement:**
        - Embryological development sequences
        - Neurovascular relationships
        - Anatomical variations

        **Recommended Actions:**
        1. Review chapters 15-16 for embryology
        2. Focus on clinical correlation questions
        3. Practice OSCE-style scenarios
        """)

def display_progress_page():
    """Display student progress dashboard"""

    st.title("📊 Learning Progress Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Chapters Read", "18", "+2 today")

    with col2:
        st.metric("Quiz Score", "87%", "+5% improvement")

    with col3:
        st.metric("Study Hours", "42", "+3 this week")

    with col4:
        st.metric("Completion", "95%", "Nearly done!")

    # Progress by system
    st.subheader("🎯 System Mastery")

    systems_data = pd.DataFrame({
        'System': ['Skeletal', 'Muscular', 'Cardiovascular', 'Respiratory', 'Nervous',
                  'Digestive', 'Urinary', 'Endocrine', 'Reproductive'],
        'Progress': [98, 95, 92, 89, 94, 91, 87, 88, 90],
        'QUiz_Score': [95, 92, 88, 85, 96, 89, 83, 87, 91]
    })

    st.dataframe(systems_data.style.background_gradient())

    # Learning timeline
    st.subheader("📈 Learning Journey")

    # Mock learning data
    dates = pd.date_range(start='2024-09-01', periods=30, freq='D')
    study_hours = [2, 1.5, 3, 2.5, 1, 3.5, 2, 2.5, 4, 1.5] * 3
    study_hours = study_hours[:30]

    chart_data = pd.DataFrame({
        'Date': dates,
        'Study Hours': study_hours
    })

    st.line_chart(chart_data.set_index('Date'))

def display_search_page():
    """Display chapter search and navigation tool"""

    st.title("🔍 Chapter Search & Navigation")

    # Search functionality
    search_term = st.text_input("Search across all chapters:", placeholder="Enter anatomical terms, topics, or keywords...")

    if search_term:
        # Mock search results (in real app, would search through content)
        results = [
            {"chapter": "1", "title": "Basic Concepts", "match": f"Found '{search_term}' in anatomical terminology section"},
            {"chapter": "3", "title": "Skeletal System", "match": f"'{search_term}' matches bone classification criteria"},
            {"chapter": "7", "title": "Nervous System", "match": f"Related to neural '{search_term}' pathways"}
        ]

        for result in results:
            with st.expander(f"📖 Chapter {result['chapter']}: {result['title']}"):
                st.write(result["match"])
                if st.button(f"Read Chapter {result['chapter']}", key=f"search_{result['chapter']}"):
                    st.session_state.selected_chapter = result["chapter"]
                    st.session_state.current_page = "chapters"
                    st.rerun()

def main():
    """Main application function"""

    # Initialize session state
    if 'app_started' not in st.session_state:
        st.session_state.app_started = True
        st.session_state.selected_chapter = "1"
        st.session_state.current_page = "chapters"

        # Welcome message
        st.balloons()
        st.success("🎉 Welcome to the CBME Human Anatomy Textbook!")

        # Brief tutorial
        with st.expander("🚀 Quick Start Guide"):
            st.markdown("""
            **How to Use This Textbook:**
            1. **Navigate**: Use the sidebar to jump between chapters
            2. **Learn**: Read content and view key learning objectives
            3. **Assess**: Take quizzes to test your understanding
            4. **Track**: Monitor your progress in the dashboard
            5. **Apply**: Connect anatomy to clinical practice examples

            **Tips:**
            - Complete chapters in order for best learning experience
            - Review key points before taking quizzes
            - Use the search function to find specific topics
            """)

    # Create UI layout
    create_navigation_sidebar()
    create_main_content()

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 10px;'>
        <small>CBME Human Anatomy Textbook v1.0 | Competency-Based Medical Education Initiative</small><br>
        <small>Developed with AI assistance | Creative Commons Attribution 4.0 International License</small>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
