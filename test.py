print("First neural network with keras\nImporting libraries...");

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

print("Libraries loaded.\nLoading dataset...");

dataset = loadtxt('pima-indians-diabetes.data.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]

print("Dataset loaded.\nDefining the keras model...");

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

print("Model defined.\nCompiling the model...");

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

print("Model compiled.\nTraining...");

model.fit(X, y, epochs=150, batch_size=10)

print("Training omplete !\nLet's evaluate our network :");
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
