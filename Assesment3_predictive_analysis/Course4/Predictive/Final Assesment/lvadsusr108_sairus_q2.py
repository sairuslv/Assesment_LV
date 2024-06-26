# -*- coding: utf-8 -*-
"""LVADSUSR108_Sairus_Q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zT4RGQrMobcY_08emsMKNyZ4_XtjTBzv
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data= pd.read_csv('/content/auto-mpg.csv')
data.head()

data.info()

data.isnull().sum()

var_mpg_df=data
var_mpg_df.dropna(inplace=True)
var_mpg_df = var_mpg_df[var_mpg_df.horsepower != '?']  # Remove '?' entries in horsepower
var_mpg_df['horsepower'] = var_mpg_df['horsepower'].astype(float)

plt.figure(figsize=(8, 6))
sns.distplot(var_mpg_df['mpg'])
plt.title('Distribution of Miles per Gallon (mpg)')
plt.xlabel('Miles per Gallon (mpg)')
plt.ylabel('Density')
plt.show()

sns.pairplot(var_mpg_df[['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration']])
plt.show()

numerical_cols = ['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration']
z_scores = np.abs(stats.zscore(var_mpg_df[numerical_cols]))
var_mpg_df_clean = var_mpg_df[(z_scores < 3).all(axis=1)]

var_X = var_mpg_df_clean[numerical_cols]
var_y = var_mpg_df_clean['mpg']

var_X_train, var_X_test, var_y_train, var_y_test = train_test_split(var_X, var_y, test_size=0.2, random_state=42)

scaler = StandardScaler()
var_X_train_scaled = scaler.fit_transform(var_X_train)
var_X_test_scaled = scaler.transform(var_X_test)

model = LinearRegression()
model.fit(var_X_train_scaled, var_y_train)

var_y_pred = model.predict(var_X_test_scaled)
rmse = mean_squared_error(var_y_test, var_y_pred, squared=False)
r2 = r2_score(var_y_test, var_y_pred)

print(f'Root Mean Square Error (RMSE): {rmse}')
print(f'R-squared (R²): {r2}')















