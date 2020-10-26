import sys, time
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
import ButtonGui as _button
import InputHandler


class AppGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.CloseApp = False
        self._input

    def CheckAppClose(self):
        if self.CloseApp == True:
            sys.exit(self.exec_())

    def initUI(self):
        self.CloseApp = False
        self._input = InputHandler.InitInput()
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

def initHandler():
    app = QApplication(sys.argv)
    gui = AppGUI()
    sys.exit(app.exec_())


def Printout():
    print("Hello")




