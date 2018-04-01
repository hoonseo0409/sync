# Regression Example With Boston Dataset: Baseline
import numpy
from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pandas as pd

"""
# load dataset
#dataset = read_csv("P1regression.csv", delim_whitespace=True, header=None)
dataset = pd.read_csv('P1regression.csv')
#dataset = dataframe.values
# split into input (X) and output (Y) variables
print (dataset)
X = dataset[0:3]
Y = dataset[3]
# define base model
"""

dataframe = read_csv('P1regression.csv',  header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables

X = dataset[:,0:3]
print(X)

Y = dataset[:,3]
print (Y)
def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(13, input_dim=3, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# evaluate model
estimator = KerasRegressor(build_fn=baseline_model, epochs=100, batch_size=5, verbose=0)
kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(estimator, X, Y, cv=kfold)
print("Baseline: %.2f (%.2f) MSE" % (results.mean(), results.std()))