'''
Exercise Question 4: Read toothpaste sales data of each month and show it using a scatter plot

Also, add a grid in the plot. gridline style should “–“.

'''

import matplotlib.pyplot as plt
import pandas as pd

dataFrame = pd.read_csv("Data\\company_sales_data.csv")

month_number = dataFrame["month_number"].tolist()
toothpaste = dataFrame["toothpaste"].tolist()

plt.scatter(month_number, toothpaste, marker="*", s=50)
plt.minorticks_on()
plt.grid(b=True, which="both", linestyle="--")
plt.title("toothpaste sales data of each month")
plt.xlabel("toothpaste")
plt.ylabel("toothpaste Sale")
plt.show()

