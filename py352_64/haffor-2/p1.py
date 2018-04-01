

import numpy
from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense

from keras.wrappers.scikit_learn import KerasRegressor


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
model.fit(x=X,y=Y,epochs=20000,batch_size=2000,validation_split=0.2)


pred=model.predict(x=X, batch_size=1000)
i=0
print (len(pred))
print (len(Y))
for i in range(1000):
    print('{} predicted, but {} is true value'.format(pred[i][0],Y[i]))



