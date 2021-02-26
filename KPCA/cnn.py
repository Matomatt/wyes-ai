"""
Created on Wed Nov 25 16:54:45 2020
@author: Syl
https://www.datacamp.com/community/tutorials/convolutional-neural-networks-python
https://www.datatechnotes.com/2020/02/classification-example-with-keras-cnn.html

https://machinelearningmastery.com/cnn-models-for-human-activity-recognition-time-series-classification/
"""

from keras.models import Sequential
from keras.layers import Dense, Conv1D, Flatten, MaxPooling1D
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_iris
from numpy import unique
import numpy as np
from movement import Movement
from movement import showResult



"""
x = [[[0.2], [0.6], [0.2], [0.1]], 
     [[1.2], [1.6], [1.2], [1.1]], 
     [[2.2], [2.6], [2.2], [2.1]]]


y = [0, 1, 2]
"""

def create_cnn(x, y):
    xtrain, xtest, ytrain, ytest=train_test_split(x, y, test_size=0.15)    
    model = Sequential()

    model.add(Conv1D(64, 2, activation="relu", input_shape=(len(x),len(x[0]), len(x[0][0]),1)))
    
    model.add(Dense(16, activation="relu"))
    
    model.add(MaxPooling1D())

    model.add(Flatten())
    model.add(Dense(unique(y).sum(), activation = 'softmax'))
    model.compile(loss = 'sparse_categorical_crossentropy', 
         optimizer = "adam",               
                  metrics = ['accuracy'])
    model.summary()
    
    print(xtrain)
    print(xtrain[0])
    
    print(ytrain)

    model.fit(xtrain, ytrain, batch_size=16,epochs=100, verbose=0)
    
    print('\n ' + '*'*15 + 'Fin du programme ' + '*'*15 )
    
    
    
    acc = model.evaluate(xtrain, ytrain)
    print("Loss:", acc[0], " Accuracy:", acc[1])
    
    pred = model.predict(xtest)
    pred_y = pred.argmax(axis=-1)
    
    cm = confusion_matrix(ytest, pred_y)
    print(cm)

    return model 


m = Movement(3,10,19,12)

m.readFromCsv("datasetbis.csv") 
m.describe()
mov = m.dimensionReduction(numberOfDimension = 1)

x = np.reshape(mov, (30,2,19 ,1))

y = []
for i in range (len(mov)):
    y.append(int(i/10))

y = np.array(y)

model = create_cnn(x,y)

