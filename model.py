import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#read the csv file
df = pd.read_csv('overseas-trade-indexes-june-2023-quarter-provisional.csv')

#remove empty fields from file
no_empty_fields = df.