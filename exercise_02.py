'''
Exercise Question 2: Get Total profit of all months and show line plot with the following Style properties

Generated line plot must include following Style properties: –

1. Line Style dotted and Line-color should be red
2. Show legend at the lower right location.
3. X label name = Month Number
4. Y label name = Sold units number
5. Add a circle marker.
6. Line marker color as read
7. Line width should be 3
'''

import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("Data\\company_sales_data.csv")
y = df ['total_profit'].tolist()
x  = df ['month_number'].tolist()

plt.plot(x, y, label = 'Profit data of last year', color='r', marker='o', markerfacecolor='k', linestyle='--', linewidth=3)
      
plt.xlabel('Month Number')
plt.ylabel('Profit in dollar')
plt.legend(loc='lower right')
plt.title('Company Sales data of last year')
plt.show()