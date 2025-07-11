# Import Libraries

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle


# Load the Dataset by using the pandas
dataset=pd.read_csv(r'C:\Users\LAHARI\Downloads\Salary_Data.csv')



# Split the data into independent and dependent variables
# Independent Variable 
X=dataset.iloc[:,:-1].values
# Dependent Variable
Y=dataset.iloc[:,-1].values


# Split the data into training and testing sets(80%-20%)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20,random_state=0)


# Train the model
regressor=LinearRegression()
regressor.fit(X_train,Y_train)

# Predict the test set
y_pred=regressor.predict(X_test)


# Visualize the training set
plt.scatter(X_train,Y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Salary vs Experience(Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# Visualize the testing set
plt.scatter(X_test,Y_test,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Salary vs Experience(Testing set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# slope is generated from linear regression algorithm which fit to dataset
m_slope=regressor.coef_


# intercept also generate by model
c_intercept=regressor.intercept_



# comparison predictions vs Actual
comparison=pd.DataFrame({'Actual':Y_test,'prediction':y_pred})



# Predict or forcast the future the data which we not trained before
# Predict the Salary for 12 and 20 years of experience using the trained model
# y=mx+c
# Prediction 1
y_12=(m_slope*12)+c_intercept
print(y_12)

# prediction 2
y_20=(m_slope*20)+c_intercept
print(y_20)


# Statistical 
# Mean
dataset.mean() # this will give mean of entire dataframe

dataset['Salary'].mean() # this will give us mean of that particular column


# Median
dataset.median() # this will give median of entire dataframe

dataset['Salary'].median() # this will give us median of that particular column


# Mode
dataset.mode() # this will give mode of entire dataframe

dataset['Salary'].mode() # this will give us mode of the particular column


# Variance
dataset.var() # this will give variance of entire dataframe

dataset['Salary'].var() # this will give us variance of that particular column


# Standard Deviation 
dataset.std() # this will give standard deviation of entire dataframe

dataset['Salary'].std() # this will give us standard deviation of that particular column


# Coefficient of Variation(CV)
# for calculating the CV we have to import a library first
from scipy.stats import variation
variation(dataset.values) # this will give CV of entire dataframe

variation(dataset['Salary']) # this will give us CV of that particular column
 

# Correlation
dataset.corr() # this willgive correlation of entire dataframe

dataset['Salary'].corr(dataset['YearsExperience']) # this will give us correlation 


# Skewness
dataset.skew() # this will give skewness of entire dataframe

dataset['Salary'].skew() # this will give us skewness of that particular column


# Standard Error
dataset.sem() # this wil give standard error of entire dataframe

dataset['Salary'].sem() # this will give us standard error of that particular column


# Z-score
# for calculating Z-score we have to import library first
import scipy.stats as stats
dataset.apply(stats.zscore) # this will give Z-score of entire dataframe

stats.zscore(dataset['Salary']) # this will give us Z-score of that particular column


# Degree of Freedom
a=dataset.shape[0] # this will gives us no.of rows
b=dataset.shape[1] # this will gives us no.of columns

degree_of_freedom=a-b 
print(degree_of_freedom) # this will give us degree of freedom for entire dataset


# Sum of Squares Regression(SSR)
y_mean=np.mean(Y)
SSR = np.sum((y_pred-y_mean)**2)
print(SSR)


# Sum of Squares Error(SSE)
Y = Y[0:6]
SSE = np.sum((Y-y_pred)**2)
print(SSE)

# Sum of Squares Total(SST)
mean_total=np.mean(dataset.values) # here dataset.to_numpy() will convert pandas Dataframe to 
SST=np.sum((dataset.values-mean_total)**2)
print(SST)


# R-Square
r_square=SSR/SST
r_square



# Check model performances
# to check overfitting(low bias high variance)
bias=regressor.score(X_train,Y_train)
print(bias)

# to check Underfitting (high bias low variance)
variance=regressor.score(X_test,Y_test)
print(variance)
train_mse=mean_squared_error(Y_train,regressor.predict(X_train))
print()
test_mse=mean_squared_error=(Y_test,y_pred)



# Save the trained model to disk
filename='linear_regression_model.pkl'
# Open a file in write-binary mode and dump the model
with open(filename,'wb') as file:
    pickle.dump(regressor,file)
print("model has been pickled and saved as linear_regression_model.pkl")

import os
os.getcwd()



