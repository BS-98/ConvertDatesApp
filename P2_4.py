from __future__ import unicode_literals
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QCheckBox, QWidget, QLabel, QLineEdit, QGridLayout, QMessageBox
from metody import GPS 


class GPSS(QWidget): 
    
    def __init__(self):
        super().__init__()

        self.interfejs()
        self.interfejs_widgets()
        
    def interfejs(self):
        # główne okno
        self.setGeometry(500,500,350,180)      # miejsce wyswietlenia się na ekranie oraz szerokość i wysokość okna;
        self.setWindowIcon(QIcon('gps2.png'))  
        self.setWindowTitle("GPS Time")        
        self.show()
    
    def interfejs_widgets(self):
        # umieszczenie i rozmieszczenie widżetów
        
        e1 = QLabel("Rok :", self)
        e2 = QLabel("Miesiąc:", self)
        e3 = QLabel("Dzień :", self)
        e4 = QLabel("Godzina :", self)
        e5 = QLabel("Minuta :", self)
        e6 = QLabel("Sekunda :", self)
        
        self.chxWeek = QCheckBox("GPS WEEK", self)
        self.chxSOW = QCheckBox("GPS SOW", self)
        self.chxDOW = QCheckBox("GPS DOW", self)
        self.chxSOD = QCheckBox("GPS SOD", self)
        
        
        self.e1Edit = QLineEdit()
        self.e2Edit = QLineEdit()
        self.e3Edit = QLineEdit()
        self.e4Edit = QLineEdit()
        self.e5Edit = QLineEdit()
        self.e6Edit = QLineEdit()
        self.chxWeekEdit = QLineEdit()
        self.chxSOWEdit  = QLineEdit()
        self.chxDOWEdit  = QLineEdit()
        self.chxSODEdit  = QLineEdit()
        
        grid  = QGridLayout()
        
        grid.addWidget(e1, 0, 0)
        grid.addWidget(e2, 1, 0)
        grid.addWidget(e3, 2, 0)
        grid.addWidget(e4, 3, 0)
        grid.addWidget(e5, 4, 0)
        grid.addWidget(e6, 5, 0)
        
        grid.addWidget(self.e1Edit, 0, 1)
        grid.addWidget(self.e2Edit, 1, 1)
        grid.addWidget(self.e3Edit, 2, 1)
        grid.addWidget(self.e4Edit, 3, 1)
        grid.addWidget(self.e5Edit, 4, 1)
        grid.addWidget(self.e6Edit, 5, 1)
        
        grid.addWidget(self.chxWeek, 1, 2)
        grid.addWidget(self.chxSOW, 2, 2)
        grid.addWidget(self.chxDOW, 3, 2)   
        grid.addWidget(self.chxSOD, 4, 2)
        
        grid.addWidget(self.chxWeekEdit, 1, 3)
        grid.addWidget(self.chxSOWEdit, 2, 3)
        grid.addWidget(self.chxDOWEdit, 3, 3)
        grid.addWidget(self.chxSODEdit, 4, 3)
        
        
        self.chxWeek.stateChanged.connect(self.dzialanie_WEEK) # sygnał, łączy sie z funkcją "dzialanie"
        self.chxSOW.stateChanged.connect(self.dzialanie_SOW)
        self.chxDOW.stateChanged.connect(self.dzialanie_DOW)
        self.chxSOD.stateChanged.connect(self.dzialanie_SOD)
   
        self.setLayout(grid)
        
        
    def dzialanie_WEEK(self, state):
        try:  
            #pobranie wartosci
            rok      = float(self.e1Edit.text())  
            miesiac  = float(self.e2Edit.text())  
            dzien    = float(self.e3Edit.text()) 
            godzina  = float(self.e4Edit.text())
            minuta   = float(self.e5Edit.text()) 
            sekunda  = float(self.e6Edit.text())
            
            if state == Qt.Checked:
                wynik = GPS(sekunda,minuta,godzina,dzien,miesiac,rok)
                
            else:
                self.chxWeekEdit.clear()
            
            self.chxWeekEdit.setText(str(wynik[0])) # wyswietlenie wyniku
            
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Brak danych!", QMessageBox.Ok)
        
    def dzialanie_SOW(self, state):
        
        try:
            rok      = float(self.e1Edit.text()) 
            miesiac  = float(self.e2Edit.text()) 
            dzien    = float(self.e3Edit.text()) 
            godzina  = float(self.e4Edit.text())
            minuta   = float(self.e5Edit.text()) 
            sekunda  = float(self.e6Edit.text())
            
            if state == Qt.Checked:
                wynik = GPS(sekunda,minuta,godzina,dzien,miesiac,rok) 
            else:
                self.chxSOWEdit.clear() 
    
            self.chxSOWEdit.setText(str(wynik[1])) 
            
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Brak danych!", QMessageBox.Ok)
            
    def dzialanie_DOW(self, state):
        
        try:
            rok      = float(self.e1Edit.text()) 
            miesiac  = float(self.e2Edit.text()) 
            dzien    = float(self.e3Edit.text()) 
            godzina  = float(self.e4Edit.text())
            minuta   = float(self.e5Edit.text()) 
            sekunda  = float(self.e6Edit.text())
                
            if state == Qt.Checked:
                wynik = GPS(sekunda,minuta,godzina,dzien,miesiac,rok) 
            else:
                self.chxDOWEdit.clear() 
        
            self.chxDOWEdit.setText(str(wynik[2])) 
            
        except ValueError:
                QMessageBox.warning(self, "Błąd", "Brak danych!", QMessageBox.Ok)
                
    def dzialanie_SOD(self, state):
        try:  
            rok      = float(self.e1Edit.text()) 
            miesiac  = float(self.e2Edit.text()) 
            dzien    = float(self.e3Edit.text())  
            godzina  = float(self.e4Edit.text())
            minuta   = float(self.e5Edit.text()) 
            sekunda  = float(self.e6Edit.text())
            
            if state == Qt.Checked:
                wynik = GPS(sekunda,minuta,godzina,dzien,miesiac,rok)
            else:
                self.chxSODEdit.clear()
    
            self.chxSODEdit.setText(str(wynik[3]))
            
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Brak danych!", QMessageBox.Ok)
            

        
    def closeEvent(self, event):
        #  wyświetlamy użytkownikowi prośbę o potwierdzenie zamknięcia
        # dziala po kliknieciu close
        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno chcesz zakończyć?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = GPSS()
    sys.exit(app.exec_())