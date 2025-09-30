# Chapter 15: Statistical Software in Medicine

## 15.1 Introduction to Statistical Software

**Statistical software** is essential for medical data analysis, from simple descriptive statistics to complex survival models. Choosing the right software depends on your needs, budget, and technical expertise.

### Why Use Statistical Software?
- **Efficiency**: Handle large datasets quickly
- **Accuracy**: Reduce calculation errors
- **Reproducibility**: Document analysis steps
- **Advanced methods**: Access to latest statistical techniques
- **Visualization**: Create publication-quality graphs

### Software Categories:
- **Commercial**: SPSS, SAS, Stata
- **Open-source**: R, Python, Julia
- **Specialized**: MedCalc, GraphPad Prism
- **Web-based**: Google Colab, RStudio Cloud

**Example 15.1**: Medical researcher workflow
- Data collection: REDCap or Excel
- Data cleaning: R or Python
- Statistical analysis: Stata or SPSS
- Visualization: R ggplot2
- Report writing: R Markdown

## 15.2 R for Medical Statistics

### 15.2.1 Getting Started with R

**R** is a free, open-source programming language for statistical computing and graphics.

**Installation:**
- Download from CRAN (cran.r-project.org)
- Install RStudio (rstudio.com) for better interface
- Install packages: install.packages("package_name")

**Basic R Syntax:**
```r
# Load data
data <- read.csv("medical_data.csv")

# Summary statistics
summary(data$blood_pressure)

# t-test
t.test(blood_pressure ~ treatment, data = data)

# Linear regression
model <- lm(blood_pressure ~ age + bmi, data = data)
summary(model)
```

### 15.2.2 Essential R Packages for Medicine

**Data manipulation:**
- **dplyr**: Data wrangling and transformation
- **tidyr**: Tidy data principles
- **readxl**: Read Excel files

**Statistical analysis:**
- **stats**: Base R statistics
- **survival**: Survival analysis
- **lme4**: Mixed effects models
- **meta**: Meta-analysis

**Visualization:**
- **ggplot2**: Advanced graphics
- **lattice**: Trellis graphics
- **plotly**: Interactive plots

**Example 15.2**: R code for medical data analysis
```r
# Load required packages
library(dplyr)
library(ggplot2)
library(survival)

# Load and clean data
data <- read.csv("patient_data.csv") %>%
  filter(!is.na(blood_pressure)) %>%
  mutate(hypertension = blood_pressure > 140)

# Create summary table
summary_table <- data %>%
  group_by(treatment) %>%
  summarise(
    mean_bp = mean(blood_pressure),
    sd_bp = sd(blood_pressure),
    n = n()
  )

# Create Kaplan-Meier plot
km_fit <- survfit(Surv(time_to_event, event) ~ treatment, data = data)
ggsurvplot(km_fit, data = data, pval = TRUE)
```

## 15.3 SPSS for Medical Research

### 15.3.1 Overview

**SPSS (Statistical Package for the Social Sciences)** is user-friendly software with point-and-click interface and syntax options.

**Strengths:**
- Intuitive graphical user interface
- Comprehensive help system
- Good for beginners
- Extensive healthcare applications

**Limitations:**
- Expensive licensing
- Less flexible for complex analyses
- Limited programming capabilities

### 15.3.2 Common SPSS Procedures

**Data Management:**
- Data Editor for data entry and cleaning
- Variable View for defining variable properties
- Transform → Compute Variable for new variables

**Statistical Tests:**
- Analyze → Descriptive Statistics
- Analyze → Compare Means (t-tests, ANOVA)
- Analyze → Regression → Linear
- Analyze → Survival → Kaplan-Meier

**Example 15.3**: SPSS syntax for analysis
```spss
* Load data
GET FILE = 'C:\data\medical_data.sav'.

* Descriptive statistics
DESCRIPTIVES VARIABLES = blood_pressure age bmi
  /STATISTICS = MEAN STDDEV MIN MAX.

* t-test
T-TEST GROUPS = treatment(1 2)
  /MISSING = ANALYSIS
  /VARIABLES = blood_pressure
  /CRITERIA = CI(.95).

* Linear regression
REGRESSION
  /MISSING LISTWISE
  /STATISTICS COEFF OUTS R ANOVA
  /CRITERIA = PIN(.05) POUT(.10)
  /NOORIGIN
  /DEPENDENT blood_pressure
  /METHOD = ENTER age bmi exercise.
```

## 15.4 Stata for Medical Statistics

### 15.4.1 Overview

**Stata** is powerful statistical software with excellent data management capabilities and extensive medical applications.

**Strengths:**
- Excellent for epidemiology and biostatistics
- Powerful graphics capabilities
- Good for large datasets
- Extensive user community

**Limitations:**
- Command-line interface (steep learning curve)
- Expensive for commercial use
- Less intuitive than SPSS

### 15.4.2 Stata Commands for Medical Analysis

**Data management:**
```stata
* Load data
use "medical_data.dta", clear

* Describe data
describe

* Summarize variables
summarize blood_pressure age bmi

* Create new variable
generate bmi_category = 1 if bmi < 25
replace bmi_category = 2 if bmi >= 25 & bmi < 30
replace bmi_category = 3 if bmi >= 30
```

**Statistical analysis:**
```stata
* t-test
ttest blood_pressure, by(treatment)

* Linear regression
regress blood_pressure age bmi exercise

* Logistic regression
logistic hypertension age bmi

* Survival analysis
stset time_to_death, failure(death = 1)
sts graph, by(treatment)
stcox age bmi treatment
```

## 15.5 Python for Medical Data Science

### 15.5.1 Python Ecosystem

**Python** is a versatile programming language with extensive libraries for data analysis.

**Key libraries:**
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scipy**: Scientific computing
- **statsmodels**: Statistical models
- **scikit-learn**: Machine learning
- **matplotlib/seaborn**: Visualization

**Example 15.4**: Python code for medical analysis
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

# Load data
data = pd.read_csv('medical_data.csv')

# Data cleaning
data = data.dropna(subset=['blood_pressure'])

# Summary statistics
print(data['blood_pressure'].describe())

# t-test
group1 = data[data['treatment'] == 1]['blood_pressure']
group2 = data[data['treatment'] == 2]['blood_pressure']
t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"t-test: t={t_stat:.3f}, p={p_value:.3f}")

# Linear regression
X = data[['age', 'bmi', 'exercise']]
X = sm.add_constant(X)  # Add intercept
y = data['blood_pressure']
model = sm.OLS(y, X).fit()
print(model.summary())
```

## 15.6 Specialized Medical Software

### 15.6.1 GraphPad Prism

**Designed specifically for biomedical research**

**Features:**
- Intuitive interface for common analyses
- Publication-quality graphs
- Non-linear regression
- Survival analysis
- Dose-response curves

**Example 15.5**: Prism workflow
1. Enter data in table format
2. Choose analysis from dropdown menu
3. Select graph type
4. Copy results to manuscript

### 15.6.2 MedCalc

**Statistical software for medical research**

**Specialized features:**
- ROC curve analysis
- Diagnostic test evaluation
- Method comparison studies
- Reference interval calculation

**Example 15.6**: MedCalc for diagnostic testing
- Import test results and gold standard
- Calculate sensitivity, specificity, likelihood ratios
- Generate ROC curve with AUC
- Compare multiple diagnostic tests

## 15.7 Data Management Best Practices

### 15.7.1 Data Cleaning

**Essential steps:**
1. **Check data structure**: Variable types, missing values
2. **Handle missing data**: Listwise, pairwise, or imputation
3. **Identify outliers**: Statistical methods and visual inspection
4. **Verify data entry**: Double data entry for critical variables
5. **Validate ranges**: Check for impossible values

**Example 15.7**: R code for data cleaning
```r
# Check for missing values
colSums(is.na(data))

# Identify outliers using IQR
Q1 <- quantile(data$blood_pressure, 0.25)
Q3 <- quantile(data$blood_pressure, 0.75)
IQR <- Q3 - Q1
outliers <- data$blood_pressure < (Q1 - 1.5*IQR) | data$blood_pressure > (Q3 + 1.5*IQR)

# Remove or flag outliers
data_clean <- data[!outliers, ]
```

### 15.7.2 Data Documentation

**Codebooks and metadata:**
- Variable names and descriptions
- Coding schemes (e.g., 1=male, 2=female)
- Units of measurement
- Data collection methods
- Analysis scripts with comments

## 15.8 Reproducible Research

### 15.8.1 Version Control

**Git and GitHub:**
- Track changes to analysis code
- Collaborate with team members
- Share analysis scripts
- Document analysis decisions

**Example 15.8**: Git workflow
```bash
# Initialize repository
git init

# Add analysis files
git add analysis.R report.Rmd

# Commit changes
git commit -m "Add initial statistical analysis"

# Push to GitHub
git push origin main
```

### 15.8.2 Literate Programming

**R Markdown and Jupyter Notebooks:**
- Combine code, results, and narrative
- Reproducible analysis reports
- Easy to update when data changes

**Example 15.9**: R Markdown structure
```markdown
---
title: "Medical Data Analysis"
author: "Researcher Name"
date: "2024-01-01"
output: html_document
---

## Data Summary
```{r}
summary(data)
```

## Statistical Analysis
```{r}
model <- lm(blood_pressure ~ age + bmi, data = data)
summary(model)
```

## Results
The regression analysis shows...
```

## 15.9 Software for Specific Analyses

### 15.9.1 Survival Analysis Software

**Specialized tools:**
- **SAS PROC LIFETEST**: Kaplan-Meier and log-rank tests
- **Stata stset and stcox**: Cox proportional hazards
- **R survival package**: Comprehensive survival analysis
- **SPSS Survival menu**: Basic survival analysis

### 15.9.2 Meta-Analysis Software

**Dedicated tools:**
- **RevMan (Review Manager)**: Cochrane collaboration tool
- **Comprehensive Meta-Analysis**: User-friendly interface
- **R meta package**: Advanced meta-analysis methods
- **Stata metan command**: Publication-quality forest plots

### 15.9.3 Diagnostic Test Software

**Specialized applications:**
- **MedCalc**: ROC curves and diagnostic accuracy
- **Meta-DiSc**: Diagnostic test meta-analysis
- **R pROC package**: ROC curve analysis
- **Stata roctab**: Basic diagnostic test evaluation

## 15.10 Choosing the Right Software

### 15.10.1 Decision Factors

**Consider:**
- **Budget**: Free vs commercial software
- **Learning curve**: Ease of use vs power
- **Data size**: Small datasets vs big data
- **Collaboration**: Team preferences and compatibility
- **Output needs**: Publication requirements

### 15.10.2 Software Comparison

| Software | Ease of Use | Power | Cost | Best For |
|----------|-------------|-------|------|----------|
| **R** | Medium | High | Free | Advanced users, reproducible research |
| **SPSS** | High | Medium | High | Beginners, healthcare settings |
| **Stata** | Medium | High | High | Epidemiologists, biostatisticians |
| **Python** | Low | Very High | Free | Data scientists, machine learning |
| **Prism** | Very High | Low | Medium | Basic biomedical research |

## 15.11 Common Software Issues and Solutions

### 15.11.1 Memory and Performance

**Problem**: Software crashes with large datasets

**Solutions:**
- Use 64-bit versions
- Increase memory allocation
- Sample large datasets for exploration
- Use database connections for very large data

### 15.11.2 Version Compatibility

**Problem**: Different software versions produce different results

**Solutions:**
- Document software version used
- Use stable, well-tested versions
- Validate results with alternative software

### 15.11.3 Learning Resources

**Free resources:**
- R: swirl package, DataCamp, Coursera
- Python: Codecademy, edX
- SPSS: IBM tutorials, YouTube
- Stata: UCLA resources, Stata YouTube channel

## 15.12 Medical Data Standards and Formats

### 15.12.1 Data Formats

**Common formats:**
- **CSV**: Comma-separated values (universal)
- **Excel**: .xlsx files (common but problematic)
- **SAS**: .sas7bdat (proprietary)
- **Stata**: .dta (efficient)
- **R**: .rds, .rda (R-specific)

### 15.12.2 Data Standards

**CDISC standards:**
- SDTM: Study data tabulation model
- ADaM: Analysis data model
- Define-XML: Metadata standard

**Example 15.10**: Clinical trial data structure
- Demographics domain (DM)
- Adverse events domain (AE)
- Concomitant medications domain (CM)
- Laboratory data domain (LB)

## 15.13 Exercises

### Exercise 15.1: R Data Analysis
Using the following R code structure, write code to:
1. Load a CSV file containing patient data
2. Calculate summary statistics for blood pressure
3. Perform t-test comparing two treatment groups
4. Create a boxplot of blood pressure by treatment

### Exercise 15.2: SPSS Analysis
Describe the SPSS menu path for:
1. Running a chi-square test
2. Creating a Kaplan-Meier survival curve
3. Performing logistic regression

### Exercise 15.3: Stata Commands
Write Stata commands to:
1. Load a dataset
2. Generate a new variable (BMI from height and weight)
3. Run a linear regression
4. Export results to Excel

### Exercise 15.4: Python Data Analysis
Write Python code to:
1. Import necessary libraries
2. Load and explore a medical dataset
3. Handle missing values
4. Create a correlation matrix

## 15.14 Exercise Answers

### Answer 15.1: R Data Analysis
```r
# 1. Load data
data <- read.csv("patient_data.csv")

# 2. Summary statistics
summary(data$blood_pressure)
sd(data$blood_pressure)

# 3. t-test
t.test(blood_pressure ~ treatment, data = data)

# 4. Boxplot
boxplot(blood_pressure ~ treatment, data = data,
        main = "Blood Pressure by Treatment",
        xlab = "Treatment", ylab = "Blood Pressure")
```

### Answer 15.2: SPSS Analysis
1. **Chi-square test**: Analyze → Descriptive Statistics → Crosstabs → Statistics → Chi-square
2. **Kaplan-Meier**: Analyze → Survival → Kaplan-Meier
3. **Logistic regression**: Analyze → Regression → Binary Logistic

### Answer 15.3: Stata Commands
```stata
# 1. Load data
use "medical_data.dta", clear

# 2. Generate BMI
generate bmi = weight / (height/100)^2

# 3. Linear regression
regress blood_pressure age bmi exercise

# 4. Export to Excel
export excel using "results.xlsx", firstrow(variables)
```

### Answer 15.4: Python Data Analysis
```python
# 1. Import libraries
import pandas as pd
import numpy as np
from scipy import stats

# 2. Load and explore data
data = pd.read_csv('medical_data.csv')
print(data.head())
print(data.info())

# 3. Handle missing values
data = data.dropna()

# 4. Correlation matrix
correlation_matrix = data.corr()
print(correlation_matrix)
```

## 15.15 Chapter Quiz

1. What is the main advantage of R over commercial statistical software?
2. Which software is best for beginners in medical statistics?
3. What is the purpose of R Markdown?
4. Why is data cleaning important before statistical analysis?
5. What is version control and why is it important for reproducible research?

## 15.16 Quiz Answers

1. Free and open-source with extensive package ecosystem
2. SPSS or GraphPad Prism for their intuitive interfaces
3. To create reproducible documents combining code, results, and narrative
4. Ensures data quality and prevents errors in analysis
5. Tracks changes to analysis code and enables collaboration

---

**Next Chapter Preview**: In Chapter 16, we'll learn how to critically appraise medical literature and interpret statistical results.
