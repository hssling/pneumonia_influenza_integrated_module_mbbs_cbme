# Chapter 17: Medical Statistics in Practice

## 17.1 Introduction to Applied Medical Statistics

**Medical statistics in practice** involves applying statistical methods to real-world healthcare problems, from clinical decision making to health policy development.

### Key Applications:
- **Clinical decision making**: Using data to guide patient care
- **Quality improvement**: Monitoring and improving healthcare delivery
- **Health policy**: Evidence-based policy development
- **Resource allocation**: Efficient use of healthcare resources
- **Research evaluation**: Assessing research proposals and results

### Challenges in Practice:
- **Data quality**: Real-world data often messy and incomplete
- **Confounding**: Multiple factors influence outcomes
- **Generalizability**: Research results may not apply to all patients
- **Uncertainty**: All statistical conclusions have some uncertainty
- **Ethical considerations**: Balancing individual vs population benefits

**Example 17.1**: Hospital quality improvement
- Monitor surgical complication rates
- Compare against national benchmarks
- Identify areas for improvement
- Implement changes and evaluate impact

## 17.2 Clinical Decision Making

### 17.2.1 Risk Prediction Models

**Models to predict patient outcomes**

**Example 17.2**: Cardiovascular risk assessment
- Framingham Risk Score: Predicts 10-year CVD risk
- Inputs: Age, gender, cholesterol, blood pressure, smoking, diabetes
- Output: Risk category (low, intermediate, high)
- Use: Guide treatment intensity

**Implementation considerations:**
- Model validation in local population
- Regular updates as new data available
- User-friendly interfaces for clinicians

### 17.2.2 Diagnostic Reasoning

**Using likelihood ratios in practice**

**Example 17.3**: Chest pain evaluation
- Pre-test probability: 20% (based on age, risk factors)
- ECG positive: LR+ = 8
- Post-test probability = 20% × 8 / (1 - 20% + 20% × 8) = 160% / 180% = 89%

**Clinical action:**
- High probability warrants urgent intervention
- Consider patient preferences and local resources

### 17.2.3 Treatment Selection

**Evidence-based treatment choices**

**Factors to consider:**
- Treatment efficacy (from RCTs)
- Patient characteristics (subgroup effects)
- Patient preferences (shared decision making)
- Cost-effectiveness
- Local availability

## 17.3 Quality Improvement and Monitoring

### 17.3.1 Statistical Process Control

**Monitor healthcare processes over time**

**Control charts:**
- **Mean chart**: Monitor process average
- **Range chart**: Monitor process variability
- **p-chart**: Monitor proportion (e.g., infection rates)
- **c-chart**: Monitor count (e.g., number of errors)

**Example 17.4**: Hospital infection rates
- Monthly surgical site infection rate
- Upper control limit: 3 SD above mean
- Lower control limit: 3 SD below mean
- Special cause variation: Points outside control limits

### 17.3.2 Benchmarking

**Compare performance against standards**

**Types of benchmarks:**
- **Internal**: Compare against own historical performance
- **External**: Compare against other institutions
- **Evidence-based**: Compare against clinical guidelines

**Example 17.5**: Hospital mortality rates
- Observed mortality: 3.2%
- Expected mortality (risk-adjusted): 2.8%
- Standardized mortality ratio: 3.2/2.8 = 1.14
- Interpretation: Slightly higher than expected

### 17.3.3 Quality Indicators

**Key performance indicators:**
- **Structure**: Resources and organization
- **Process**: How care is delivered
- **Outcome**: Results of care

**Example 17.6**: Diabetes care quality
- Process indicators: HbA1c testing, eye exams, foot exams
- Outcome indicators: HbA1c control, complication rates
- Use: Identify gaps in care delivery

## 17.4 Health Economics and Outcomes Research

### 17.4.1 Cost-Effectiveness Analysis

**Compare costs and benefits of interventions**

**Key measures:**
- **Cost-effectiveness ratio**: Cost per QALY gained
- **Incremental cost-effectiveness ratio**: Additional cost per additional benefit
- **Willingness to pay**: Threshold for cost-effectiveness

**Example 17.7**: New diabetes medication
- Additional cost: $500 per year
- Additional benefit: 0.1 QALY
- ICER: $500 / 0.1 = $5,000 per QALY
- Threshold: $50,000 per QALY (cost-effective)

### 17.4.2 Budget Impact Analysis

**Assess financial impact on healthcare budget**

**Example 17.8**: New treatment adoption
- Target population: 1,000 patients
- Treatment cost: $2,000 per patient per year
- Current treatment cost: $1,000 per patient per year
- Budget impact: $1,000 × 1,000 = $1,000,000 increase

## 17.5 Epidemiology in Practice

### 17.5.1 Disease Surveillance

**Monitor disease patterns and trends**

**Systems:**
- **Passive surveillance**: Healthcare providers report cases
- **Active surveillance**: Systematic case finding
- **Sentinel surveillance**: Monitor specific sites

**Example 17.9**: COVID-19 surveillance
- Daily case counts and test positivity rates
- Hospitalization and death rates
- Variant surveillance
- Use: Guide public health response

### 17.5.2 Outbreak Investigation

**Steps in outbreak investigation:**
1. **Confirm outbreak**: More cases than expected
2. **Verify diagnosis**: Confirm case definitions
3. **Case finding**: Identify all cases
4. **Descriptive epidemiology**: Time, place, person analysis
5. **Generate hypotheses**: Possible sources
6. **Test hypotheses**: Analytical studies
7. **Implement control measures**: Stop outbreak
8. **Evaluate control**: Assess effectiveness

**Example 17.10**: Foodborne outbreak
- 50 cases of gastroenteritis
- Common food exposure: Chicken salad
- Case-control study: OR = 15.2 (95% CI: 4.1-56.3)
- Source identified and removed

## 17.6 Research Ethics and Statistics

### 17.6.1 Ethical Statistical Practice

**Principles:**
- **Honesty**: Report results accurately
- **Transparency**: Share methods and data
- **Objectivity**: Avoid bias in analysis and interpretation
- **Competence**: Use appropriate methods
- **Confidentiality**: Protect patient privacy

**Example 17.11**: Data sharing
- Share analysis code and datasets when possible
- Protect patient confidentiality
- Enable reproducible research
- Facilitate meta-analysis

### 17.6.2 Institutional Review Boards

**IRB responsibilities:**
- Review research protocols
- Assess risk-benefit ratio
- Ensure informed consent
- Monitor ongoing studies
- Protect vulnerable populations

## 17.7 Data Management in Healthcare

### 17.7.1 Electronic Health Records

**Statistical considerations:**
- **Data quality**: Accuracy, completeness, timeliness
- **Standardization**: Common data formats and coding
- **Privacy**: HIPAA compliance and de-identification
- **Integration**: Combine data from multiple sources

**Example 17.12**: EHR data analysis
- Extract patient cohorts
- Calculate quality metrics
- Identify gaps in care
- Support clinical decision making

### 17.7.2 Big Data in Medicine

**Large-scale healthcare data analysis**

**Sources:**
- Electronic health records
- Claims data
- Registries
- Wearable devices
- Social media

**Challenges:**
- Data volume and velocity
- Data variety and veracity
- Privacy and security
- Statistical methods for big data

## 17.8 Policy and Guidelines Development

### 17.8.1 Evidence-Based Guidelines

**Process:**
1. **Formulate questions**: Key clinical questions
2. **Systematic review**: Comprehensive literature search
3. **Grade evidence**: Assess quality and strength
4. **Make recommendations**: Balance benefits and harms
5. **External review**: Peer review and stakeholder input
6. **Update regularly**: Incorporate new evidence

**Example 17.13**: Hypertension guidelines
- Systematic review of trials
- GRADE evidence assessment
- Treatment recommendations by risk group
- Regular updates as new evidence emerges

### 17.8.2 Health Technology Assessment

**Evaluate new technologies for adoption**

**Components:**
- **Clinical effectiveness**: Does it work?
- **Cost-effectiveness**: Is it worth the cost?
- **Budget impact**: Financial implications
- **Organizational impact**: Implementation requirements
- **Ethical and social implications**: Broader effects

## 17.9 Statistical Challenges in Practice

### 17.9.1 Missing Data

**Common in medical research**

**Methods:**
- **Complete case analysis**: Use only complete records
- **Imputation**: Fill in missing values
- **Multiple imputation**: Account for imputation uncertainty
- **Sensitivity analysis**: Assess impact of missing data

**Example 17.14**: Clinical trial with dropouts
- 20% dropout rate
- Multiple imputation preserves sample size
- Sensitivity analysis shows results robust to missing data assumptions

### 17.9.2 Confounding in Observational Data

**Control for confounding factors**

**Methods:**
- **Restriction**: Limit analysis to specific subgroups
- **Matching**: Match exposed to unexposed on confounders
- **Stratification**: Analyze within strata of confounders
- **Regression adjustment**: Include confounders as covariates
- **Propensity scores**: Balance confounding factors

### 17.9.3 Multiple Comparisons

**Control false positive rate**

**Methods:**
- **Pre-specification**: Define primary outcome in advance
- **Bonferroni correction**: Divide alpha by number of tests
- **False Discovery Rate**: Control proportion of false positives
- **Hierarchical testing**: Test in logical order

## 17.10 Future Directions

### 17.10.1 Precision Medicine

**Individualized treatment based on patient characteristics**

**Statistical approaches:**
- **Biomarker identification**: Find predictive markers
- **Subgroup analysis**: Identify treatment-responsive groups
- **Machine learning**: Pattern recognition in complex data
- **Bayesian methods**: Incorporate prior knowledge

**Example 17.15**: Cancer treatment
- Genetic profiling identifies tumor mutations
- Statistical models predict treatment response
- Personalized treatment recommendations

### 17.10.2 Real-World Evidence

**Use of real-world data for evidence generation**

**Sources:**
- Electronic health records
- Claims databases
- Patient registries
- Mobile health apps

**Advantages:**
- Large sample sizes
- Diverse populations
- Long-term outcomes
- Lower cost

**Challenges:**
- Data quality and completeness
- Confounding and bias
- Missing randomization
- Statistical methods for causal inference

### 17.10.3 Artificial Intelligence in Healthcare

**Machine learning applications**

**Areas:**
- **Medical imaging**: Automated interpretation
- **Risk prediction**: Complex pattern recognition
- **Treatment optimization**: Personalized recommendations
- **Drug discovery**: Identify new compounds

**Statistical considerations:**
- **Validation**: Ensure models work in new data
- **Interpretability**: Understand model decisions
- **Bias**: Avoid perpetuating healthcare disparities
- **Regulation**: Ensure safety and efficacy

## 17.11 Case Studies

### 17.11.1 Case Study 1: Hospital Quality Improvement

**Scenario**: Hospital wants to reduce surgical complications

**Statistical approach:**
1. **Baseline assessment**: Calculate current complication rate
2. **Risk adjustment**: Account for patient severity
3. **Control charts**: Monitor rates over time
4. **Intervention evaluation**: Compare pre and post intervention
5. **Sustainability**: Long-term monitoring

**Results:**
- Baseline rate: 5.2%
- Post-intervention: 3.1% (p=0.02)
- Sustained improvement over 2 years

### 17.11.2 Case Study 2: Clinical Guideline Development

**Scenario**: Develop guidelines for diabetes management

**Process:**
1. **Systematic review**: 50 relevant studies
2. **Meta-analysis**: Combine evidence
3. **GRADE assessment**: Evaluate evidence quality
4. **Recommendation formulation**: Balance benefits and harms
5. **Implementation**: Disseminate and evaluate uptake

**Outcome:**
- Strong recommendation for metformin as first-line therapy
- Conditional recommendation for newer agents
- Regular updates planned

### 17.11.3 Case Study 3: Outbreak Investigation

**Scenario**: Cluster of foodborne illness

**Investigation:**
1. **Case identification**: 25 cases identified
2. **Hypothesis generation**: Common restaurant exposure
3. **Case-control study**: OR = 12.5 (95% CI: 3.8-41.2)
4. **Source identification**: Contaminated chicken
5. **Control measures**: Restaurant closure and food recall

**Impact:**
- Outbreak contained
- Prevention measures implemented
- Public health system strengthened

## 17.12 Professional Development

### 17.12.1 Continuous Learning

**Resources:**
- **Journals**: New England Journal of Medicine, JAMA, BMJ
- **Textbooks**: Updated editions of statistics texts
- **Online courses**: Coursera, edX, DataCamp
- **Conferences**: Professional society meetings
- **Webinars**: Regular educational sessions

### 17.12.2 Collaboration

**Interdisciplinary teams:**
- **Clinicians**: Domain expertise
- **Statisticians**: Methodological expertise
- **Epidemiologists**: Study design expertise
- **Data scientists**: Computational expertise
- **Policy makers**: Implementation expertise

### 17.12.3 Ethical Considerations

**Professional responsibilities:**
- Maintain competence in statistical methods
- Ensure appropriate use of statistics
- Protect patient confidentiality
- Contribute to evidence base
- Mentor junior colleagues

## 17.13 Exercises

### Exercise 17.1: Quality Improvement Project
Design a statistical plan for a hospital quality improvement project:

**Scenario**: Reduce medication errors in ICU

1. Define outcome measure
2. Plan data collection
3. Design control chart
4. Plan analysis of intervention effect

### Exercise 17.2: Cost-Effectiveness Analysis
Evaluate two treatments for hypertension:

**Treatment A**: Cost $500/year, reduces events by 15%
**Treatment B**: Cost $800/year, reduces events by 25%
**Baseline event rate**: 5% per year

1. Calculate ICER for Treatment B vs A
2. Interpret cost-effectiveness
3. Consider willingness-to-pay threshold

### Exercise 17.3: Outbreak Investigation
An outbreak of 30 cases of gastrointestinal illness occurs:

**Suspected source**: Local restaurant
**Incubation period**: 24-48 hours

1. Design case-control study
2. Calculate sample size
3. Plan statistical analysis

### Exercise 17.4: Evidence Implementation
A new guideline recommends Treatment X for diabetes. Your clinic has 500 diabetic patients.

1. Assess current performance
2. Plan implementation strategy
3. Design evaluation of implementation

## 17.14 Exercise Answers

### Answer 17.1: Quality Improvement Project
1. **Outcome measure**: Medication error rate per 1000 patient-days
2. **Data collection**: Daily error reporting, monthly audits
3. **Control chart**: p-chart for proportion of errors
4. **Intervention analysis**: Compare pre and post rates, use run chart to assess patterns

### Answer 17.2: Cost-Effectiveness Analysis
1. **ICER calculation**:
   - Additional cost: $800 - $500 = $300
   - Additional benefit: 25% - 15% = 10% risk reduction
   - ICER: $300 / 0.10 = $3,000 per 10% risk reduction

2. **Interpretation**: Cost-effective if threshold > $3,000 per 10% risk reduction

3. **Willingness to pay**: Depends on healthcare system (typically $50,000-$100,000 per QALY)

### Answer 17.3: Outbreak Investigation
1. **Case-control study**:
   - Cases: People with illness
   - Controls: People without illness, matched by age and neighborhood
   - Exposure: Restaurant meals in past 48 hours

2. **Sample size**: 30 cases, 60 controls (for 80% power)

3. **Analysis**: Chi-square test for association, calculate odds ratios

### Answer 17.4: Evidence Implementation
1. **Current performance**: Audit current diabetes management practices
2. **Implementation strategy**: Education sessions, decision support tools, performance feedback
3. **Evaluation**: Pre-post comparison of treatment rates, patient outcomes

## 17.15 Chapter Quiz

1. What is statistical process control used for?
2. What is the difference between efficacy and effectiveness?
3. What is the purpose of health technology assessment?
4. Why is missing data a problem in medical research?
5. What is precision medicine?

## 17.16 Quiz Answers

1. To monitor healthcare processes and detect unusual variation
2. Efficacy is benefit under ideal conditions; effectiveness is benefit in real-world practice
3. To evaluate new technologies for adoption in healthcare systems
4. Can bias results and reduce statistical power
5. Individualized treatment based on patient characteristics and genetic profile

---

**Next Chapter Preview**: In Chapter 18, we'll explore advanced statistical topics and emerging trends in medical statistics.
