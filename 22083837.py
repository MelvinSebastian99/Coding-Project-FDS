# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 13:27:38 2024

@author: melvi
"""


# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 13:27:38 2024

@author: melvi
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# Read data from CSV file
data = pd.read_csv('data7-1.csv', header=None, names=['Salary'])

# Determine the probability density function utilizing Gaussian Kernel Density Estimation (KDE).
kde = gaussian_kde(data['Salary'], bw_method=0.5)  

# Create data points to plot the Probability Density Function (PDF)
val = np.linspace(data['Salary'].min(), data['Salary'].max())
pdf = kde.evaluate(val)

# Calculate mean annual salary
salaries = data['Salary']
mean_salary = np.mean(data['Salary'])
mean_salary = round(mean_salary, 2)
lower_bound = 0.75 * mean_salary
upper_bound = mean_salary

# Calculate fraction of population between 0.75W~ and W~
x_values = salaries[(salaries >= lower_bound) & (salaries <= upper_bound)]
fraction_population = len(x_values) / len(salaries)
fraction_population_rounded = round(fraction_population, 2)
# Print mean annual salary and fraction of population
print(f"Mean Annual Salary: {mean_salary}")
print(f"Fraction of Population between 0.75W~ and W~: {fraction_population_rounded}")

# Plotting histogram and PDF
plt.figure(figsize=(8, 6))
plt.hist(data['Salary'], bins=30, density=True,
         alpha=0.7, label='Histogram', edgecolor='black')
plt.plot(val, pdf, label='Probability Density Function',)
plt.axvline(mean_salary, color='red', linestyle='dashed',
            linewidth=2, label=f'Mean Salary ($\~{{W}}$): {mean_salary}')
plt.axvspan(lower_bound, upper_bound, color='yellow', alpha=0.3,
            label=f'Population Fraction (X): {fraction_population_rounded}')
plt.xlabel('Salary (Euros)')
plt.ylabel('Probability Density')
plt.title('Probability Density Function of Annual Salaries')
plt.xlim(0, plt.xlim()[1])
plt.ylim(0, plt.ylim()[1])
plt.legend()
plt.tight_layout()
plt.show()







