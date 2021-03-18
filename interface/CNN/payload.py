
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
import pandas as pd
from matplotlib import pyplot
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import to_categorical, np_utils

def shuffleData(x, y):
    c = list(zip(x,y))
    random.shuffle(c)
    x, y = zip(*c)
    return x, y

def splitData(data , splitRatio = 0.6):
    print('split data function model')

    X = []
    Y = []
    for movementID in range(len(data)):
        for essai in data[movementID]:
            X.append(essai)
            Y.append(movementID)

    nbMovementToClassify = max(Y)

    # Shuffling the dataset
    df = pd.DataFrame({'X': X, 'Y': Y})
    print(df)
    df = df.sample(frac = 1)
    print(df)

    # Splitting the dataset
    X_train = list(df['X'])[:int(len(X)*splitRatio)]
    X_test = list(df['X'])[int(len(X)*splitRatio):]
    Y_train = list(df['Y'])[:int(len(Y)*splitRatio)]
    Y_test = list(df['Y'])[int(len(Y)*splitRatio):]

    # Convert 1-dimensional class arrays to nbMovementToClassify-dimensional class matrices
    Y_train = np_utils.to_categorical(Y_train, nbMovementToClassify+1)
    Y_test = np_utils.to_categorical(Y_test, nbMovementToClassify+1)

    # Make it compatible with the convolution2D layer
    X_train = np.expand_dims(X_train, -1)
    X_test = np.expand_dims(X_test, -1)

    return X_train, Y_train, X_test, Y_test


def createModel(X_train, Y_train): # 30 12 19
    print('create model function ')
    print("LEN X", len(X_train), len(X_train[0]), len(X_train[0][0]))
    n_captors, n_timesteps, n_outputs = len(X_train[0]), len(X_train[0][0]) , len(Y_train[0])
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

def loadData(fileName = "datasetTest"):
    # open the file in read binary mode
    file = open(fileName, "rb")
    #read the file to numpy array
    return np.load(file, allow_pickle=True)

def loadDataOldFormat(nameFile = "CNN/datasetbis.csv"):
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
