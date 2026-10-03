import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis


scores = pd.Series(
    [78, 85, np.nan, 92, 67, 74, 88, np.nan, 81, 95],
    index=[
        "Student A",
        "Student B",
        "Student C",
        "Student D",
        "Student E",
        "Student F",
        "Student G",
        "Student H",
        "Student I",
        "Student J"
    ]
)

print("Original Exam Scores:")
print(scores)

# (a) Descriptive Statistics
print("\nStatistics:")
print(scores.describe())

# (b) Skewness and Kurtosis
# Remove missing values before calculating
clean_scores = scores.dropna()

skewness = skew(clean_scores)
kurt = kurtosis(clean_scores)

print("\nDistribution Shape:")
print("Skewness:", skewness)
print("Kurtosis:", kurt)

# Describe skewness
if skewness > 0:
    print("The distribution is positively skewed.")
elif skewness < 0:
    print("The distribution is negatively skewed.")
else:
    print("The distribution is approximately symmetric.")


# (c) Count Missing Values
missing_values = scores.isnull().sum()

print("\nNumber of Missing Scores:")
print(missing_values)


# (d) Fill Missing Values with Mean
mean_score = scores.mean()

completed_scores = scores.fillna(mean_score)

print("\nMean Score:")
print(mean_score)

print("\nCompleted Exam Scores:")
print(completed_scores)