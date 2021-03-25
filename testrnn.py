# first neural network with keras make predictions
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# load the dataset
dataset = loadtxt('dataset.csv', delimiter=',')
data = dataset[:, 0:8]
pred = dataset[:, 8]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(data, pred, epochs=150, batch_size=10, verbose=0)
# make class predictions with the model
predictions = model.predict_classes(data)
# summarize the first 5 cases
accuracy = 0
for i in range(100):
    print('%s => %d (expected %d)' % (data[i].tolist(), predictions[i], pred[i]))
# evaluate the keras model
_, accuracy = model.evaluate(data, pred)
print('Accuracy: %.2f' % (accuracy*100))
