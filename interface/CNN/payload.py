from CNN.movement import Movement
from CNN.movement import showResult


from keras.models import Sequential
from keras.layers import Dense, Conv1D, Flatten, MaxPooling1D
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_iris
from numpy import unique
import numpy as np

# cnn model
from numpy import mean
from numpy import std
from numpy import dstack
from pandas import read_csv
from matplotlib import pyplot
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.utils import to_categorical


def splitData(data , percent = 0.9, number_of_movements = 10):
    print('split data function model')
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    for i in range(len(data)):
        if i%number_of_movements < number_of_movements*percent:
            y_train.append(int((i- i%number_of_movements)/number_of_movements))
            x_train.append(data[i])
        else:
            y_test.append(int((i- i%number_of_movements)/number_of_movements))
            x_test.append(data[i])
    try:
        for i in range(len(x_train)):
            for j in range(len(x_train[i])):
                x_train[i][j] = x_train[i][j].tolist()

        for i in range(len(x_test)):
            for j in range(len(x_test[i])):
                x_test[i][j] = x_test[i][j].tolist()
    except:
        print('',end='')

    x_train1 = []
    # 30 6 38
    # 30 12 19
    for i in range(len(x_train)): #30 12 19 
        x_train1.append(x_train[i][0])
        x_train1.append(x_train[i][1])
        #x_train1[i].extend(x_train[i][1])


    x_test1 = []
    for i in range(len(x_test)):
        x_test1.append(x_test[i][0])
        x_test1.append(x_test[i][1])
        #x_test1[i].extend(x_test[i][1])

    return x_train1 , y_train , x_test1, y_test

def createModel(xtrain1, ytrain ,verbose = 0,epochs = 10,batch_size= 32): # 30 12 19 
    print('create model function ')
    n_timesteps, n_features, n_outputs = len(xtrain1[0]), len(xtrain1[0][0]) , 1
    model = Sequential()

    model.add(Convolution2D(32, (3, 3), activation="relu", input_shape=(12,19,1)))
    print (model.output_shape)

    model.add(Convolution2D(32, (3, 3), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(512, activation="relu"))
    model.add(Dropout(0.6))
    model.add(Dense(3, activation="softmax"))

    model.compile(loss='categorical_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])
    model.summary()
    model.fit(xtrain1, ytrain, epochs=epochs, batch_size=batch_size, verbose=verbose)

    return model

def loadData(nameFile = "CNN/datasetbis.csv"):
    print('load data function ')
    m = Movement(3,10,19,12)
    m.readFromCsv(nameFile)
    m.describe()
    return m.dimensionReduction(numberOfDimension = 6) #30 2 19 6

def train(model,xtrain1, ytrain, xtest1 , ytest):
    verbose, epochs, batch_size = 0, 10, 32
    print('train model function ')
    model.fit(xtrain1, ytrain, epochs=epochs, batch_size=batch_size, verbose=verbose)
    _, accuracy = model.evaluate(xtest1, ytest, batch_size=batch_size, verbose=0)
    print(f'accuracy :\t {accuracy}')
    return model

def predict():
    print('predict function ')
