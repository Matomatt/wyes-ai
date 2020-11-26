import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPen, QTransform
from PyQt5.QtCore import Qt, QTimer
from math import sqrt
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
        self.positions = [150,0, 450,0, 625,250, 450,520, 150,520, 0,250]
        rotation =  [0, 0, 90, 180, 180, 270]
        captors=[]
        for i in range(0,6):
            captor = QLabel(self)
            img = QPixmap('ir-detector-small.png')
            transform = QTransform().rotate(rotation[i])
            img = img.transformed(transform, Qt.SmoothTransformation)
            captor.setPixmap(img)
            captor.move(self.positions[i*2]-5, self.positions[i*2+1]-5)
            captors.append(captor)
        ##Timer
        self.sampleTimer=QTimer()
        self.sampleTimer.timeout.connect(self.sample)
        self.show()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
        painter.drawRect(20,20,600,500)

    def startRec(self):
        self.statusBar().showMessage('Recording...')
        self.recordedMovementListBuffer = []
        self.recordMovement = True

    def stopRec(self):
        self.recordMovement = False
        self.recordedMovementsDB.append(self.recordedMovementListBuffer)
        self.statusBar().showMessage('Recording stopped')

    def mouseMoveEvent(self, event):
        self.lastMousePosition[0] = event.x()-20;
        self.lastMousePosition[1] = event.y()-20;

    def mousePressEvent(self, e):
        if self.recordMovement == False:
            self.sampleMovement = False
            return
        if e.buttons() == Qt.LeftButton:
            self.sampleMovement = True
            self.recordedMovementBuffer = []
            self.sampleTimer.start(1000/self.sampleRate)

    def mouseReleaseEvent(self, e):
        self.sampleMovement = False
        if self.recordMovement:
            self.recordedMovementListBuffer.append(self.recordedMovementBuffer)

    def sample(self):
        if self.sampleMovement == True:
            distances=[]
            x = self.lastMousePosition[0]
            y = self.lastMousePosition[1]
            for i in range(0,6):
                distances.append( sqrt( (sqrt((x-self.positions[i*2])**2) + sqrt((y-self.positions[i*2+1])**2))**2 ) )
            self.statusBar().showMessage(' '.join(map(str, distances)))
            self.recordedMovementBuffer.append(distances)
            self.sampleTimer.start(1000/self.sampleRate)
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
