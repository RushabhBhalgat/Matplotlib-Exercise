'''
Exercise Question 8: Calculate total sale data for last year for each product and show it using a Pie chart
Note: In Pie chart display Number of units sold per year for each product in percentage
'''

import matplotlib.pyplot as plt
import pandas as pd

dataFrame = pd.read_csv("Data\\company_sales_data.csv")

facecream = dataFrame["facecream"].sum()
facewash = dataFrame["facewash"].sum()
toothpaste = dataFrame["toothpaste"].sum()
bathingsoap = dataFrame["bathingsoap"].sum()
shampoo = dataFrame["shampoo"].sum()
moisturizer = dataFrame["moisturizer"].sum()

saleList = [facecream, facewash, toothpaste, bathingsoap, shampoo, moisturizer]
labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
plt.axis("equal")
plt.pie(saleList, labels=labels, autopct="%1.1f%%")
plt.legend(loc='lower right')
plt.title('Sales data')
plt.show()