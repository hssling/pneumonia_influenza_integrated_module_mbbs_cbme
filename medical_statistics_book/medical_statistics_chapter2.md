# Chapter 2: Describing Data

## 2.1 Introduction to Data Description

**Descriptive statistics** summarize and organize data to make it more understandable. They help us see patterns, trends, and outliers in medical data without making inferences about larger populations.

### Why Describe Data?
- **Pattern Recognition**: Identify trends and relationships
- **Data Quality Check**: Spot errors and inconsistencies
- **Communication**: Present findings clearly to others
- **Decision Support**: Guide clinical and policy decisions

**Example 2.1**: A hospital administrator wants to understand patient wait times. Instead of looking at 1,000 individual records, descriptive statistics can show the average wait time, how much variation exists, and whether most patients wait a reasonable time.

## 2.2 Presenting Categorical Data

### 2.2.1 Frequency Tables

**Frequency tables** show how often each category occurs.

**Example 2.2**: Blood types in 200 patients

| Blood Type | Frequency | Percentage |
|------------|-----------|------------|
| A          | 60        | 30%        |
| B          | 50        | 25%        |
| AB         | 30        | 15%        |
| O          | 60        | 30%        |
| **Total**  | **200**   | **100%**   |

**Calculation**:
- Percentage = (Frequency ÷ Total) × 100
- A: (60 ÷ 200) × 100 = 30%

### 2.2.2 Cross-Tabulation (Contingency Tables)

Cross-tabulation shows relationships between two categorical variables.

**Example 2.3**: Smoking status and lung cancer diagnosis

|            | Lung Cancer | No Lung Cancer | Total |
|------------|-------------|----------------|-------|
| **Smokers**| 45          | 55             | 100   |
| **Non-smokers** | 5       | 95             | 100   |
| **Total**  | 50          | 150            | 200   |

**Row Percentages**:
- Smokers with lung cancer: (45 ÷ 100) × 100 = 45%
- Non-smokers with lung cancer: (5 ÷ 100) × 100 = 5%

## 2.3 Presenting Numerical Data

### 2.3.1 Frequency Distributions for Discrete Data

**Example 2.4**: Number of children per family in 50 families

| Number of Children | Frequency | Cumulative Frequency |
|-------------------|-----------|---------------------|
| 0                 | 5         | 5                   |
| 1                 | 15        | 20                  |
| 2                 | 20        | 40                  |
| 3                 | 8         | 48                  |
| 4                 | 2         | 50                  |

**Cumulative frequency** shows how many families have that number or fewer children.

### 2.3.2 Histograms for Continuous Data

**Histograms** show the distribution of continuous data using bars.

**Example 2.5**: Distribution of systolic blood pressure in 100 adults

```
Blood Pressure (mmHg)
140-149: ████████ (8)
130-139: █████████████ (13)
120-129: ████████████████████ (20)
110-119: ████████████████ (16)
100-109: ██████ (6)
 90-99:  ██ (2)
```

### 2.3.3 Stem-and-Leaf Plots

Stem-and-leaf plots show individual values while maintaining shape.

**Example 2.6**: Age at diagnosis of Type 2 diabetes (n=20)

```
4 | 2 5 8
5 | 0 2 3 5 7 8 9
6 | 0 1 3 5
7 | 2 5
```

Key: 5|2 = 52 years

## 2.4 Measures of Central Tendency

### 2.4.1 Mean (Arithmetic Average)

**Formula**: x̄ = Σx / n

Where:
- Σx = sum of all values
- n = number of observations

**Example 2.7**: Calculate mean blood glucose levels (mg/dL) from 5 patients:
95, 105, 110, 115, 125

Mean = (95 + 105 + 110 + 115 + 125) ÷ 5 = 550 ÷ 5 = 110 mg/dL

**Weighted Mean**: Used when values have different importance
Formula: x̄ = Σ(w × x) / Σw

**Example 2.8**: Average grade with different credit hours
- Course A: Grade 85, Credits 3
- Course B: Grade 92, Credits 4
- Course C: Grade 78, Credits 2

Weighted mean = (85×3 + 92×4 + 78×2) ÷ (3+4+2) = (255 + 368 + 156) ÷ 9 = 779 ÷ 9 = 86.6

### 2.4.2 Median

**Median** is the middle value when data is arranged in order.

**Example 2.9**: Find median of: 85, 90, 92, 95, 98
Ordered: 85, 90, 92, 95, 98
Median = 92 (middle value)

**Example 2.10**: Even number of observations: 85, 90, 92, 95, 98, 100
Ordered: 85, 90, 92, 95, 98, 100
Median = (92 + 95) ÷ 2 = 93.5

### 2.4.3 Mode

**Mode** is the most frequent value.

**Example 2.11**: Number of daily medications: 1, 2, 2, 3, 3, 3, 4, 5
Mode = 3 (appears three times)

**Bimodal**: Two modes
**Multimodal**: More than two modes

### 2.4.4 Choosing the Right Measure

| Data Type | Best Measure | Reason |
|-----------|--------------|---------|
| **Symmetric distribution** | Mean | Uses all information |
| **Skewed distribution** | Median | Not affected by outliers |
| **Categorical data** | Mode | Only measure available |
| **Ordinal data** | Median | Preserves order |

## 2.5 Measures of Dispersion (Variability)

### 2.5.1 Range

**Range** = Maximum value - Minimum value

**Example 2.12**: Blood pressure readings: 110, 115, 120, 125, 180
Range = 180 - 110 = 70 mmHg

**Interquartile Range (IQR)** = Q3 - Q1
- Q1 = 25th percentile (lower quartile)
- Q3 = 75th percentile (upper quartile)

**Example 2.13**: Find IQR of: 2, 4, 7, 8, 9, 10, 12, 15, 18, 20
Ordered: 2, 4, 7, 8, 9, 10, 12, 15, 18, 20
Q1 = 7 (2.5th position), Q3 = 15 (7.5th position)
IQR = 15 - 7 = 8

### 2.5.2 Variance and Standard Deviation

**Variance** measures average squared deviation from the mean.

**Population Variance Formula**:
σ² = Σ(x - μ)² / N

**Sample Variance Formula**:
s² = Σ(x - x̄)² / (n - 1)

**Example 2.14**: Calculate variance of: 8, 10, 12, 14, 16
Mean = 12
Deviations: 8-12=-4, 10-12=-2, 12-12=0, 14-12=2, 16-12=4
Squared deviations: 16, 4, 0, 4, 16
Sum = 40
Variance = 40 ÷ 4 = 10 (n-1 = 5-1 = 4)

**Standard Deviation** = √Variance

**Example 2.15**: Standard deviation = √10 = 3.16

### 2.5.3 Coefficient of Variation

**Coefficient of Variation (CV)** = (Standard Deviation ÷ Mean) × 100%

**Example 2.16**: Compare variability of two measurements:
- Blood glucose: Mean = 110 mg/dL, SD = 15 → CV = (15÷110)×100 = 13.6%
- Hemoglobin: Mean = 13 g/dL, SD = 2 → CV = (2÷13)×100 = 15.4%

Higher CV indicates more relative variability.

## 2.6 Distribution Shapes

### 2.6.1 Normal Distribution

**Bell-shaped curve**, symmetric around the mean
- Mean = Median = Mode
- 68% of data within 1 SD of mean
- 95% within 2 SD of mean
- 99.7% within 3 SD of mean

**Example 2.17**: Adult heights follow normal distribution
- Mean = 165 cm, SD = 10 cm
- 68% between 155-175 cm
- 95% between 145-185 cm

### 2.6.2 Skewed Distributions

**Right-skewed (Positive skew)**: Tail extends to the right
- Mean > Median > Mode
- Example: Income distribution, age at retirement

**Left-skewed (Negative skew)**: Tail extends to the left
- Mean < Median < Mode
- Example: Test scores where most students do well

### 2.6.3 Bimodal Distribution

Two peaks, often indicating two subgroups.

**Example 2.18**: Height distribution in a mixed adult-child population shows two peaks.

## 2.7 Outliers and Data Cleaning

### 2.7.1 Identifying Outliers

**Statistical Methods**:
- Values beyond 2-3 SD from mean
- Values outside 1.5 × IQR from quartiles

**Example 2.19**: Blood pressure data: 110, 115, 120, 125, 200
- Mean = 134, SD = 37
- 200 is more than 2 SD above mean (134 + 74 = 208)
- Likely an outlier or data entry error

### 2.7.2 Handling Outliers

1. **Verify**: Check if the value is possible
2. **Investigate**: Look for data entry errors
3. **Consider**: Whether outlier represents important information
4. **Decide**: Exclude, transform, or analyze separately

## 2.8 Summary Statistics for Medical Data

### 2.8.1 Five-Number Summary

Minimum, Q1, Median, Q3, Maximum

**Example 2.20**: Length of hospital stay (days): 1, 2, 3, 4, 5, 6, 7, 8, 10, 15
- Minimum: 1
- Q1: 3
- Median: 5.5
- Q3: 8.5
- Maximum: 15

### 2.8.2 Box Plots (Box-and-Whisker Plots)

Visual representation of five-number summary.

```
     Q1   Median    Q3
     |     |       |
  Min |-----|-------|-----| Max
      |           |
    Whiskers   Box
```

## 2.9 Medical Examples and Interpretation

### 2.9.1 Laboratory Values

**Example 2.21**: Serum cholesterol levels in healthy adults
- Mean: 185 mg/dL
- Median: 180 mg/dL
- SD: 35 mg/dL
- Range: 120-280 mg/dL

**Interpretation**: Most values between 150-220 mg/dL (mean ± 1 SD)

### 2.9.2 Clinical Measurements

**Example 2.22**: Body temperature in 100 healthy adults
- Mean: 98.6°F
- SD: 0.7°F
- 95% of values between 97.2-100.0°F (mean ± 2 SD)

### 2.9.3 Epidemiological Data

**Example 2.23**: Age distribution of COVID-19 cases
- Mean age: 45 years
- Median age: 42 years
- Mode: 35 years
- Slightly right-skewed distribution

## 2.10 Exercises

### Exercise 2.1: Calculate Summary Statistics
Calculate mean, median, mode, range, and standard deviation for:
Blood glucose levels (mg/dL): 85, 92, 95, 98, 102, 105, 108, 112, 115, 125

### Exercise 2.2: Frequency Table
Create a frequency table for the following data (patient ages):
25, 30, 35, 35, 40, 40, 40, 45, 45, 50, 50, 50, 50, 55, 60, 65, 70, 75

### Exercise 2.3: Distribution Shape
Describe the shape of each distribution:
1. Heights of adult males
2. Number of children per family
3. Age at death from lung cancer
4. Test scores in a difficult exam

### Exercise 2.4: Outlier Detection
Identify potential outliers in this dataset:
Hospital stay (days): 2, 3, 3, 4, 4, 5, 5, 6, 7, 45

## 2.11 Exercise Answers

### Answer 2.1: Summary Statistics
Data: 85, 92, 95, 98, 102, 105, 108, 112, 115, 125

**Mean**: (85+92+95+98+102+105+108+112+115+125) ÷ 10 = 1037 ÷ 10 = 103.7 mg/dL

**Median**: Ordered: 85, 92, 95, 98, 102, 105, 108, 112, 115, 125
Middle values: 102 and 105, median = (102+105)÷2 = 103.5 mg/dL

**Mode**: No value repeats, no mode

**Range**: 125 - 85 = 40 mg/dL

**Standard Deviation**:
1. Calculate variance: Σ(x - mean)² = (-18.7)² + (-11.7)² + (-8.7)² + (-5.7)² + (-1.7)² + (1.3)² + (4.3)² + (8.3)² + (11.3)² + (21.3)²
2. Sum of squared deviations = 349.69 + 136.89 + 75.69 + 32.49 + 2.89 + 1.69 + 18.49 + 68.89 + 127.69 + 453.69 = 1268.1
3. Variance = 1268.1 ÷ 9 = 140.9
4. SD = √140.9 = 11.87 mg/dL

### Answer 2.2: Frequency Table

| Age Group | Frequency | Percentage |
|-----------|-----------|------------|
| 25-29     | 1         | 5.6%       |
| 30-34     | 1         | 5.6%       |
| 35-39     | 2         | 11.1%      |
| 40-44     | 3         | 16.7%      |
| 45-49     | 2         | 11.1%      |
| 50-54     | 4         | 22.2%      |
| 55-59     | 1         | 5.6%       |
| 60-64     | 1         | 5.6%       |
| 65-69     | 1         | 5.6%       |
| 70-74     | 1         | 5.6%       |
| 75-79     | 1         | 5.6%       |
| **Total** | **18**    | **100%**   |

### Answer 2.3: Distribution Shape
1. **Normal distribution** - Bell-shaped, symmetric
2. **Right-skewed** - Most families have 1-3 children, few have many
3. **Right-skewed** - Most deaths occur at older ages, few at very young ages
4. **Left-skewed** - Most students score low, few score very high

### Answer 2.4: Outlier Detection
Hospital stay: 2, 3, 3, 4, 4, 5, 5, 6, 7, 45

**Mean**: (2+3+3+4+4+5+5+6+7+45) ÷ 10 = 84 ÷ 10 = 8.4 days

**Using 2 SD method**:
1. Calculate SD: Sum of squared deviations from mean = 40.96 + 29.16 + 29.16 + 19.36 + 19.36 + 12.96 + 12.96 + 6.76 + 1.96 + 1332.56 = 1507.2
2. Variance = 1507.2 ÷ 9 = 167.47
3. SD = √167.47 = 12.94 days
4. 2 SD above mean = 8.4 + 25.88 = 34.28 days

**45 days is greater than 34.28 days, so it's an outlier.**

**Using IQR method**:
1. Ordered data: 2, 3, 3, 4, 4, 5, 5, 6, 7, 45
2. Q1 = 3.5, Q3 = 6.5
3. IQR = 6.5 - 3.5 = 3
4. Upper limit = Q3 + 1.5×IQR = 6.5 + 4.5 = 11

**45 days exceeds 11 days, confirming it's an outlier.**

## 2.12 Chapter Quiz

1. What is the difference between mean and median?
2. When would you use median instead of mean?
3. What does a right-skewed distribution look like?
4. How do you calculate the interquartile range?
5. What information does a box plot show?

## 2.13 Quiz Answers

1. Mean is the arithmetic average; median is the middle value when ordered
2. When data is skewed or contains outliers
3. Asymmetric with long tail on the right side
4. Q3 minus Q1 (75th percentile minus 25th percentile)
5. Minimum, Q1, median, Q3, and maximum values

---

**Next Chapter Preview**: In Chapter 3, we'll explore probability concepts and probability distributions commonly used in medical statistics.
