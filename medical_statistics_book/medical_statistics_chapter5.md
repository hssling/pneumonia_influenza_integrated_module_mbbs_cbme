# Chapter 5: Hypothesis Testing

## 5.1 Introduction to Hypothesis Testing

**Hypothesis testing** is a statistical method used to make decisions about population parameters based on sample data.

### Key Concepts:
- **Null Hypothesis (H₀)**: Statement of no effect or no difference
- **Alternative Hypothesis (H₁)**: Statement of effect or difference
- **Test Statistic**: Value calculated from sample data
- **p-value**: Probability of observing data if null hypothesis is true
- **Significance Level (α)**: Probability of rejecting null when it's true (usually 0.05)

**Example 5.1**: Testing a new blood pressure medication
- H₀: New drug has no effect on blood pressure (μ = 120 mmHg)
- H₁: New drug reduces blood pressure (μ < 120 mmHg)
- Sample of 50 patients shows mean = 115 mmHg
- Is this difference due to drug effect or chance?

## 5.2 Steps in Hypothesis Testing

### The Hypothesis Testing Process:
1. **State hypotheses** (null and alternative)
2. **Set significance level** (usually α = 0.05)
3. **Collect and analyze data**
4. **Calculate test statistic**
5. **Determine p-value or critical value**
6. **Make decision** (reject or fail to reject H₀)
7. **Draw conclusion** in context of research question

### 5.2.1 One-Tailed vs Two-Tailed Tests

**Two-tailed test**: Alternative hypothesis has no direction
- H₀: μ = 120
- H₁: μ ≠ 120
- Tests for any difference (increase or decrease)

**One-tailed test**: Alternative hypothesis has specific direction
- H₀: μ = 120
- H₁: μ < 120 (or μ > 120)
- Tests for difference in specific direction
- More powerful but requires prior knowledge of direction

## 5.3 Testing Means: t-Tests

### 5.3.1 One-Sample t-Test

**Tests whether sample mean differs from known population mean**

**Formula:**
t = (x̄ - μ₀) / (s / √n)

**Example 5.2**: Hospital length of stay
- Known standard: μ = 5 days
- Sample: n=30, x̄=4.2 days, s=1.8 days
- H₀: μ = 5 days
- H₁: μ ≠ 5 days

**Calculations:**
t = (4.2 - 5) / (1.8 / √30) = (-0.8) / (1.8 / 5.477) = -0.8 / 0.329 = -2.43

**Critical value** for α=0.05, df=29: ±2.045
**p-value** = 0.021

**Decision**: |t| = 2.43 > 2.045, reject H₀
**Conclusion**: Hospital stay is significantly shorter than standard (p=0.021)

### 5.3.2 Two-Sample t-Test

**Tests whether two independent samples have different means**

**Formula:**
t = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂)

**Example 5.3**: Treatment comparison
- Treatment A: n=50, x̄=85, s=12
- Treatment B: n=45, x̄=91, s=11
- H₀: μA = μB
- H₁: μA ≠ μB

**Calculations:**
t = (85 - 91) / √(144/50 + 121/45) = (-6) / √(2.88 + 2.689) = -6 / √5.569 = -6 / 2.36 = -2.54

**Critical value** for α=0.05, df=93: ±1.986
**Decision**: |t| = 2.54 > 1.986, reject H₀
**Conclusion**: Significant difference between treatments (p=0.013)

### 5.3.3 Paired t-Test

**Tests whether paired samples have different means**

**Example 5.4**: Before-after treatment
Blood pressure before and after treatment for 20 patients:
- Mean difference = -8 mmHg
- SD of differences = 6 mmHg
- H₀: μdifference = 0
- H₁: μdifference ≠ 0

**Calculations:**
t = (-8 - 0) / (6 / √20) = -8 / (6 / 4.472) = -8 / 1.342 = -5.96

**Critical value** for α=0.05, df=19: ±2.093
**Decision**: |t| = 5.96 > 2.093, reject H₀
**Conclusion**: Treatment significantly reduces blood pressure (p<0.001)

## 5.4 Testing Proportions

### 5.4.1 One-Sample Test for Proportions

**Formula:**
z = (p - π₀) / √(π₀(1-π₀)/n)

**Example 5.5**: Vaccination rate
- National target: π₀ = 0.90
- Sample: n=200, 170 vaccinated (p=0.85)
- H₀: π = 0.90
- H₁: π ≠ 0.90

**Calculations:**
z = (0.85 - 0.90) / √(0.90×0.10/200) = (-0.05) / √(0.09/200) = -0.05 / √0.00045 = -0.05 / 0.0212 = -2.36

**Critical value**: ±1.96
**Decision**: |z| = 2.36 > 1.96, reject H₀
**Conclusion**: Vaccination rate significantly below target (p=0.018)

### 5.4.2 Two-Sample Test for Proportions

**Formula:**
z = (p₁ - p₂) / √(p(1-p)(1/n₁ + 1/n₂))

Where p = (x₁ + x₂)/(n₁ + n₂)

**Example 5.6**: Treatment success rates
- Treatment A: 45/100 = 0.45
- Treatment B: 60/120 = 0.50
- H₀: πA = πB
- H₁: πA ≠ πB

**Calculations:**
p = (45 + 60)/(100 + 120) = 105/220 = 0.477
SE = √(0.477×0.523 × (1/100 + 1/120)) = √(0.249 × 0.0183) = √0.00456 = 0.0675
z = (0.45 - 0.50) / 0.0675 = -0.05 / 0.0675 = -0.74

**Critical value**: ±1.96
**Decision**: |z| = 0.74 < 1.96, fail to reject H₀
**Conclusion**: No significant difference in success rates (p=0.46)

## 5.5 Chi-Square Tests

### 5.5.1 Chi-Square Test for Association

**Tests relationship between two categorical variables**

**Formula:**
χ² = Σ(Oᵢⱼ - Eᵢⱼ)² / Eᵢⱼ

**Example 5.7**: Smoking and lung cancer

|          | Cancer | No Cancer | Total |
|----------|--------|-----------|-------|
| Smokers  | 45     | 55        | 100   |
| Non-smokers | 5    | 95        | 100   |
| Total    | 50     | 150       | 200   |

**Expected values:**
- Smokers with cancer: (100×50)/200 = 25
- Smokers without cancer: (100×150)/200 = 75
- Non-smokers with cancer: (100×50)/200 = 25
- Non-smokers without cancer: (100×150)/200 = 75

**Calculations:**
χ² = (45-25)²/25 + (55-75)²/75 + (5-25)²/25 + (95-75)²/75
   = (400)/25 + (400)/75 + (400)/25 + (400)/75
   = 16 + 5.333 + 16 + 5.333 = 42.666

**Critical value** for α=0.05, df=1: 3.841
**Decision**: χ² = 42.666 > 3.841, reject H₀
**Conclusion**: Significant association between smoking and lung cancer (p<0.001)

### 5.5.2 Chi-Square Test for Goodness of Fit

**Tests whether observed frequencies match expected frequencies**

**Example 5.8**: Blood type distribution
Observed: A=60, B=50, AB=30, O=60 (n=200)
Expected: A=50, B=50, AB=20, O=80 (based on known population frequencies)

**Calculations:**
χ² = (60-50)²/50 + (50-50)²/50 + (30-20)²/20 + (60-80)²/80
   = 100/50 + 0/50 + 100/20 + 400/80
   = 2 + 0 + 5 + 5 = 12

**Critical value** for α=0.05, df=3: 7.815
**Decision**: χ² = 12 > 7.815, reject H₀
**Conclusion**: Blood type distribution differs from expected (p=0.007)

## 5.6 Non-Parametric Tests

### 5.6.1 Mann-Whitney U Test

**Non-parametric alternative to two-sample t-test**

**Example 5.9**: Comparing pain scores
- Treatment A: 3, 5, 7, 9, 11
- Treatment B: 2, 4, 6, 8, 10

**Calculations:**
Rank all values: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Ranks: B2, A3, B4, A5, B6, A7, B8, A9, B10, A11

U = n₁×n₂ + n₁(n₁+1)/2 - R₁ = 5×5 + 5×6/2 - 23 = 25 + 15 - 23 = 17

**Critical value** for α=0.05: U=2
**Decision**: U=17 > 2, fail to reject H₀
**Conclusion**: No significant difference in pain scores

### 5.6.2 Wilcoxon Signed-Rank Test

**Non-parametric alternative to paired t-test**

**Example 5.10**: Before-after blood pressure
Differences: -12, -8, -5, -3, -1, 1, 3, 5, 8, 12

**Calculations:**
Absolute differences: 12, 8, 5, 3, 1, 1, 3, 5, 8, 12
Ranks: 10, 7.5, 5, 3, 1.5, 1.5, 3, 5, 7.5, 10

Sum of positive ranks = 1.5 + 3 + 5 + 7.5 = 17
Sum of negative ranks = 10 + 7.5 + 5 + 3 + 1.5 = 27

**Test statistic**: Smaller sum = 17
**Critical value** for α=0.05, n=10: 8
**Decision**: 17 > 8, fail to reject H₀
**Conclusion**: No significant change in blood pressure

## 5.7 Multiple Testing and Error Rates

### 5.7.1 Type I and Type II Errors

**Type I Error (α)**: Rejecting null hypothesis when it's true
- False positive
- Probability = significance level (usually 0.05)

**Type II Error (β)**: Failing to reject null hypothesis when it's false
- False negative
- Probability = 1 - power

**Power**: Probability of correctly rejecting false null hypothesis
- Target power: 80-90% for most studies

### 5.7.2 Multiple Testing Problem

**Problem**: When conducting multiple tests, probability of at least one Type I error increases

**Example 5.11**: Testing 20 independent hypotheses at α=0.05
Probability of at least one false positive = 1 - (0.95)²⁰ = 1 - 0.358 = 0.642 or 64.2%

**Solutions:**
- **Bonferroni correction**: Divide α by number of tests (α=0.05/20=0.0025)
- **False Discovery Rate (FDR)**: Control proportion of false positives among rejections

## 5.8 Power Analysis

### 5.8.1 Factors Affecting Power

**Power increases with:**
- Larger sample size
- Larger effect size
- Lower variability
- Higher significance level
- One-tailed vs two-tailed tests

**Example 5.12**: Sample size for detecting treatment effect
- Want 80% power to detect 5 mmHg difference in blood pressure
- SD = 15 mmHg, α = 0.05, two-tailed

**Formula:**
n = 2 × (Zα/2 + Zβ)² × σ² / δ² = 2 × (1.96 + 0.84)² × 225 / 25 = 2 × (2.8)² × 9 = 2 × 7.84 × 9 = 141.12 ≈ 142 per group

### 5.8.2 Post-Hoc Power Analysis

**Calculate power of completed study**

**Example 5.13**: Study with non-significant result
- n=50 per group, effect size = 3 mmHg, SD=15 mmHg
- Actual power = 1 - β where β is probability of Type II error

**Calculations:**
δ/σ = 3/15 = 0.2 (small effect)
With n=50 per group, power ≈ 20%

**Conclusion**: Study was underpowered to detect small effect

## 5.9 Medical Applications of Hypothesis Testing

### 5.9.1 Clinical Trials

**Example 5.14**: Drug efficacy testing
- Phase III trial: New diabetes drug vs placebo
- Primary outcome: HbA1c reduction
- H₀: No difference in HbA1c reduction
- H₁: New drug produces greater reduction

**Statistical considerations:**
- Multiple outcomes require adjustment
- Interim analyses for early stopping
- Intention-to-treat vs per-protocol analysis

### 5.9.2 Diagnostic Testing

**Example 5.15**: New diagnostic test
- H₀: New test no better than existing test
- H₁: New test has higher sensitivity
- Compare sensitivity and specificity

### 5.9.3 Epidemiological Studies

**Example 5.16**: Risk factor analysis
- H₀: No association between exposure and disease
- H₁: Exposure increases disease risk
- Use chi-square or logistic regression

## 5.10 Common Mistakes in Hypothesis Testing

### 5.10.1 p-Value Misinterpretation

**Common misconception**: p-value is probability that null hypothesis is true

**Correct interpretation**: p-value is probability of observing data (or more extreme) if null hypothesis is true

### 5.10.2 Significance vs Clinical Importance

**Statistical significance** ≠ **clinical importance**
- Large sample can make tiny differences statistically significant
- Small sample can miss clinically important differences

### 5.10.3 Multiple Testing Without Correction

**Problem**: Conducting multiple tests without adjusting significance level
**Solution**: Pre-specify primary outcome, use correction methods

## 5.11 Exercises

### Exercise 5.1: One-Sample t-Test
A sample of 25 patients has mean blood glucose of 140 mg/dL with SD=20 mg/dL. Known population mean is 130 mg/dL. Test whether sample differs significantly from population at α=0.05.

### Exercise 5.2: Two-Sample Test for Proportions
Group A: 30/100 developed complications (30%)
Group B: 15/80 developed complications (18.8%)
Test whether complication rates differ significantly at α=0.05.

### Exercise 5.3: Chi-Square Test
Test association between gender and diabetes:

|        | Diabetes | No Diabetes | Total |
|--------|----------|-------------|-------|
| Male   | 25       | 75          | 100   |
| Female | 35       | 65          | 100   |
| Total  | 60       | 140         | 200   |

### Exercise 5.4: Power Analysis
Calculate sample size needed per group to detect 10% difference in success rates (from 60% to 70%) with 80% power and α=0.05.

## 5.12 Exercise Answers

### Answer 5.1: One-Sample t-Test
H₀: μ = 130
H₁: μ ≠ 130

t = (140 - 130) / (20 / √25) = 10 / (20/5) = 10/4 = 2.5

Critical value for α=0.05, df=24: ±2.064
|t| = 2.5 > 2.064, reject H₀
p-value ≈ 0.019

**Conclusion**: Sample mean significantly different from population mean

### Answer 5.2: Two-Sample Test for Proportions
H₀: πA = πB
H₁: πA ≠ πB

p = (30 + 15)/(100 + 80) = 45/180 = 0.25
SE = √(0.25×0.75 × (1/100 + 1/80)) = √(0.1875 × 0.0225) = √0.00422 = 0.065

z = (0.30 - 0.188) / 0.065 = 0.112 / 0.065 = 1.72

Critical value: ±1.96
|z| = 1.72 < 1.96, fail to reject H₀
p-value ≈ 0.085

**Conclusion**: No significant difference in complication rates

### Answer 5.3: Chi-Square Test
Expected values:
Male with diabetes: (100×60)/200 = 30
Male without diabetes: (100×140)/200 = 70
Female with diabetes: (100×60)/200 = 30
Female without diabetes: (100×140)/200 = 70

χ² = (25-30)²/30 + (75-70)²/70 + (35-30)²/30 + (65-70)²/70
   = 25/30 + 25/70 + 25/30 + 25/70
   = 0.833 + 0.357 + 0.833 + 0.357 = 2.38

Critical value for α=0.05, df=1: 3.841
χ² = 2.38 < 3.841, fail to reject H₀

**Conclusion**: No significant association between gender and diabetes

### Answer 5.4: Power Analysis
For proportions: n = (Zα/2 + Zβ)² × 2π(1-π) / δ²
Where π = (0.60 + 0.70)/2 = 0.65, δ = 0.10

n = (1.96 + 0.84)² × 2×0.65×0.35 / 0.10² = (2.8)² × 0.455 / 0.01 = 7.84 × 45.5 = 356.72 ≈ 357 per group

## 5.13 Chapter Quiz

1. What is the difference between Type I and Type II errors?
2. When would you use a one-tailed test?
3. What does a p-value of 0.03 mean?
4. Why is power analysis important?
5. What is the Bonferroni correction used for?

## 5.14 Quiz Answers

1. Type I: Rejecting true null hypothesis; Type II: Failing to reject false null hypothesis
2. When you have strong prior evidence about the direction of effect
3. 3% probability of observing data if null hypothesis is true
4. To ensure study can detect clinically important effects
5. To adjust significance level when conducting multiple tests

---

**Next Chapter Preview**: In Chapter 6, we'll explore tests for categorical data, including chi-square tests and measures of association.
