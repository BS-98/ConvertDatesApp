from __future__ import unicode_literals
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox
from P2 import CDJD
from P2_2 import JDCD
from P2_3 import MetodaHirvonena
from P2_4 import GPSS

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()

        self.interfejs()
        self.interfejs_widgets()
        
    def interfejs(self):
        # główne okno
        self.setGeometry(500,500,300,100)                    # szerokość i wysokość okna;
        self.setWindowIcon(QIcon('dwa2.png'))  # ikona graficzna programu
        self.setWindowTitle("Projekt 2")    # tytuł okna
        self.show()

    def interfejs_widgets(self):
        
        self.buttonJD = QPushButton("Przeliczenie na datę juliańską", self)
        self.buttonCD = QPushButton("Przeliczenie na datę gregoriańską", self)
        self.buttonGPS = QPushButton("Przeliczenie na czas GPS", self)
        self.buttonHirv = QPushButton("Metoda Hirvonena", self)
            
        grid = QGridLayout()
        
        grid.addWidget(self.buttonJD, 0, 0)
        grid.addWidget(self.buttonCD, 0, 1)
        grid.addWidget(self.buttonGPS, 1, 0)
        grid.addWidget(self.buttonHirv, 1, 1)
        
        self.setLayout(grid)
        
        self.buttonJD.clicked.connect(self.dzialanie)
        self.buttonCD.clicked.connect(self.dzialanie)
        self.buttonHirv.clicked.connect(self.dzialanie)
        self.buttonGPS.clicked.connect(self.dzialanie)
        

    def dzialanie(self):

        nadawca = self.sender()
        
        if nadawca.text() == "Przeliczenie na datę gregoriańską":
             self.next = JDCD()
             
        elif nadawca.text() == "Metoda Hirvonena":
             self.next = MetodaHirvonena()
             
        elif nadawca.text() == "Przeliczenie na datę juliańską":
             self.next = CDJD()
        
        else:
            self.next = GPSS()
        

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = MainWindow()
    sys.exit(app.exec_())
    
