from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel




def QuitButton(AppGUI):
    qbtn = QPushButton('Quit', AppGUI)
    qbtn.clicked.connect(QApplication.instance().quit)
    qbtn.resize(qbtn.sizeHint())
    qbtn.move(50, 200)