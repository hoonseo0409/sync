

import numpy
from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

dataframe = read_csv('P1regression.csv',  header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables

X = dataset[:,0:3]
print(len(X[0]))

Y = dataset[:,3]
print (len(Y))

# create model
model = Sequential()
model.add(Dense(20, input_dim=3, kernel_initializer='normal', activation='relu'))
model.add(Dense(10, input_dim=3, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))
# Compile model
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x=X,y=Y,epochs=500,batch_size=256,validation_split=0.2)


"""
# define wider model
def wider_model():
    # create model
    model = Sequential()
    model.add(Dense(20, input_dim=3, kernel_initializer='normal', activation='linear'))
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# evaluate model with standardized dataset
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(build_fn=model, epochs=100, batch_size=5,
verbose=0)))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(pipeline, X, Y, cv=kfold)
print (results)
print("Wider: %.2f (%.2f) MSE" % (results.mean(), results.std()))
"""