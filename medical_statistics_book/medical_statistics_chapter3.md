# Chapter 3: Probability and Probability Distributions

## 3.1 Basic Probability Concepts

**Probability** is the likelihood that an event will occur, expressed as a number between 0 and 1.

### 3.1.1 Definitions and Rules

**Key Terms:**
- **Experiment**: Any process that produces an outcome (e.g., tossing a coin, measuring blood pressure)
- **Outcome**: Result of an experiment (e.g., heads, tails)
- **Event**: One or more outcomes of interest (e.g., getting heads)
- **Sample Space**: All possible outcomes

**Probability Rules:**
1. **Range**: 0 ≤ P(event) ≤ 1
2. **Certainty**: P(certain event) = 1
3. **Impossibility**: P(impossible event) = 0
4. **Addition Rule**: P(A or B) = P(A) + P(B) - P(A and B)
5. **Multiplication Rule**: P(A and B) = P(A) × P(B|A)

### 3.1.2 Types of Probability

**Classical Probability**: Based on equally likely outcomes
- P(heads) = 1/2 for fair coin
- P(rolling 6) = 1/6 for fair die

**Empirical Probability**: Based on observed data
- P(rain tomorrow) = (number of rainy days) ÷ (total days observed)
- P(heart attack) = (number of cases) ÷ (population at risk)

**Subjective Probability**: Based on personal judgment
- P(success of new treatment) based on expert opinion

## 3.2 Probability in Medical Contexts

### 3.2.1 Diagnostic Testing

**Example 3.1**: Mammography screening for breast cancer
- Sensitivity = P(positive test | cancer) = 0.85
- Specificity = P(negative test | no cancer) = 0.90
- Prevalence = P(cancer) = 0.01

**Positive Predictive Value** = P(cancer | positive test)
= (Sensitivity × Prevalence) ÷ (Sensitivity × Prevalence + (1-Specificity) × (1-Prevalence))
= (0.85 × 0.01) ÷ (0.85 × 0.01 + 0.10 × 0.99) = 0.0085 ÷ 0.1075 = 0.079 or 7.9%

### 3.2.2 Treatment Outcomes

**Example 3.2**: Success rates of two treatments
- Treatment A: 80% success rate (P(success) = 0.80)
- Treatment B: 70% success rate (P(success) = 0.70)

If a patient succeeds, what's the probability they received Treatment A?

**Bayesian Approach:**
P(A | success) = P(success | A) × P(A) ÷ P(success)
Assuming equal probability of receiving either treatment:
P(A | success) = 0.80 × 0.50 ÷ (0.80 × 0.50 + 0.70 × 0.50) = 0.40 ÷ 0.75 = 0.533 or 53.3%

## 3.3 Discrete Probability Distributions

### 3.3.1 Binomial Distribution

**Binomial** experiments have:
- Fixed number of trials (n)
- Two possible outcomes (success/failure)
- Constant probability of success (p)
- Independent trials

**Formula:**
P(X = k) = C(n,k) × pᵏ × (1-p)ⁿ⁻ᵏ

Where C(n,k) = n! / (k!(n-k)!) is the combination

**Example 3.3**: Side effects of medication
A drug causes side effects in 20% of patients. If 5 patients take the drug, what's the probability exactly 2 experience side effects?

P(X=2) = C(5,2) × 0.20² × 0.80³ = 10 × 0.04 × 0.512 = 0.2048 or 20.5%

**Mean and Variance:**
- Mean = n × p
- Variance = n × p × (1-p)

For this example: Mean = 5 × 0.20 = 1, Variance = 5 × 0.20 × 0.80 = 0.8

### 3.3.2 Poisson Distribution

**Poisson** distribution models rare events occurring randomly over time or space.

**Formula:**
P(X = k) = (e⁻ᵅ × ᵅᵏ) / k!

Where ᵅ is the average rate (mean)

**Example 3.4**: Hospital admissions
A hospital emergency department receives an average of 3 admissions per hour. What's the probability of exactly 5 admissions in one hour?

P(X=5) = (e⁻³ × 3⁵) / 5! = (0.0498 × 243) / 120 = 12.09 / 120 = 0.1008 or 10.1%

**When to use Poisson:**
- Events occur independently
- Rate is constant
- Events are rare
- Time/space is continuous

## 3.4 Continuous Probability Distributions

### 3.4.1 Normal Distribution

**Normal** (Gaussian) distribution is symmetric, bell-shaped, defined by mean (μ) and standard deviation (σ).

**Key Properties:**
- Mean = Median = Mode
- 68% of data within μ ± 1σ
- 95% within μ ± 2σ
- 99.7% within μ ± 3σ

**Standard Normal Distribution**: Mean = 0, SD = 1
- Z-score = (x - μ) / σ
- Used to find probabilities and percentiles

**Example 3.5**: Birth weights
Birth weights are normally distributed with μ = 3.3 kg, σ = 0.5 kg.

What percentage of babies weigh between 2.8 kg and 3.8 kg?

Z-scores:
Z₁ = (2.8 - 3.3) / 0.5 = -1.0
Z₂ = (3.8 - 3.3) / 0.5 = 1.0

Area between Z = -1.0 and Z = 1.0 = 68%

### 3.4.2 Standard Normal Table Usage

**Example 3.6**: Find probability that birth weight > 3.8 kg
Z = (3.8 - 3.3) / 0.5 = 1.0
P(Z > 1.0) = 1 - 0.8413 = 0.1587 or 15.9%

**Finding Percentiles:**
What birth weight corresponds to the 10th percentile?

Find Z where P(Z < z) = 0.10, Z = -1.28
x = μ + Zσ = 3.3 + (-1.28)×0.5 = 3.3 - 0.64 = 2.66 kg

## 3.5 Medical Applications of Probability Distributions

### 3.5.1 Clinical Measurements

**Example 3.7**: Blood pressure distribution
Systolic blood pressure in healthy adults: μ = 120 mmHg, σ = 15 mmHg

**Questions:**
1. What percentage have BP > 140 mmHg?
   Z = (140-120)/15 = 1.33
   P(Z > 1.33) = 1 - 0.9082 = 0.0918 or 9.2%

2. What BP value is the 95th percentile?
   Find Z where P(Z < z) = 0.95, Z = 1.645
   x = 120 + 1.645×15 = 120 + 24.7 = 144.7 mmHg

### 3.5.2 Laboratory Values

**Example 3.8**: Serum cholesterol
Total cholesterol in adults: μ = 200 mg/dL, σ = 40 mg/dL

**Reference Ranges:**
- Normal: < 200 mg/dL
- Borderline high: 200-239 mg/dL
- High: ≥ 240 mg/dL

What percentage fall into each category?

**Normal (< 200):**
Z = (200-200)/40 = 0
P(Z < 0) = 0.50 or 50%

**Borderline high (200-239):**
Z₁ = 0, Z₂ = (239-200)/40 = 0.975
P(0 < Z < 0.975) = 0.9082 - 0.5000 = 0.4082 or 40.8%

**High (≥ 240):**
Z = (240-200)/40 = 1.0
P(Z > 1.0) = 0.1587 or 15.9%

### 3.5.3 Epidemiology and Disease Occurrence

**Example 3.9**: Disease incidence
Hospital sees average of 2 new diabetes cases per week.

**Questions:**
1. Probability of exactly 3 cases next week?
   P(X=3) = (e⁻² × 2³) / 3! = (0.1353 × 8) / 6 = 1.0824 / 6 = 0.1804 or 18.0%

2. Probability of at least 1 case next week?
   P(X ≥ 1) = 1 - P(X=0) = 1 - (e⁻²) = 1 - 0.1353 = 0.8647 or 86.5%

## 3.6 Central Limit Theorem

**Central Limit Theorem (CLT)**: The distribution of sample means approaches normal distribution as sample size increases, regardless of the shape of the original population.

**Key Points:**
- Works for n ≥ 30 (large samples)
- Mean of sample means = population mean
- Standard error = σ / √n
- Enables use of normal distribution for inference

**Example 3.10**: Blood glucose in population
Population: μ = 100 mg/dL, σ = 20 mg/dL

**Sample of n=25:**
- Mean of sample means = 100 mg/dL
- Standard error = 20 / √25 = 20/5 = 4 mg/dL
- 95% of sample means between 100 ± 1.96×4 = 92.2 to 107.8 mg/dL

## 3.7 Probability and Medical Decision Making

### 3.7.1 Risk Assessment

**Absolute Risk**: Probability of event occurring
- 5-year risk of heart attack = 0.15 (15%)

**Relative Risk**: Ratio of probabilities
- RR = P(event | exposure) ÷ P(event | no exposure)
- RR = 0.15 ÷ 0.05 = 3.0 (3 times higher risk)

**Attributable Risk**: Difference in probabilities
- AR = 0.15 - 0.05 = 0.10 (10% of cases attributable to exposure)

### 3.7.2 Clinical Prediction Rules

**Example 3.11**: Wells score for DVT
- Score 0-2: Low probability (3%)
- Score 3-8: Moderate probability (17%)
- Score >8: High probability (75%)

**Decision Threshold:**
- If pretest probability > 10%, order D-dimer test
- If D-dimer positive, probability increases to 25-30%

## 3.8 Exercises

### Exercise 3.1: Basic Probability
A test for a disease has sensitivity 90% and specificity 85%. Disease prevalence is 5%.

1. What is the probability of a positive test result?
2. What is the positive predictive value?
3. What is the negative predictive value?

### Exercise 3.2: Binomial Distribution
A vaccine is 70% effective. If 10 people are vaccinated:

1. What is the probability exactly 8 are protected?
2. What is the probability at least 8 are protected?
3. What is the expected number protected?

### Exercise 3.3: Normal Distribution
Hemoglobin levels in healthy adults: μ = 14 g/dL, σ = 1.5 g/dL

1. What percentage have levels between 12.5 and 15.5 g/dL?
2. What hemoglobin level is the 5th percentile?
3. What is the probability of hemoglobin > 17 g/dL?

### Exercise 3.4: Poisson Distribution
A clinic sees an average of 4 new patients with hypertension per day.

1. What is the probability of exactly 6 new cases tomorrow?
2. What is the probability of at most 2 new cases?
3. What is the probability of more than 8 new cases?

## 3.9 Exercise Answers

### Answer 3.1: Basic Probability
1. **Probability of positive test**:
   P(+) = Sensitivity × Prevalence + (1-Specificity) × (1-Prevalence)
   = 0.90 × 0.05 + 0.15 × 0.95 = 0.045 + 0.1425 = 0.1875 or 18.8%

2. **Positive Predictive Value**:
   PPV = Sensitivity × Prevalence ÷ P(+) = 0.90 × 0.05 ÷ 0.1875 = 0.045 ÷ 0.1875 = 0.24 or 24%

3. **Negative Predictive Value**:
   NPV = Specificity × (1-Prevalence) ÷ (1-P(+)) = 0.85 × 0.95 ÷ 0.8125 = 0.8075 ÷ 0.8125 = 0.994 or 99.4%

### Answer 3.2: Binomial Distribution
p = 0.70, n = 10

1. **P(X=8)** = C(10,8) × 0.70⁸ × 0.30² = 45 × 0.0576 × 0.09 = 45 × 0.005184 = 0.2333 or 23.3%

2. **P(X≥8)** = P(X=8) + P(X=9) + P(X=10)
   P(X=9) = C(10,9) × 0.70⁹ × 0.30¹ = 10 × 0.0404 × 0.30 = 0.1212
   P(X=10) = C(10,10) × 0.70¹⁰ × 0.30⁰ = 1 × 0.0282 × 1 = 0.0282
   Total = 0.2333 + 0.1212 + 0.0282 = 0.3827 or 38.3%

3. **Expected value** = n × p = 10 × 0.70 = 7

### Answer 3.3: Normal Distribution
μ = 14, σ = 1.5

1. **P(12.5 < X < 15.5)**:
   Z₁ = (12.5-14)/1.5 = -1.0
   Z₂ = (15.5-14)/1.5 = 1.0
   P(-1.0 < Z < 1.0) = 0.8413 - 0.1587 = 0.6826 or 68.3%

2. **5th percentile**:
   Find Z where P(Z < z) = 0.05, Z = -1.645
   x = 14 + (-1.645)×1.5 = 14 - 2.4675 = 11.53 g/dL

3. **P(X > 17)**:
   Z = (17-14)/1.5 = 2.0
   P(Z > 2.0) = 1 - 0.9772 = 0.0228 or 2.3%

### Answer 3.4: Poisson Distribution
ᵅ = 4

1. **P(X=6)** = (e⁻⁴ × 4⁶) / 6! = (0.0183 × 4096) / 720 = 74.94 / 720 = 0.1041 or 10.4%

2. **P(X ≤ 2)** = P(0) + P(1) + P(2)
   P(0) = e⁻⁴ = 0.0183
   P(1) = (e⁻⁴ × 4¹)/1! = 0.0183 × 4 = 0.0732
   P(2) = (e⁻⁴ × 4²)/2! = 0.0183 × 16 / 2 = 0.2928 / 2 = 0.1464
   Total = 0.0183 + 0.0732 + 0.1464 = 0.2379 or 23.8%

3. **P(X > 8)** = 1 - P(X ≤ 8)
   First find P(X ≤ 8) using Poisson tables or calculator
   P(X ≤ 8) ≈ 0.9786
   P(X > 8) = 1 - 0.9786 = 0.0214 or 2.1%

## 3.10 Chapter Quiz

1. What is the difference between classical and empirical probability?
2. When would you use a binomial distribution?
3. What is the 68-95-99.7 rule for normal distributions?
4. What does the Central Limit Theorem tell us?
5. How do you calculate positive predictive value?

## 3.11 Quiz Answers

1. Classical is based on theory/equally likely outcomes; empirical is based on observed data
2. For experiments with fixed number of independent trials, each with two outcomes
3. 68% within 1 SD, 95% within 2 SD, 99.7% within 3 SD of the mean
4. Sample means become normally distributed as sample size increases
5. PPV = (Sensitivity × Prevalence) ÷ [Sensitivity × Prevalence + (1-Specificity) × (1-Prevalence)]

---

**Next Chapter Preview**: In Chapter 4, we'll learn about sampling methods and sampling distributions, which form the foundation for statistical inference.
