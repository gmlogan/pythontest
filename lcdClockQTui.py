import main
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
import os
from time import strftime
import datetime
import time


import datetime
class Flag:
    def __init__(self,name,up,down, starttime):
        self.name=name
        self.updelta=up
        self.downdelta=down
        self.uptime=starttime-datetime.timedelta(minutes=self.updelta)
        self.downtime=starttime-datetime.timedelta(minutes=self.downdelta)

    def isFlagRaised(self):
        if datetime.datetime.now()> self.uptime:
            return True
        else:
            return False



class myWindow(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.setupUi(self)
        self.myactions()
        self.starttime = self.calcstarttime()
        self.timer = QtCore.QTimer(self)

    def myactions(self):
        self.startButton.clicked.connect(self.on_startbutton_clicked)
        self.stopButton.clicked.connect(self.on_stopbutton_clicked)

    def on_startbutton_clicked(self):
        print("Start button is pressed ")
        print(self.starttime)
        self.wFlag = Flag("Warning", 5, 0, self.starttime)
        self.pFlag = Flag("Preparatory", 4, 1, self.starttime)
        self.startclock()
        pix=QtGui.QPixmap("pflag.jpg")
        self.label.setPixmap(pix)
        self.label.resize(pix.width(), pix.height())
        self.label.show()


    def on_stopbutton_clicked(self):
        print("Stop button is pressed ")
        self.timer.stop()
        self.label.hide()

    def calcstarttime(self):
        timenow = datetime.datetime.now()
        starttime = timenow.replace(second=0, microsecond=0) + datetime.timedelta(minutes=6)
        return starttime

    def updateclock(self):
        self.lcdNumber.display(strftime("%H" + ":" + "%M" + ":" + "%S"))
        print(datetime.datetime.now().replace(microsecond=0))
        print(self.wFlag.name, self.wFlag.isFlagRaised())
        print(self.pFlag.name, self.pFlag.isFlagRaised())

    def startclock(self):
        self.timer.timeout.connect(self.updateclock)
        self.timer.start(1000)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = myWindow()
    fb.show()
    app.exec_()