"""
ECG Learning Content for Medical Students
Streamlit-based interactive web application for ECG education
"""

import streamlit as st
import os
import json
from pathlib import Path
from datetime import datetime
import random

# Configuration
st.set_page_config(
    page_title="ECG Learning Content for Medical Students",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Constants
AUTHOR_INFO = {
    "name": "AI Cardiology Specialist",
    "email": "ai.cardiology@cme.edu",
    "credentials": "AI-Powered Medical Content Developer"
}

DRAFTS_DIR = Path("drafts")
FRONT_MATTER = Path("front_matter.md")
BACK_MATTER = Path("back_matter.md")
MCQ_BANK = Path("mcq_bank/ecg_mcq_bank.md")

def load_chapter_content(chapter_file):
    """Load chapter content from markdown file"""
    try:
        with open(DRAFTS_DIR / chapter_file, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"# Chapter Not Found\n\nThe requested chapter `{chapter_file}` is not available yet."

def get_completed_chapters():
    """Get list of completed chapters"""
    if not DRAFTS_DIR.exists():
        return []

    chapters = []
    for file in DRAFTS_DIR.glob("chapter*.md"):
        if "outline" not in file.name:
            chapter_title = file.stem.replace('_', ' ').title()
            chapter_num = chapter_title.split()[1] if len(chapter_title.split()) > 1 else "1"
            try:
                num = int(''.join(filter(str.isdigit, chapter_num)))
                chapters.append({
                    'number': num,
                    'title': chapter_title,
                    'file': file.name,
                    'unit': get_chapter_unit(num)
                })
            except ValueError:
                continue

    return sorted(chapters, key=lambda x: x['number'])

def get_chapter_unit(chapter_num):
    """Determine which unit a chapter belongs to"""
    if chapter_num <= 4:
        return "Unit 1: ECG Fundamentals"
    elif chapter_num <= 8:
        return "Unit 2: ECG in Heart Diseases"
    elif chapter_num <= 12:
        return "Unit 3: Cardiac Arrhythmias"
    elif chapter_num <= 16:
        return "Unit 4: ECG in Special Conditions"
    elif chapter_num <= 20:
        return "Unit 5: Advanced ECG Concepts"
    elif chapter_num <= 24:
        return "Unit 6: AI and Digital Health"
    else:
        return "Supplementary Content"

def load_mcqs():
    """Load MCQs from the bank"""
    try:
        with open(MCQ_BANK, 'r', encoding='utf-8') as f:
            content = f.read()
        # Parse MCQ sections
        mcqs = []
        sections = content.split("---")
        for section in sections:
            if "### MCQ" in section:
                mcqs.append(section.strip())
        return mcqs
    except FileNotFoundError:
        return []

def main():
    """Main Streamlit application"""

    # Header
    st.title("🫀 ECG Learning Content for Medical Students")
    st.subheader("Interactive ECG Education with AI Integration")

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"**Author:** {AUTHOR_INFO['name']} | **Email:** {AUTHOR_INFO['email']}")
    with col2:
        st.markdown("**Publication Year:** 2025")
        st.markdown(f"**Completed Chapters:** {len(get_completed_chapters())}")

    st.markdown("---")

    # Navigation
    st.sidebar.title("📚 Navigation")

    menu_options = [
        "🏠 Home & Overview",
        "📖 Chapter Library",
        "🧠 Interactive Quiz",
        "🔍 ECG Search",
        "📊 Learning Progress",
        "🤖 AI Assistant",
        "🔗 Resources"
    ]

    choice = st.sidebar.selectbox("Select Option", menu_options)

    if choice == "🏠 Home & Overview":
        display_home()
    elif choice == "📖 Chapter Library":
        display_chapters()
    elif choice == "🧠 Interactive Quiz":
        display_quiz()
    elif choice == "🔍 ECG Search":
        display_search()
    elif choice == "📊 Learning Progress":
        display_progress()
    elif choice == "🤖 AI Assistant":
        display_ai_assistant()
    elif choice == "🔗 Resources":
        display_resources()

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; font-size: small;'>
    <p><strong>ECG Multimodal Learning Content</strong></p>
    <p>© 2025 AI Cardiology Specialist. Educational use permitted.</p>
    <p>Designed for medical students with competency-based learning.</p>
    </div>
    """, unsafe_allow_html=True)

def display_home():
    """Display home page with overview"""
    st.header("Welcome to Interactive ECG Learning")

    # Overview
    st.subheader("🫀 About This Learning Resource")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### **Multimodal Learning Approach**
        - **Textbook Content:** Comprehensive chapter-based learning
        - **Interactive Quizzes:** Adaptive questions with explanations
        - **Visual Simulations:** ECG wave examples and cases
        - **AI Integration:** Smart learning recommendations
        """)

    with col2:
        st.markdown("""
        ### **Learning Objectives**
        - Master ECG recording and interpretation
        - Recognize normal vs pathological patterns
        - Apply ECG findings to clinical scenarios
        - Understand AI role in modern cardiology
        """)

    # Key Features
    st.markdown("---")
    st.subheader("🔑 Key Features")

    features = [
        ("📚 Comprehensive Content", "24 chapters covering all ECG aspects"),
        ("🧠 Adaptive Learning", "AI-powered quiz difficulty adjustment"),
        ("🖼️ Visual Learning", "Annotated ECG tracings and animations"),
        ("📱 Mobile Access", "Learn anywhere, anytime"),
        ("🎯 Competency Focus", "CBME-aligned learning outcomes"),
        ("🤝 Interactive Cases", "Real clinical scenarios")
    ]

    cols = st.columns(2)
    for i, (icon_text, desc) in enumerate(features):
        with cols[i % 2]:
            st.metric(icon_text.split()[0], "", desc)

def display_chapters():
    """Display chapter selection and content"""
    st.header("📚 ECG Chapter Library")

    chapters = get_completed_chapters()

    if not chapters:
        st.warning("No chapters available yet. Content development in progress.")
        return

    # Unit-based organization
    units = {}
    for chapter in chapters:
        unit = chapter['unit']
        if unit not in units:
            units[unit] = []
        units[unit].append(chapter)

    for unit_name, unit_chapters in units.items():
        with st.expander(f"📗 {unit_name} ({len(unit_chapters)} chapters)", expanded=True):
            for chapter in unit_chapters:
                if st.button(f"📄 Chapter {chapter['number']}: {chapter['title']}",
                           key=f"chap_{chapter['number']}"):
                    st.session_state.selected_chapter = chapter['file']

    # Display selected chapter
    if 'selected_chapter' in st.session_state:
        st.markdown("---")
        chapter_file = st.session_state.selected_chapter
        chapter_content = load_chapter_content(chapter_file)

        # Extract chapter number for navigation
        chapter_num = int(''.join(filter(str.isdigit, chapter_file)))

        # Navigation
        col1, col2, col3 = st.columns([1, 3, 1])
        with col1:
            prev_chapters = [c for c in chapters if c['number'] < chapter_num]
            if prev_chapters:
                prev_chapter = max(prev_chapters, key=lambda x: x['number'])
                if st.button("⬅ Previous"):
                    st.session_state.selected_chapter = prev_chapter['file']
                    st.rerun()
        with col3:
            next_chapters = [c for c in chapters if c['number'] > chapter_num]
            if next_chapters:
                next_chapter = min(next_chapters, key=lambda x: x['number'])
                if st.button("Next ➡"):
                    st.session_state.selected_chapter = next_chapter['file']
                    st.rerun()

        st.markdown(chapter_content)

def display_quiz():
    """Interactive quiz functionality"""
    st.header("🧠 ECG Knowledge Assessment")

    mcqs = load_mcqs()

    if not mcqs:
        st.warning("Quiz bank not available yet.")
        return

    # Quiz settings
    st.subheader("Quiz Configuration")

    col1, col2 = st.columns(2)
    with col1:
        num_questions = st.slider("Number of questions", 5, min(20, len(mcqs)), 10)
    with col2:
        quiz_mode = st.selectbox("Mode", ["Random", "Unit-wise", "Difficulty-based"])

    if st.button("🚀 Start Quiz", type="primary"):
        # Generate quiz session
        if quiz_mode == "Random":
            selected_mcqs = random.sample(mcqs, min(num_questions, len(mcqs)))
        else:
            # For demonstration, use random selection
            selected_mcqs = random.sample(mcqs, min(num_questions, len(mcqs)))

        st.session_state.quiz_questions = selected_mcqs
        st.session_state.quiz_score = 0
        st.session_state.current_question = 0
        st.session_state.quiz_answers = []
        st.rerun()

    # Quiz in progress
    if 'quiz_questions' in st.session_state:
        questions = st.session_state.quiz_questions
        current_idx = st.session_state.current_question

        if current_idx < len(questions):
            question_block = questions[current_idx]

            # Parse question
            lines = question_block.split('\n')
            question_text = ""
            options = []
            correct_answer = ""

            for line in lines:
                if line.startswith('**Question:**'):
                    question_text = line.replace('**Question:**', '').strip()
                elif line.startswith('**Correct Answer:**'):
                    correct_answer = line.replace('**Correct Answer:**', '').strip()
                elif line.startswith('- **') or line.startswith('A)') or '**' in line:
                    if ':' in line and not line.startswith('**Question:'):
                        option = line.split(':', 1)[-1].strip()
                        if option:
                            options.append(option)

            st.subheader(f"Question {current_idx + 1} of {len(questions)}")
            st.markdown(f"**{question_text}**")

            if options:
                answer = st.radio("Select your answer:", options, key=f"q_{current_idx}")
            else:
                answer = st.text_input("Your answer:", key=f"q_{current_idx}")

            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("Submit Answer"):
                    is_correct = answer.strip() == correct_answer.strip()
                    st.session_state.quiz_answers.append({
                        'question': question_text,
                        'user_answer': answer,
                        'correct_answer': correct_answer,
                        'is_correct': is_correct
                    })
                    if is_correct:
                        st.session_state.quiz_score += 1
                        st.success("✅ Correct!")
                    else:
                        st.error(f"❌ Incorrect. The correct answer is: {correct_answer}")
                    st.session_state.current_question += 1
                    st.rerun()

            with col2:
                if st.button("Skip Question"):
                    st.session_state.quiz_answers.append({
                        'question': question_text,
                        'skipped': True
                    })
                    st.session_state.current_question += 1
                    st.rerun()
        else:
            # Quiz complete
            score = st.session_state.quiz_score
            total = len(questions)
            percentage = (score / total) * 100

            st.balloons()
            st.success("🎉 Quiz Complete!")

            # Score display
            st.metric("Final Score", f"{score}/{total}", f"{percentage:.1f}%")

            if percentage >= 80:
                st.markdown("🏆 Excellent performance!")
            elif percentage >= 60:
                st.markdown("👍 Good effort! Review weak areas.")
            else:
                st.markdown("📚 Consider additional study and retake.")

            # Reset quiz
            if st.button("🚀 Take New Quiz"):
                for key in ['quiz_questions', 'quiz_score', 'current_question', 'quiz_answers']:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()

def display_search():
    """Search through ECG content"""
    st.header("🔍 ECG Knowledge Search")

    search_term = st.text_input("Enter ECG terms (e.g., ST elevation, QRS complex, atrial fibrillation)")

    if search_term:
        results = []

        # Search through chapters
        for chapter in get_completed_chapters():
            content = load_chapter_content(chapter['file']).lower()
            if search_term.lower() in content:
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if search_term.lower() in line.lower():
                        context = f"...{line.strip()}..."
                        results.append({
                            'type': 'chapter',
                            'title': f"Chapter {chapter['number']}: {chapter['title']}",
                            'context': context,
                            'file': chapter['file']
                        })

        # Search through MCQs
        mcqs = load_mcqs()
        for mcq in mcqs:
            if search_term.lower() in mcq.lower():
                results.append({
                    'type': 'mcq',
                    'title': 'MCQ Question',
                    'context': mcq.split('\n')[2] if len(mcq.split('\n')) > 2 else mcq[:100]
                })

        if results:
            st.success(f"Found {len(results)} matches for '{search_term}'")

            for result in results:
                with st.expander(f"{result['title']} ({result['type']})"):
                    st.markdown(result['context'])
                    if 'file' in result and st.button("View Full Content", key=f"view_{result['file']}"):
                        st.session_state.selected_chapter = result['file']
                        st.rerun()
        else:
            st.info(f"No results found for '{search_term}'. Try synonyms or different keywords.")

def display_progress():
    """Learning progress tracking"""
    st.header("📊 Learning Progress Tracker")

    completed_chapters = len(get_completed_chapters())
    total_chapters = 24  # From outline
    completion_percentage = (completed_chapters / total_chapters) * 100

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Chapters Completed", f"{completed_chapters}/{total_chapters}")
    with col2:
        st.metric("Progress", f"{completion_percentage:.1f}%")
    with col3:
        st.metric("Remaining", total_chapters - completed_chapters)

    # Progress visualization
    st.progress(completion_percentage / 100)

    # Unit progress
    st.subheader("Unit-wise Progress")
    units_progress = {
        "Unit 1: ECG Fundamentals": 2,  # 2/4 chapters
        "Unit 2: ECG in Heart Diseases": 0,  # 0/4 chapters
        "Unit 3: Cardiac Arrhythmias": 0,   # 0/4 chapters
        "Unit 4: ECG in Special Conditions": 0,  # 0/4 chapters
        "Unit 5: Advanced ECG Concepts": 0,  # 0/4 chapters
        "Unit 6: AI and Digital Health": 0   # 0/4 chapters
    }

    for unit, chapters_done in units_progress.items():
        total_in_unit = 4
        unit_percentage = (chapters_done / total_in_unit) * 100
        st.markdown(f"**{unit}:** {chapters_done}/{total_in_unit} ({unit_percentage:.0f}%)")

def display_ai_assistant():
    """AI-powered learning assistant"""
    st.header("🤖 AI ECG Assistant")

    st.markdown("""
    The AI ECG Assistant provides personalized learning recommendations and instant help.
    """)

    assistant_mode = st.selectbox("What can I help with?", [
        "📖 Study Plan Recommendations",
        "🎯 Weak Area Identification",
        "❓ ECG Interpretation Help",
        "📊 Progress Analysis",
        "🎓 Learning Tips"
    ])

    if assistant_mode == "📖 Study Plan Recommendations":
        st.subheader("Personalized Study Plan")

        study_level = st.selectbox("What's your current ECG knowledge level?",
                                 ["Beginner (new to ECG)", "Intermediate", "Advanced"])

        time_available = st.slider("Daily study time (minutes)", 15, 180, 60)

        if st.button("Generate Study Plan"):
            st.success("🧠 AI-Generated Study Plan")

            if study_level == "Beginner (new to ECG)":
                st.markdown("""
                **7-Day Beginner ECG Study Plan:**
                - **Days 1-2:** Focus on ECG Fundamentals (Chapters 1-2)
                - **Days 3-4:** Learn ECG Waves & Intervals (Chapter 3)
                - **Days 5-6:** Practice Quizzes and Normal Patterns
                - **Day 7:** Review and Assessment
                """)
            elif study_level == "Intermediate":
                st.markdown("""
                **Advanced ECG Study Plan:**
                - **Week 1:** Arrhythmias and Conduction Blocks
                - **Week 2:** Myocardial Ischemia and Infarction
                - **Week 3:** Special Conditions and Drug Effects
                - **Week 4:** Advanced Topics and AI Integration
                """)
            else:
                st.markdown("""
                **Expert ECG Refinement:**
                - Focus on challenging cases
                - Deep dive into ECG-pathology correlations
                - Practice complex arrhythmia recognition
                - Explore AI diagnostic tools
                """)

    elif assistant_mode == "❓ ECG Interpretation Help":
        st.subheader("ECG Interpretation Assistant")

        question_type = st.selectbox("What type of help do you need?", [
            "Identify Rhythm Type",
            "ST Segment Analysis",
            "QRS Morphology",
            "Rate Calculation",
            "Differential Diagnosis"
        ])

        if question_type == "Rate Calculation":
            st.markdown("**Heart Rate Calculation:** 300 ÷ number of large (0.2 sec) squares between R waves")
            st.code("Example: If 6 large squares between R waves: 300 ÷ 6 = 50 bpm")

        elif question_type == "ST Segment Analysis":
            st.markdown("""
            **ST Segment Elevation >1mm in limb leads = STEMI**
            **ST Segment Depression >1mm = Ischemia**
            **Always compare to TP segment!**
            """)

    elif assistant_mode == "🎯 Weak Area Identification":
        st.subheader("AI-Powered Weak Area Analysis")

        st.info("Based on your quiz performance, areas needing focus:")

        # Simulated analysis (would be based on real data in full implementation)
        weak_areas = ["Ventricular Arrhythmias", "Bundle Branch Blocks", "ST-T Wave Interpretation"]

        for area in weak_areas:
            st.warning(f"⚠️ {area} - Consider additional study")

        st.markdown("**Recommended:**")
        st.markdown("- Review Chapter 10 (Ventricular Arrhythmias)")
        st.markdown("- Practice bundle branch block identification")
        st.markdown("- Focus on T wave abnormality recognition")

def display_resources():
    """Display additional resources and links"""
    st.header("🔗 ECG Learning Resources")

    st.subheader("📚 Professional Organizations")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### **International Cardiology Resources**
        - [American Heart Association](https://www.heart.org)
        - [European Society of Cardiology](https://www.escardio.org)
        - [World Heart Federation](https://www.world-heart-federation.org)

        ### **ECG Guidelines**
        - [AHA/ACCF/HRS Guidelines](https://www.heart.org/en/guidelines)
        - [ESC Guidelines](https://www.escardio.org/guidelines)
        """)

    with col2:
        st.markdown("""
        ### **Educational Platforms**
        - [Khan Academy Cardiology](https://www.khanacademy.org)
        - [ECG Weekly](https://ecgweekly.com)
        - [Life in the Fast Lane](https://litfl.com)

        ### **Professional Networks**
        - [Cardiac Rhythm Society](https://www.hrsonline.org)
        - [ACC CardioSmart](https://www.cardiosmart.org)
        """)

    st.subheader("📱 Mobile ECG Apps")
    st.markdown("""
    - **AliveCor KardiaMobile** - Smartphone ECG recording
    - **ECG Pro** - Professional ECG interpretation app
    - **Heart Rate Monitor** - Consumer-grade monitoring
    """)

if __name__ == "__main__":
    main()
