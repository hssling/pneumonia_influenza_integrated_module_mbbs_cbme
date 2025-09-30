# Chapter 12: Diagnostic and Screening Tests

## 12.1 Introduction to Diagnostic Testing

**Diagnostic tests** help determine whether a patient has a particular disease or condition. **Screening tests** identify disease in apparently healthy populations.

### Key Concepts:
- **Sensitivity**: Ability to correctly identify diseased individuals
- **Specificity**: Ability to correctly identify non-diseased individuals
- **Predictive Values**: Probability of disease given test result
- **Likelihood Ratios**: How much test result changes disease probability

### Why Special Statistical Methods?
- **Verification bias**: Not all patients get gold standard test
- **Spectrum bias**: Test performance varies across disease severity
- **Prevalence effects**: Predictive values depend on disease prevalence
- **Multiple tests**: Combining tests optimally

**Example 12.1**: Mammography screening
- Test: Mammogram
- Disease: Breast cancer
- Population: Women over 50
- Goal: Early detection to improve outcomes

## 12.2 Measures of Test Performance

### 12.2.1 Sensitivity and Specificity

**Sensitivity** = P(Test positive | Disease present)
**Specificity** = P(Test negative | Disease absent)

**Example 12.2**: HIV testing

|           | Disease Present | Disease Absent | Total |
|-----------|-----------------|----------------|-------|
| **Test Positive** | 95 (TP)         | 10 (FP)        | 105   |
| **Test Negative** | 5 (FN)          | 990 (TN)       | 995   |
| **Total**         | 100             | 1000           | 1100  |

**Sensitivity** = 95/100 = 0.95 or 95%
**Specificity** = 990/1000 = 0.99 or 99%

### 12.2.2 Predictive Values

**Positive Predictive Value (PPV)** = P(Disease | Test positive)
**Negative Predictive Value (NPV)** = P(No disease | Test negative)

**From previous example:**
**PPV** = 95/105 = 0.905 or 90.5%
**NPV** = 990/995 = 0.995 or 99.5%

### 12.2.3 Relationship Between Measures

**PPV and NPV depend on prevalence:**
PPV = Sensitivity × Prevalence / (Sensitivity × Prevalence + (1-Specificity) × (1-Prevalence))

**Example 12.3**: Same test, different prevalence
- Low prevalence (1%): PPV = 95×0.01 / (95×0.01 + 5×0.99) = 0.95/5.9 = 16.1%
- High prevalence (20%): PPV = 95×0.20 / (95×0.20 + 5×0.80) = 19/23 = 82.6%

## 12.3 Likelihood Ratios

### 12.3.1 Definition and Interpretation

**Positive Likelihood Ratio (LR+)** = Sensitivity / (1-Specificity)
**Negative Likelihood Ratio (LR-)** = (1-Sensitivity) / Specificity

**Interpretation:**
- LR+ > 10: Large increase in disease probability
- LR+ 5-10: Moderate increase
- LR+ 2-5: Small increase
- LR+ 1-2: Minimal increase

**Example 12.4**: HIV test likelihood ratios
- Sensitivity = 0.95, Specificity = 0.99
- LR+ = 0.95 / 0.01 = 95
- LR- = 0.05 / 0.99 = 0.051

**Interpretation:**
- Positive test: 95 times more likely in diseased
- Negative test: About 20 times less likely in diseased

### 12.3.2 Using Likelihood Ratios

**Pre-test odds** = Pre-test probability / (1 - Pre-test probability)
**Post-test odds** = Pre-test odds × Likelihood ratio
**Post-test probability** = Post-test odds / (1 + Post-test odds)

**Example 12.5**: Converting odds to probability
- Pre-test probability = 0.10 (10%)
- Pre-test odds = 0.10/0.90 = 0.111
- Positive test, LR+ = 95
- Post-test odds = 0.111 × 95 = 10.55
- Post-test probability = 10.55 / 11.55 = 0.913 or 91.3%

## 12.4 ROC Curves

### 12.4.1 Basic Concepts

**ROC (Receiver Operating Characteristic) curve** plots sensitivity vs (1-specificity) at different test cutoffs.

**Area Under Curve (AUC)**:
- AUC = 1.0: Perfect test
- AUC = 0.5: No discriminatory ability (diagonal line)
- AUC > 0.8: Good test
- AUC > 0.9: Excellent test

**Example 12.6**: PSA test for prostate cancer
- Different cutoffs: 2.0, 3.0, 4.0, 10.0 ng/mL
- Plot sensitivity vs false positive rate
- AUC = 0.75 (moderate accuracy)

### 12.4.2 Comparing ROC Curves

**Test if one diagnostic test is better than another**

**Example 12.7**: New vs existing biomarker
- New test: AUC = 0.82
- Existing test: AUC = 0.76
- Difference significant (p=0.03)
- New test better at distinguishing disease

## 12.5 Bayesian Approaches to Diagnosis

### 12.5.1 Pre-test and Post-test Probability

**Using Bayes' theorem for diagnosis:**

P(Disease | Test) = P(Test | Disease) × P(Disease) / P(Test)

**Example 12.8**: Clinical diagnosis
- Pre-test probability = 0.30 (based on symptoms, history)
- Test sensitivity = 0.90, specificity = 0.85
- Positive test result

**Post-test probability** = 0.90 × 0.30 / (0.90 × 0.30 + 0.15 × 0.70) = 0.27 / 0.375 = 0.72 or 72%

### 12.5.2 Fagan's Nomogram

**Graphical tool for calculating post-test probabilities**

**Steps:**
1. Mark pre-test probability
2. Mark likelihood ratio
3. Read post-test probability

## 12.6 Multiple Tests and Test Combinations

### 12.6.1 Parallel Testing

**Test positive if either test positive**

**Combined sensitivity** = 1 - (1-Sens1) × (1-Sens2)
**Combined specificity** = Spec1 × Spec2

**Example 12.9**: Two screening tests
- Test A: Sens=0.80, Spec=0.90
- Test B: Sens=0.85, Spec=0.85
- Parallel: Sens=0.97, Spec=0.765

### 12.6.2 Serial Testing

**Test positive only if both tests positive**

**Combined sensitivity** = Sens1 × Sens2
**Combined specificity** = 1 - (1-Spec1) × (1-Spec2)

**Example 12.10**: Confirmatory testing
- Screening test: Sens=0.95, Spec=0.80
- Confirmatory test: Sens=0.90, Spec=0.99
- Serial: Sens=0.855, Spec=0.998

## 12.7 Diagnostic Test Accuracy Studies

### 12.7.1 Study Designs

**Cross-sectional study**: Single time point
**Case-control study**: Separate diseased and non-diseased groups
**Cohort study**: Follow patients over time

### 12.7.2 Sources of Bias

**Verification bias**: Not all patients receive gold standard
**Spectrum bias**: Study population not representative
**Review bias**: Knowledge of test result affects interpretation
**Incorporation bias**: Test result influences gold standard

### 12.7.3 STARD Guidelines

**Standards for Reporting Diagnostic Accuracy Studies**

**Key elements:**
- Patient selection and recruitment
- Test methods and interpretation
- Gold standard definition
- Blinding procedures
- Handling of indeterminate results

## 12.8 Medical Applications

### 12.8.1 Cancer Screening

**Example 12.11**: Colorectal cancer screening
- Tests: FOBT, colonoscopy, CT colonography
- Compare sensitivity and specificity
- Consider interval cancers (false negatives)
- Balance benefits vs harms (complications, overdiagnosis)

### 12.8.2 Cardiovascular Risk Assessment

**Example 12.12**: Coronary artery disease diagnosis
- Tests: Exercise ECG, stress echocardiography, coronary angiography
- Use likelihood ratios to update pre-test probability
- Guide decisions about invasive testing

### 12.8.3 Infectious Disease Testing

**Example 12.13**: COVID-19 diagnosis
- PCR test: High sensitivity, high specificity
- Rapid antigen test: Lower sensitivity, high specificity
- Serial testing to improve sensitivity
- Prevalence affects predictive values

## 12.9 Sample Size for Diagnostic Studies

### 12.9.1 Factors Affecting Sample Size

**Larger samples needed when:**
- Smaller difference in accuracy to detect
- Lower disease prevalence
- Higher desired precision
- Multiple subgroups

**Formula for sensitivity:**
n = (Zα/2)² × Sensitivity × (1-Sensitivity) / E²

**Example 12.14**: Estimating sensitivity
- Want 95% CI width of ±5%
- Estimated sensitivity = 0.85
- n = (1.96)² × 0.85 × 0.15 / (0.05)² = 3.8416 × 0.1275 / 0.0025 = 0.49 / 0.0025 = 196 diseased patients

### 12.9.2 Sample Size for Comparing Tests

**Compare sensitivity of two tests**

**Formula:**
n = 2 × (Zα/2 + Zβ)² × p(1-p) / δ²

Where p = average sensitivity, δ = difference to detect

## 12.10 Advanced Diagnostic Methods

### 12.10.1 Latent Class Analysis

**No gold standard available**

**Statistical model:**
- Estimates true disease status
- Estimates test sensitivity and specificity
- Accounts for conditional dependence

**Example 12.15**: Multiple imperfect tests
- Three diagnostic tests for disease
- No perfect gold standard
- Latent class model estimates true accuracy

### 12.10.2 Diagnostic Meta-Analysis

**Combines results from multiple studies**

**Methods:**
- Bivariate random effects model
- Hierarchical summary ROC curves
- Accounts for between-study heterogeneity

**Example 12.16**: Systematic review of diagnostic tests
- 15 studies of new biomarker
- Summary sensitivity = 0.82 (95% CI: 0.78-0.86)
- Summary specificity = 0.88 (95% CI: 0.84-0.91)

## 12.11 Common Mistakes in Diagnostic Testing

### 12.11.1 Confusing Sensitivity and PPV

**Problem**: Using sensitivity as probability of disease

**Reality**: PPV depends on prevalence

**Example**: HIV test
- Sensitivity = 99.9%
- In low prevalence population (0.1%): PPV ≈ 50%
- In high prevalence population (10%): PPV ≈ 92%

### 12.11.2 Over-reliance on p-values

**Problem**: Statistical significance vs clinical importance

**Solution**: Focus on confidence intervals and effect sizes

### 12.11.3 Spectrum Bias

**Problem**: Testing extremes of disease severity

**Solution**: Include full spectrum of patients (early to advanced disease)

## 12.12 Exercises

### Exercise 12.1: Calculate Test Performance
A study of a new diagnostic test:

|           | Disease Present | Disease Absent | Total |
|-----------|-----------------|----------------|-------|
| **Test Positive** | 45              | 15             | 60    |
| **Test Negative** | 5               | 135            | 140   |
| **Total**         | 50              | 150            | 200   |

1. Calculate sensitivity, specificity, PPV, NPV
2. Calculate positive and negative likelihood ratios
3. If prevalence is 10%, what would PPV and NPV be?

### Exercise 12.2: ROC Curve Interpretation
A diagnostic test has the following performance at different cutoffs:

| Cutoff | Sensitivity | 1-Specificity |
|--------|-------------|---------------|
| 1      | 1.00        | 1.00          |
| 2      | 0.95        | 0.60          |
| 3      | 0.85        | 0.30          |
| 4      | 0.70        | 0.15          |
| 5      | 0.50        | 0.08          |
| 6      | 0.30        | 0.05          |

1. Plot the ROC curve
2. Estimate AUC
3. Choose optimal cutoff for 80% sensitivity

### Exercise 12.3: Bayesian Calculation
A patient has 40% pre-test probability of disease. Test has LR+ = 8.

1. Calculate post-test probability of disease
2. If test is negative (LR- = 0.2), what is post-test probability?

### Exercise 12.4: Test Combination
Two tests for disease detection:
- Test A: Sensitivity 0.90, Specificity 0.85
- Test B: Sensitivity 0.85, Specificity 0.90

Calculate sensitivity and specificity for:
1. Parallel testing (positive if either positive)
2. Serial testing (positive only if both positive)

## 12.13 Exercise Answers

### Answer 12.1: Test Performance
1. **Sensitivity** = 45/50 = 0.90 or 90%
   **Specificity** = 135/150 = 0.90 or 90%
   **PPV** = 45/60 = 0.75 or 75%
   **NPV** = 135/140 = 0.964 or 96.4%

2. **LR+** = 0.90 / 0.10 = 9
   **LR-** = 0.10 / 0.90 = 0.111

3. **With 10% prevalence:**
   **PPV** = 0.90 × 0.10 / (0.90 × 0.10 + 0.10 × 0.90) = 0.09 / 0.18 = 0.50 or 50%
   **NPV** = 0.90 × 0.90 / (0.10 × 0.10 + 0.90 × 0.90) = 0.81 / 0.91 = 0.89 or 89%

### Answer 12.2: ROC Curve
1. **ROC curve** would show points: (1.00,1.00), (0.60,0.95), (0.30,0.85), (0.15,0.70), (0.08,0.50), (0.05,0.30)

2. **AUC** ≈ 0.85 (good test)

3. **For 80% sensitivity**: Look for cutoff where sensitivity ≈ 0.80
   - Cutoff 3: Sensitivity = 0.85, closest to 0.80
   - 1-Specificity = 0.30 (specificity = 0.70)

### Answer 12.3: Bayesian Calculation
1. **Pre-test odds** = 0.40/0.60 = 0.667
   **Post-test odds** = 0.667 × 8 = 5.33
   **Post-test probability** = 5.33/(1+5.33) = 5.33/6.33 = 0.842 or 84.2%

2. **Post-test odds** = 0.667 × 0.2 = 0.133
   **Post-test probability** = 0.133/(1+0.133) = 0.133/1.133 = 0.117 or 11.7%

### Answer 12.4: Test Combination
1. **Parallel testing:**
   **Sensitivity** = 1 - (1-0.90)×(1-0.85) = 1 - 0.10×0.15 = 1 - 0.015 = 0.985
   **Specificity** = 0.85 × 0.90 = 0.765

2. **Serial testing:**
   **Sensitivity** = 0.90 × 0.85 = 0.765
   **Specificity** = 1 - (1-0.85)×(1-0.90) = 1 - 0.15×0.10 = 1 - 0.015 = 0.985

## 12.14 Chapter Quiz

1. What is the difference between sensitivity and positive predictive value?
2. When would you use parallel vs serial testing?
3. What does an AUC of 0.75 mean?
4. Why do predictive values depend on disease prevalence?
5. What is verification bias in diagnostic studies?

## 12.15 Quiz Answers

1. Sensitivity is fixed test property; PPV depends on prevalence and specificity
2. Parallel for screening (high sensitivity); serial for confirmation (high specificity)
3. Test has 75% chance of correctly distinguishing diseased from non-diseased
4. Bayes' theorem: PPV = Sensitivity × Prevalence / (Sensitivity × Prevalence + (1-Specificity) × (1-Prevalence))
5. Not all test results verified with gold standard, leading to biased accuracy estimates

---

**Next Chapter Preview**: In Chapter 13, we'll explore clinical trial design and the statistical considerations for randomized controlled trials.
