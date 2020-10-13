'''
Exercise Question 7: Read the total profit of each month and show it using the 
histogram to see most common profit ranges
'''

import matplotlib.pyplot as plt 
import pandas as pd 

dataFrame = pd.read_csv("Data\\company_sales_data.csv")

total_profit = dataFrame["total_profit"].tolist()

profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
labels = ['low', 'average', 'Good', 'Best']

plt.hist(total_profit, profit_range, label=labels)
plt.xlabel('profit range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.title('Profit data')
plt.show()

