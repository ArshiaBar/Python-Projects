import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import numpy as np

file_path = r'stats.xlsx'

try:
    df = pd.read_excel(file_path, usecols=['Cocoa Percent'])
    df2 = pd.read_excel(file_path, usecols=['Rating'])
except FileNotFoundError:
    print(f"File '{file_path}' not found. Check the file path.")

data = df['Cocoa Percent']
data2 = df2['Rating']

plt.scatter(data, data2)
plt.show()

# Create histogram
plt.hist(data, bins=59)
plt.xlabel('Cocoa Percent')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

# Create a boxplot
plt.boxplot(data)
plt.ylabel('Cocoa Percent')
plt.title('Boxplot')
plt.show()

#mean
mean_value = np.mean(data)

#median
median_value = np.median(data)

#mode
mode_value = data.mode().iloc[0]

#quartiles
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

#range
data_range = np.max(data) - np.min(data)

#population variance
data_variance = np.var(data)

#population standard deviation
data_dev = np.std(data)

num_data = data.count()
#1% trimmed mean
trim1 = np.sort(data)[round(0.1*num_data):round(-0.1*num_data)]  # Remove top and bottom 1%
trimmed_mean1 = np.mean(trim1)

#2.5% trimmed mean
trim2 = np.sort(data)[round(0.025*num_data):round(-0.025*num_data)]  # Remove top and bottom 2.5%
trimmed_mean2 = np.mean(trim2)

print(f"Mean: {mean_value:.4f}")
print(f"Median: {median_value:.2f}")
print(f"Mode: {mode_value:.2f}")
print(f"Q1 (25th percentile): {q1:.2f}")
print(f"Q3 (75th percentile): {q3:.2f}")
print(f"Range: {data_range:.2f}")
print(f"Variance: {data_variance:.4f}")
print(f"Standard Deviation: {data_dev:.4f}")
print(f"1% Trimmed Mean: {trimmed_mean1:.2f}")
print(f"2.5% Trimmed Mean: {trimmed_mean2:.2f}")

population_mean=mean_value

#---------------------------------------------------------------------------------
import statistics

sample = np.random.choice(data, size=int(0.10 * len(data)), replace=False)

plt.hist(sample, bins=59)
plt.xlabel('Cocoa Percent')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

plt.boxplot(sample)
plt.ylabel('Cocoa Percent')
plt.title('Boxplot')
plt.show()

#mean
mean_value = np.mean(sample)

#median
median_value = np.median(sample)

#mode
mode_value = statistics.mode(sample)

#quartiles
q1 = np.percentile(sample, 25)
q3 = np.percentile(sample, 75)

#range
data_range = np.max(sample) - np.min(sample)

#sample variance
data_variance = np.var(sample)

#sample standard deviation
data_dev = np.std(sample)

num_data = len(sample)
#1% trimmed mean
trim1 = np.sort(sample)[round(0.1*num_data):round(-0.1*num_data)]
trimmed_mean1 = np.mean(trim1)

#2.5% trimmed mean
trim2 = np.sort(sample)[round(0.025*num_data):round(-0.025*num_data)]
trimmed_mean2 = np.mean(trim2)

print(f"Mean: {mean_value:.4f}")
print(f"Median: {median_value:.2f}")
print(f"Mode: {mode_value:.2f}")
print(f"Q1 (25th percentile): {q1:.2f}")
print(f"Q3 (75th percentile): {q3:.2f}")
print(f"Range: {data_range:.2f}")
print(f"Variance: {data_variance:.4f}")
print(f"Standard Deviation: {data_dev:.4f}")
print(f"1% Trimmed Mean: {trimmed_mean1:.2f}")
print(f"2.5% Trimmed Mean: {trimmed_mean2:.2f}")

sample_mean=mean_value
sample_sd=data_dev
sample_num_of_data=num_data

import scipy.stats as st

#alphas
a1=(1-0.75)
a2=(1-0.85)
a3=(1-0.95)

confidence75 =[sample_mean-(-st.norm.ppf(a1/2)*sample_sd),sample_mean+(-st.norm.ppf(a1/2)*sample_sd)]
confidence85 =[sample_mean-(-st.norm.ppf(a2/2)*sample_sd),sample_mean+(-st.norm.ppf(a2/2)*sample_sd)]
confidence95 =[sample_mean-(-st.norm.ppf(a3/2)*sample_sd),sample_mean+(-st.norm.ppf(a3/2)*sample_sd)]

print(f"75% Confidence Interval: ({confidence75[0]:.3f}, {confidence75[1]:.3f})")
print(f"85% Confidence Interval: ({confidence85[0]:.3f}, {confidence85[1]:.3f})")
print(f"95% Confidence Interval: ({confidence95[0]:.3f}, {confidence95[1]:.3f})")

import math

t_statistic=(population_mean-sample_mean)/(sample_sd/(math.sqrt(sample_num_of_data)))
print(f"t statistic is {t_statistic:.4f}")

from scipy.stats import t

p_value = 2 * (1 - t.cdf(abs(t_statistic), sample_num_of_data-1))
print(f"pvalue is {p_value:.3f}")
if p_value <=0.05:
    print("Null hypothesis is rejected")
else:
    print("Null hypothesis is not rejected")

from scipy.stats import pearsonr

correlation_coefficient, _ = pearsonr(data, data2)
coefficient_of_determination = correlation_coefficient**2

print(f'Correlation Coefficient: {correlation_coefficient:.2f}')
print(f'Coefficient of Determination: {coefficient_of_determination:.2f}')