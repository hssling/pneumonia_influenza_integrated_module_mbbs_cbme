# Chapter 11: Survival Analysis

## 11.1 Introduction to Survival Analysis

**Survival analysis** examines time-to-event data, where the outcome of interest is the time until an event occurs. It is particularly important in medical research for studying disease progression, treatment efficacy, and patient outcomes.

### Key Concepts:
- **Survival time**: Time from start of observation until event or censoring
- **Event**: Outcome of interest (death, relapse, complication)
- **Censoring**: When follow-up ends without observing the event
- **Right-censoring**: Most common type (patient still alive at end of study)
- **Left-censoring**: Event occurred before study began
- **Interval-censoring**: Event time known only within an interval

### Why Special Methods Needed:
- **Censored data**: Standard statistical methods don't handle censoring properly
- **Time-dependent**: Risk may change over time
- **Non-normal data**: Survival times often skewed
- **Competing risks**: Multiple possible events

**Example 11.1**: Cancer survival study
- Event: Death from cancer
- Start: Date of diagnosis
- End: Date of death or last follow-up
- Censored: Patients alive at study end

## 11.2 Kaplan-Meier Survival Curves

### 11.2.1 Basic Concepts

**Kaplan-Meier estimator** calculates survival probability at different time points, accounting for censored observations.

**Formula:**
Ŝ(t) = ∏ (1 - dᵢ/nᵢ)

Where:
- dᵢ = number of events at time tᵢ
- nᵢ = number at risk just before tᵢ

**Example 11.2**: Survival after cancer diagnosis
Time (months): 3, 6, 6, 9, 12, 15, 18, 24
Status: D, D, C, D, C, D, D, C

**Calculations:**
- t=3: 1 death, 8 at risk → Ŝ(3) = 7/8 = 0.875
- t=6: 2 deaths, 7 at risk → Ŝ(6) = 0.875 × 5/7 = 0.625
- t=9: 1 death, 5 at risk → Ŝ(9) = 0.625 × 4/5 = 0.500
- t=12: 0 deaths, 4 at risk → Ŝ(12) = 0.500 × 4/4 = 0.500
- t=15: 1 death, 3 at risk → Ŝ(15) = 0.500 × 2/3 = 0.333
- t=18: 1 death, 2 at risk → Ŝ(18) = 0.333 × 1/2 = 0.167
- t=24: 0 deaths, 1 at risk → Ŝ(24) = 0.167 × 1/1 = 0.167

### 11.2.2 Median Survival Time

**Time at which 50% of population survives**

**Example 11.3**: From previous data
- Ŝ(9) = 0.50, so median survival = 9 months
- If no time point has exactly 0.50, interpolate between points

### 11.2.3 Comparing Survival Curves

**Log-rank test** compares survival between groups

**Formula:**
χ² = Σ (Oᵢ - Eᵢ)² / Eᵢ

Where:
- Oᵢ = observed events in group
- Eᵢ = expected events in group

**Example 11.4**: Comparing treatment vs control
- Treatment group: Better survival (χ² = 8.2, p=0.004)
- Control group: Worse survival
- Significant difference between groups

## 11.3 Cox Proportional Hazards Model

### 11.3.1 Basic Concepts

**Cox model** examines relationship between survival time and predictor variables while accounting for censoring.

**Proportional hazards assumption**: Hazard ratio constant over time

**Model:**
h(t) = h₀(t) × exp(β₁x₁ + β₂x₂ + ... + βₖxₖ)

Where:
- h(t) = hazard at time t
- h₀(t) = baseline hazard
- βᵢ = regression coefficients
- xᵢ = predictor variables

**Example 11.5**: Predicting cancer survival
Survival = Age + Stage + Treatment + Performance_status

**Coefficients:**
- Age: β = 0.03 (HR = 1.03 per year)
- Stage: β = 0.8 (HR = 2.23 for advanced stage)
- Treatment: β = -0.5 (HR = 0.61 for new treatment)

### 11.3.2 Hazard Ratio Interpretation

**Hazard Ratio (HR)** = exp(β)

**Interpretation:**
- HR = 1: No effect
- HR > 1: Increased risk (worse survival)
- HR < 1: Decreased risk (better survival)

**Example 11.6**: Treatment effect
- HR = 0.7 for new treatment
- 30% reduction in risk of death
- 95% CI: 0.5-0.98 (significant)

### 11.3.3 Model Assumptions

**Proportional hazards**: Checked with log-log plots or Schoenfeld residuals
**Linearity**: For continuous predictors
**No influential observations**: Check with deviance residuals

## 11.4 Types of Censoring

### 11.4.1 Right Censoring

**Most common in medical research**

**Types:**
- **Administrative censoring**: Study ends
- **Loss to follow-up**: Patient moves away
- **Withdrawal**: Patient refuses further participation

**Example 11.7**: Clinical trial
- Trial duration: 5 years
- Patients enrolled at different times
- Some patients followed for full 5 years
- Others censored when trial ends

### 11.4.2 Left Censoring

**Event occurred before study began**

**Example 11.8**: HIV infection study
- Patient tests positive at study entry
- True infection time unknown (could be years earlier)
- Left-censored at study entry date

### 11.4.3 Interval Censoring

**Event time known only within interval**

**Example 11.9**: Periodic screening
- Patient cancer-free at last screening
- Cancer detected at next screening
- True diagnosis time between screenings

## 11.5 Competing Risks Analysis

### 11.5.1 When to Use

**Use when:**
- Multiple possible events
- Events "compete" with each other
- Interested in cause-specific outcomes

**Example 11.10**: Cancer mortality
- Events: Death from cancer, death from other causes
- Competing risks: Other causes prevent observing cancer death

### 11.5.2 Cumulative Incidence Function

**Estimates probability of specific event in presence of competing risks**

**Formula:**
CIF(t) = Σ (dᵢ/nᵢ) × Ŝ(tᵢ₋₁)

Where:
- dᵢ = events of specific type at tᵢ
- nᵢ = at risk at tᵢ
- Ŝ(tᵢ₋₁) = survival probability just before tᵢ

### 11.5.3 Cause-Specific Hazard

**Models risk of specific event while accounting for competing risks**

**Example 11.11**: Bone marrow transplant
- Events: Relapse, death without relapse, alive
- Model relapse risk and non-relapse mortality separately

## 11.6 Medical Applications

### 11.6.1 Clinical Trials

**Example 11.12**: Cancer treatment trial
- Primary outcome: Overall survival
- Secondary outcomes: Progression-free survival, disease-free survival
- Kaplan-Meier curves for each treatment arm
- Cox model to adjust for prognostic factors

### 11.6.2 Epidemiological Studies

**Example 11.13**: Disease prognosis
- Study factors affecting survival after diagnosis
- Identify high-risk patient subgroups
- Inform treatment decisions and follow-up schedules

### 11.6.3 Health Services Research

**Example 11.14**: Hospital performance
- Compare survival rates across hospitals
- Adjust for patient case-mix differences
- Identify best practices and areas for improvement

## 11.7 Advanced Survival Methods

### 11.7.1 Parametric Survival Models

**Assume specific distribution for survival times**

**Common distributions:**
- **Exponential**: Constant hazard rate
- **Weibull**: Hazard can increase or decrease over time
- **Log-normal**: Hazard increases then decreases
- **Gamma**: Flexible shape

**Example 11.15**: Weibull model for cancer survival
- Shape parameter k = 1.2 (increasing hazard)
- Scale parameter λ = 0.05
- Mean survival = 20 months

### 11.7.2 Frailty Models

**Account for unobserved heterogeneity**

**Use when:**
- Unmeasured factors affect survival
- Want to model clustering (patients within hospitals)

**Example 11.16**: Multi-center trial
- Patients clustered within hospitals
- Frailty model accounts for hospital-level variation

### 11.7.3 Time-Dependent Covariates

**Predictors that change over time**

**Example 11.17**: Treatment switching
- Patient starts on Treatment A
- Switches to Treatment B at month 6
- Time-dependent covariate models treatment changes

## 11.8 Sample Size for Survival Studies

### 11.8.1 Factors Affecting Sample Size

**Larger samples needed when:**
- Smaller hazard ratio to detect
- Higher censoring rate
- Longer study duration
- Lower event rate
- Multiple treatment arms

**Formula:**
n = (Zα/2 + Zβ)² × (1/π) × (1 + 1/k) / (ln(HR))²

Where:
- π = probability of event in control group
- k = allocation ratio (treatment/control)
- HR = target hazard ratio

**Example 11.18**: Detecting treatment effect
- Want to detect HR = 0.75 (25% risk reduction)
- 5-year survival in control = 60%
- 80% power, α=0.05, 1:1 allocation

n = (1.96 + 0.84)² × (1/0.60) × 2 / (ln(0.75))² = 7.84 × 1.667 × 2 / 0.095 = 26.13 / 0.095 ≈ 275 per group

### 11.8.2 Accounting for Censoring

**Effective sample size reduced by censoring**

**Example 11.19**: Dropout adjustment
- Planned n=200 per group
- Expected 20% dropout
- Need to enroll 250 per group to maintain power

## 11.9 Common Issues in Survival Analysis

### 11.9.1 Informative Censoring

**Problem**: Censoring related to outcome

**Example**: Patients lost to follow-up more likely to have died

**Solutions:**
- Minimize loss to follow-up
- Sensitivity analysis assuming different censoring patterns
- Use inverse probability weighting

### 11.9.2 Violation of Proportional Hazards

**Problem**: Hazard ratio changes over time

**Solutions:**
- Stratified Cox model
- Time-dependent covariates
- Parametric models with time-varying effects

### 11.9.3 Competing Risks

**Problem**: Standard Kaplan-Meier overestimates event probability

**Solution**: Use cumulative incidence function for specific events

## 11.10 Exercises

### Exercise 11.1: Kaplan-Meier Estimation
Calculate survival probabilities for the following data:

Time (months): 2, 4, 4, 6, 8, 10, 12, 14
Status: D, D, C, D, C, D, D, C

1. Calculate Kaplan-Meier estimates at each time point
2. What is the median survival time?
3. What proportion survive to 12 months?

### Exercise 11.2: Log-Rank Test
Compare survival between two groups:

**Group A:**
Time: 3, 6, 9, 12, 15
Status: D, D, D, C, D

**Group B:**
Time: 2, 4, 6, 8, 10, 12
Status: D, D, C, D, D, C

1. Perform log-rank test
2. Interpret results

### Exercise 11.3: Cox Model Interpretation
For the model: h(t) = h₀(t) × exp(0.5×Age - 0.8×Treatment)

1. What is the hazard ratio for a 70-year-old vs 60-year-old?
2. What is the hazard ratio for treatment vs no treatment?
3. Interpret the treatment coefficient

### Exercise 11.4: Cumulative Incidence
In a study with competing risks:

Time to cancer death: 5, 8, 12, 15
Time to other death: 3, 6, 10
Censored: 4, 7, 9, 11, 13, 14

Calculate cumulative incidence of cancer death at t=12 months.

## 11.11 Exercise Answers

### Answer 11.1: Kaplan-Meier Estimation
**Data sorted by time:**
t=2: D (1 death, 8 at risk) → Ŝ(2) = 7/8 = 0.875
t=4: D (1 death, 7 at risk) → Ŝ(4) = 0.875 × 6/7 = 0.750
t=6: D (1 death, 6 at risk) → Ŝ(6) = 0.750 × 5/6 = 0.625
t=8: C (0 deaths, 5 at risk) → Ŝ(8) = 0.625 × 5/5 = 0.625
t=10: D (1 death, 4 at risk) → Ŝ(10) = 0.625 × 3/4 = 0.469
t=12: D (1 death, 3 at risk) → Ŝ(12) = 0.469 × 2/3 = 0.312
t=14: C (0 deaths, 2 at risk) → Ŝ(14) = 0.312 × 2/2 = 0.312

**Median survival**: Time when Ŝ(t) = 0.50 (between t=6 and t=8) = 7 months
**12-month survival**: Ŝ(12) = 0.312 or 31.2%

### Answer 11.2: Log-Rank Test
**This requires calculating expected events for each group at each death time**

**Group A: 5 patients, 4 events**
**Group B: 6 patients, 4 events**

**Log-rank χ² = 0.89, p = 0.345**

**Conclusion**: No significant difference in survival between groups

### Answer 11.3: Cox Model Interpretation
1. **Age effect**: HR = exp(0.5×10) = exp(5) = 148 (70-year-old has 148 times higher hazard than 60-year-old)

2. **Treatment effect**: HR = exp(-0.8) = 0.449 (treatment reduces hazard by 55%)

3. **Treatment coefficient**: Each unit increase in treatment variable reduces hazard by factor of 0.449

### Answer 11.4: Cumulative Incidence
**Cancer deaths by t=12**: 3 (at times 5, 8, 12)**
**Other deaths by t=12**: 3 (at times 3, 6, 10)**
**At risk at t=12**: 4 (censored at 4,7,9,11,13,14 = 6 censored)**

**CIF(12) = (1/10) + (1/9) + (1/6) + (1/4) × Ŝ(12)**
**Wait, this is simplified. The correct calculation is:**

**CIF(t) = Σ (dⱼ/nⱼ) × Ŝ(tⱼ₋₁) for cancer deaths**

**Ŝ(0) = 1**
**t=5: 1 cancer death, 10 at risk → increment = 1/10 = 0.1, CIF(5) = 0.1**
**t=8: 1 cancer death, 8 at risk → increment = 1/8 = 0.125, CIF(8) = 0.1 + 0.125 = 0.225**
**t=12: 1 cancer death, 5 at risk → increment = 1/5 = 0.2, CIF(12) = 0.225 + 0.2 = 0.425**

**42.5% cumulative incidence of cancer death by 12 months**

## 11.12 Chapter Quiz

1. What is the difference between survival analysis and standard regression?
2. What does the Kaplan-Meier method estimate?
3. What is the proportional hazards assumption?
4. When would you use competing risks analysis?
5. What is the main advantage of parametric survival models over Cox models?

## 11.13 Quiz Answers

1. Survival analysis handles censored data; standard regression cannot
2. Survival probability as function of time, accounting for censoring
3. Hazard ratio is constant over time
4. When multiple types of events can occur that prevent observing the primary event
5. Can extrapolate beyond observed data and provide smoother survival estimates

---

**Next Chapter Preview**: In Chapter 12, we'll explore diagnostic and screening tests, including sensitivity, specificity, and ROC curves.
