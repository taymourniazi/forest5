# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:43:15 2018

@author: asd
"""

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn

# importing dataset
# first locate file directory in file explorer
dataset = pd.read_csv('forest5.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

# the following line will display dataframe in spyder as before it shows 
# an error - object arrays are currenlty not supported
dX = pd.DataFrame(X)
dY = pd.DataFrame(Y)
# Or there is one more option to view with following piece of code
np.set_printoptions(threshold=100)
X
#OR more simply
print(X)

#Dealing with missing values in column
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

#Encoding Categorical Variable
#The following lines create a class to categorical variable Country
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
#following line assign the first indices country
X[:, 0]=labelencoder_X.fit_transform(X[:, 0])

#creating dummy variables to assign country to number rather then it size
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

"""now handling dependant variable y in which we dont use onehotencoder as system-
#knows its a categorical variable"""
# Remember Y is the 'Purchased' Variable
labelencoder_Y = LabelEncoder()
Y=labelencoder_Y.fit_transform(Y)

##splitting datset into training and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

'''feature scaling allows to put different range of data into same scale like age and salary'''
#feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
