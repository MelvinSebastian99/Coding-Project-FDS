# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 13:27:38 2024

@author: melvi
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read data from the file
data = pd.read_csv('data7-1.csv')  # Replace 'your_data_file.csv' with your file name
data.columns = ['Salary']  # Set the column name explicitly
salaries = data['Salary']  # Assuming the column containing salaries is named 'Salary'

# Calculate the probability density function and plot histogram
plt.figure(figsize=(12, 8))
plt.hist(salaries, density=True, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel('Salary')
plt.ylabel('Probability Density')
plt.title('Probability Density Function of Salaries')

# Calculate mean salary (W~)
mean_salary = np.mean(salaries)

# Calculate the fraction of population between 0.75W~ and W~
lower_bound = 0.75 * mean_salary
upper_bound = mean_salary
x_values = salaries[(salaries >= lower_bound) & (salaries <= upper_bound)]
fraction_population = len(x_values) / len(salaries)

# Round values if needed
mean_salary_rounded = round(mean_salary, 2)
fraction_population_rounded = round(fraction_population, 2)

# Plot mean salary and fraction on the graph
plt.axvline(mean_salary, color='red', linestyle='dashed', linewidth=2, label=f'Mean Salary ($\~{{W}}$): {mean_salary_rounded}')
plt.axvspan(lower_bound, upper_bound, color='green', alpha=0.3, label=f'Population Fraction (X): {fraction_population_rounded}')

plt.legend()
plt.show()

# Print the values
print(f"Mean Annual Salary (W~): {mean_salary_rounded}")
print(f"Fraction of population with salaries between 0.75W~ and W~ (X): {fraction_population_rounded}")





