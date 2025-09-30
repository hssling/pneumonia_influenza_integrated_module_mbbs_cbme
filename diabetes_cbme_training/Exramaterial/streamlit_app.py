#!/usr/bin/env python3
"""
Medical Statistics Streamlit Application
Interactive Data Science Platform for Medical Statistics Education

Usage:
    streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0

Features:
- Interactive sample size calculations
- Data visualization dashboard
- Clinical decision support
- Statistical analysis tools
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
import statistics
import math

# Page configuration
st.set_page_config(
    page_title="Medical Statistics Interactive App",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for medical theme
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 2rem;
    }
    .card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .metric-card {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

def diabetes_training():
    """Diabetes training interactive module"""
    st.header("🩺 Diabetes Mellitus Interactive Training")

    st.markdown("""
    **Competency-Based Medical Education (CBME) Module**

    This interactive platform helps MBBS students master diabetes management through:
    - **Interactive Quizzes**: Test your knowledge with clinical scenarios
    - **Case Studies**: Practice clinical decision-making
    - **Educational Resources**: Comprehensive training materials
    """)

    # Training mode selection
    training_mode = st.selectbox(
        "Choose Training Mode:",
        ["🏠 Module Overview", "📝 Interactive Quiz", "📊 Case Study", "📚 Resources"]
    )

    if training_mode == "🏠 Module Overview":
        show_diabetes_overview()
    elif training_mode == "📝 Interactive Quiz":
        diabetes_quiz()
    elif training_mode == "📊 Case Study":
        diabetes_case_study()
    elif training_mode == "📚 Resources":
        diabetes_resources()

def show_diabetes_overview():
    """Show diabetes module overview"""
    st.subheader("📋 Module Objectives")

    objectives = [
        "Diagnose diabetes mellitus using clinical and laboratory criteria",
        "Manage Type 1 and Type 2 diabetes with appropriate treatment regimens",
        "Prevent and manage acute complications (hypoglycemia, DKA, HHS)",
        "Monitor and manage long-term complications",
        "Provide patient education on lifestyle modifications and self-management",
        "Implement community screening and preventive programs"
    ]

    for i, obj in enumerate(objectives, 1):
        st.write(f"**{i}.** {obj}")

    st.markdown("---")

    # Learning materials
    st.subheader("📖 Available Materials")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Clinical Content:**")
        st.write("- Pathophysiology & diagnosis")
        st.write("- Treatment protocols")
        st.write("- Complications management")
        st.write("- Emergency management")

    with col2:
        st.markdown("**Educational Tools:**")
        st.write("- 200+ MCQ questions")
        st.write("- Case studies")
        st.write("- Patient education materials")
        st.write("- Screening protocols")

def diabetes_quiz():
    """Interactive diabetes quiz"""
    st.subheader("📝 Diabetes Knowledge Assessment")

    # Load quiz questions (simplified for demo)
    questions = [
        {
            "question": "What is the gold standard diagnostic test for diabetes mellitus?",
            "options": ["Fasting plasma glucose", "Postprandial blood glucose", "Oral glucose tolerance test", "Random blood glucose"],
            "correct": 2,
            "explanation": "OGTT is considered the gold standard as it assesses glucose metabolism under standardized conditions."
        },
        {
            "question": "According to ADA 2023 guidelines, diabetes is confirmed when HbA1c is:",
            "options": ["≥ 6.0%", "≥ 6.5%", "≥ 7.0%", "≥ 7.5%"],
            "correct": 1,
            "explanation": "ADA defines diabetes as HbA1c ≥ 6.5% on two occasions."
        },
        {
            "question": "Which is the most common chronic complication of diabetes?",
            "options": ["Diabetic retinopathy", "Diabetic nephropathy", "Diabetic neuropathy", "Coronary artery disease"],
            "correct": 2,
            "explanation": "Diabetic peripheral neuropathy affects 60-70% of patients and is the most common complication."
        }
    ]

    # Quiz state management
    if 'quiz_state' not in st.session_state:
        st.session_state.quiz_state = {
            'current_question': 0,
            'answers': [],
            'score': 0,
            'completed': False
        }

    quiz_state = st.session_state.quiz_state

    if not quiz_state['completed']:
        # Show current question
        if quiz_state['current_question'] < len(questions):
            q = questions[quiz_state['current_question']]

            st.markdown(f"**Question {quiz_state['current_question'] + 1}:**")
            st.write(q["question"])

            user_answer = st.radio("Select your answer:", q["options"], key=f"q_{quiz_state['current_question']}")

            if st.button("Submit Answer"):
                correct_idx = q["correct"]
                is_correct = user_answer == q["options"][correct_idx]

                quiz_state['answers'].append({
                    'question': q["question"],
                    'user_answer': user_answer,
                    'correct_answer': q["options"][correct_idx],
                    'is_correct': is_correct,
                    'explanation': q["explanation"]
                })

                if is_correct:
                    quiz_state['score'] += 1
                    st.success("✓ Correct!")
                else:
                    st.error("✗ Incorrect")

                st.info(f"**Explanation:** {q['explanation']}")

                quiz_state['current_question'] += 1
                st.rerun()
        else:
            # Quiz completed
            quiz_state['completed'] = True
            st.rerun()

    # Show results
    if quiz_state['completed']:
        st.success("🎉 Quiz Completed!")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Questions", len(questions))

        with col2:
            st.metric("Correct Answers", quiz_state['score'])

        percentage = (quiz_state['score'] / len(questions)) * 100

        if percentage >= 90:
            st.success("🏆 **Excellent! Expert Level**")
        elif percentage >= 70:
            st.info("👍 **Good Performance! Very Good Level**")
        else:
            st.warning("📚 Keep studying! Needs improvement")

        # Show detailed results
        st.subheader("Detailed Results")
        for i, answer in enumerate(quiz_state['answers']):
            status = "✅" if answer['is_correct'] else "❌"
            st.write(f"**Q{i+1}:** {status}")
            if not answer['is_correct']:
                st.write(f"   Your answer: {answer['user_answer']}")
                st.write(f"   Correct answer: {answer['correct_answer']}")

        if st.button("Restart Quiz"):
            st.session_state.quiz_state = {
                'current_question': 0,
                'answers': [],
                'score': 0,
                'completed': False
            }
            st.rerun()

def diabetes_case_study():
    """Interactive diabetes case study"""
    st.subheader("📊 Diabetes Case Study")

    st.write("**Case Scenario:** A 55-year-old male presents with frequent urination, excessive thirst, and unexplained weight loss over the past 2 months. He has a family history of diabetes.")

    st.write("**Vital Signs:** BP 140/85 mmHg, BMI 28.5 kg/m²")

    st.write("**Laboratory Results:** Fasting glucose 180 mg/dL, HbA1c 8.2%")

    st.markdown("**Questions:**")

    clinical_decision = st.multiselect(
        "What is the most likely diagnosis?",
        ["Type 1 Diabetes Mellitus", "Type 2 Diabetes Mellitus", "Gestational Diabetes", "Prediabetes"],
        default=[]
    )

    if st.button("Submit Assessment"):
        if "Type 2 Diabetes Mellitus" in clinical_decision:
            st.success("✅ **Correct!** Based on age, BMI, and presentation, this is likely Type 2 DM.")
        else:
            st.error("❌ Consider the patient's age, BMI, and gradual onset of symptoms.")

    st.markdown("**Clinical Management Decision:**")
    management = st.selectbox(
        "Choose initial management approach:",
        ["Immediate insulin therapy", "Oral hypoglycemics + lifestyle modification", "Dietary control only", "Surgery"]
    )

    if management == "Oral hypoglycemics + lifestyle modification":
        st.success("✅ **Excellent choice!** Metformin + lifestyle intervention is first-line for Type 2 DM.")
    elif management == "Immediate insulin therapy":
        st.warning("⚠️ Consider oral agents first unless symptomatic hyperglycemia is present.")
    else:
        st.info("💡 Think about the most evidence-based initial approach for new-onset Type 2 DM.")

def diabetes_resources():
    """Diabetes educational resources"""
    st.subheader("📚 Educational Resources")

    st.write("**Available Training Materials:**")

    resources = [
        "📄 MCQ Bank (200+ questions)",
        "📖 Case Study Collection",
        "🎭 Role-Playing Scenarios",
        "🏥 Screening Protocols",
        "🎓 Patient Education Materials",
        "🧮 Clinical Decision Algorithms"
    ]

    for resource in resources:
        st.write(f"- {resource}")

    st.info("All materials are available in the training folder for offline use.")

def main():
    """Main application function"""
    st.markdown('<h1 class="main-header">📊 Medical Statistics Interactive Platform</h1>',
                unsafe_allow_html=True)

    st.markdown("""
    **Welcome to the Interactive Medical Statistics Platform!**

    This application provides powerful data analysis tools for medical research and education.
    Choose from the sidebar options to explore various statistical methods and visualizations.
    """)

    # Sidebar navigation
    st.sidebar.title("🧮 Tools & Calculators")
    app_mode = st.sidebar.selectbox(
        "Choose a tool:",
        ["🏠 Home", "🩺 Diabetes Training", "📏 Sample Size Calculator", "📊 Data Visualization",
         "🔬 Statistical Tests", "📈 Correlation Analysis", "🏥 Clinical Decision"]
    )

    # Main content area based on selection
    if app_mode == "🏠 Home":
        show_homepage()
    elif app_mode == "🩺 Diabetes Training":
        diabetes_training()
    elif app_mode == "📏 Sample Size Calculator":
        sample_size_calculator()
    elif app_mode == "📊 Data Visualization":
        data_visualization()
    elif app_mode == "🔬 Statistical Tests":
        statistical_tests()
    elif app_mode == "📈 Correlation Analysis":
        correlation_analysis()
    elif app_mode == "🏥 Clinical Decision":
        clinical_decision_support()

def show_homepage():
    """Show homepage with overview and key metrics"""
    st.subheader("🎯 Platform Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📏 Calculators", "6+ Tools")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📊 Visualizations", "Interactive")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("🏥 Clinical Tools", "Decision Support")
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📈 Statistical Tests", "Multiple Methods")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # About section
    st.subheader("📚 About This Application")
    st.markdown("""
    This interactive platform complements the book "Essential Medical Statistics: A Practical Guide
    for Healthcare Professionals" by Dr. Siddalingaiah H S. It provides:

    - **Resource-Limited Calculator**: Minimal dependencies, works offline
    - **Educational Focus**: Designed for medical students and practitioners
    - **Evidence-Based**: Based on established statistical principles
    - **Interactive Learning**: Hands-on exploration of statistical concepts

    **Institution**: Shridevi Institute of Medical Sciences & Research Hospital, Tumkur, Karnataka, India
    **Contact**: +91-8941087719
    """)

def sample_size_calculator():
    """Interactive sample size calculator for medical studies"""
    st.header("📏 Sample Size Calculator")
    st.markdown("Calculate appropriate sample sizes for medical research studies.")

    # Calculator inputs
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Study Parameters")

        test_type = st.selectbox(
            "Test Type:",
            ["Means Difference", "Proportions Difference", "Survival Analysis"]
        )

        power = st.slider("Power (1-β):", 0.70, 0.95, 0.80, 0.05)
        alpha = st.selectbox("Alpha (α):", [0.05, 0.01, 0.10], index=0)
        tails = st.selectbox("Test Type:", ["Two-tailed", "One-tailed"])

        if test_type == "Means Difference":
            effect_size = st.number_input("Expected Mean Difference:", 0.1, 10.0, 2.0)
            sd = st.number_input("Standard Deviation:", 0.1, 20.0, 5.0)
        elif test_type == "Proportions Difference":
            p1 = st.slider("Proportion 1:", 0.0, 1.0, 0.20, 0.01)
            p2 = st.slider("Proportion 2:", 0.0, 1.0, 0.40, 0.01)
        else:  # Survival Analysis
            hr = st.number_input("Hazard Ratio:", 0.1, 5.0, 0.75)
            prob_event = st.slider("Probability of Event:", 0.0, 1.0, 0.30, 0.01)

    with col2:
        st.subheader("Sample Size Results")

        if st.button("Calculate Sample Size"):
            try:
                n = calculate_sample_size(test_type, effect_size if 'effect_size' in locals() else None,
                                        sd if 'sd' in locals() else None, power, alpha, tails,
                                        p1 if 'p1' in locals() else None,
                                        p2 if 'p2' in locals() else None,
                                        hr if 'hr' in locals() else None,
                                        prob_event if 'prob_event' in locals() else None)

                st.success(f"**Required sample size per group:** {n}")

                # Power analysis visualization
                powers = np.linspace(0.1, 0.99, 100)
                effect_sizes = generate_power_curve(test_type, n, alpha, tails)

                if len(effect_sizes) > 0:
                    fig = px.line(x=powers, y=effect_sizes,
                                labels={'x': 'Power', 'y': 'Effect Size'},
                                title=f"Power Analysis for {test_type}")
                    st.plotly_chart(fig)

            except Exception as e:
                st.error(f"Calculation error: {str(e)}")

def calculate_sample_size(test_type, effect_size=None, sd=None, power=0.80,
                         alpha=0.05, tails="Two-tailed", p1=None, p2=None,
                         hr=None, prob_event=None):
    """Calculate sample size using appropriate statistical formulas"""

    # Normal distribution inverse for critical values
    from scipy.stats import norm

    alpha_critical = norm.ppf(1 - alpha/2) if tails == "Two-tailed" else norm.ppf(1 - alpha)
    beta_critical = norm.ppf(power)

    if test_type == "Means Difference":
        variance = sd * sd
        numerator = variance * (alpha_critical + beta_critical) ** 2
        return math.ceil(numerator / (effect_size * effect_size))

    elif test_type == "Proportions Difference":
        p_avg = (p1 + p2) / 2
        numerator = p_avg * (1 - p_avg) * (alpha_critical + beta_critical) ** 2
        delta = abs(p1 - p2)
        return math.ceil(numerator / (delta * delta))

    else:  # Survival Analysis
        # Simplified hazard ratio formula
        delta = abs(math.log(hr)) * math.sqrt(prob_event)
        numerator = (alpha_critical + beta_critical) ** 2
        return math.ceil(numerator / (2 * delta * delta))

def data_visualization():
    """Interactive data visualization for medical datasets"""
    st.header("📊 Interactive Data Visualization")

    # Load sample datasets
    datasets = {
        "Patient Demographics": pd.DataFrame({
            'age': np.random.normal(50, 15, 100),
            'bmi': np.random.normal(27, 5, 100),
            'bp': np.random.normal(135, 20, 100),
            'cholesterol': np.random.normal(240, 40, 100),
            'gender': np.random.choice(['Male', 'Female'], 100)
        }),
        "Clinical Trial Data": pd.DataFrame({
            'treatment': np.random.choice(['Treatment A', 'Treatment B', 'Placebo'], 120),
            'baseline_bp': np.random.normal(140, 20, 120),
            'final_bp': np.random.normal(130, 18, 120),
            'adverse_events': np.random.choice([0, 1], 120, p=[0.85, 0.15])
        })
    }

    selected_dataset = st.selectbox("Choose Dataset:", list(datasets.keys()))

    df = datasets[selected_dataset]

    # Visualization options
    viz_type = st.selectbox("Visualization Type:",
                           ["Scatter Plot", "Histogram", "Box Plot", "Correlation Heatmap"])

    if viz_type == "Scatter Plot":
        col1, col2 = st.columns(2)
        with col1:
            x_var = st.selectbox("X-axis:", df.select_dtypes(include=[np.number]).columns)
        with col2:
            y_var = st.selectbox("Y-axis:", df.select_dtypes(include=[np.number]).columns)

        if x_var and y_var:
            fig = px.scatter(df, x=x_var, y=y_var,
                           title=f"{y_var} vs {x_var}")
            st.plotly_chart(fig)

    elif viz_type == "Histogram":
        var = st.selectbox("Variable:", df.select_dtypes(include=[np.number]).columns)
        bins = st.slider("Number of bins:", 5, 50, 20)

        fig = px.histogram(df, x=var, nbins=bins,
                          title=f"Distribution of {var}")
        st.plotly_chart(fig)

    elif viz_type == "Box Plot":
        var = st.selectbox("Variable:", df.select_dtypes(include=[np.number]).columns)
        group_by = st.selectbox("Group by (optional):",
                              ['None'] + list(df.select_dtypes(include=['object']).columns))

        if group_by == 'None':
            fig = px.box(df, y=var, title=f"Box Plot of {var}")
        else:
            fig = px.box(df, x=group_by, y=var,
                        title=f"Box Plot of {var} by {group_by}")
        st.plotly_chart(fig)

    elif viz_type == "Correlation Heatmap":
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        corr_matrix = df[numeric_cols].corr()

        fig = px.imshow(corr_matrix,
                       text_auto='.2f',
                       aspect="auto",
                       title="Correlation Matrix")
        st.plotly_chart(fig)

def statistical_tests():
    """Perform statistical tests on uploaded data"""
    st.header("🔬 Statistical Tests")

    # File upload
    uploaded_file = st.file_uploader("Upload CSV file:",
                                   type=['csv'],
                                   help="Upload your data for statistical analysis")

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success(f"Data loaded successfully! {len(df)} rows × {len(df.columns)} columns")

            # Choose analysis
            analysis_type = st.selectbox(
                "Choose Statistical Test:",
                ["Descriptive Statistics", "t-Test", "Chi-Square Test",
                 "ANOVA", "Correlation", "Regression"]
            )

            if analysis_type == "Descriptive Statistics":
                st.subheader("Descriptive Statistics")

                numeric_cols = df.select_dtypes(include=[np.number]).columns
                if len(numeric_cols) > 0:
                    stats_df = df[numeric_cols].describe()
                    st.dataframe(stats_df)

                    # Visualization
                    selected_var = st.selectbox("Visualize distribution:",
                                              numeric_cols)

                    fig = px.histogram(df, x=selected_var, marginal="box",
                                     title=f"Distribution of {selected_var}")
                    st.plotly_chart(fig)

            elif analysis_type == "t-Test":
                st.subheader("Independent t-Test")

                numeric_cols = df.select_dtypes(include=[np.number]).columns
                if len(numeric_cols) == 0:
                    st.error("No numeric columns found!")
                else:
                    col1, col2 = st.columns(2)
                    with col1:
                        var1 = st.selectbox("Variable 1:", numeric_cols)
                    with col2:
                        var2 = st.selectbox("Variable 2:", numeric_cols)

                    if st.button("Run t-Test"):
                        t_stat, p_value = stats.ttest_ind(df[var1], df[var2])

                        st.success(".4f"
                                 ".4f")

                        if p_value < 0.05:
                            st.info("**Significant difference** (p < 0.05)")
                        else:
                            st.info("**No significant difference** (p ≥ 0.05)")

        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

def correlation_analysis():
    """Perform correlation analysis"""
    st.header("📈 Correlation Analysis")

    uploaded_file = st.file_uploader("Upload dataset for correlation analysis:",
                                   type=['csv'])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        numeric_cols = df.select_dtypes(include=[np.number]).columns

        if len(numeric_cols) >= 2:
            st.subheader("Correlation Matrix")

            # Calculate correlations
            corr_matrix = df[numeric_cols].corr()

            # Display matrix
            st.dataframe(corr_matrix.style.background_gradient(cmap='RdBu', axis=None))

            # Scatter plot matrix for selected variables
            st.subheader("Scatter Plot Matrix")
            selected_vars = st.multiselect("Select variables to plot:",
                                         numeric_cols,
                                         default=list(numeric_cols)[:4])

            if len(selected_vars) >= 2:
                fig = px.scatter_matrix(df[selected_vars],
                                       title="Scatter Plot Matrix")
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Need at least 2 numeric columns for correlation analysis.")

def clinical_decision_support():
    """Clinical decision support interface"""
    st.header("🏥 Clinical Decision Support")

    st.markdown("""
    **Note**: This is an educational tool. Always consult with qualified healthcare
    professionals for actual clinical decisions.
    """)

    # Basic patient information inputs
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age:", 1, 120, 50)
    with col2:
        gender = st.selectbox("Gender:", ["Female", "Male", "Other"])
    with col3:
        presenting_symptom = st.selectbox("Main Symptom:", [
            "Chest Pain", "Abdominal Pain", "Headache", "Fever",
            "Shortness of Breath", "Nausea/Vomiting", "Fatigue"
        ])

    # Basic vitals
    st.subheader("Vital Signs")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        hr = st.number_input("Heart Rate (bpm):", 40, 200, 80)
    with col2:
        bp_systolic = st.number_input("BP Systolic (mmHg):", 80, 250, 120)
    with col3:
        temp = st.number_input("Temperature (°C):", 35.0, 42.0, 37.0)
    with col4:
        rr = st.number_input("Respiratory Rate:", 6, 60, 16)

    if st.button("Analyze"):
        # Simple clinical decision support logic
        findings = []

        # Check vital signs
        if bp_systolic >= 140:
            findings.append("**Hypertension** - Consider antihypertensive medication")
        if hr > 100:
            findings.append("**Tachycardia** - Assess for causes (anxiety, infection, etc.)")
        if temp > 38:
            findings.append("**Fever** - Consider infection screening")

        # Symptom-based recommendations
        if presenting_symptom == "Chest Pain":
            if bp_systolic >= 140 or hr > 100:
                findings.append("**Chest Pain with Elevated Vitals** - Consider cardiomyopathy or pulmonary embolism")
            else:
                findings.append("**Chest Pain Assessment** - Rule out cardiac origin with ECG and troponin")

        st.subheader("Clinical Assessment")
        if findings:
            for finding in findings:
                st.warning(finding)
        else:
            st.success("**Normal Assessment** - No immediate concerns identified")

        st.info("""
        **Disclaimer**: This tool provides general educational recommendations only.
        Always perform thorough clinical assessment and consider multiple factors.
        """)

if __name__ == "__main__":
    main()
