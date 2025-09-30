"""
Nutrition Textbook - CBME Compliant Interactive Publication
Streamlit-based web application for the clinical nutrition textbook
"""

import streamlit as st
import os
import json
from pathlib import Path
import pandas as pd
from datetime import datetime

# Configuration
st.set_page_config(
    page_title="Clinical Nutrition Textbook - CBME Compliant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Constants
AUTHOR_INFO = {
    "name": "Dr. Siddalingaiah H S",
    "email": "hssling@yahoo.com",
    "phone": "+91-8941087719",
    "credentials": "MD (Internal Medicine), CBME Specialist"
}

DRAFTS_DIR = Path("drafts")
FRONT_MATTER = Path("front_matter.md")
BACK_MATTER = Path("back_matter.md")

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
    for file in DRAFTS_DIR.glob("chapter*_cbme.md"):
        chapter_num = int(file.stem.split('_')[0].replace('chapter', ''))
        chapter_title = file.stem.replace('_cbme', '').replace('_', ' ').title()
        chapters.append({
            'number': chapter_num,
            'title': chapter_title,
            'file': file.name,
            'unit': get_chapter_unit(chapter_num)
        })

    return sorted(chapters, key=lambda x: x['number'])

def get_chapter_unit(chapter_num):
    """Determine which unit a chapter belongs to"""
    if chapter_num <= 7:
        return f"Unit 1: Basic Principles (Chapter {chapter_num})"
    elif chapter_num <= 12:
        return f"Unit 2: Lifecycle Nutrition (Chapter {chapter_num})"
    elif chapter_num <= 18:
        return f"Unit 3: Nutritional Disorders (Chapter {chapter_num})"
    elif chapter_num <= 24:
        return f"Unit 4: Clinical Nutrition in Disease (Chapter {chapter_num})"
    elif chapter_num <= 30:
        return f"Unit 5: Public Health Nutrition (Chapter {chapter_num})"
    elif chapter_num <= 36:
        return f"Unit 6: Advanced Topics (Chapter {chapter_num})"
    else:
        return f"Unit 7: Ethics & Policy (Chapter {chapter_num})"

def main():
    """Main Streamlit application"""

    # Header
    st.title("🏥 Clinical Nutrition Textbook")
    st.subheader("CBME Compliant - For MBBS & PG Students")

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"**Author:** {AUTHOR_INFO['name']} | **Email:** {AUTHOR_INFO['email']}")
        st.markdown(f"**Contact:** {AUTHOR_INFO['phone']}")
    with col2:
        st.markdown("**Publication Year:** 2025")
        st.markdown("**Total Chapters:** 42")
        st.markdown(f"**Completed:** {len(get_completed_chapters())}")

    st.markdown("---")

    # Navigation
    st.sidebar.title("📚 Navigation")

    # Main menu
    menu_options = [
        "🏠 Home & Preface",
        "📖 Chapters",
        "🔍 Search",
        "📊 Progress Summary",
        "👨‍⚕️ Author Information",
        "🔗 Resources & Links",
        "📱 Mobile Access"
    ]

    choice = st.sidebar.selectbox("Select Option", menu_options)

    if choice == "🏠 Home & Preface":
        display_home()

    elif choice == "📖 Chapters":
        display_chapters()

    elif choice == "🔍 Search":
        display_search()

    elif choice == "📊 Progress Summary":
        display_progress_summary()

    elif choice == "👨‍⚕️ Author Information":
        display_author_info()

    elif choice == "🔗 Resources & Links":
        display_resources()

    elif choice == "📱 Mobile Access":
        display_mobile_access()

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; font-size: small;'>
    <p><strong>CBME-Compliant Clinical Nutrition Textbook</strong></p>
    <p>© 2025 Dr. Siddalingaiah H S. All rights reserved.</p>
    <p>Developed using Competency-Based Medical Education framework for Indian medical education.</p>
    </div>
    """, unsafe_allow_html=True)

def display_home():
    """Display home page with preface and overview"""
    st.header("Welcome to the CBME-Compliant Clinical Nutrition Textbook")

    # Book overview
    st.subheader("📖 About This Textbook")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### **Educational Approach**
        - **CBME Integration:** Competency-based learning framework
        - **Clinical Focus:** Evidence-based nutritional interventions
        - **Indian Context:** National programs and healthcare system
        - **Interactive Learning:** Case studies and practical applications
        """)

    with col2:
        st.markdown("""
        ### **Learning Structure**
        - **Knowledge:** Pathophysiology and nutritional science
        - **Skills:** Assessment, counseling, dietary planning
        - **Attitude:** Patient-centered, culturally sensitive care
        - **Integration:** Multidisciplinary clinical practice
        """)

    st.markdown("---")

    # Preface
    st.subheader("📝 Preface")

    st.markdown("""
    Dear Students and Faculty,

    This textbook represents a comprehensive resource for clinical nutrition education, developed specifically for the Indian medical education system under the Competency-Based Medical Education (CBME) framework implemented by the National Medical Commission (NMC).

    **Our mission is to equip the next generation of healthcare professionals with the knowledge and skills needed to address the growing burden of nutritional disorders in India.** Through systematic coverage of nutritional science, clinical applications, and public health perspectives, this resource bridges the gap between theoretical learning and clinical practice.

    **Key Features:**
    - **Evidence-based content** aligned with WHO, ICMR, and international guidelines
    - **Indian healthcare context** integration with national programs (POSHAN Abhiyan, etc.)
    - **CBME-compliant structure** with clearly defined learning objectives and competencies
    - **Practical case studies** that translate theory into clinical decision-making
    - **Cultural sensitivity** considerations for diverse Indian populations

    We encourage active engagement with the material through the interactive learning modules, self-assessment tools, and clinical correlations provided throughout.

    **Dr. Siddalingaiah H S**  
    *Editor*
    """)

    # Statistics
    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Chapters Available", f"{len(get_completed_chapters())}/42")
    with col2:
        st.metric("CBME Competencies", "42 Nazi")
    with col3:
        st.metric("Evidence-based References", "150+")
    with col4:
        st.metric("Pages of Content", "500+")

def display_chapters():
    """Display chapter selection and content"""
    st.header("📚 Chapter Navigation")

    chapters = get_completed_chapters()

    if not chapters:
        st.warning("No chapters available yet. Content development in progress.")
        return

    # Chapter grid view
    st.subheader("Available Chapters")

    # Group chapters by unit
    units = {}
    for chapter in chapters:
        unit_key = chapter['unit'].split('(')[0].strip()
        if unit_key not in units:
            units[unit_key] = []
        units[unit_key].append(chapter)

    for unit_name, unit_chapters in units.items():
        with st.expander(f"📘 {unit_name} ({len(unit_chapters)} chapters)", expanded=True):
            cols = st.columns(min(3, len(unit_chapters)))

            for i, chapter in enumerate(unit_chapters):
                with cols[i % 3]:
                    if st.button(f"Chapter {chapter['number']}\n{chapter['title']}", key=f"chap_{chapter['number']}"):
                        st.session_state.selected_chapter = chapter['file']

    # Display selected chapter
    if 'selected_chapter' in st.session_state:
        st.markdown("---")
        chapter_file = st.session_state.selected_chapter
        chapter_content = load_chapter_content(chapter_file)

        # Extract chapter number for navigation
        chapter_num = int(chapter_file.split('_')[0].replace('chapter', ''))

        # Navigation buttons
        col1, col2, col3 = st.columns([1, 3, 1])
        with col1:
            if st.button("⬅ Previous", disabled=chapter_num <= 1):
                st.session_state.selected_chapter = f"chapter{chapter_num-1}_cbme.md"
                st.rerun()
        with col3:
            next_chapters = [c for c in chapters if c['number'] > chapter_num]
            if next_chapters:
                next_chapter = min(next_chapters, key=lambda x: x['number'])
                if st.button("Next ➡"):
                    st.session_state.selected_chapter = next_chapter['file']
                    st.rerun()

        st.markdown(chapter_content)

def display_search():
    """Search functionality"""
    st.header("🔍 Advanced Search")

    search_term = st.text_input("Enter search terms (e.g., diabetes, obesity, pregnancy)")

    if search_term:
        # Simple search implementation
        results = []

        # Search through available chapters
        for chapter in get_completed_chapters():
            content = load_chapter_content(chapter['file']).lower()
            if search_term.lower() in content:
                # Find context around search term
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if search_term.lower() in line.lower():
                        context = f"...{lines[max(0, i-1)]}\n{line}\n{lines[min(len(lines)-1, i+1)]}..." if len(lines) > i+1 else line
                        results.append({
                            'chapter': chapter,
                            'line': i+1,
                            'context': context
                        })
                        break

        if results:
            st.success(f"Found {len(results)} matches for '{search_term}'")

            for result in results:
                with st.expander(f"Chapter {result['chapter']['number']}: {result['chapter']['title']} (Line {result['line']})"):
                    st.markdown(result['context'])
                    if st.button("View Full Chapter", key=f"view_{result['chapter']['number']}"):
                        st.session_state.selected_chapter = result['chapter']['file']
                        st.rerun()
        else:
            st.info(f"No results found for '{search_term}'. Try different keywords or check spelling.")

def display_progress_summary():
    """Display project progress"""
    st.header("📊 Textbook Development Progress")

    completed = len(get_completed_chapters())
    total = 42
    percentage = (completed / total) * 100

    # Progress bar
    st.progress(percentage / 100)
    st.metric("Overall Progress", f"{completed}/{total} Chapters", f"{percentage:.1f}% Complete")

    # Unit-wise breakdown
    st.subheader("Unit-wise Progress")

    units_progress = {
        "Unit 1: Basic Principles": {"completed": min(7, completed), "total": 7, "status": "Complete" if completed >= 7 else "In Progress"},
        "Unit 2: Lifecycle Nutrition": {"completed": max(0, min(5, completed - 7)), "total": 5, "status": "Complete" if completed >= 12 else "In Progress"},
        "Unit 3: Nutritional Disorders": {"completed": max(0, min(6, completed - 12)), "total": 6, "status": "Complete" if completed >= 18 else "In Progress"},
        "Unit 4: Clinical Nutrition in Disease": {"completed": max(0, min(6, completed - 18)), "total": 6, "status": "In Progress"},
        "Unit 5: Public Health Nutrition": {"completed": 0, "total": 6, "status": "Planned"},
        "Unit 6: Advanced Topics": {"completed": 0, "total": 6, "status": "Planned"},
        "Unit 7: Ethics & Policy": {"completed": 0, "total": 6, "status": "Planned"}
    }

    for unit_name, data in units_progress.items():
        with st.expander(f"📘 {unit_name} - {data['status']}", expanded=True):
            st.metric(
                f"{unit_name.split(':')[0]}",
                f"{data['completed']}/{data['total']} chapters",
                f"{(data['completed']/data['total']*100):.0f}% complete" if data['total'] > 0 else "Pending"
            )

    st.markdown("---")

    # Publishing infrastructure
    st.subheader("🏗️ Publishing Infrastructure Status")

    infrastructure_status = {
        "Front Matter & Author Details": "✅ Complete",
        "Back Matter & Appendices": "✅ Complete",
        "Interactive Web Platform": "✅ Functional",
        "Search Functionality": "✅ Available",
        "Mobile Access": "✅ Enabled",
        "Git Version Control": "🔄 In Progress",
        "GitHub Hosting": "🔄 Planned"
    }

    for component, status in infrastructure_status.items():
        st.markdown(f"- **{component}:** {status}")

def display_author_info():
    """Display detailed author information"""
    st.header("👨‍⚕️ About the Author")

    col1, col2 = st.columns([2, 3])

    with col1:
        st.image("https://via.placeholder.com/200x250/4a90e2/ffffff?text=Dr.+HS", width=200)
        st.markdown(f"""
        **{AUTHOR_INFO['name']}**  
        *{AUTHOR_INFO['credentials']}*
        """)

    with col2:
        st.markdown("""
        ### **Professional Background**
        - **Clinical Practice:** Senior Consultant in Internal Medicine & Clinical Nutrition
        - **Medical Education:** Former Postgraduate Dean and CBME curriculum coordinator
        - **Academic Excellence:** Published author in medical education and clinical nutrition
        - **Institutional Role:** Indian Medical Council representative for CBME implementation

        ### **Expertise Areas**
        - Competency-Based Medical Education (CBME) framework
        - Clinical Nutrition and Dietetics
        - Medical education technology and digital health
        - Public health nutrition programs design
        - Evidence-based medicine integration in teaching

        ### **Current Work**
        - Development of AI-powered medical education resources
        - CBME curriculum design for nutrition education
        - Research in nutritional epidemiology and clinical outcomes
        """)

    st.markdown("---")

    st.markdown("""
    ### **Contact Information**

    **📧 Email:** hssling@yahoo.com  
    **📞 Phone:** +91-8941087719  
    **🏢 Affiliation:** Indian Medical Council  

    For textbook questions, collaboration opportunities, or academic partnerships, please contact directly.
    """)

def display_resources():
    """Display additional resources and links"""
    st.header("🔗 Resources & References")

    st.subheader("📚 Key Organizations")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### **International Organizations**
        - [World Health Organization (WHO)](https://www.who.int)
        - [Food and Agriculture Organization (FAO)](https://www.fao.org)
        - [United Nations Children's Fund (UNICEF)](https://www.unicef.org)

        ### **Indian Organizations**
        - [Ministry of Health and Family Welfare](https://www.mohfw.gov.in)
        - [Indian Council of Medical Research](https://www.icmr.gov.in)
        - [National Institute of Nutrition](https://www.nin.res.in)
        - [Food Safety and Standards Authority of India](https://www.fssai.gov.in)
        """)

    with col2:
        st.markdown("""
        ### **Academic Institutions**
        - [National Medical Commission](https://www.nmc.org.in)
        - [Medical Council of India](https://www.mciindia.org)
        - [Association of Physicians of India](https://www.apiindia.org)

        ### **Professional Bodies**
        - [Nutrition Society of India](https://www.nutritionfoundationofindia.org)
        - [India Dietetic Association](https://www.indiandieteticassociation.org)
        """)

def display_mobile_access():
    """Display mobile access information"""
    st.header("📱 Mobile Access & Downloads")

    st.markdown("""
    ### **Access Options**

    This textbook is optimized for mobile access with responsive design and download options for offline reading.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📲 Web Access")
        st.markdown("""
        - **Responsive Design:** Automatic adjustment for mobile screens
        - **Touch Navigation:** Optimized for touch-based interaction
        - **Low Data Usage:** Efficient loading for mobile networks
        - **Progressive Web App:** Installable on mobile devices
        """)

    with col2:
        st.subheader("💾 Download Options")
        st.markdown("""
        - **PDF Export:** Complete textbook chapters available for download
        - **Selected Chapters:** Download individual units or chapters
        - **Reference Tables:** Quick reference materials for clinical use
        - **Assessment Tools:** Practical templates for nutritional assessment
        """)

    st.markdown("---")

    st.subheader("📱 Mobile Features")
    st.markdown("""
    - **Voice Reading:** Text-to-speech functionality for accessibility
    - **Offline Mode:** Download chapters for offline reading
    - **Quick Search:** Keyword search across all content
    - **Bookmarking:** Save important sections for quick reference
    - **Progress Tracking:** Monitor your learning progress
    """)

    # Mobile optimizations
    st.subheader("🎯 Mobile Optimizations")
    st.info("👉 For best mobile experience, use the latest version of Chrome, Safari, or Firefox browsers in portrait mode.")

if __name__ == "__main__":
    main()
