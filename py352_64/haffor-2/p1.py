# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense
<<<<<<< HEAD

from keras.wrappers.scikit_learn import KerasRegressor


dataframe = read_csv('P1regression.csv',  header=None)
dataset = dataframe.values


=======
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)
# load pima indians dataset
dataset = numpy.loadtxt("P1regression.csv", delimiter=",")

# split into input (X) and output (Y) variables
>>>>>>> b5cf4ff745194b695e2bef7b3f4c851bd332b8e7
X = dataset[:,0:3]
Y = dataset[:,3]
<<<<<<< HEAD
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

print (len(pred))
print (len(Y))
for i in range(1000):
    print('{} predicted, but {} is true value'.format(pred[i][0],Y[i]))



=======
# create model 
model = Sequential()
model.add(Dense(12, input_dim=3, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=150, batch_size=10)
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
>>>>>>> b5cf4ff745194b695e2bef7b3f4c851bd332b8e7
