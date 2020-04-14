import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import pandas as pd
import scipy as sp

df = pd.read_csv('MDG_Export_20191227.csv')
print(df.head())

# 1.How many different countries are represented? How many missing values are there by country, year and series?

"""
How different  countruies are repreesented
"""
df['Country'].count()
print(df)


