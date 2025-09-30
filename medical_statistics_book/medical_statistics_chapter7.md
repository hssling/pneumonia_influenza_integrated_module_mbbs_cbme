# Chapter 7: Correlation and Regression

## 7.1 Introduction to Correlation

**Correlation** measures the strength and direction of the linear relationship between two continuous variables.

### 7.1.1 Types of Correlation

**Positive Correlation**: Variables increase together
- Example: Height and weight
- As height increases, weight tends to increase

**Negative Correlation**: One variable increases as the other decreases
- Example: Age and physical fitness
- As age increases, fitness tends to decrease

**No Correlation**: No linear relationship
- Example: Shoe size and intelligence
- No predictable relationship

### 7.1.2 Correlation Coefficient (r)

**Formula:**
r = Σ((x - x̄)(y - ȳ)) / √[Σ(x - x̄)² × Σ(y - ȳ)²]

**Range**: -1 ≤ r ≤ +1
- r = +1: Perfect positive correlation
- r = -1: Perfect negative correlation
- r = 0: No linear correlation

**Example 7.1**: Blood pressure and age
Age (years): 30, 35, 40, 45, 50, 55, 60
BP (mmHg): 110, 115, 120, 125, 130, 135, 140

**Calculations:**
Mean age = 45, Mean BP = 125
Σ((x-45)(y-125)) = (-15×-15) + (-10×-10) + (-5×-5) + (0×0) + (5×5) + (10×10) + (15×15) = 225 + 100 + 25 + 0 + 25 + 100 + 225 = 700
Σ(x-45)² = 225 + 100 + 25 + 0 + 25 + 100 + 225 = 700
Σ(y-125)² = 225 + 100 + 25 + 0 + 25 + 100 + 225 = 700

r = 700 / √(700 × 700) = 700 / 700 = 1.0

**Perfect positive correlation** (as expected)

## 7.2 Pearson Correlation Coefficient

### 7.2.1 Interpretation of r Values

| |r| Value | Strength | Interpretation |
|----------|----------|----------|----------------|
| 0.00-0.19 | Very weak | Probably meaningless |
| 0.20-0.39 | Weak | Low correlation |
| 0.40-0.59 | Moderate | Moderate correlation |
| 0.60-0.79 | Strong | High correlation |
| 0.80-1.00 | Very strong | Very high correlation |

### 7.2.2 Hypothesis Testing for Correlation

**Hypotheses:**
- H₀: ρ = 0 (no correlation in population)
- H₁: ρ ≠ 0 (correlation exists in population)

**Test Statistic:**
t = r × √(n-2) / √(1-r²)

**Example 7.2**: Testing correlation significance
n=25, r=0.45

t = 0.45 × √23 / √(1-0.2025) = 0.45 × 4.796 / √0.7975 = 2.158 / 0.893 = 2.42

Critical value for α=0.05, df=23: ±2.069
|t| = 2.42 > 2.069, reject H₀
**Conclusion**: Significant correlation (p=0.023)

### 7.2.3 Correlation vs Causation

**Correlation does not imply causation**

**Example 7.3**: Ice cream sales and drowning deaths
- Both increase in summer months
- Correlation exists but no causal relationship
- Both caused by third factor: hot weather

**Spurious Correlation**: Apparent relationship due to confounding
**Reverse Causation**: Apparent cause is actually effect

## 7.3 Spearman Rank Correlation

### 7.3.1 When to Use Spearman Correlation

**Use when:**
- Data is ordinal (ranks)
- Data is not normally distributed
- Outliers are present
- Testing monotonic relationships (not just linear)

**Formula:**
rₛ = 1 - (6 × Σd²) / (n(n²-1))

Where d = difference in ranks

**Example 7.4**: Patient satisfaction and length of stay
Satisfaction ranks: 1, 2, 3, 4, 5
Length of stay ranks: 2, 1, 4, 3, 5

Differences (d): -1, 1, -1, 1, 0
Σd² = 1 + 1 + 1 + 1 + 0 = 4

rₛ = 1 - (6×4)/(5×24) = 1 - 24/120 = 1 - 0.2 = 0.8

**Strong positive correlation** between satisfaction and length of stay

## 7.4 Simple Linear Regression

### 7.4.1 Regression Equation

**Equation:**
ŷ = a + b×x

Where:
- ŷ = predicted value of y
- a = y-intercept
- b = slope
- x = value of predictor variable

**Formulas:**
b = Σ((x - x̄)(y - ȳ)) / Σ(x - x̄)²
a = ȳ - b×x̄

**Example 7.5**: Predicting weight from height
Height (cm): 160, 165, 170, 175, 180
Weight (kg): 55, 60, 65, 70, 75

**Calculations:**
x̄ = 170, ȳ = 65
Σ(x-170) = -10, -5, 0, 5, 10 = 0
Σ(y-65) = -10, -5, 0, 5, 10 = 0
Σ((x-170)(y-65)) = 100 + 25 + 0 + 25 + 100 = 250
Σ(x-170)² = 100 + 25 + 0 + 25 + 100 = 250

b = 250 / 250 = 1.0
a = 65 - 1.0×170 = 65 - 170 = -105

**Equation**: Weight = -105 + 1.0 × Height

**Interpretation**:
- For every 1 cm increase in height, weight increases by 1 kg
- At height = 0 cm, weight = -105 kg (not meaningful)

### 7.4.2 Assessing Regression Model

**Coefficient of Determination (R²)**:
- Proportion of variance in y explained by x
- R² = (correlation coefficient)²
- Example: r = 0.8, R² = 0.64 (64% of variance explained)

**Standard Error of Estimate**:
- Measures accuracy of predictions
- SE = √[Σ(ŷ - y)² / (n-2)]

## 7.5 Medical Applications of Correlation

### 7.5.1 Clinical Measurements

**Example 7.6**: BMI and blood pressure
- Study of 200 adults
- Correlation between BMI and systolic BP: r = 0.65
- Strong positive correlation
- For every 1 unit increase in BMI, BP increases by 2.3 mmHg

### 7.5.2 Laboratory Values

**Example 7.7**: Hemoglobin and hematocrit
- Perfect linear relationship (r ≈ 1.0)
- Hematocrit = 3 × Hemoglobin (approximately)
- Can predict one from the other

### 7.5.3 Epidemiological Studies

**Example 7.8**: Risk factors and disease
- Correlation between cholesterol and heart disease: r = 0.35
- Moderate correlation
- Other factors also influence heart disease risk

## 7.6 Introduction to Multiple Regression

### 7.6.1 Multiple Regression Equation

**Equation:**
ŷ = a + b₁×x₁ + b₂×x₂ + ... + bₖ×xₖ

**Example 7.9**: Predicting blood pressure
BP = 80 + 0.5×Age + 1.2×BMI - 3.0×Exercise

**Interpretation**:
- Baseline BP = 80 mmHg (when all predictors = 0)
- Each year of age increases BP by 0.5 mmHg
- Each BMI unit increases BP by 1.2 mmHg
- Regular exercise decreases BP by 3.0 mmHg

### 7.6.2 Multiple Correlation Coefficient

**R**: Correlation between observed y and predicted ŷ
- R = √(1 - SSE/SST)
- 0 ≤ R ≤ 1
- Higher R indicates better prediction

## 7.7 Assumptions of Linear Regression

### 7.7.1 Key Assumptions

1. **Linearity**: Linear relationship between variables
2. **Independence**: Observations are independent
3. **Homoscedasticity**: Constant variance across x values
4. **Normality**: Residuals are normally distributed
5. **No multicollinearity**: Predictor variables not highly correlated

### 7.7.2 Checking Assumptions

**Residual Plots**:
- Plot residuals vs predicted values
- Look for random scatter (no patterns)
- Check for constant spread

**Normal Probability Plot**:
- Plot residuals against normal distribution
- Should follow straight line

**Variance Inflation Factor (VIF)**:
- VIF > 10 indicates multicollinearity
- VIF = 1 / (1 - R²) for each predictor

## 7.8 Model Building and Selection

### 7.8.1 Stepwise Regression

**Forward Selection**:
- Start with no predictors
- Add predictor that most improves model
- Continue until no significant improvement

**Backward Elimination**:
- Start with all predictors
- Remove least significant predictor
- Continue until all remaining predictors significant

**Example 7.10**: Building model for diabetes risk
Potential predictors: Age, BMI, Family history, Exercise, Diet score

**Final model**: Risk = -2.1 + 0.03×Age + 0.15×BMI + 1.2×Family history - 0.8×Exercise

### 7.8.2 Model Fit Statistics

**Adjusted R²**:
- R² adjusted for number of predictors
- R²_adj = 1 - [(n-1)/(n-k-1)] × (1-R²)
- Penalizes models with too many predictors

**Akaike Information Criterion (AIC)**:
- AIC = n×ln(SSE/n) + 2k
- Lower AIC indicates better model
- Balances fit and complexity

## 7.9 Prediction and Confidence Intervals

### 7.9.1 Confidence Interval for Mean Response

**Predicts mean y for given x values**

**Formula:**
CI = ŷ ± tα/2 × SE(ŷ)

**Example 7.11**: Predicting blood pressure
For patient with Age=50, BMI=25
ŷ = 80 + 0.5×50 + 1.2×25 = 80 + 25 + 30 = 135 mmHg

95% CI: 135 ± 2.1 × 3.2 = 135 ± 6.7 = 128.3 to 141.7 mmHg

### 7.9.2 Prediction Interval for Individual Response

**Predicts range for single new observation**

**Formula:**
PI = ŷ ± tα/2 × SE(prediction)

**Generally wider than confidence interval**

**Example 7.12**: Same patient
95% PI: 135 ± 2.1 × 5.8 = 135 ± 12.2 = 122.8 to 147.2 mmHg

## 7.10 Correlation and Regression in Medical Research

### 7.10.1 Diagnostic Testing

**Example 7.13**: Biomarker correlation
- Correlation between new biomarker and disease severity: r = 0.75
- Strong correlation suggests biomarker may be useful
- Regression equation to predict severity from biomarker level

### 7.10.2 Treatment Outcomes

**Example 7.14**: Dose-response relationship
- Correlation between drug dose and treatment effect: r = 0.82
- Strong positive correlation
- Regression to find optimal dose

### 7.10.3 Risk Prediction

**Example 7.15**: Cardiovascular risk score
- Multiple regression model with 8 risk factors
- Predicts 10-year risk of heart disease
- R = 0.78, explains 61% of risk variation

## 7.11 Common Mistakes in Correlation and Regression

### 7.11.1 Correlation Assumptions

**Problem**: Using Pearson correlation inappropriately
- Data not normally distributed
- Outliers present
- Non-linear relationship

**Solution**: Use Spearman correlation or transform data

### 7.11.2 Overfitting

**Problem**: Model fits training data too closely
- Too many predictors for sample size
- Poor prediction on new data

**Solution**: Use adjusted R², cross-validation

### 7.11.3 Extrapolation

**Problem**: Making predictions outside range of data
- Regression line may not hold outside observed range

**Solution**: Only predict within range of x values used to build model

## 7.12 Exercises

### Exercise 7.1: Calculate Correlation
Calculate Pearson correlation coefficient for:
Age: 25, 30, 35, 40, 45, 50
Blood Pressure: 110, 115, 118, 125, 130, 135

### Exercise 7.2: Simple Linear Regression
Fit regression line for:
Height (cm): 150, 155, 160, 165, 170, 175, 180
Weight (kg): 50, 55, 60, 65, 70, 75, 80

### Exercise 7.3: Model Interpretation
For the regression equation: BP = 90 + 0.8×Age - 2.0×Exercise
- What is the predicted BP for a 40-year-old who exercises regularly?
- How much does BP change for each year of age?
- What does the exercise coefficient mean?

### Exercise 7.4: Correlation vs Causation
Explain why correlation between coffee consumption and heart disease might not mean coffee causes heart disease.

## 7.13 Exercise Answers

### Answer 7.1: Correlation Coefficient
**Data:**
x (Age): 25, 30, 35, 40, 45, 50
y (BP): 110, 115, 118, 125, 130, 135

**Means**: x̄ = 37.5, ȳ = 122.2

**Deviations:**
x-x̄: -12.5, -7.5, -2.5, 2.5, 7.5, 12.5
y-ȳ: -12.2, -7.2, -4.2, 2.8, 7.8, 12.8

**Σ(x-x̄)(y-ȳ)** = (-12.5×-12.2) + (-7.5×-7.2) + (-2.5×-4.2) + (2.5×2.8) + (7.5×7.8) + (12.5×12.8)
                = 152.5 + 54.0 + 10.5 + 7.0 + 58.5 + 160.0 = 442.5

**Σ(x-x̄)²** = 156.25 + 56.25 + 6.25 + 6.25 + 56.25 + 156.25 = 437.5
**Σ(y-ȳ)²** = 148.84 + 51.84 + 17.64 + 7.84 + 60.84 + 163.84 = 451.84

**r = 442.5 / √(437.5 × 451.84) = 442.5 / √197,680 = 442.5 / 444.6 = 0.995**

**Very strong positive correlation**

### Answer 7.2: Linear Regression
**Data:**
x (Height): 150, 155, 160, 165, 170, 175, 180
y (Weight): 50, 55, 60, 65, 70, 75, 80

**Means**: x̄ = 165, ȳ = 65

**Σ(x-x̄)(y-ȳ)** = (-15×-15) + (-10×-10) + (-5×-5) + (0×0) + (5×5) + (10×10) + (15×15)
                = 225 + 100 + 25 + 0 + 25 + 100 + 225 = 700

**Σ(x-x̄)²** = 225 + 100 + 25 + 0 + 25 + 100 + 225 = 700

**b = 700 / 700 = 1.0**
**a = 65 - 1.0 × 165 = 65 - 165 = -100**

**Equation**: Weight = -100 + 1.0 × Height

### Answer 7.3: Model Interpretation
**Equation**: BP = 90 + 0.8×Age - 2.0×Exercise

1. **Predicted BP for 40-year-old who exercises regularly**:
   Exercise = 1 (regular), Age = 40
   BP = 90 + 0.8×40 - 2.0×1 = 90 + 32 - 2 = 120 mmHg

2. **BP change per year of age**: +0.8 mmHg per year

3. **Exercise coefficient**: Regular exercise decreases blood pressure by 2.0 mmHg compared to no exercise

### Answer 7.4: Correlation vs Causation
**Coffee and heart disease correlation might be due to:**
- **Confounding**: Coffee drinkers more likely to smoke, stress, poor diet
- **Reverse causation**: People with heart disease may drink more coffee
- **Selection bias**: Study population not representative
- **Measurement error**: Inaccurate measurement of coffee consumption or heart disease

**Need randomized controlled trial to establish causation**

## 7.14 Chapter Quiz

1. What does a correlation coefficient of -0.8 indicate?
2. When should you use Spearman correlation instead of Pearson?
3. What is the difference between correlation and regression?
4. What does R² tell you in regression analysis?
5. Why is extrapolation problematic in regression?

## 7.15 Quiz Answers

1. Strong negative correlation (as one variable increases, the other decreases substantially)
2. When data is not normally distributed, has outliers, or is ordinal
3. Correlation measures strength of relationship; regression predicts one variable from another
4. Proportion of variance in dependent variable explained by independent variables
5. Regression model may not be valid outside the range of observed data

---

**Next Chapter Preview**: In Chapter 8, we'll explore multiple regression analysis and advanced regression techniques.
