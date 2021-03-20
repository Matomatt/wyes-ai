import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPen, QTransform
from PyQt5.QtCore import Qt, QTimer
from math import sqrt, atan, cos, sin, pi
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime
import serial
import time
import global_variables as gv

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        ##Window
        self.title = 'Glasses calibration'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 200
        self.sampleRate = 200
        self.calibrationTime = 3
        self.lastSampledValues = []
        self.means = []
        ##Init
        self.initUI()
        self.counter = 0
        self.counterThreshold = self.calibrationTime * self.sampleRate

        self.sampleTimer=QTimer()
        self.sampleTimer.timeout.connect(self.sample)
        self.sampleTimer.start(int(1000/self.sampleRate))


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #Labels
        self.recordingLabel = QLabel(self)
        self.recordingLabel.setText("Restez immobile pendant 3 secondes s'il-vous plait")
        self.recordingLabel.move(0,0)
        self.recordingLabel.resize(300, 20)

        self.show()

    def sample(self):
        line = (str(gv.esp.readline())[18:][:-7]).split(',')
        if (len(line)!=7): return;

        captValList = []
        for l in line:
            try: captValList.append(int(l.split(':')[1]))
            except: print(line);  return;

        captValList = captValList[:6]
        if len(self.lastSampledValues) < 6: self.lastSampledValues = captValList; return;
        mean=0
        for i in range(len(captValList)):
            mean += abs(self.lastSampledValues[i] - captValList[i])/6
        self.means.append(mean)
        self.lastSampledValues = captValList

        self.counter+=1
        if (self.counter > self.counterThreshold): self.close()



def start():
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
    print("LEN MEAN", len(ex.means))
    try:
        means = ex.means[int(len(ex.means)/3):int(len(ex.means)*2/3)]
    except:
        means = [gv.minThreshold]
    ex.destroy()

    return max(means)
