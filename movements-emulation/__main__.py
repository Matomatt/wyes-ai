import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPen, QTransform
from PyQt5.QtCore import Qt, QTimer
from math import sqrt, atan, cos, sin, pi
import numpy as numpy

## Detecter le mouvement avec la variation des capteurs au lieu du clic
##
##

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        ##Window
        self.title = 'Skin around the eyes movements simulation'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 640
        ##Movements recording
        self.lastMousePosition=[None, None]
        self.recordMovement = False;
        self.sampleMovement = False;
        self.sampleRate = 20
        self.recordedMovementBuffer = []
        self.recordedMovementListBuffer = []
        self.recordedMovementsDB = []
        ##Init
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        ##Buttons
        buttonRec = QPushButton('Record new movement', self)
        buttonRec.setToolTip('Start the recording of a new movement, do it multiple times to build the database')
        buttonRec.move(20,560)
        buttonRec.resize(150, 30)
        buttonRec.clicked.connect(self.startRec)
        buttonStopRec = QPushButton('Stop recording', self)
        buttonStopRec.setToolTip('Stop the recording of the new movement')
        buttonStopRec.move(220,560)
        buttonStopRec.clicked.connect(self.stopRec)
        buttonMakeFile = QPushButton('Save to file', self)
        buttonMakeFile.setToolTip('Save all the recorded movements to the dataset.csv file')
        buttonMakeFile.move(420,560)
        buttonMakeFile.clicked.connect(self.makeFile)
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
        ##Timer
        self.sampleTimer=QTimer()
        self.sampleTimer.timeout.connect(self.sample)
        self.show()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
        painter.drawRect(20,20,600,500)
        for i in range(0,3):
            painter.drawEllipse(int(self.circles[i*3]-self.circles[i*3+2]/2)+20, int(self.circles[i*3+1]-self.circles[i*3+2]/2)+20, int(self.circles[i*3+2]), int(self.circles[i*3+2]))

    def startRec(self):
        self.statusBar().showMessage('Recording...')
        self.recordedMovementListBuffer = []
        self.recordMovement = True

    def stopRec(self):
        self.recordMovement = False
        self.recordedMovementsDB.append(self.recordedMovementListBuffer)
        self.statusBar().showMessage('Recording stopped')

    def circleCollisions(self, i, j, distToMove):
        if (sqrt( (self.circles[i*3]-self.circles[j*3])**2 + (self.circles[i*3+1]-self.circles[j*3+1])**2 ) < self.circles[i*3+2]/2+self.circles[j*3+2]/2):
            dirVect = [self.circles[i*3]-self.circles[j*3], self.circles[i*3+1]-self.circles[j*3+1]]
            angle=atan(dirVect[1]/dirVect[0])+(self.circles[i*3]>self.circles[j*3])*pi;
            self.circles[j*3]+=distToMove*cos(angle);
            self.circles[j*3+1]+=distToMove*sin(angle);

    def mouseMoveEvent(self, event):
        for i in range(0, 3):
            if (self.sampleMovement==True and sqrt( (event.x()-20-self.circles[i*3])**2 + (event.y()-20-self.circles[i*3+1])**2 ) < self.circles[i*3+2]/2):
                self.circles[i*3]+=(event.x()-self.lastMousePosition[0]-20);
                self.circles[i*3+1]+=(event.y()-self.lastMousePosition[1]-20);
                for j in range(0,3):
                    if (i!=j):
                        self.circleCollisions(i,j,sqrt( (event.x()-self.lastMousePosition[0]-20)**2 + (event.y()-self.lastMousePosition[1]-20)**2 ));
                        self.circleCollisions(j,3-(i+j),sqrt( (event.x()-self.lastMousePosition[0]-20)**2 + (event.y()-self.lastMousePosition[1]-20)**2 ));
                self.update();
        self.lastMousePosition[0] = event.x()-20;
        self.lastMousePosition[1] = event.y()-20;

    def mousePressEvent(self, e):
        if self.recordMovement == False:
            self.sampleMovement = False
            return
        if e.buttons() == Qt.LeftButton:
            self.sampleMovement = True
            self.recordedMovementBuffer = []
            self.sampleTimer.start(int(1000/self.sampleRate))

    def mouseReleaseEvent(self, e):
        self.sampleMovement = False
        if self.recordMovement:
            self.recordedMovementListBuffer.append(self.recordedMovementBuffer)
            self.circles = self.circlesInitPos.copy()
            self.update()
            self.statusBar().showMessage('Movement saved, you can make it again to fill the dataset.')

    def sample(self):
        if self.sampleMovement == True:
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
            self.statusBar().showMessage(' '.join(map(str, distances)))
            self.recordedMovementBuffer.append(distances)
            self.sampleTimer.start(int(1000/self.sampleRate))
        else:
            self.sampleTimer.stop()

    def makeFile(self):
        a = numpy.asarray(self.recordedMovementsDB, dtype=object)
        numpy.savetxt("dataset.csv", a, fmt="%s")
        self.statusBar().showMessage('Saved successfully !')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
