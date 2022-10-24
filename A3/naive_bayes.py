#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 5990- Assignment #3
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

import pandas as pd
import numpy as np
from feature_engine.discretisation import EqualFrequencyDiscretiser
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score
from sklearn.preprocessing import KBinsDiscretizer
import warnings

warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', 10)
features = ['Year', 'Month', 'Day', 'Hour', 'Humidity', 'Wind Speed (km/h)', 'Wind Bearing (degrees)',
            'Visibility (km)', 'Pressure (millibars)', 'Temperature (C)']

#11 classes after discretization
classes = [i for i in range(-22, 40, 6)]

#reading the training data
df_train = pd.read_csv('weather_training.csv')
# print(df_train)
# print("Before")
# print(df_train.dtypes)
# df_train = df_train.copy()
df_train['Formatted Date'] = pd.to_datetime(pd.read_csv('weather_training.csv')['Formatted Date'], format='%Y-%m-%d %H:%M:%S.%f %z')
df_train['Year'] = df_train['Formatted Date'].apply(lambda x: x.year)
df_train['Month'] = df_train['Formatted Date'].apply(lambda x: x.month)
df_train['Day'] = df_train['Formatted Date'].apply(lambda x: x.day)
df_train['Hour'] = df_train['Formatted Date'].apply(lambda x: x.hour)
df_train['Humidity'] = df_train['Humidity'].apply(lambda x: x*100)
# df_train = df_train.astype({'Wind Bearing (degrees)': 'int', 'Year': 'int', 'Month': 'int', 'Day': 'int', 'Hour': 'int'})
df_train = df_train.astype({'Humidity': 'int', 'Wind Speed (km/h)': 'int', 'Visibility (km)': 'int', 'Pressure (millibars)': 'int', 'Temperature (C)': 'int'})
df_train = df_train.drop('Formatted Date', axis=1)
# print("After")
# print(df_train.dtypes)

#reading the test data
df_test = pd.read_csv('weather_test.csv')
# print("Before")
# print(df_test.dtypes)
# df_test = df_test.copy()
df_test['Formatted Date'] = pd.to_datetime(pd.read_csv('weather_test.csv')['Formatted Date'], format='%Y-%m-%d %H:%M:%S.%f %z')
df_test['Year'] = df_test['Formatted Date'].apply(lambda x: x.year)
df_test['Month'] = df_test['Formatted Date'].apply(lambda x: x.month)
df_test['Day'] = df_test['Formatted Date'].apply(lambda x: x.day)
df_test['Hour'] = df_test['Formatted Date'].apply(lambda x: x.hour)
df_test['Humidity'] = df_test['Humidity'].apply(lambda x: x*100)

# df_test = df_test.astype({'Wind Bearing (degrees)': 'int', 'Year': 'int', 'Month': 'int', 'Day': 'int', 'Hour': 'int'})
df_test = df_test.astype({'Humidity': 'int', 'Wind Speed (km/h)': 'int', 'Visibility (km)': 'int', 'Pressure (millibars)': 'int', 'Temperature (C)': 'int'})
df_test = df_test.drop('Formatted Date', axis=1)
# print("After")
# print(df_test.dtypes)

X_training = df_train[features[:len(features)-1]]
# print(X_training)
y_training = df_train[features[len(features)-1]]
#print(y_training)

# X_training, X_test, y_training, y_test = train_test_split(X, y, test_size=(len(df_test)/len(df_train)), random_state=0)
# Use test set instead of test split
X_test = df_test[features[:len(features)-1]]
# print(X_test)
y_test = df_test[features[len(features)-1]]
# print(y_test)

# del X_test["Temperature (C)"]


#update the training class values according to the discretization (11 values only)
#update the test class values according to the discretization (11 values only)

disc = KBinsDiscretizer(n_bins=11, encode='ordinal').fit(X_training)
X_training = disc.transform(X_training)
print("X train")
print(X_training)

disc = KBinsDiscretizer(n_bins=11, encode='ordinal').fit(X_test)
X_test = disc.transform(X_test)
print()
print("X test")
print(X_test)

# disc = EqualFrequencyDiscretiser(q=11, variables=features[:len(features)-1]).fit(X_training)
# X_training = disc.transform(X_training)
#
# disc = EqualFrequencyDiscretiser(q=11, variables=features[:len(features)-1]).fit(X_test)
# X_test = disc.transform(X_test)
#
# #fitting the naive_bayes to the data
clf = GaussianNB()
clf = clf.fit(X_training, y_training)
#
# #make the naive_bayes prediction for each test sample and start computing its accuracy
# #the prediction should be considered correct if the output value is [-15%,+15%] distant from the real output values
# #to calculate the % difference between the prediction and the real output values use: 100*(|predicted_value - real_value|)/real_value))
# #print the naive_bayes accuracy
y_prediction = clf.predict(X_test)

accurate = 0
for i in range(len(y_prediction)):
    difference = 100 * (abs(y_prediction[i] - y_test[i]) / y_test[i])
    if 15 > difference > -15:
        accurate += 1

accuracy = accurate / len(y_prediction)

print(f'naive_bayes accuracy: {accuracy}')



