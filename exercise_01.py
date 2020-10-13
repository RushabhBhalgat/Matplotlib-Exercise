'''
Exercise 1: Read Total profit of all months and show it using a line plot
'''
import matplotlib.pyplot as plt
import pandas as pd

data_frame = pd.read_csv("Data\\company_sales_data.csv")
#print(data_frame)
x = data_frame["month_number"].tolist()
#print(x)
y = data_frame["total_profit"].tolist()
#print(y)
plt.plot(x, y, label="Profit Made Each Month")
plt.title("Read Total profit of all months")
plt.xlabel("month_number")
plt.ylabel("total_profit")
plt.legend()
plt.show()