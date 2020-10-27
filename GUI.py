import sys, time
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5 import QtCore
import ButtonGui as _button
import InputHandler


class AppGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.CloseApp = False
        self.StartLogicThread()

    def CheckAppClose(self):
        if self.CloseApp == True:
            sys.exit(self.exec_())

    def StartLogicThread(self):
        self.threads = []
        _logicThread = LogicThread()
        self.threads.append(_logicThread)
        _logicThread.start()

    def initUI(self):
        self.CloseApp = False
        #self._input = InputHandler.InitInput()
        self.MakeButtons()
        self.SetWindow()
        
    def MakeButtons(self):
        _button.QuitButton(self)

    def MakeLabels(self):
        None
    def SetWindow(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Simple')
        self.show()


class LogicThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.ExitMainLoop = None
        self._input = InputHandler.Input_Handler()
        self.MainLoop()
    def __del__():
        self.wait()

    def run(self):
        self.ExitMainLoop = False
        print("Run Function")
        self.MainLoop()

    def MainLoop(self):
        while self.ExitMainLoop == False:
            print("In MainLoop")
            self.ExitMainLoop = InputHandler.TempInput()
        print("Exiting MainLoop")

        

def initHandler():
    app = QApplication(sys.argv)
    gui = AppGUI()
    sys.exit(app.exec_())


def Printout():
    print("Hello")




