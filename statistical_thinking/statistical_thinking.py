import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import pandas as pd
import scipy as sp

data = pd.read_csv('MDG_Export_20191227.csv')
df = pd.DataFrame(data ,columns=['Country', 'year', 'series'])
# print(data.describe())

# 1.How many different countries are represented? How many missing values are there by country, year and series?

"""
How different  countruies are represented
"""
df_num_countries = len(df.groupby('Country'))
print(df_num_countries)

"""
How many missing values are there by country, year and series?

"""
print((len(df[df.isnull().any(axis=1)])))