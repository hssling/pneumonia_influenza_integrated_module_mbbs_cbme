# Chapter 14: Meta-Analysis

## 14.1 Introduction to Meta-Analysis

**Meta-analysis** is a statistical method that combines results from multiple independent studies to provide a more precise estimate of treatment effects and identify patterns across studies.

### Why Use Meta-Analysis?
- **Increased power**: Combine small studies to detect small effects
- **Improved precision**: Narrower confidence intervals
- **Resolve controversies**: Clarify conflicting results
- **Generate hypotheses**: Identify gaps in research
- **Inform policy**: Provide robust evidence for decision-making

### Key Concepts:
- **Effect size**: Standardized measure of treatment effect
- **Heterogeneity**: Variation between study results
- **Publication bias**: Studies with significant results more likely published
- **Forest plot**: Graphical display of results
- **Fixed vs random effects**: Different assumptions about study variation

**Example 14.1**: Antihypertensive drug meta-analysis
- 15 randomized trials of new blood pressure medication
- Each trial too small to detect moderate effects
- Meta-analysis combines evidence to assess overall efficacy

## 14.2 Types of Effect Sizes

### 14.2.1 For Continuous Outcomes

**Standardized Mean Difference (SMD):**
SMD = (Mean₁ - Mean₂) / SD_pooled

**Example 14.2**: Blood pressure reduction
- Treatment group: Mean = 145, SD = 12
- Control group: Mean = 150, SD = 11
- Pooled SD = 11.5
- SMD = (145-150)/11.5 = -5/11.5 = -0.43

**Interpretation:**
- SMD = 0.2: Small effect
- SMD = 0.5: Medium effect
- SMD = 0.8: Large effect

### 14.2.2 For Binary Outcomes

**Odds Ratio (OR):**
OR = (a×d) / (b×c)

Where 2×2 table:
|         | Event | No Event |
|---------|-------|----------|
| **Treatment** | a     | b        |
| **Control**   | c     | d        |

**Risk Ratio (RR):**
RR = a/(a+b) ÷ c/(c+d)

**Example 14.3**: Treatment success
- Treatment: 45/100 successes (45%)
- Control: 30/100 successes (30%)
- RR = 45/100 ÷ 30/100 = 1.5
- OR = (45×70) / (55×30) = 3150 / 1650 = 1.91

### 14.2.3 For Survival Data

**Hazard Ratio (HR):**
HR = h_treatment(t) / h_control(t)

**Example 14.4**: Cancer survival
- Treatment group: 20% mortality at 5 years
- Control group: 30% mortality at 5 years
- HR = 0.67 (33% risk reduction)

## 14.3 Fixed Effect vs Random Effects Models

### 14.3.1 Fixed Effect Model

**Assumes all studies estimate same true effect**

**Formula:**
θ̂ = Σ(wᵢ × θᵢ) / Σ(wᵢ)

Where wᵢ = 1 / SE(θᵢ)²

**Use when:**
- Studies very similar
- Goal is to estimate common effect
- Low heterogeneity

**Example 14.5**: Identical clinical trials
- 5 trials of same drug vs placebo
- Similar patients, same outcome measure
- Fixed effect model appropriate

### 14.3.2 Random Effects Model

**Assumes studies estimate different true effects**

**Formula:**
θ̂ = Σ(wᵢ* × θᵢ) / Σ(wᵢ*)

Where wᵢ* = 1 / (SE(θᵢ)² + τ²)

**Use when:**
- Studies clinically diverse
- Goal is to generalize to broader population
- High heterogeneity

**Example 14.6**: Multi-center trials
- Different countries, different patient populations
- Random effects model accounts for between-study variation

## 14.4 Assessing Heterogeneity

### 14.4.1 Measures of Heterogeneity

**Cochran's Q:**
Q = Σ(wᵢ × (θᵢ - θ̂)²)

**I² statistic:**
I² = (Q - df) / Q × 100%

**Interpretation:**
- I² = 0-25%: Low heterogeneity
- I² = 25-50%: Moderate heterogeneity
- I² = 50-75%: Substantial heterogeneity
- I² > 75%: High heterogeneity

**Example 14.7**: Blood pressure meta-analysis
- Q = 25.6, df = 9
- I² = (25.6 - 9)/25.6 × 100% = 16.6/25.6 × 100% = 64.8%
- Substantial heterogeneity

### 14.4.2 Sources of Heterogeneity

**Clinical heterogeneity:**
- Different patient populations
- Different interventions
- Different outcome measures

**Methodological heterogeneity:**
- Different study designs
- Different quality
- Different analysis methods

**Statistical heterogeneity:**
- Small study effects
- Publication bias
- Chance variation

## 14.5 Publication Bias and Small Study Effects

### 14.5.1 Funnel Plot

**Plot effect size vs precision (1/SE)**

**Symmetric funnel**: No publication bias
**Asymmetric funnel**: Publication bias likely

**Example 14.8**: Funnel plot assessment
- Small studies show large effects
- Large studies show small effects
- Asymmetric funnel suggests publication bias

### 14.5.2 Statistical Tests for Bias

**Egger's test**: Regression of effect size on precision
**Begg's test**: Rank correlation between effect size and variance

**Example 14.9**: Egger's test
- Regression coefficient = 2.1, p=0.03
- Significant asymmetry, possible publication bias

### 14.5.3 Trim and Fill Method

**Estimates number of missing studies**
**Imputes missing studies and recalculates effect**

**Example 14.10**: Publication bias correction
- Original effect: OR = 1.8
- After trim and fill: OR = 1.5
- Adjusted for missing negative studies

## 14.6 Forest Plots

### 14.6.1 Basic Components

**Horizontal lines**: Confidence intervals for each study
**Boxes**: Point estimates (size proportional to weight)
**Diamond**: Overall effect estimate
**Vertical line**: Line of no effect

**Example 14.11**: Forest plot interpretation
- Most studies favor treatment (boxes to right of line)
- Overall effect: OR = 1.6 (95% CI: 1.3-2.0)
- Significant benefit of treatment

### 14.6.2 Subgroup Analyses in Forest Plots

**Separate estimates for different subgroups**

**Example 14.12**: Treatment effect by age
- Young patients: OR = 2.1 (1.6-2.8)
- Older patients: OR = 1.3 (0.9-1.8)
- Test for subgroup differences: p=0.04

## 14.7 Meta-Regression

### 14.7.1 Basic Concepts

**Regression of effect size on study characteristics**

**Model:**
θᵢ = β₀ + β₁×Xᵢ + εᵢ

**Example 14.13**: Effect size vs study quality
- X = quality score (0-10)
- β₁ = -0.15 (higher quality studies show smaller effects)
- p=0.02 (quality explains some heterogeneity)

### 14.7.2 Covariates in Meta-Regression

**Study-level characteristics:**
- Sample size
- Publication year
- Study quality
- Patient characteristics
- Intervention details

**Example 14.14**: Dose-response meta-regression
- Studies with different drug doses
- Effect size increases with dose
- β = 0.3 per mg increase, p<0.001

## 14.8 Network Meta-Analysis

### 14.8.1 When to Use

**Multiple treatments compared indirectly**

**Example 14.15**: Three hypertension drugs
- Drug A vs placebo: 5 studies
- Drug B vs placebo: 4 studies
- Drug A vs Drug B: 2 studies
- Network meta-analysis compares all three

### 14.8.2 Statistical Methods

**Bayesian hierarchical models**
**Markov Chain Monte Carlo (MCMC) estimation**

**Example 14.16**: Treatment ranking
- Drug A: Mean effect -12 mmHg (95% CrI: -15 to -9)
- Drug B: Mean effect -10 mmHg (95% CrI: -13 to -7)
- Drug C: Mean effect -8 mmHg (95% CrI: -11 to -5)
- Drug A most effective

## 14.9 Medical Applications

### 14.9.1 Systematic Reviews

**Example 14.17**: Diabetes treatment guidelines
- Meta-analysis of 25 trials
- New drug reduces HbA1c by 0.8% (95% CI: 0.6-1.0)
- Low heterogeneity (I² = 15%)
- No publication bias detected

### 14.9.2 Epidemiological Research

**Example 14.18**: Risk factor meta-analysis
- 30 studies of smoking and lung cancer
- Combined OR = 4.2 (95% CI: 3.8-4.7)
- High heterogeneity explained by study design differences

### 14.9.3 Health Technology Assessment

**Example 14.19**: Cost-effectiveness analysis
- Meta-analysis of treatment efficacy
- Combined with cost data
- Inform reimbursement decisions

## 14.10 Quality Assessment in Meta-Analysis

### 14.10.1 Risk of Bias Assessment

**Cochrane Risk of Bias Tool:**
- Random sequence generation
- Allocation concealment
- Blinding
- Incomplete outcome data
- Selective reporting
- Other bias

**Example 14.20**: Quality assessment
- 15 studies reviewed
- 8 low risk of bias
- 5 moderate risk
- 2 high risk
- Sensitivity analysis excluding high risk studies

### 14.10.2 GRADE System

**Grading of Recommendations Assessment, Development and Evaluation**

**Quality factors:**
- Risk of bias
- Inconsistency
- Indirectness
- Imprecision
- Publication bias

**Example 14.21**: GRADE assessment
- Initial quality: High (RCTs)
- Downgrade for inconsistency: Moderate
- Downgrade for imprecision: Low
- Final quality: Low

## 14.11 Advanced Meta-Analysis Methods

### 14.11.1 Individual Patient Data (IPD) Meta-Analysis

**Combines raw data from multiple studies**

**Advantages:**
- More detailed analyses
- Subgroup analyses with more power
- Time-to-event analyses
- Handle missing data better

**Disadvantages:**
- Requires cooperation from all study authors
- Time-consuming and expensive
- Some studies may not share data

**Example 14.22**: IPD meta-analysis
- 10 trials of cancer treatment
- Combined dataset: 2,500 patients
- Identify treatment-by-covariate interactions

### 14.11.2 Cumulative Meta-Analysis

**Add studies chronologically**

**Example 14.23**: Treatment efficacy over time
- 1990: OR = 1.2 (not significant)
- 1995: Add 3 studies, OR = 1.4 (p=0.04)
- 2000: Add 5 studies, OR = 1.6 (p<0.001)
- Shows when treatment benefit became clear

## 14.12 Common Mistakes in Meta-Analysis

### 14.12.1 Combining Apples and Oranges

**Problem**: Including incompatible studies

**Solutions:**
- Strict inclusion criteria
- Subgroup analyses
- Meta-regression to explain differences

### 14.12.2 Ignoring Heterogeneity

**Problem**: Using fixed effect model when substantial heterogeneity exists

**Solution**: Use random effects model and investigate sources of heterogeneity

### 14.12.3 Publication Bias Over-Correction

**Problem**: Overly aggressive adjustment for publication bias

**Solution**: Use multiple methods and sensitivity analyses

## 14.13 Exercises

### Exercise 14.1: Calculate Pooled Effect Size
Three studies of treatment effect:

**Study 1:** OR = 2.1, 95% CI: 1.4-3.2
**Study 2:** OR = 1.8, 95% CI: 1.1-2.9
**Study 3:** OR = 2.5, 95% CI: 1.6-3.9

1. Calculate pooled OR using fixed effect model
2. Calculate heterogeneity (Q and I²)
3. Interpret results

### Exercise 14.2: Funnel Plot Assessment
A meta-analysis includes studies with varying sample sizes and effect sizes. Describe how you would:
1. Create a funnel plot
2. Assess for publication bias
3. Test for asymmetry

### Exercise 14.3: Meta-Regression
Studies have different mean ages. Effect sizes and mean ages:

**Study 1:** OR = 2.1, Mean age = 45
**Study 2:** OR = 1.8, Mean age = 52
**Study 3:** OR = 2.5, Mean age = 38
**Study 4:** OR = 1.6, Mean age = 58

1. Perform meta-regression of effect size on age
2. Interpret the results

### Exercise 14.4: Subgroup Analysis
A meta-analysis shows overall treatment benefit. Two subgroups:

**Subgroup 1 (n=400):** OR = 1.8, p=0.01
**Subgroup 2 (n=200):** OR = 1.2, p=0.45

1. Test for subgroup interaction
2. Interpret the findings

## 14.14 Exercise Answers

### Answer 14.1: Pooled Effect Size
1. **Fixed effect model:**
   - Study 1 weight = 1/(ln(3.2/1.4))² ≈ 25%
   - Study 2 weight = 1/(ln(2.9/1.1))² ≈ 20%
   - Study 3 weight = 1/(ln(3.9/1.6))² ≈ 55%
   - Pooled OR ≈ 2.2

2. **Heterogeneity:**
   - Q = Σ weights × (lnOR - lnOR_pooled)² ≈ 3.2
   - I² = (3.2 - 2)/3.2 × 100% = 37.5% (moderate)

3. **Interpretation**: Moderate heterogeneity, fixed effect model appropriate

### Answer 14.2: Funnel Plot Assessment
1. **Create funnel plot**: Plot effect size (OR) vs precision (1/SE) or sample size
2. **Assess asymmetry**: Look for missing studies in areas where small negative studies should be
3. **Test asymmetry**: Use Egger's test (regression of effect size on precision)

### Answer 14.3: Meta-Regression
1. **Regression model**: lnOR = β₀ + β₁×Age
   - β₁ = -0.02 (not significant, p=0.15)
   - Age does not explain effect size variation

2. **Interpretation**: No significant relationship between study mean age and effect size

### Answer 14.4: Subgroup Analysis
1. **Interaction test**: Compare effect sizes between subgroups
   - Difference in lnOR = ln(1.8) - ln(1.2) = 0.588 - 0.182 = 0.406
   - Test if difference significant

2. **Interpretation**: Subgroup 1 shows stronger effect, but interaction test needed to determine if difference is significant

## 14.15 Chapter Quiz

1. What is the main advantage of meta-analysis over individual studies?
2. When would you use a random effects model?
3. What does a funnel plot assess?
4. What is the GRADE system used for?
5. What is the difference between fixed effect and random effects models?

## 14.16 Quiz Answers

1. Increased statistical power and more precise effect estimates
2. When studies are heterogeneous or want to generalize beyond included studies
3. Publication bias and small study effects
4. Assessing quality of evidence and strength of recommendations
5. Fixed effect assumes one true effect; random effects assumes distribution of true effects

---

**Next Chapter Preview**: In Chapter 15, we'll explore statistical software commonly used in medical research.
