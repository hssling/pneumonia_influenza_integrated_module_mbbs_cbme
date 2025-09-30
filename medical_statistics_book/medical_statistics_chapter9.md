# Chapter 9: Analysis of Variance (ANOVA)

## 9.1 Introduction to ANOVA

**Analysis of Variance (ANOVA)** compares means across three or more groups to determine if there are statistically significant differences.

### Why Use ANOVA?
- **Multiple group comparisons**: More efficient than multiple t-tests
- **Controls Type I error**: Maintains overall significance level
- **Provides additional information**: Which groups differ from each other

**Example 9.1**: Comparing treatment outcomes
- 4 different treatments for hypertension
- Want to know if any treatment works better than others
- ANOVA tells us if differences exist between treatments

## 9.2 One-Way ANOVA

### 9.2.1 Basic Concepts

**One-way ANOVA** tests for differences in means across k independent groups

**Hypotheses:**
- H₀: μ₁ = μ₂ = μ₃ = ... = μₖ (all means equal)
- H₁: At least one mean differs from others

**Key Assumptions:**
- Independent observations
- Normally distributed outcome within each group
- Equal variances across groups (homoscedasticity)

### 9.2.2 ANOVA Table

| Source | Sum of Squares | df | Mean Square | F | p-value |
|--------|----------------|----|-------------|---|---------|
| Between | SSB | k-1 | MSB = SSB/(k-1) | MSB/MSE |       |
| Within  | SSW | n-k | MSE = SSW/(n-k) |           |       |
| Total   | SST | n-1 |                 |           |       |

**Example 9.2**: Blood pressure by treatment group

| Treatment | n | Mean BP | SD |
|-----------|---|---------|----|
| A         | 25 | 145    | 12 |
| B         | 25 | 140    | 11 |
| C         | 25 | 138    | 13 |
| D         | 25 | 142    | 12 |

**Calculations:**
- Overall mean = 141.25
- SSB = 25×(145-141.25)² + 25×(140-141.25)² + 25×(138-141.25)² + 25×(142-141.25)² = 25×(3.75)² × 4 = 25×14.0625×4 = 1406.25
- SSW = (25-1)×12² + (25-1)×11² + (25-1)×13² + (25-1)×12² = 24×(144 + 121 + 169 + 144) = 24×578 = 13,872

**F = MSB/MSE = 1406.25/3 ÷ 13872/96 = 468.75 ÷ 144.5 = 3.24**

**Critical F-value** for α=0.05, df=(3,96): 2.70
**F = 3.24 > 2.70, reject H₀ (p=0.025)**

## 9.3 Post-Hoc Tests

### 9.3.1 When to Use Post-Hoc Tests

**Use when:**
- ANOVA shows significant differences
- Want to know which specific groups differ
- Need to control for multiple comparisons

### 9.3.2 Tukey's Honestly Significant Difference (HSD)

**Controls family-wise error rate**

**Formula:**
HSD = q × √(MSE/n)

Where q is studentized range statistic

**Example 9.3**: Comparing treatment means
- Group A (145) vs B (140): Difference = 5
- Group A (145) vs C (138): Difference = 7
- Group B (140) vs C (138): Difference = 2

**HSD for α=0.05 = 3.8**

**Significant differences:**
- A vs C: 7 > 3.8
- A vs B: 5 > 3.8
- B vs C: 2 < 3.8 (not significant)

### 9.3.3 Bonferroni Correction

**Adjusts p-values for multiple comparisons**

**Formula:**
Adjusted α = α / number of comparisons

**Example 9.4**: 6 pairwise comparisons
- Original α = 0.05
- Adjusted α = 0.05/6 = 0.0083
- Use t-test with α = 0.0083 for each comparison

## 9.4 Two-Way ANOVA

### 9.4.1 Basic Concepts

**Two-way ANOVA** examines effects of two independent variables and their interaction

**Main Effects**: Effect of each independent variable alone
**Interaction Effect**: Combined effect of both variables

**Example 9.5**: Treatment and gender effects on blood pressure

|          | Treatment A | Treatment B | Treatment C |
|----------|-------------|-------------|-------------|
| **Male**   | 140         | 135         | 138         |
| **Female** | 145         | 142         | 136         |

**Questions:**
- Does treatment affect blood pressure?
- Does gender affect blood pressure?
- Does treatment effect differ by gender?

### 9.4.2 ANOVA Table for Two-Way

| Source          | SS | df | MS | F |
|-----------------|----|----|----|---|
| Treatment       | SSA | a-1 | MSA | MSA/MSE |
| Gender          | SSB | b-1 | MSB | MSB/MSE |
| Interaction     | SSAB | (a-1)(b-1) | MSAB | MSAB/MSE |
| Error           | SSE | n-ab | MSE |       |
| Total           | SST | n-1 |     |       |

## 9.5 Repeated Measures ANOVA

### 9.5.1 When to Use

**Use when:**
- Same subjects measured multiple times
- Want to control for individual differences
- More powerful than independent groups design

**Example 9.6**: Blood pressure measured before treatment, after 1 month, after 3 months, after 6 months

**Advantages:**
- Controls for between-subject variability
- Requires fewer subjects
- Can detect smaller effects

### 9.5.2 Sphericity Assumption

**Requires equal correlations between all pairs of measurements**

**Mauchly's Test**: Tests sphericity assumption
**Greenhouse-Geisser Correction**: Adjusts degrees of freedom when sphericity violated

## 9.6 Non-Parametric Alternatives

### 9.6.1 Kruskal-Wallis Test

**Non-parametric alternative to one-way ANOVA**

**Use when:**
- Data not normally distributed
- Variances not equal
- Small sample sizes

**Formula:**
H = (12/n(n+1)) × Σ(Rᵢ²/nᵢ) - 3(n+1)

**Example 9.7**: Comparing pain scores across treatments
- Treatment A: 3, 5, 7, 4, 6
- Treatment B: 2, 4, 6, 3, 5
- Treatment C: 1, 3, 5, 2, 4

**H = 6.4, p = 0.041**
**Conclusion**: Significant difference in pain scores between treatments

### 9.6.2 Friedman Test

**Non-parametric alternative to repeated measures ANOVA**

**Use for:**
- Ordinal or non-normal data
- Repeated measurements on same subjects

## 9.7 Effect Size in ANOVA

### 9.7.1 Eta-Squared (η²)

**Formula:**
η² = SSB / SST

**Interpretation:**
- η² = 0.01: Small effect
- η² = 0.06: Medium effect
- η² = 0.14: Large effect

**Example 9.8**: Treatment effect on blood pressure
- SSB = 1406.25, SST = 1406.25 + 13872 = 15278.25
- η² = 1406.25 / 15278.25 = 0.092 (medium effect)

### 9.7.2 Omega-Squared (ω²)

**Less biased effect size estimate**

**Formula:**
ω² = (SSB - (k-1)×MSE) / (SST + MSE)

## 9.8 Medical Applications of ANOVA

### 9.8.1 Clinical Trials

**Example 9.9**: Comparing multiple treatments
- Phase II trial comparing 4 different doses of new drug
- Primary outcome: Reduction in HbA1c
- ANOVA to test for dose-response relationship
- Post-hoc tests to identify optimal dose

### 9.8.2 Epidemiological Studies

**Example 9.10**: Comparing disease rates across regions
- 5 different states with different health policies
- Compare diabetes prevalence rates
- ANOVA to test for regional differences
- Control for age, gender, socioeconomic factors

### 9.8.3 Quality Improvement

**Example 9.11**: Comparing hospital performance
- 10 hospitals in a region
- Compare patient satisfaction scores
- ANOVA to identify hospitals with significantly different performance
- Target quality improvement efforts

## 9.9 Sample Size for ANOVA

### 9.9.1 Factors Affecting Sample Size

**Larger samples needed when:**
- More groups being compared
- Smaller effect size to detect
- Higher desired power
- Lower significance level
- Greater within-group variability

**Formula:**
n = (2σ²(Zα/2 + Zβ)²) / δ² × (k / (k-1))

Where:
- k = number of groups
- δ = minimum detectable difference between means

**Example 9.12**: Comparing 4 treatment groups
- Want to detect 5 mmHg difference in blood pressure
- SD = 12 mmHg, 80% power, α=0.05

n = (2×144×(1.96 + 0.84)²) / 25 × (4/3) = (288×7.84) / 25 × 1.333 = 2258 / 25 × 1.333 = 90.32 × 1.333 ≈ 120 per group

### 9.9.2 Power Analysis

**Post-hoc power analysis:**
- Calculate power of completed study
- Determine if study was adequately powered

**A priori power analysis:**
- Calculate required sample size before starting study

## 9.10 Common Mistakes in ANOVA

### 9.10.1 Violation of Assumptions

**Problem**: ANOVA sensitive to assumption violations

**Solutions:**
- Check normality with Shapiro-Wilk test
- Check homogeneity of variance with Levene's test
- Use non-parametric alternatives when assumptions violated
- Transform data if possible

### 9.10.2 Multiple t-Tests Instead of ANOVA

**Problem**: Increases Type I error rate

**Example**: Comparing 4 groups with t-tests
- 6 pairwise comparisons
- Family-wise error rate = 1 - (0.95)⁶ = 0.265 or 26.5%

**Solution**: Use ANOVA first, then post-hoc tests

### 9.10.3 Interpreting Non-Significant ANOVA

**Problem**: Concluding all groups are equal when ANOVA is non-significant

**Reality**: May be no difference, or study underpowered to detect existing differences

**Solution**: Calculate and report power of study

## 9.11 Advanced ANOVA Designs

### 9.11.1 ANCOVA (Analysis of Covariance)

**Combines ANOVA with regression**

**Uses:**
- Control for confounding variables
- Increase statistical power
- More precise estimates

**Example 9.13**: Treatment comparison controlling for age
- Outcome: Treatment success
- Factor: Treatment type
- Covariate: Patient age

**Model:**
Success = Treatment + Age + Treatment×Age + ε

### 9.11.2 MANOVA (Multivariate ANOVA)

**Analyzes multiple outcome variables simultaneously**

**Use when:**
- Multiple related outcomes
- Want to control overall Type I error
- Interested in combination of outcomes

**Example 9.14**: Multiple outcomes in diabetes trial
- Outcomes: HbA1c, blood pressure, weight, quality of life
- Single test for overall treatment effect across all outcomes

## 9.12 Exercises

### Exercise 9.1: One-Way ANOVA
A study compares length of hospital stay across three wards:

| Ward A | Ward B | Ward C |
|--------|--------|--------|
| 5      | 4      | 3      |
| 7      | 6      | 5      |
| 6      | 5      | 4      |
| 8      | 7      | 6      |
| 5      | 4      | 3      |

1. Calculate the ANOVA table
2. Test for significant differences at α=0.05
3. Calculate effect size (η²)

### Exercise 9.2: Post-Hoc Tests
For the data in Exercise 9.1, if ANOVA is significant:
1. Perform Tukey's HSD test
2. Which wards differ significantly?

### Exercise 9.3: Two-Way ANOVA
A study examines effects of treatment (A, B) and gender (Male, Female) on blood pressure reduction:

|          | Treatment A | Treatment B |
|----------|-------------|-------------|
| **Male**   | 12, 15, 14, 16 | 10, 13, 11, 14 |
| **Female** | 18, 20, 19, 17 | 16, 18, 15, 17 |

1. Calculate main effects and interaction
2. Interpret the results

### Exercise 9.4: Non-Parametric Alternative
The data in Exercise 9.1 may not be normally distributed. Perform Kruskal-Wallis test and compare results to ANOVA.

## 9.13 Exercise Answers

### Answer 9.1: One-Way ANOVA
**Means**: Ward A = 6.2, Ward B = 5.2, Ward C = 4.2
**Overall mean = 5.2**

**SSB = 5×((6.2-5.2)² + (5.2-5.2)² + (4.2-5.2)²) = 5×(1 + 0 + 1) = 10**
**SSW = (5-1)×(2² + 1.6² + 1.2²) = 4×(4 + 2.56 + 1.44) = 4×8 = 32**
**SST = SSB + SSW = 42**

**MSB = 10/2 = 5**
**MSE = 32/12 = 2.667**
**F = 5/2.667 = 1.875**

**Critical F for α=0.05, df=(2,12) = 3.89**
**F = 1.875 < 3.89, fail to reject H₀**

**η² = SSB/SST = 10/42 = 0.238 (large effect)**

### Answer 9.2: Post-Hoc Tests
**HSD = q√(MSE/n) = 3.77√(2.667/5) = 3.77√0.533 = 3.77×0.73 = 2.75**

**Differences:**
- A vs B: 6.2 - 5.2 = 1.0 < 2.75 (not significant)
- A vs C: 6.2 - 4.2 = 2.0 < 2.75 (not significant)
- B vs C: 5.2 - 4.2 = 1.0 < 2.75 (not significant)

**No significant pairwise differences**

### Answer 9.3: Two-Way ANOVA
**Main effect of treatment:**
- Treatment A: (12+15+14+16+18+20+19+17)/8 = 131/8 = 16.375
- Treatment B: (10+13+11+14+16+18+15+17)/8 = 114/8 = 14.25
- Difference = 2.125

**Main effect of gender:**
- Male: (12+15+14+16+10+13+11+14)/8 = 105/8 = 13.125
- Female: (18+20+19+17+16+18+15+17)/8 = 140/8 = 17.5
- Difference = 4.375

**Interaction**: Treatment effect differs by gender (females benefit more from treatment)

### Answer 9.4: Kruskal-Wallis Test
**Ranks:**
Ward A: 5,7,6,8,5 → ranks 11,13,12,14,11 (average rank 12.2)
Ward B: 4,6,5,7,4 → ranks 8,12,11,13,8 (average rank 10.4)
Ward C: 3,5,4,6,3 → ranks 4,11,8,12,4 (average rank 7.8)

**H = (12/15×14) × (12.2²/5 + 10.4²/5 + 7.8²/5) - 3×16 = (12/210) × (74.4 + 54.0 + 30.4) - 48 = 0.057 × 158.8 - 48 = 9.05 - 48 = -38.95**

**Wait, calculation error. Let me recalculate properly:**

**H = 12/(15×14) × (5×12.2² + 5×10.4² + 5×7.8²) - 3×16**
**= 12/210 × (5×148.84 + 5×108.16 + 5×60.84) - 48**
**= 0.0571 × (744.2 + 540.8 + 304.2) - 48**
**= 0.0571 × 1589.2 - 48 = 90.7 - 48 = 42.7**

**This is not right either. Let me use correct formula:**

**H = (12/n(n+1)) × Σ(Rᵢ²/nᵢ) - 3(n+1)**
**= (12/15×16) × (12.2²/5 + 10.4²/5 + 7.8²/5) - 3×16**
**= (12/240) × (148.84/5 + 108.16/5 + 60.84/5) - 48**
**= 0.05 × (29.768 + 21.632 + 12.168) - 48**
**= 0.05 × 63.568 - 48 = 3.178 - 48 = -44.822**

**I need to use the standard formula correctly. The Kruskal-Wallis test statistic is:**

**H = [12/(n(n+1))] × Σ(Rᵢ²/nᵢ) - 3(n+1)**

**Where Rᵢ are the rank sums:**

**Rank sum A = 11+13+12+14+11 = 61, average rank = 61/5 = 12.2**
**Rank sum B = 8+12+11+13+8 = 52, average rank = 52/5 = 10.4**
**Rank sum C = 4+11+8+12+4 = 39, average rank = 39/5 = 7.8**

**H = [12/(15×16)] × (61²/5 + 52²/5 + 39²/5) - 3×16**
**= (12/240) × (3721/5 + 2704/5 + 1521/5) - 48**
**= 0.05 × (744.2 + 540.8 + 304.2) - 48**
**= 0.05 × 1589.2 - 48 = 79.46 - 48 = 31.46**

**Critical value for α=0.05, df=2 = 5.99**
**H = 31.46 > 5.99, reject H₀**

**Conclusion**: Significant difference in length of stay between wards (non-parametric test agrees with ANOVA conclusion)**

## 9.14 Chapter Quiz

1. What is the main advantage of ANOVA over multiple t-tests?
2. When would you use a post-hoc test?
3. What assumption must be met for repeated measures ANOVA?
4. What does eta-squared measure?
5. Why might you choose Kruskal-Wallis over ANOVA?

## 9.15 Quiz Answers

1. Controls overall Type I error rate and is more efficient
2. When ANOVA shows significant differences and you want to know which groups differ
3. Sphericity (equal correlations between all measurement pairs)
4. Proportion of variance explained by the independent variable
5. When data are not normally distributed or variances are unequal

---

**Next Chapter Preview**: In Chapter 10, we'll explore non-parametric tests for data that don't meet normality assumptions.
