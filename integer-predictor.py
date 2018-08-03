import numpy as np
np.set_printoptions(threshold=np.inf)
import pandas as pd
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings(action="ignore", module="sklearn", message="^internal gelsd")

# defs
print('Program expects comma-separated list of integers in column in .csv file (see README.md for example).\n')


def linearizer(lowerLimit, upperLimit): # including lower and upper limit!
    upperLimit += 1
    out = []
    while (lowerLimit < upperLimit):
        out.append(lowerLimit)
        lowerLimit += 1
    return out 


# get and prepare Data
inputFile = input('Please specify input file (eg. example.csv): ')
inputData = pd.read_csv(inputFile, delimiter=',', header=None)
y = inputData.iloc[:,0]  #select first column, next column would be [:,1] etc.
length_y = len(y.index)

x = []
x = linearizer(0, (length_y - 1)) #minus 1 to compensate for position 0
###


x = pd.DataFrame(x) #convert from simple Python array to pd dataframe (as supported by sklearn)


# fit&predict
model = LinearRegression()
model.fit(x, y)
positionsToPredict = input('For how many positions do you want to predict ahead (int)? ')
positionsToPredict = int(positionsToPredict)

new_data = linearizer(length_y, (positionsToPredict + length_y))

new_data = pd.DataFrame(new_data)
prediction = model.predict(new_data)

#prediction = prediction.DataFrame.to_string()
print('\nPredictions based on Linear Regression:\n\n',prediction)