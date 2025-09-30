# Appendix B: Statistical Tables and Reference Guides

## B.1 Critical Values for Common Statistical Tests

### Standard Normal (Z) Distribution
| Confidence Level | Two-tailed | One-tailed |
|------------------|------------|------------|
| 90% | 1.645 | 1.282 |
| 95% | 1.960 | 1.645 |
| 99% | 2.576 | 2.326 |

### t-Distribution Critical Values (α = 0.05, two-tailed)
| df | t-value | df | t-value | df | t-value |
|----|---------|----|---------|----|---------|
| 1 | 12.706 | 10 | 2.228 | 30 | 2.042 |
| 2 | 4.303 | 15 | 2.131 | 40 | 2.021 |
| 3 | 3.182 | 20 | 2.086 | 50 | 2.009 |
| 4 | 2.776 | 25 | 2.060 | 100 | 1.984 |
| 5 | 2.571 |  | | ∞ | 1.960 |

### Chi-Square Distribution Critical Values (α = 0.05)
| df | χ²-value | df | χ²-value | df | χ²-value |
|----|----------|----|----------|----|----------|
| 1 | 3.841 | 10 | 18.307 | 20 | 31.410 |
| 2 | 5.991 | 15 | 24.996 | 25 | 37.652 |
| 3 | 7.815 | 16 | 26.296 | 30 | 43.773 |
| 4 | 9.488 | 17 | 27.587 | 40 | 55.758 |
| 5 | 11.070 | 18 | 28.869 | 50 | 67.505 |

### F-Distribution Critical Values (α = 0.05)
| df1 | df2=5 | df2=10 | df2=20 | df2=50 | df2=∞ |
|-----|-------|--------|--------|--------|-------|
| 1 | 6.61 | 5.64 | 5.29 | 5.08 | 4.96 |
| 2 | 5.79 | 5.05 | 4.76 | 4.58 | 4.46 |
| 3 | 5.41 | 4.74 | 4.47 | 4.31 | 4.19 |
| 4 | 5.19 | 4.56 | 4.31 | 4.15 | 4.04 |
| 5 | 5.05 | 4.44 | 4.20 | 4.05 | 3.94 |

## B.2 Sample Size Tables

### Sample Size for Means (95% CI, ±5% margin of error)
| Population SD | Sample Size | Population SD | Sample Size |
|---------------|-------------|---------------|-------------|
| 5 | 39 | 20 | 246 |
| 10 | 97 | 25 | 384 |
| 15 | 173 | 30 | 541 |

### Sample Size for Proportions (95% CI, ±5% margin of error)
| Expected Proportion | Sample Size | Expected Proportion | Sample Size |
|-------------------|-------------|-------------------|-------------|
| 0.10 | 139 | 0.40 | 369 |
| 0.20 | 246 | 0.50 | 385 |
| 0.30 | 323 | 0.50 | 385 |

### Sample Size for Comparing Two Means
| Effect Size | Power 80% | Power 90% | Power 95% |
|-------------|-----------|-----------|-----------|
| Small (0.2) | 394 | 527 | 697 |
| Medium (0.5) | 64 | 86 | 113 |
| Large (0.8) | 26 | 34 | 45 |

## B.3 Diagnostic Test Reference Values

### Sensitivity and Specificity Combinations
| Sensitivity | Specificity | LR+ | LR- | Interpretation |
|-------------|-------------|-----|-----|----------------|
| 0.95 | 0.95 | 19.0 | 0.053 | Excellent |
| 0.90 | 0.90 | 9.0 | 0.111 | Very Good |
| 0.85 | 0.85 | 5.7 | 0.176 | Good |
| 0.80 | 0.80 | 4.0 | 0.250 | Fair |
| 0.70 | 0.70 | 2.3 | 0.429 | Poor |

### AUC Interpretation
| AUC Range | Interpretation | Clinical Utility |
|-----------|----------------|------------------|
| 0.90-1.00 | Excellent | High |
| 0.80-0.90 | Very Good | Good |
| 0.70-0.80 | Good | Fair |
| 0.60-0.70 | Fair | Limited |
| 0.50-0.60 | Poor | Not useful |

## B.4 Quick Reference Formulas

### Descriptive Statistics
- **Mean**: x̄ = Σx/n
- **Median**: Middle value in ordered data
- **Mode**: Most frequent value
- **Variance**: s² = Σ(x - x̄)²/(n-1)
- **Standard Deviation**: s = √s²
- **Standard Error**: SE = s/√n

### Hypothesis Testing
- **Z-test**: Z = (x̄ - μ)/(σ/√n)
- **t-test**: t = (x̄ - μ)/(s/√n)
- **Chi-square**: χ² = Σ(O-E)²/E
- **Correlation**: r = Σ((x-x̄)(y-ȳ)) / √[Σ(x-x̄)²Σ(y-ȳ)²]

### Regression
- **Slope**: b = Σ((x-x̄)(y-ȳ)) / Σ(x-x̄)²
- **Intercept**: a = ȳ - b×x̄
- **R²**: Proportion of variance explained

### Sample Size
- **Means**: n = 2(Zα/2 + Zβ)²σ²/δ²
- **Proportions**: n = 2(Zα/2 + Zβ)²p(1-p)/δ²
- **Survival**: n = (Zα/2 + Zβ)² / (p×ln(HR)²)

## B.5 Effect Size Benchmarks

### Cohen's Guidelines for Effect Sizes
| Effect Size | d (Means) | r (Correlation) | η² (ANOVA) |
|-------------|-----------|-----------------|-------------|
| Small | 0.2 | 0.1 | 0.01 |
| Medium | 0.5 | 0.3 | 0.06 |
| Large | 0.8 | 0.5 | 0.14 |

### Clinical Significance Benchmarks
| Measure | Small Effect | Medium Effect | Large Effect |
|---------|--------------|----------------|--------------|
| **Blood Pressure** | 2-5 mmHg | 5-10 mmHg | >10 mmHg |
| **HbA1c** | 0.2-0.4% | 0.4-0.7% | >0.7% |
| **Weight Loss** | 1-2 kg | 2-5 kg | >5 kg |
| **Mortality** | RR 0.85-0.95 | RR 0.70-0.85 | RR <0.70 |

## B.6 Statistical Software Quick Reference

### R Quick Commands
```r
# Load data
data <- read.csv("file.csv")

# Summary statistics
summary(data$variable)
mean(data$variable); sd(data$variable)

# t-test
t.test(variable ~ group, data = data)

# Linear regression
model <- lm(outcome ~ predictor1 + predictor2, data = data)
summary(model)

# Survival analysis
library(survival)
km <- survfit(Surv(time, event) ~ group, data = data)
plot(km)
```

### SPSS Quick Commands
```spss
* Load data
GET FILE = 'file.sav'.

* Descriptive statistics
DESCRIPTIVES VARIABLES = bp age bmi.

* t-test
T-TEST GROUPS = treatment(1 2) /VARIABLES = outcome.

* Regression
REGRESSION /DEPENDENT outcome /METHOD = ENTER age bmi.
```

### Stata Quick Commands
```stata
* Load data
use "file.dta", clear

* Summary statistics
summarize variable

* t-test
ttest variable, by(group)

* Regression
regress outcome predictor1 predictor2
```

## B.7 Checklist for Study Design

### Randomized Controlled Trial Checklist
- [ ] Clear research question and hypothesis
- [ ] Appropriate study population defined
- [ ] Randomization method specified
- [ ] Blinding procedures described
- [ ] Sample size calculation provided
- [ ] Primary and secondary outcomes defined
- [ ] Statistical analysis plan pre-specified
- [ ] Ethical approval obtained
- [ ] Data monitoring committee established
- [ ] Publication plan outlined

### Observational Study Checklist
- [ ] Study design clearly stated (cohort/case-control)
- [ ] Exposure and outcome definitions clear
- [ ] Confounding variables identified
- [ ] Sample size justification provided
- [ ] Statistical methods appropriate
- [ ] Missing data handling described
- [ ] Sensitivity analyses planned
- [ ] Generalizability discussed

### Diagnostic Study Checklist
- [ ] Reference standard clearly defined
- [ ] Patient spectrum described
- [ ] Blinding procedures specified
- [ ] Reproducibility assessed
- [ ] ROC analysis performed
- [ ] Clinical utility discussed
- [ ] Cost-effectiveness considered

## B.8 Quality Assessment Tools

### Cochrane Risk of Bias Tool (RCTs)
**Selection Bias:**
- Random sequence generation
- Allocation concealment

**Performance Bias:**
- Blinding of participants and personnel

**Detection Bias:**
- Blinding of outcome assessment

**Attrition Bias:**
- Incomplete outcome data

**Reporting Bias:**
- Selective reporting

**Other Bias:**
- Other sources of bias

### Newcastle-Ottawa Scale (Observational Studies)
**Selection (0-4 stars):**
- Representativeness of exposed cohort
- Selection of non-exposed cohort
- Ascertainment of exposure
- Outcome not present at start

**Comparability (0-2 stars):**
- Comparability on confounding factors

**Outcome (0-3 stars):**
- Assessment of outcome
- Follow-up length
- Adequacy of follow-up

## B.9 Publication Guidelines

### CONSORT Checklist (RCTs)
- Title and abstract
- Introduction (background, objectives)
- Methods (trial design, participants, interventions, outcomes, sample size, randomization, blinding, statistical methods)
- Results (participant flow, recruitment, baseline data, numbers analyzed, outcomes, ancillary analyses, harms)
- Discussion (limitations, generalizability, interpretation)
- Other information (registration, protocol, funding)

### STROBE Checklist (Observational Studies)
- Title and abstract
- Introduction (background, objectives)
- Methods (study design, setting, participants, variables, data sources, bias, study size, quantitative variables)
- Results (participants, descriptive data, outcome data, main results, other analyses)
- Discussion (key results, limitations, interpretation, generalizability)
- Other information (funding)

### PRISMA Checklist (Systematic Reviews)
- Title, abstract, introduction
- Methods (protocol, eligibility criteria, information sources, search, study selection, data collection, data items, risk of bias, summary measures, synthesis, risk of bias, additional analyses)
- Results (study selection, study characteristics, risk of bias, results of individual studies, synthesis of results, risk of bias, additional analysis)
- Discussion (summary of evidence, limitations, conclusions)
- Funding

## B.10 Statistical Symbols and Notation

### Greek Letters
- α (alpha): Significance level, Type I error rate
- β (beta): Regression coefficient, Type II error rate
- χ² (chi-square): Chi-square test statistic
- δ (delta): Difference, effect size
- ε (epsilon): Error term
- η² (eta-squared): Effect size in ANOVA
- μ (mu): Population mean
- π (pi): Population proportion
- ρ (rho): Population correlation coefficient
- σ (sigma): Population standard deviation
- σ² (sigma-squared): Population variance
- τ (tau): Kendall's correlation coefficient
- θ (theta): Parameter of interest

### Latin Letters
- a: Intercept in regression
- b: Slope in regression
- CI: Confidence interval
- df: Degrees of freedom
- H₀: Null hypothesis
- H₁: Alternative hypothesis
- n: Sample size
- N: Population size
- OR: Odds ratio
- p: p-value, sample proportion
- r: Correlation coefficient
- RR: Relative risk
- s: Sample standard deviation
- SE: Standard error
- t: t-test statistic
- x̄: Sample mean
- z: Z-test statistic

### Mathematical Notation
- Σ: Summation
- ∏: Product
- √: Square root
- ≈: Approximately equal to
- ≠: Not equal to
- ≤: Less than or equal to
- ≥: Greater than or equal to
- ∝: Proportional to
- ∼: Distributed as
- |: Given that
- &: And
- ∨: Or

---

*These tables and reference guides provide quick access to critical values, formulas, and checklists commonly needed in medical statistics. Use them as quick reference during data analysis and study design.*
