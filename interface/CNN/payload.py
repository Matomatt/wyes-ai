
from CNN.movement import Movement
from CNN.movement import showResult


from keras.models import Sequential
from keras.layers import Dense, Conv1D, Flatten, MaxPooling1D
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_iris
from numpy import unique
import numpy as np
import random
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
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import to_categorical

def shuffleData(x, y):
    c = list(zip(x,y))
    random.shuffle(c)
    x, y = zip(*c)
    return x, y

def splitData(data , percent = 0.6, number_of_movements = 10):
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

    for i in range(len(x_train)):
        for j in range(len(x_train[i])):
            x_train[i][j] = x_train[i][j].tolist()

    for i in range(len(x_test)):
        for j in range(len(x_test[i])):
            x_test[i][j] = x_test[i][j].tolist()


    x_train1 = []
    # 30 6 38
    # 30 12 19
    for i in range(len(x_train)):
        temp = []
        for j in range(len(x_train[i])):
            temp.append(x_train[i][j])
        x_train1.append(temp)
        #x_train1.append(x_train[i][0])
        #x_train1.append(x_train[i][1])
        #x_train1[i].extend(x_train[i][1])


    x_test1 = []
    for i in range(len(x_test)):
        temp = []
        for j in range(len(x_test[i])):
            temp.append(x_test[i][j])
        x_test1.append(temp)

    # x_train1 , y_train = shuffleData(x_train1 , y_train)
    # x_test1, y_test = shuffleData(x_test1, y_test)

    return np.array(x_train1) , np.array(y_train), np.array(x_test1), np.array(y_test)


def createModel(xtrain1): # 30 12 19
    print('create model function ')
    print("LEN X", len(xtrain1), len(xtrain1[0]), len(xtrain1[0][0]))
    n_captors, n_timesteps, n_outputs = len(xtrain1[0]), len(xtrain1[0][0]) , 3
    print("TIME STEP", n_timesteps, "CAPTORS", n_captors)

    model = Sequential()

    model.add(Convolution2D(32, (3, 3), activation="relu", input_shape=(n_captors, n_timesteps, 1)))
    print ("INPUT SHAPE", model.input_shape)

    model.add(Convolution2D(32, (3, 3), activation="relu"))
    # model.add(MaxPooling2D(pool_size=(2,2)))
    # model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512, activation="relu"))
    model.add(Dropout(0.1))
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(n_outputs, activation="softmax"))
    print ("OUTPUT SHAPE", model.output_shape)

    model.compile(loss='categorical_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])
    model.summary()

    return model

def uniformData(mov):
    for i in range(len(mov)): #30
        mov_ = []
        for j in range(len(mov[0])): #12
            mov_.append(max(mov[i][j]))
        mov[i] /= max(mov_)
    return mov

def loadData(nameFile = "CNN/datasetbis.csv"):
    print('load data function ')
    m = Movement(3,10,19,12)
    m.readFromCsv(nameFile)
    m.describe()
    return uniformData(m.getMovements())

def train(model,xtrain1, ytrain, xtest1 , ytest):
    verbose, epochs, batch_size = 0, 100, len(xtrain1)
    print(ytrain)
    print("LEN Y", len(ytrain), len(ytrain[0]))
    print('train model function ')
    model.fit(xtrain1, ytrain, epochs=epochs, batch_size=batch_size, verbose=verbose)
    _, accuracy = model.evaluate(xtest1, ytest, batch_size=batch_size, verbose=0)
    print(f'accuracy :\t {accuracy}')
    return model

def predict():
    print('predict function ')
