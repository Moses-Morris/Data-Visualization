import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#read the csv file
df = pd.read_csv('overseas-trade-indexes-june-2023-quarter-provisional.csv')

#remove empty fields from file
no_empty_fields = df.dropna()

print(no_empty_fields.head(8))


#print the columns only
print("Here are the columns:")
print(df.columns)

x = df["Period"]
y = df["Data_value"]
#plot a line chart
plt.plot(x,y, marker='.', linestyle='-', color='r', label='line label')
plt.xlabel('Yearly')
plt.ylabel('Data_value')
plt.legend()
plt.title('Overseas Trade Indexes')
plt.grid(True)
plt.show()


