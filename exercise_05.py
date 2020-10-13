'''
Exercise Question 5: Read face cream and facewash product sales data and show it using the bar chart

The bar chart should display the number of units sold per month for each product. 
Add a separate bar for each product in the same chart.

'''

import matplotlib.pyplot as plt
import pandas as pd

dataFrame = pd.read_csv("Data\\company_sales_data.csv")

facecream = dataFrame["facecream"].tolist()
facewash = dataFrame["facewash"].tolist()
month_number = dataFrame["month_number"].tolist()

plt.bar([a-0.25 for a in month_number], facecream, width=0.25, label="facecream", align="edge")
plt.bar([a+0.25 for a in month_number], facewash, width=-0.25, label="facewash", align="edge")

plt.xlabel("month_number")
plt.ylabel("Product Sales")
plt.minorticks_on()
plt.grid(b=True, which="major", linewidth="1", linestyle="--")
plt.legend()
plt.show()


