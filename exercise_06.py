'''
Exercise Question 6: Read sales data of bathing soap of all months and show it using a bar chart.
Save this plot to your hard disk

'''
import matplotlib.pyplot as plt
import pandas as pd 

dataFrame = pd.read_csv("Data\\company_sales_data.csv")

month_number = dataFrame["month_number"].tolist()
bathingsoap = dataFrame["bathingsoap"].tolist()

plt.bar(month_number, bathingsoap, label="Bathing Soap Sales", )
plt.title("bathing soap of all months")
plt.xlabel("month_number")
plt.ylabel("Bathing Soap Sales")
plt.grid(b=True, which="major", linewidth= 1, linestyle="--")
plt.legend()
plt.show()


