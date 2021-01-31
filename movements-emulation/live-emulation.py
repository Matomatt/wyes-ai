import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPen, QTransform
from PyQt5.QtCore import Qt, QTimer
from math import sqrt, atan, cos, sin, pi
import numpy as np
from sklearn import preprocessing

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        ##Window
        self.title = 'Skin around the eyes movements simulation'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 640
        self.FPS=60
        ##Sampling
        self.lastMousePosition=[None, None]
        self.mousePressed = False
        self.sampleRate = 200
        self.lastSample = [0]*12;
        self.circleSpeed = 1;
        self.selectedCircles=[False]*3
        ##Init
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        ##Captors
        self.captors = [150,0, 450,0, 625,250, 450,520, 150,520, 0,250]
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
        self.circles = [100,400,150, 230,200,300, 480,300,226]
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
        self.show()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
        painter.drawRect(20,20,600,500)
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

    def getLastSampledValues():
        return self.lastSample

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
