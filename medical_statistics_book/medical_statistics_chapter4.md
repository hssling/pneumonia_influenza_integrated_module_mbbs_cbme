# Chapter 4: Sampling and Sampling Distributions

## 4.1 Introduction to Sampling

**Sampling** is the process of selecting a subset of individuals from a population to estimate characteristics of the whole population.

### Why Sample?
- **Cost-effective**: Cheaper than studying entire population
- **Time-efficient**: Faster data collection and analysis
- **Practical**: Often impossible to study entire populations
- **Accurate**: With proper methods, can provide precise estimates

**Example 4.1**: A health department wants to estimate vaccination coverage in a city of 10 million people. Instead of surveying everyone, they can survey 2,000 randomly selected individuals and get a reliable estimate.

## 4.2 Types of Sampling Methods

### 4.2.1 Probability Sampling

**Simple Random Sampling**: Every individual has equal chance of selection
- Like drawing names from a hat
- Most basic probability sampling method

**Systematic Sampling**: Select every kth individual from a list
- Order population by some criteria
- Choose starting point randomly, then every kth person

**Stratified Sampling**: Divide population into subgroups (strata), sample from each
- Ensures representation of important subgroups
- More precise estimates for subgroup comparisons

**Cluster Sampling**: Sample groups of individuals (clusters) rather than individuals
- Useful when population is geographically dispersed
- More practical but less precise than simple random sampling

### 4.2.2 Non-Probability Sampling

**Convenience Sampling**: Sample easily accessible individuals
- Quick and inexpensive
- Prone to bias
- Not generalizable

**Purposive Sampling**: Select individuals based on specific characteristics
- Useful for qualitative research
- Requires expert judgment

**Snowball Sampling**: Participants recruit other participants
- Useful for hard-to-reach populations
- May introduce bias

## 4.3 Sampling Error and Bias

### 4.3.1 Sampling Error

**Sampling error** is the difference between sample statistic and true population parameter due to random variation.

**Standard Error (SE)** measures sampling error:
- SE = σ / √n (for means)
- SE = √(p(1-p)/n) (for proportions)

**Example 4.2**: Mean blood pressure
- Population: μ = 120 mmHg, σ = 15 mmHg
- Sample of n=100: SE = 15 / √100 = 15/10 = 1.5 mmHg
- 95% of sample means within 120 ± 1.96×1.5 = 117.1 to 122.9 mmHg

### 4.3.2 Sources of Bias

**Selection Bias**: Systematic error in how participants are chosen
- Example: Only surveying hospital visitors for community health study

**Non-response Bias**: People who don't respond differ from those who do
- Example: Mail survey where healthy people are less likely to respond

**Measurement Bias**: Systematic error in data collection
- Example: Poorly calibrated blood pressure machine

**Confounding Bias**: Mixing of effects between exposure and outcome
- Example: Apparent link between coffee and heart disease actually due to smoking

## 4.4 Sampling Distributions

### 4.4.1 Distribution of Sample Means

**Central Limit Theorem**: As sample size increases, the distribution of sample means approaches normal distribution.

**Properties:**
- Mean of sample means = population mean (μ)
- Standard error = σ / √n
- Shape becomes normal regardless of population shape (for n ≥ 30)

**Example 4.3**: Population of patient ages
Population shape: Right-skewed (more young patients)
- Sample size n=5: Sample means still somewhat skewed
- Sample size n=30: Sample means approximately normal
- Sample size n=100: Sample means clearly normal

### 4.4.2 Distribution of Sample Proportions

**For large samples**, distribution of sample proportions is approximately normal.

**Mean** = population proportion (π)
**Standard Error** = √(π(1-π)/n)

**Example 4.4**: Vaccination coverage
- Population proportion vaccinated: π = 0.70
- Sample of n=400: SE = √(0.70×0.30/400) = √(0.21/400) = √0.000525 = 0.023
- 95% of sample proportions within 0.70 ± 1.96×0.023 = 0.655 to 0.745

## 4.5 Sample Size Determination

### 4.5.1 Sample Size for Estimating Means

**Formula for means:**
n = (Zα/2 × σ / E)²

Where:
- Zα/2 = Z-score for desired confidence level
- σ = population standard deviation
- E = desired margin of error

**Example 4.5**: Estimating mean blood glucose
- Want 95% confidence, margin of error ±5 mg/dL
- Population SD = 20 mg/dL
- Z for 95% = 1.96

n = (1.96 × 20 / 5)² = (39.2 / 5)² = 7.84² = 61.5 ≈ 62

### 4.5.2 Sample Size for Estimating Proportions

**Formula for proportions:**
n = (Zα/2)² × π(1-π) / E²

**Example 4.6**: Estimating disease prevalence
- Want 95% confidence, margin of error ±3%
- Estimated prevalence π = 0.10 (use 0.5 for maximum sample size)
- Z for 95% = 1.96

n = (1.96)² × 0.10 × 0.90 / (0.03)² = 3.8416 × 0.09 / 0.0009 = 0.3457 / 0.0009 = 384.1 ≈ 385

### 4.5.3 Factors Affecting Sample Size

**Larger sample size needed when:**
- Smaller margin of error desired
- Higher confidence level required
- Greater variability in population
- Smaller difference to detect (for hypothesis testing)

**Smaller sample size possible when:**
- Larger margin of error acceptable
- Lower confidence level sufficient
- Less variability in population

## 4.6 Confidence Intervals

### 4.6.1 Confidence Interval for Means

**Formula:**
CI = x̄ ± (tα/2 × SE)

Where:
- x̄ = sample mean
- tα/2 = t-value for desired confidence and degrees of freedom
- SE = s / √n (sample standard error)

**Example 4.7**: Mean hospital stay
Sample of 50 patients: x̄ = 4.2 days, s = 2.1 days

**95% CI:**
- SE = 2.1 / √50 = 2.1 / 7.07 = 0.297
- t-value for 95%, df=49 ≈ 2.01
- CI = 4.2 ± 2.01 × 0.297 = 4.2 ± 0.597 = 3.603 to 4.797 days

**Interpretation**: We are 95% confident that the true mean hospital stay is between 3.6 and 4.8 days.

### 4.6.2 Confidence Interval for Proportions

**Formula:**
CI = p ± (Zα/2 × SE)

Where:
- p = sample proportion
- SE = √(p(1-p)/n)

**Example 4.8**: Vaccination rate
Sample of 400 children: 320 vaccinated (p = 0.80)

**95% CI:**
- SE = √(0.80×0.20/400) = √(0.16/400) = √0.0004 = 0.02
- CI = 0.80 ± 1.96 × 0.02 = 0.80 ± 0.0392 = 0.761 to 0.839 or 76.1% to 83.9%

### 4.6.3 Confidence Interval for Difference Between Means

**Formula:**
CI = (x̄₁ - x̄₂) ± (tα/2 × SE)

Where SE = √(s₁²/n₁ + s₂²/n₂)

**Example 4.9**: Treatment comparison
- Treatment A: n=100, x̄=85, s=12
- Treatment B: n=120, x̄=82, s=11

**95% CI for difference:**
- Difference = 85 - 82 = 3
- SE = √(144/100 + 121/120) = √(1.44 + 1.008) = √2.448 = 1.565
- t-value for df≈200 ≈ 1.96
- CI = 3 ± 1.96 × 1.565 = 3 ± 3.067 = -0.067 to 6.067

**Interpretation**: 95% CI includes 0, so no significant difference between treatments.

## 4.7 Medical Sampling Applications

### 4.7.1 Survey Research

**Example 4.10**: National Health Survey
- Population: All adults in India (900 million)
- Sample: 100,000 adults using stratified multi-stage sampling
- Ensures representation by age, gender, region, urban/rural

**Sampling Design:**
- Stratify by state and urban/rural
- Select districts (clusters) within strata
- Select households within districts
- Select individuals within households

### 4.7.2 Clinical Trials

**Example 4.11**: Drug trial sample size
Testing new diabetes drug vs placebo

**Requirements:**
- 80% power to detect 10% difference in HbA1c
- Alpha = 0.05
- SD = 1.5% HbA1c
- Equal allocation to treatment and control

**Sample size per group:**
n = 2 × (Zα/2 + Zβ)² × σ² / δ² = 2 × (1.96 + 0.84)² × 2.25 / 1² = 2 × (2.8)² × 2.25 = 2 × 7.84 × 2.25 = 35.28 ≈ 36 per group

### 4.7.3 Quality Improvement

**Example 4.12**: Hospital infection rates
- Monthly sampling of 200 patient charts
- Track catheter-associated urinary tract infections (CAUTI)
- Use control charts to detect unusual patterns

**Statistical Process Control:**
- Upper control limit = mean + 3 SD
- Lower control limit = mean - 3 SD
- Values outside limits signal potential problems

## 4.8 Sampling in Epidemiology

### 4.8.1 Disease Surveillance

**Sentinel Surveillance**: Monitor specific sites for disease trends
- Selected hospitals report notifiable diseases
- Early warning system for outbreaks

**Population-based Surveillance**: Random sample of population
- More representative but resource-intensive
- Used for prevalence estimation

### 4.8.2 Outbreak Investigations

**Case-control studies in outbreaks:**
- Sample cases (affected individuals)
- Sample controls (unaffected individuals)
- Compare exposure histories

**Cohort studies in outbreaks:**
- Follow exposed and unexposed groups
- Monitor for disease development

## 4.9 Common Sampling Mistakes

### 4.9.1 Volunteer Bias

**Problem**: Volunteers differ from general population
- Healthier, more motivated individuals volunteer
- Results not generalizable

**Solution**: Use probability sampling methods

### 4.9.2 Non-response Bias

**Problem**: Non-respondents differ from respondents
- Busy people don't complete surveys
- Sick people may be overrepresented

**Solution**: Follow-up reminders, incentives, multiple contact methods

### 4.9.3 Sampling Frame Issues

**Problem**: Sampling frame doesn't match target population
- Using phone book excludes people without landlines
- Using hospital records misses people not seeking care

**Solution**: Use multiple frames, post-stratification weighting

## 4.10 Exercises

### Exercise 4.1: Sample Size for Means
Calculate sample size needed to estimate mean blood pressure with:
- 95% confidence
- Margin of error ±3 mmHg
- Population SD = 15 mmHg

### Exercise 4.2: Sample Size for Proportions
Calculate sample size needed to estimate vaccination coverage with:
- 95% confidence
- Margin of error ±5%
- Expected coverage = 80%

### Exercise 4.3: Confidence Interval
A sample of 225 patients showed 180 had controlled diabetes (80%).
Calculate 95% confidence interval for true proportion.

### Exercise 4.4: Sampling Methods
For each scenario, recommend the most appropriate sampling method and explain why:

1. Estimating prevalence of hypertension in a large city
2. Studying patient satisfaction in a hospital
3. Investigating a disease outbreak in a village
4. Evaluating a new treatment for a rare disease

## 4.11 Exercise Answers

### Answer 4.1: Sample Size for Means
n = (Zα/2 × σ / E)² = (1.96 × 15 / 3)² = (29.4 / 3)² = 9.8² = 96.04 ≈ 97

### Answer 4.2: Sample Size for Proportions
n = (Zα/2)² × π(1-π) / E² = (1.96)² × 0.80 × 0.20 / (0.05)² = 3.8416 × 0.16 / 0.0025 = 0.6147 / 0.0025 = 245.88 ≈ 246

### Answer 4.3: Confidence Interval
p = 0.80, n = 225
SE = √(0.80×0.20/225) = √(0.16/225) = √0.000711 = 0.0267
95% CI = 0.80 ± 1.96 × 0.0267 = 0.80 ± 0.0523 = 0.748 to 0.852 or 74.8% to 85.2%

### Answer 4.4: Sampling Methods
1. **Stratified random sampling** - Ensures representation of different socioeconomic groups and geographic areas in the city
2. **Systematic sampling** - Simple and efficient for hospital patient list, every 10th patient provides good representation
3. **Cluster sampling** - Village is a natural cluster, more practical than trying to sample individuals across wide area
4. **Purposive sampling** - Rare disease requires finding specific cases, probability sampling would be inefficient

## 4.12 Chapter Quiz

1. What is the difference between probability and non-probability sampling?
2. What factors increase required sample size?
3. What does the Central Limit Theorem tell us about sample means?
4. How do you interpret a 95% confidence interval?
5. Name three common sources of bias in sampling

## 4.13 Quiz Answers

1. Probability sampling gives every individual known chance of selection; non-probability does not
2. Smaller margin of error, higher confidence level, greater population variability
3. Sample means become normally distributed as sample size increases
4. If we repeated the sampling many times, 95% of intervals would contain the true population parameter
5. Selection bias, non-response bias, measurement bias

---

**Next Chapter Preview**: In Chapter 5, we'll learn about confidence intervals and hypothesis testing, the foundation of statistical inference in medical research.
