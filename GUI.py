import sys, time
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5 import QtCore
import ButtonGui as _button
import InputHandler
#pyQt5 gui
#CReates a thread so other threads must be created here to perform loop logic
class AppGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.CloseApp = False
        self.StartLogicThread()

    def CheckAppClose(self):
        if self.CloseApp == True:
            sys.exit(self.exec_())
    #Create my logic thread. Example: Input
    def StartLogicThread(self):
        self.threads = []
        _logicThread = LogicThread()
        self.threads.append(_logicThread)
        _logicThread.start()
    #Initialize function, put anything that needs to be init inside here
    def initUI(self):
        self.CloseApp = False
        #self._input = InputHandler.InitInput()
        self.MakeButtons()
        self.SetWindow()
        
    def MakeButtons(self):
        _button.QuitButton(self)

    def MakeLabels(self):
        None
    #Set the windows Geomtry and the title then show it
    def SetWindow(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Simple')
        self.show()

#Logic Thread class. This Class runs on it own thread so it can perform logic
class LogicThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.ExitMainLoop = None
        self._input = InputHandler.Input_Handler()
    #This get run first, anything that needs to be initialized can be put in here
    def run(self):
        self.ExitMainLoop = False
        print("Run Function")
        self.MainLoop()
        return
    #MainLoop where everything that needs to be looped will be put
    def MainLoop(self):
        while self.ExitMainLoop == False:
            self.ExitMainLoop = self._input.ContinueInput() #Check if input should be continued
            self._input.HandleInput() #Go to inputhandler to handle all of our input needs
        print("Input Has Been Stopped")

    #def __del__(self): #Close thread fuinction, waits for thread to finish before closing it out
    #    self.wait() #This function seems to be causing problems --------------------------
        
#Just little function to Init the gui. Dont know why I put it here. Might move this to main()
def initHandler():
    app = QApplication(sys.argv)
    gui = AppGUI()
    sys.exit(app.exec_())






