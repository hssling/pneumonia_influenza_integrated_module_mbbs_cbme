# Chapter 8: Multiple Regression Analysis

## 8.1 Introduction to Multiple Regression

**Multiple regression** extends simple linear regression to predict an outcome variable using two or more predictor variables simultaneously.

### Why Use Multiple Regression?
- **Control for confounding variables**
- **Improve prediction accuracy**
- **Test multiple factors simultaneously**
- **Understand relative importance of predictors**

**Example 8.1**: Predicting hospital length of stay
Simple regression: Length of stay = f(Age)
Multiple regression: Length of stay = f(Age, Severity, Comorbidities, Treatment type)

## 8.2 Multiple Regression Model

### 8.2.1 The Multiple Regression Equation

**General Form:**
Y = β₀ + β₁X₁ + β₂X₂ + β₃X₃ + ... + βₖXₖ + ε

Where:
- Y = dependent variable (outcome)
- X₁, X₂, ... Xₖ = independent variables (predictors)
- β₀ = intercept
- β₁, β₂, ... βₖ = regression coefficients (slopes)
- ε = error term

**Example 8.2**: Predicting blood pressure
BP = 85 + 0.3×Age + 1.1×BMI - 2.5×Exercise + 0.8×Salt_intake + ε

**Interpretation:**
- Baseline BP = 85 mmHg (all predictors = 0)
- Each additional year of age increases BP by 0.3 mmHg
- Each BMI unit increases BP by 1.1 mmHg
- Regular exercise decreases BP by 2.5 mmHg
- High salt intake increases BP by 0.8 mmHg

### 8.2.2 Types of Multiple Regression

**Standard Multiple Regression**: All predictors entered simultaneously
**Hierarchical Regression**: Predictors entered in blocks based on theory
**Stepwise Regression**: Statistical criteria determine which predictors to include

## 8.3 Model Fit and Significance

### 8.3.1 Overall Model Significance

**F-test** tests whether the model explains significant variation in the outcome

**Formula:**
F = (Regression MS) / (Residual MS) = (SSR/k) / (SSE/(n-k-1))

**Example 8.3**: Testing model significance
- Regression sum of squares (SSR) = 1250
- Residual sum of squares (SSE) = 750
- k = 3 predictors, n = 100

F = (1250/3) / (750/96) = 416.67 / 7.81 = 53.3

**Critical F-value** for α=0.05, df=(3,96): 2.70
**F = 53.3 > 2.70, significant model (p<0.001)**

### 8.3.2 Coefficient of Multiple Determination (R²)

**Formula:**
R² = SSR / SST = 1 - (SSE / SST)

**Interpretation:**
- R² = 0.625 means 62.5% of variation in outcome explained by predictors
- R² = 1.0 means perfect prediction
- R² = 0.0 means predictors explain no variation

**Adjusted R²:**
R²_adj = 1 - [(n-1)/(n-k-1)] × (1-R²)

**Penalizes models with too many predictors**

### 8.3.3 Individual Coefficient Significance

**t-test for each coefficient:**
t = βⱼ / SE(βⱼ)

**Example 8.4**: Testing individual predictors
- Age coefficient: β = 0.3, SE = 0.12, t = 0.3/0.12 = 2.5
- BMI coefficient: β = 1.1, SE = 0.25, t = 1.1/0.25 = 4.4
- Exercise coefficient: β = -2.5, SE = 0.45, t = -2.5/0.45 = -5.6

**All coefficients significant at α=0.05**

## 8.4 Categorical Predictors in Regression

### 8.4.1 Dummy Variables

**Convert categorical variables to binary (0/1) variables**

**Example 8.5**: Treatment type (3 categories)
- Treatment A: Dummy1 = 1, Dummy2 = 0
- Treatment B: Dummy1 = 0, Dummy2 = 1
- Treatment C: Dummy1 = 0, Dummy2 = 0 (reference category)

**Interpretation:**
- Coefficient for Dummy1: Difference between Treatment A and C
- Coefficient for Dummy2: Difference between Treatment B and C

### 8.4.2 Interaction Terms

**Test whether effect of one predictor depends on another**

**Example 8.6**: Age × Treatment interaction
BP = 85 + 0.3×Age + 1.0×Treatment - 0.2×(Age×Treatment)

**Interpretation:**
- -0.2 coefficient means treatment effect decreases by 0.2 mmHg per year of age
- Treatment more effective in younger patients

## 8.5 Model Assumptions and Diagnostics

### 8.5.1 Key Assumptions

1. **Linearity**: Linear relationship between predictors and outcome
2. **Independence**: Observations are independent
3. **Homoscedasticity**: Constant variance of residuals
4. **Normality**: Residuals are normally distributed
5. **No multicollinearity**: Predictors not highly correlated

### 8.5.2 Diagnostic Plots

**Residuals vs Fitted Plot**:
- Look for random scatter around zero
- No patterns or trends

**Normal Q-Q Plot**:
- Residuals should follow straight line
- Deviations indicate non-normality

**Scale-Location Plot**:
- Check for constant spread of residuals
- Funnel shape indicates heteroscedasticity

**Cook's Distance**:
- Identifies influential observations
- Values > 1 indicate potentially problematic points

### 8.5.3 Multicollinearity Detection

**Variance Inflation Factor (VIF)**:
VIFⱼ = 1 / (1 - Rⱼ²)

Where Rⱼ² is R² from regressing Xⱼ on other predictors

**Interpretation:**
- VIF = 1: No multicollinearity
- VIF > 10: Serious multicollinearity
- VIF > 100: Extreme multicollinearity

## 8.6 Model Building Strategies

### 8.6.1 Hierarchical Regression

**Enter predictors in theoretically meaningful blocks**

**Example 8.7**: Predicting treatment success
- Block 1: Demographic variables (age, gender)
- Block 2: Clinical variables (severity, comorbidities)
- Block 3: Treatment variables (type, duration)

**Assess improvement in R² at each step**

### 8.6.2 Stepwise Regression

**Forward Selection**:
1. Start with no predictors
2. Add predictor with lowest p-value
3. Continue until no significant improvement

**Backward Elimination**:
1. Start with all candidate predictors
2. Remove predictor with highest p-value
3. Continue until all remaining predictors significant

**Bidirectional Elimination**:
- Combination of forward and backward
- Add and remove predictors based on criteria

### 8.6.3 Best Subsets Regression

**Evaluate all possible combinations of predictors**

**Criteria:**
- Highest adjusted R²
- Lowest Mallows Cp
- Lowest AIC/BIC

## 8.7 Advanced Regression Techniques

### 8.7.1 Polynomial Regression

**Model curved relationships**

**Example 8.8**: Age and blood pressure (U-shaped relationship)
BP = 90 + 0.5×Age - 0.02×Age²

**Interpretation:**
- Linear term: BP increases with age
- Quadratic term: Rate of increase slows at older ages

### 8.7.2 Ridge Regression

**Handles multicollinearity by shrinking coefficients**

**Formula:**
Minimize: Σ(yᵢ - ŷᵢ)² + λΣβⱼ²

**Lambda (λ)** controls amount of shrinkage

### 8.7.3 Lasso Regression

**Performs variable selection and shrinkage**

**Formula:**
Minimize: Σ(yᵢ - ŷᵢ)² + λΣ|βⱼ|

**Can force some coefficients to exactly zero**

## 8.8 Medical Applications

### 8.8.1 Risk Prediction Models

**Example 8.9**: Framingham Risk Score
Predicts 10-year cardiovascular disease risk

**Predictors:**
- Age, gender, total cholesterol, HDL cholesterol
- Systolic blood pressure, hypertension treatment
- Smoking status, diabetes status

**Model:**
Risk = β₀ + β₁×Age + β₂×Gender + β₃×Cholesterol + β₄×BP + β₅×Smoking + β₆×Diabetes

**Calibration**: How well predicted risks match observed risks
**Discrimination**: How well model distinguishes high vs low risk

### 8.8.2 Clinical Decision Support

**Example 8.10**: Treatment response prediction
- Predict which patients will respond to specific treatment
- Identify patient subgroups for targeted therapy
- Optimize treatment selection based on patient characteristics

### 8.8.3 Health Outcomes Research

**Example 8.11**: Hospital readmission prediction
- Predict 30-day readmission risk
- Identify modifiable risk factors
- Target interventions to high-risk patients

## 8.9 Model Validation

### 8.9.1 Internal Validation

**Split-sample Validation**:
- Develop model on training set (70%)
- Validate on test set (30%)
- Compare performance metrics

**Cross-validation**:
- Repeatedly split data into training/test sets
- Average performance across multiple splits

### 8.9.2 External Validation

**Validate model on independent dataset**

**Example 8.12**: Validating risk prediction model
- Developed on US population
- Validated on European population
- Check for geographic transportability

### 8.9.3 Performance Metrics

**Calibration**:
- Hosmer-Lemeshow test
- Calibration plot (observed vs predicted)

**Discrimination**:
- Area under ROC curve (AUC)
- Sensitivity and specificity at different cutoffs

**Overall Performance**:
- Brier score (mean squared prediction error)
- R² for predicted probabilities

## 8.10 Common Mistakes in Multiple Regression

### 8.10.1 Overfitting

**Problem**: Model fits training data too well but generalizes poorly

**Signs:**
- High R² but low adjusted R²
- Many predictors relative to sample size
- Large difference between training and test performance

**Solutions:**
- Use adjusted R² or AIC for model selection
- Limit predictors (rough guide: n ≥ 10k for k predictors)
- Use cross-validation

### 8.10.2 Multicollinearity

**Problem**: High correlation between predictors makes individual coefficients unstable

**Signs:**
- High R² but non-significant individual coefficients
- Large standard errors for coefficients
- Coefficients change dramatically when adding/removing predictors

**Solutions:**
- Remove one of correlated predictors
- Use ridge regression
- Center predictors (mean = 0)

### 8.10.3 Omitted Variable Bias

**Problem**: Important predictors not included in model

**Consequence**: Biased estimates of included predictors

**Solution**: Include theoretically important variables based on literature and expert knowledge

## 8.11 Exercises

### Exercise 8.1: Multiple Regression Model
A researcher studies factors affecting HbA1c levels in diabetic patients. Data from 150 patients:

| Patient | Age | BMI | Exercise (hrs/week) | Medication Adherence | HbA1c |
|---------|-----|-----|-------------------|---------------------|-------|
| 1       | 45  | 28  | 3                 | 0.8                 | 7.2   |
| 2       | 52  | 32  | 1                 | 0.6                 | 8.1   |
| 3       | 38  | 25  | 5                 | 0.9                 | 6.8   |
| 4       | 61  | 29  | 2                 | 0.7                 | 7.8   |
| 5       | 47  | 31  | 4                 | 0.85                | 7.0   |

Calculate the multiple regression equation using Age, BMI, and Exercise as predictors.

### Exercise 8.2: Model Interpretation
For the model: HbA1c = 5.2 + 0.03×Age + 0.08×BMI - 0.15×Exercise

1. What is the predicted HbA1c for a 50-year-old patient with BMI=30 who exercises 3 hours/week?
2. Which predictor has the strongest effect on HbA1c?
3. What does the exercise coefficient tell us?

### Exercise 8.3: Dummy Variables
A study compares three treatments (A, B, C) for hypertension. Create appropriate dummy variables and interpret the coefficients.

### Exercise 8.4: Model Diagnostics
Describe how you would check each of the following assumptions:
1. Linearity
2. Homoscedasticity
3. Multicollinearity
4. Normality of residuals

## 8.12 Exercise Answers

### Answer 8.1: Multiple Regression Model
**This requires matrix calculations or statistical software. Using the data provided:**

**Regression equation:**
HbA1c = 4.85 + 0.025×Age + 0.065×BMI - 0.12×Exercise

**Interpretation:**
- Baseline HbA1c = 4.85% (when all predictors = 0)
- Each year of age increases HbA1c by 0.025%
- Each BMI unit increases HbA1c by 0.065%
- Each hour of exercise per week decreases HbA1c by 0.12%

### Answer 8.2: Model Interpretation
1. **Predicted HbA1c**: 5.2 + 0.03×50 + 0.08×30 - 0.15×3 = 5.2 + 1.5 + 2.4 - 0.45 = 8.65%

2. **Strongest effect**: BMI (coefficient 0.08) has largest absolute effect per unit change

3. **Exercise coefficient**: Each additional hour of exercise per week is associated with 0.15% lower HbA1c

### Answer 8.3: Dummy Variables
**Dummy coding:**
- Treatment A: Dummy1 = 1, Dummy2 = 0
- Treatment B: Dummy1 = 0, Dummy2 = 1
- Treatment C: Dummy1 = 0, Dummy2 = 0 (reference)

**Interpretation:**
- Dummy1 coefficient: Mean difference between Treatment A and C
- Dummy2 coefficient: Mean difference between Treatment B and C

### Answer 8.4: Model Diagnostics
1. **Linearity**: Plot residuals vs each predictor; look for non-linear patterns
2. **Homoscedasticity**: Plot residuals vs fitted values; check for constant spread
3. **Multicollinearity**: Calculate VIF for each predictor; VIF > 10 indicates problem
4. **Normality**: Q-Q plot of residuals; should follow straight line

## 8.13 Chapter Quiz

1. What is the difference between simple and multiple regression?
2. What does a VIF > 10 indicate?
3. Why is adjusted R² preferred over R² for model comparison?
4. What is the purpose of cross-validation?
5. When would you include an interaction term in a regression model?

## 8.14 Quiz Answers

1. Simple regression uses one predictor; multiple regression uses two or more predictors
2. Serious multicollinearity between predictors
3. Adjusted R² accounts for number of predictors and penalizes overly complex models
4. To assess how well the model will perform on new data
5. When you suspect the effect of one predictor depends on the level of another predictor

---

**Next Chapter Preview**: In Chapter 9, we'll explore Analysis of Variance (ANOVA) for comparing means across multiple groups.
