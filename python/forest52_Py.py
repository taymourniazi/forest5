# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:19:52 2018

@author: asd
"""

#Simple Linear Regression
#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn

# importing dataset
# first locate file directory in file explorer
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, 0].values
Y = dataset.iloc[:, 1].values


from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

#feature scaling allows to put different range of data into same scale like age and salary
#feature scaling
""" we dont need feature scaling in simple lnear regression"""
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""


#I got an error ValueError: Expected 2D array, got 1D array instead
"""this folloing code will change your 1D array to 2d array as show invariable explorer 
name Size"""
"""
X_train=X_train.reshape(-1,1)
X_test=X_test.reshape(-1,1)
Y_train=Y_train.reshape(-1,1)
Y_test=Y_test.reshape(-1,1)
Y=Y.reshape(-1,1)
X=X.reshape(-1,1)"""

#Fitting Simple Linear Regression Model to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predicting the test set results
y_pred = regressor.predict(X_test)

#plotting the data observation FOR TRAIN DATA with help of matplotlib
plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()

#plotting the data observation FOR test Data with help of matplotlib
plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()
