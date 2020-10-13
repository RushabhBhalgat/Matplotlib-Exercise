'''
Exercise Question 3: Read all product sales data and show it  using a multiline plot

Display the number of units sold per month for each product using multiline plots. 
(i.e., Separate Plotline for each product ).

'''
import matplotlib.pyplot as plt
import pandas as pd

dataFrame = pd.read_csv("Data\\company_sales_data.csv")
#print(dataFrame)

month_number = dataFrame["month_number"].tolist()
facecream = dataFrame["facecream"].tolist()
facewash = dataFrame["facewash"].tolist()
toothpaste = dataFrame["toothpaste"].tolist()
bathingsoap = dataFrame["bathingsoap"].tolist()
shampoo = dataFrame["shampoo"].tolist()
moisturizer = dataFrame["moisturizer"].tolist()

plt.plot(month_number, facecream, label="Face Cream Sales Data", marker="x", linewidth="3")
plt.plot(month_number, facewash, label="Facewash Sales Data", marker="x", linewidth="3")
plt.plot(month_number, toothpaste, label="toothpaste Sales Data", marker="x", linewidth="3")
plt.plot(month_number, bathingsoap, label="bathingsoap Sales Data", marker="x", linewidth="3")
plt.plot(month_number, shampoo, label="shampoo Sales Data", marker="x", linewidth="3")
plt.plot(month_number, moisturizer, label="moisturizer Sales Data", marker="x", linewidth="3")

plt.title("Product sales data")
plt.xlabel("month_number")
plt.ylabel("Product Sales")
plt.legend()
plt.show()