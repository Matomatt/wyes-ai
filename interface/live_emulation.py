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

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        ##Window
        self.title = 'Skin around the eyes movements simulation'
        self.left = 10
        self.top = 10
        self.width = 1040
        self.height = 1040
        self.FPS=60
        ##Sampling
        self.lastMousePosition=[None, None]
        self.mousePressed = False
        self.sampleRate = 200
        self.lastSample = [0]*12;
        self.circleSpeed = 1;
        self.selectedCircles=[False]*3
        ##Processing
        self.initProcessing();
        ##Init
        try:
            self.esp = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)
        except:
            self.esp = None
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        ##Captors
        self.captors = [333,0, 666,0, 1025,500, 666,1020, 333,1020, 0,500]
        self.rotation =  [0, 0, 90, 180, 180, 270]
        captors=[]
        for i in range(0,6):
            captor = QLabel(self)
            img = QPixmap('ir-detector-small.png')
            transform = QTransform().rotate(self.rotation[i])
            img = img.transformed(transform, Qt.SmoothTransformation)
            captor.setPixmap(img)
            captor.move(self.captors[i*2]-5, self.captors[i*2+1]-5)
            captors.append(captor)
        self.circles = [200,640,200, 410,340,360, 750,480,280]
        self.circlesInitPos = self.circles.copy()
        ##Timers
        self.sampleTimer=QTimer()
        self.sampleTimer.timeout.connect(self.sample)
        self.sampleTimer.start(int(1000/self.sampleRate))
        self.backToPosTimer=QTimer()
        self.backToPosTimer.timeout.connect(self.comeBackToPosition)
        self.backToPosTimer.start(int(1000/self.FPS))
        self.updateTimer=QTimer()
        self.updateTimer.timeout.connect(self.paintUpdate)
        self.updateTimer.start(int(1000/self.FPS))
        self.startProcessingTimer = QTimer()
        self.startProcessingTimer.timeout.connect(self.startProcessing)
        self.startProcessingTimer.start(self.processingStartAfter)
        self.show()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
        painter.drawRect(20,20,1020,1020)
        for i in range(0,3):
            painter.drawEllipse(int(self.circles[i*3]-self.circles[i*3+2]/2)+20, int(self.circles[i*3+1]-self.circles[i*3+2]/2)+20, int(self.circles[i*3+2]), int(self.circles[i*3+2]))

    def paintUpdate(self):
        self.update();

    def circleCollisions(self, i, j, distToMove):
        if (sqrt( (self.circles[i*3]-self.circles[j*3])**2 + (self.circles[i*3+1]-self.circles[j*3+1])**2 ) < self.circles[i*3+2]/2+self.circles[j*3+2]/2):
            dirVect = [self.circles[i*3]-self.circles[j*3], self.circles[i*3+1]-self.circles[j*3+1]]
            angle=atan(dirVect[1]/dirVect[0])+(self.circles[i*3]>self.circles[j*3])*pi;
            self.circles[j*3]+=distToMove*cos(angle);
            self.circles[j*3+1]+=distToMove*sin(angle);

    def comeBackToPosition(self):
        for i in range(0, 3):
            if (not self.selectedCircles[i]):
                distx=(self.circlesInitPos[i*3]-self.circles[i*3])*(self.circleSpeed/self.FPS)
                disty=(self.circlesInitPos[i*3+1]-self.circles[i*3+1])*(self.circleSpeed/self.FPS)
                if (abs(distx) + abs(disty) < 0.1):
                    continue
                dist = sqrt(distx**2 + disty**2)
                self.circles[i*3]+=distx
                self.circles[i*3+1]+=disty
                for j in range(0,3):
                    if (i!=j):
                        self.circleCollisions(i,j,dist);
                        self.circleCollisions(j,3-(i+j),dist);


    def mouseMoveEvent(self, event):
        for i in range(0, 3):
            if (self.selectedCircles[i]):
                # x = (event.x()-self.circles[i*3])
                # y = (event.y()-self.circles[i*3+1])
                # if ((abs(x)+abs(y))<0.01):
                #     continue
                # distx = (x/(abs(x)+abs(y)))*(self.circleSpeed*3/self.FPS)
                # disty = (y/(abs(x)+abs(y)))*(self.circleSpeed*3/self.FPS)
                distx = (event.x()-self.lastMousePosition[0]-20)
                disty = (event.y()-self.lastMousePosition[1]-20)
                dist = sqrt(distx**2 + disty**2)
                self.circles[i*3]+=distx
                self.circles[i*3+1]+=disty
                for j in range(0,3):
                    if (i!=j):
                        self.circleCollisions(i,j,dist);
                        self.circleCollisions(j,3-(i+j),dist);
        self.lastMousePosition[0] = event.x()-20;
        self.lastMousePosition[1] = event.y()-20;

    def mousePressEvent(self, event):
        self.mousePressed = True
        for i in range(0, 3):
            self.selectedCircles[i] = False
            if (self.mousePressed == True and sqrt( (event.x()-20-self.circles[i*3])**2 + (event.y()-20-self.circles[i*3+1])**2 ) < self.circles[i*3+2]/2):
                self.selectedCircles[i] = True

    def mouseReleaseEvent(self, e):
        self.mousePressed = False
        for i in range(0, 3):
            self.selectedCircles[i] = False

    def sample(self):
        distances=[600]*6
        for i in range(0,6):
            x = self.captors[i*2]-5
            y = self.captors[i*2+1]-5
            for j in range(0,3):
                cx=self.circles[j*3]+20
                cy=self.circles[j*3+1]+20
                cr=self.circles[j*3+2]/2
                angle=(self.rotation[i]-90)*pi/180
                vect=[int(cos(angle)), int(sin(angle))]
                if (abs(x-cx)<=cr and vect[1]!=0 or abs(y-cy)<=cr and vect[0]!=0):
                    dist = (abs(y-cy) + sqrt(abs(cr**2-(x-cx)**2))*vect[0])*abs(vect[0]) + (abs(x-cx) + sqrt(abs(cr**2-(y-cy)**2))*vect[1])*abs(vect[1])

                    if (abs(dist) < distances[i]):
                        distances[i] = abs(int(dist))
                        self.lastSample[i] = distances[i]
                        self.lastSample[i+6] = distances[i]
        self.statusBar().showMessage(' '.join(map(str, distances)))

    def getLastSampledValues(self):
        if (self.esp != None):
            line = str(esp.readline())
            line = line[2:len(line)-5]
            info = line.split(", ")
            liste = []
            for i in info:
                test = i
                if(test.isdigit()) :
                    liste.append(int(i))
            print (self.lastSample, " vs ", liste)
            return liste

        return self.lastSample

















    def initProcessing(self):
        self.processingStartAfter = 500
        self.processingCallInterval = 79
        self.numberOfSamples = 19
        self.record = [[0]*12]*self.numberOfSamples;
        self.processingLastSample = [0]*12
        self.counter = self.numberOfSamples
        self.counterPrefix = 0
        self.tresMin = 50
        self.tresMax = 140
        self.recording = False
        self.keepingLastValues = 2

    def startProcessing(self):
        self.processingLastSample = self.getLastSampledValues()[0:]
        self.processingTimer=QTimer()
        self.processingTimer.timeout.connect(self.processing)
        self.processingTimer.start(self.processingCallInterval)
        self.startProcessingTimer.stop()
        print("processing started")

    def processing(self): #called every processingCallInterval ms
        record = self.record[1:]

        arr = [0]*12
        mean = 0
        for i in range(len(arr)):
            arr[i] = self.getLastSampledValues()[i] - self.processingLastSample[i]
            mean += abs(arr[i])/len(arr)
        record.append(arr)

        self.record = record[0:]
        self.processingLastSample = self.getLastSampledValues()[0:]


        if (mean>=self.tresMin and mean <= self.tresMax and not self.recording):
            print(mean)
            self.recording = True

        if (self.recording):
            self.counter-=1
            if (self.counter<=self.keepingLastValues):
                # saveFigMovementsBySensor(record, "allcaptors", self.counterPrefix, self.numberOfSamples)
                # saveFigMovementsSummed(record, "summed", self.counterPrefix, self.numberOfSamples)
                # print("graphs saved " + str(datetime.now()))
                self.counter=self.numberOfSamples
                self.counterPrefix +=1
                self.recording = False
                self.essai = record[0:]
                self.close()


def saveFigMovementsBySensor(array, name, prefix, numberOfSamples):

    fig, axs = plt.subplots(1,2,figsize=(40,10))

    list_couleur = ["darkgreen", "gold", "coral", "magenta", "cyan", "red", "black", "teal", "deepskyblue", "orange", "yellowgreen", "olive", "rosybrown", "silver", "gray", "peru"]

    gauche = []
    droit = []
    for j in range(6):
        g = []
        d = []
        for i in range(numberOfSamples):
            g.append((array[i])[j])
            d.append((array[i])[j])
        gauche.append(g)
        droit.append(d)

    #implementation des courbs dans les graphe
    for compteur in range(6):
        #oeil gauche
        axs[0].plot(gauche[compteur], marker = 'x',  c = list_couleur[compteur], label = "capt %s" % compteur)

        #oeil droit
        axs[1].plot(droit[compteur], marker = 'x',  c = list_couleur[compteur])

    axs[0].set_title("capteur gauche")
    axs[1].set_title("capteur droit")

    #pas de legend pour xs[1] car la elle est la meme que pour axs[0]
    axs[0].legend()

    #creation des fichiers contenant les graphes
    fig.savefig(name + '{}.png'.format(str(datetime.now())))
    fig.clf()
    plt.close()

def saveFigMovementsSummed(array, name, prefix, numberOfSamples):

    fig, axs = plt.subplots(1,2,figsize=(40,10))

    list_couleur = ["darkgreen", "gold", "coral", "magenta", "cyan", "red", "black", "teal", "deepskyblue", "orange", "yellowgreen", "olive", "rosybrown", "silver", "gray", "peru"]

    gauche = []
    droit = []
    for i in range(numberOfSamples):
        gauche.append(0)
        droit.append(0)
        for j in range(6):
            gauche[i] = abs(array[i][j])/6 + gauche[i]
            droit[i] = abs(array[i][j])/6 + droit[i]

    #oeil gauche
    axs[0].plot(gauche, marker = 'x',  c = list_couleur[0], label = "courbe")

    #oeil droit
    axs[1].plot(droit, marker = 'x',  c = list_couleur[3])

    axs[0].set_title("capteur gauche")
    axs[1].set_title("capteur droit")

    #pas de legend pour xs[1] car la elle est la meme que pour axs[0]
    axs[0].legend()

    #creation des fichiers contenant les graphes
    # fig.savefig(name + '{}.png'.format(prefix))
    fig.savefig(name + '{}.png'.format(str(datetime.now())))
    fig.clf()
    plt.close()


# Result :
# Check all captors to find a significant variation that would mean the start of a movement









def start():
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
    try:
        essai = ex.essai[0:]
    except:
        essai = None
    ex.destroy()

    return essai
