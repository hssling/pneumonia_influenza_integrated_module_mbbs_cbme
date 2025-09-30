# Chapter 6: Tests for Categorical Data

## 6.1 Introduction to Categorical Data Analysis

**Categorical data** consists of variables that can be divided into distinct groups or categories. These categories may be unordered (nominal) or ordered (ordinal).

### Types of Categorical Variables:
- **Nominal**: Blood type, gender, marital status
- **Ordinal**: Cancer stage, pain severity, education level
- **Binary**: Yes/no, success/failure, alive/dead

### Why Special Methods for Categorical Data?
- Cannot use means or standard deviations
- Different probability distributions (binomial, multinomial)
- Special considerations for small cell counts
- Different measures of association

**Example 6.1**: Hospital data
- Patient outcomes: survived/died (binary)
- Treatment type: A, B, C, D (nominal)
- Pain level: none, mild, moderate, severe (ordinal)

## 6.2 Chi-Square Tests

### 6.2.1 Chi-Square Test for Independence

**Tests whether two categorical variables are independent**

**Hypotheses:**
- H₀: Variables are independent (no association)
- H₁: Variables are associated

**Formula:**
χ² = Σ(Oᵢⱼ - Eᵢⱼ)² / Eᵢⱼ

Where:
- Oᵢⱼ = observed frequency in cell i,j
- Eᵢⱼ = expected frequency = (row i total × column j total) / grand total

**Example 6.2**: Treatment and outcome

| Treatment | Success | Failure | Total |
|-----------|---------|---------|-------|
| A         | 45      | 15      | 60    |
| B         | 35      | 25      | 60    |
| Total     | 80      | 40      | 120   |

**Expected values:**
- A/Success: (60×80)/120 = 40
- A/Failure: (60×40)/120 = 20
- B/Success: (60×80)/120 = 40
- B/Failure: (60×40)/120 = 20

**Calculations:**
χ² = (45-40)²/40 + (15-20)²/20 + (35-40)²/40 + (25-20)²/20
   = 25/40 + 25/20 + 25/40 + 25/20
   = 0.625 + 1.25 + 0.625 + 1.25 = 3.75

**Critical value** for α=0.05, df=1: 3.841
**Decision**: χ² = 3.75 < 3.841, fail to reject H₀
**Conclusion**: No significant association between treatment and outcome

### 6.2.2 Chi-Square Test for Homogeneity

**Tests whether distributions are the same across groups**

**Example 6.3**: Treatment response by gender

| Gender | Good Response | Poor Response | Total |
|--------|---------------|----------------|-------|
| Male   | 30            | 20             | 50    |
| Female | 45            | 25             | 70    |
| Total  | 75            | 45             | 120   |

**Expected values:**
- Male/Good: (50×75)/120 = 31.25
- Male/Poor: (50×45)/120 = 18.75
- Female/Good: (70×75)/120 = 43.75
- Female/Poor: (70×45)/120 = 26.25

**Calculations:**
χ² = (30-31.25)²/31.25 + (20-18.75)²/18.75 + (45-43.75)²/43.75 + (25-26.25)²/26.25
   = 1.5625 + 1.5625 + 1.5625 + 1.5625 = 6.25

**Critical value** for α=0.05, df=1: 3.841
**Decision**: χ² = 6.25 > 3.841, reject H₀
**Conclusion**: Response differs significantly by gender

### 6.2.3 Chi-Square Test for Trend

**Tests for trend in ordinal categorical data**

**Example 6.4**: Dose-response relationship

| Dose (mg) | Response | No Response | Total |
|-----------|----------|-------------|-------|
| 0         | 10       | 40          | 50    |
| 50        | 20       | 30          | 50    |
| 100       | 35       | 15          | 50    |
| 200       | 45       | 5           | 50    |

**Trend analysis** shows significant linear trend (χ²trend = 45.2, p<0.001)

## 6.3 Measures of Association

### 6.3.1 Relative Risk (Risk Ratio)

**Formula:**
RR = Risk in exposed / Risk in unexposed = P(Disease|Exposed) / P(Disease|Unexposed)

**Example 6.5**: Smoking and lung cancer
- Smokers: 45/100 = 0.45
- Non-smokers: 5/100 = 0.05
- RR = 0.45 / 0.05 = 9.0

**Interpretation**: Smokers have 9 times the risk of lung cancer compared to non-smokers

**Confidence Interval for RR:**
CI = e^(ln(RR) ± 1.96 × SE(ln(RR)))

### 6.3.2 Odds Ratio

**Formula:**
OR = (Odds in exposed) / (Odds in unexposed) = [P(D| E)/(1-P(D|E))] / [P(D| Ē)/(1-P(D| Ē))]

**Example 6.6**: Case-control study
- Cases (with disease): 45 smokers, 5 non-smokers
- Controls (without disease): 55 smokers, 95 non-smokers

**Odds in cases**: 45/5 = 9.0
**Odds in controls**: 55/95 = 0.579
**OR = 9.0 / 0.579 = 15.5**

**Interpretation**: Cases are 15.5 times more likely to be smokers than controls

### 6.3.3 Comparison of RR and OR

| Measure | Study Design | Range | When to Use |
|---------|--------------|-------|-------------|
| **Relative Risk** | Cohort studies | 0 to ∞ | When following people forward in time |
| **Odds Ratio** | Case-control studies | 0 to ∞ | When looking backward from disease |

**When OR ≈ RR:**
- When disease is rare (prevalence < 10%)
- OR = 15.5, RR = 9.0 (disease prevalence = 50/200 = 25%, so OR > RR)

## 6.4 Fisher's Exact Test

**Used when sample size is small or expected cell counts < 5**

**Example 6.7**: Rare adverse event

| Treatment | Event | No Event | Total |
|-----------|-------|----------|-------|
| New Drug  | 3     | 47       | 50    |
| Standard  | 0     | 50       | 50    |
| Total     | 3     | 97       | 100   |

**Fisher's Exact Test**: p = 0.035
**Conclusion**: Significant difference in adverse event rates

## 6.5 McNemar's Test

**Tests for paired categorical data (before-after, matched pairs)**

**Example 6.8**: Diagnostic test agreement

| Test 2 Positive | Test 2 Negative | Total |
|-----------------|-----------------|-------|
| **Test 1 Positive** | 40              | 10              | 50    |
| **Test 1 Negative** | 5               | 45              | 50    |
| **Total**           | 45              | 55              | 100   |

**McNemar's Test**:
- Discordant pairs: 10 + 5 = 15
- Test statistic = (10-5)² / 15 = 25/15 = 1.667
- Critical value for α=0.05: 3.841
- Not significant (p > 0.05)

## 6.6 Tests for Ordinal Data

### 6.6.1 Mantel-Haenszel Test

**Tests association in stratified 2×2 tables**

**Example 6.9**: Treatment effect by age group

**Age < 50:**
| Treatment | Success | Failure |
|-----------|---------|---------|
| A         | 25      | 5       |
| B         | 15      | 15      |

**Age ≥ 50:**
| Treatment | Success | Failure |
|-----------|---------|---------|
| A         | 20      | 10      |
| B         | 10      | 20      |

**Mantel-Haenszel OR** = 3.0 (95% CI: 1.8-5.1)
**Test for homogeneity**: No significant difference between strata

### 6.6.2 Jonckheere-Terpstra Test

**Tests for ordered alternatives in multiple groups**

**Example 6.10**: Dose-response with 4 dose levels
- Tests whether response increases with dose
- More powerful than chi-square when trend is expected

## 6.7 Advanced Categorical Data Methods

### 6.7.1 Logistic Regression

**Models relationship between categorical outcome and predictor variables**

**Example 6.11**: Predicting treatment success
- Outcome: Success/failure
- Predictors: Age, gender, treatment type, baseline severity

**Model:**
logit(P(success)) = β₀ + β₁×Age + β₂×Gender + β₃×Treatment + β₄×Severity

**Interpretation:**
- Odds ratio for treatment = e^β₃
- For each year increase in age, odds of success change by factor e^β₁

### 6.7.2 Loglinear Models

**Models multi-way contingency tables**

**Example 6.12**: Three-way table analysis
- Variables: Treatment, Outcome, Gender
- Tests for three-way interactions
- Models complex relationships between multiple categorical variables

## 6.8 Medical Applications

### 6.8.1 Epidemiology

**Example 6.13**: Disease risk factors
- Case-control study of 500 cases and 500 controls
- Exposure: Smoking, alcohol, diet, exercise
- Calculate odds ratios for each risk factor
- Control for confounding using logistic regression

### 6.8.2 Clinical Trials

**Example 6.14**: Multi-center trial analysis
- 10 centers, 2 treatments, binary outcome
- Use stratified analysis to account for center differences
- Mantel-Haenszel test for overall treatment effect

### 6.8.3 Diagnostic Testing

**Example 6.15**: Test accuracy across subgroups
- New diagnostic test for diabetes
- Test performance in different age groups
- Use stratified analysis to check consistency
- Calculate sensitivity and specificity for each subgroup

## 6.9 Sample Size for Categorical Data

### 6.9.1 Sample Size for Proportions

**Formula:**
n = (Zα/2 + Zβ)² × [π₁(1-π₁) + π₂(1-π₂)] / (π₁ - π₂)²

**Example 6.16**: Detecting difference in complication rates
- Want to detect difference between 10% and 20%
- 80% power, α=0.05

n = (1.96 + 0.84)² × [0.10×0.90 + 0.20×0.80] / (0.10)² = (2.8)² × 0.25 / 0.01 = 7.84 × 25 = 196 per group

### 6.9.2 Sample Size for Chi-Square Tests

**Depends on:**
- Number of categories
- Expected effect size
- Desired power

**Rule of thumb**: Need at least 5 observations per cell for valid chi-square test

## 6.10 Common Issues with Categorical Data

### 6.10.1 Small Cell Counts

**Problem**: Chi-square test unreliable when expected counts < 5

**Solutions:**
- Combine categories
- Use Fisher's exact test
- Increase sample size

### 6.10.2 Zero Cell Counts

**Problem**: Cannot calculate odds ratio when any cell is zero

**Solutions:**
- Add 0.5 to all cells (small sample correction)
- Use different study design
- Report as "could not be calculated"

### 6.10.3 Multiple Comparisons

**Problem**: Testing multiple associations increases false positive rate

**Solutions:**
- Pre-specify primary hypothesis
- Use Bonferroni correction
- Control false discovery rate

## 6.11 Exercises

### Exercise 6.1: Chi-Square Test
Test association between smoking and heart disease:

| Smoking | Heart Disease | No Heart Disease | Total |
|---------|---------------|------------------|-------|
| Yes     | 120           | 180              | 300   |
| No      | 30            | 270              | 300   |
| Total   | 150           | 450              | 600   |

### Exercise 6.2: Calculate Odds Ratio
From the following case-control study data:
- Cases: 80 exposed, 20 unexposed
- Controls: 40 exposed, 60 unexposed

### Exercise 6.3: Relative Risk vs Odds Ratio
In a cohort study:
- Exposed: 50 developed disease, 150 remained healthy
- Unexposed: 20 developed disease, 180 remained healthy

Calculate both RR and OR and explain the difference.

### Exercise 6.4: Fisher's Exact Test
Small study of treatment side effects:

| Treatment | Side Effect | No Side Effect | Total |
|-----------|-------------|----------------|-------|
| New       | 2           | 18             | 20    |
| Standard  | 0           | 20             | 20    |
| Total     | 2           | 38             | 40    |

## 6.12 Exercise Answers

### Answer 6.1: Chi-Square Test
**Expected values:**
- Yes/Disease: (300×150)/600 = 75
- Yes/No Disease: (300×450)/600 = 225
- No/Disease: (300×150)/600 = 75
- No/No Disease: (300×450)/600 = 225

**χ² = (120-75)²/75 + (180-225)²/225 + (30-75)²/75 + (270-225)²/225**
   = 2025/75 + 2025/225 + 2025/75 + 2025/225
   = 27 + 9 + 27 + 9 = 72

**Critical value** for α=0.05, df=1: 3.841
**χ² = 72 > 3.841, reject H₀**
**Conclusion**: Significant association between smoking and heart disease

### Answer 6.2: Odds Ratio
**Odds in cases**: 80/20 = 4.0
**Odds in controls**: 40/60 = 0.667
**OR = 4.0 / 0.667 = 6.0**

**Interpretation**: Cases are 6 times more likely to be exposed than controls

### Answer 6.3: Relative Risk vs Odds Ratio
**Risk in exposed**: 50/200 = 0.25
**Risk in unexposed**: 20/200 = 0.10
**RR = 0.25 / 0.10 = 2.5**

**Odds in exposed**: 50/150 = 0.333
**Odds in unexposed**: 20/180 = 0.111
**OR = 0.333 / 0.111 = 3.0**

**Difference**: Disease prevalence = 70/400 = 17.5% (not rare), so OR > RR

### Answer 6.4: Fisher's Exact Test
**This is a 2×2 table with small numbers**
**Fisher's exact p-value = 0.248**

**Conclusion**: No significant difference in side effect rates (p > 0.05)

## 6.13 Chapter Quiz

1. When should you use Fisher's exact test instead of chi-square?
2. What is the difference between relative risk and odds ratio?
3. What does a significant chi-square test tell you?
4. Why are small cell counts problematic for chi-square tests?
5. What is the Mantel-Haenszel test used for?

## 6.14 Quiz Answers

1. When sample size is small or expected cell counts are less than 5
2. RR compares risks; OR compares odds; OR approximates RR when disease is rare
3. There is a statistically significant association between the variables
4. Chi-square test assumptions are violated, leading to unreliable results
5. Testing association in stratified data or multiple 2×2 tables

---

**Next Chapter Preview**: In Chapter 7, we'll explore correlation and regression analysis for continuous data.
