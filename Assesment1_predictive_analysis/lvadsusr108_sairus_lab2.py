# -*- coding: utf-8 -*-
"""LVADSUSR108_Sairus_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SV7zKbBGhbfM4fllI3Az_PNxj27KQTqc
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

var_booking_data = pd.read_csv('/content/booking.csv')
var_booking_data.head()

missing_values_booking = var_booking_data.isnull().sum()
missing_values_booking

duplicates_booking = var_booking_data.duplicated().sum()

duplicates_booking

import seaborn as sns
import matplotlib.pyplot as plt
fig, axs = plt.subplots(4, figsize=(5, 10))

sns.boxplot(var_booking_data['number of adults'], ax=axs[0]).set_title('Number of Adults Distribution')
sns.boxplot(var_booking_data['number of children'], ax=axs[1]).set_title('Number of Children Distribution')
sns.boxplot(var_booking_data['lead time'], ax=axs[2]).set_title('Lead Time Distribution')
sns.boxplot(var_booking_data['average price'], ax=axs[3]).set_title('Average Price Distribution')

plt.tight_layout()
plt.show()

# encodding
var_encoded = pd.get_dummies(var_booking_data,
                        columns=['type of meal', 'room type', 'market segment type', 'booking status'], drop_first=True)
var_encoded.drop(['Booking_ID', 'date of reservation'], axis=1, inplace=True)
var_encoded

# Dividing the data
var_X_booking = var_encoded.drop('booking status_Not_Canceled', axis=1)
var_y_booking = var_encoded['booking status_Not_Canceled']
var_X_train_booking, var_X_test_booking, var_y_train_booking, var_y_test_booking = train_test_split(var_X_booking, var_y_booking, test_size=0.2, random_state=42)

var_X_booking.shape

var_y_booking.shape

model_booking = LogisticRegression(max_iter=10000)
model_booking.fit(var_X_train_booking, var_y_train_booking)

y_pred_booking = model_booking.predict(var_X_test_booking)

# Model Evaluation
accuracy = accuracy_score(var_y_test_booking, y_pred_booking)
precision = precision_score(var_y_test_booking, y_pred_booking)
recall = recall_score(var_y_test_booking, y_pred_booking)
f1 = f1_score(var_y_test_booking, y_pred_booking)
conf_matrix = confusion_matrix(var_y_test_booking, y_pred_booking)

print(f'Accuracy: {accuracy}\nPrecision: {precision}\nRecall: {recall}\nF1-Score: {f1}\nConfusion Matrix: \n{conf_matrix}')

# Above CF states that:-
# True Negative (TN): 1471
# False Positive (FP): 931
# False Negative (FN): 510
# True Positive (TP): 4345
# It highlights the balance between true positives, true negatives, and the respective errors (false positives and negatives).
# In my opinion it is quite good but not that good can be imporved.













