from __future__ import unicode_literals 
from PyQt5.QtGui import QIcon 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QHBoxLayout, QMessageBox #wgranie widżetów
from metody import data_julianska 

class CDJD(QWidget): 
    
    def __init__(self):
        super().__init__()

        self.interfejs()
        self.interfejs_widgets()
        
    def interfejs(self):
        # główne okno
        self.setGeometry(500,500,150,130)                    # miejsce wyswietlenia się na ekranie oraz szerokość i wysokość okna
        self.setWindowIcon(QIcon('kalendarz2.png'))          
        self.setWindowTitle("CDJD")
        self.show()

    def interfejs_widgets(self):
        # umieszczenie i rozmieszczenie widżetów
        e1 = QLabel("Rok", self)
        e2 = QLabel("Miesiąc", self)
        e3 = QLabel("Dzień", self)
        e4 = QLabel("Godzina", self)
        e5 = QLabel("Minuta", self)
        e6 = QLabel("Sekunda", self)
#        
        buttonJD = QPushButton("Data Juliańska", self)
        buttonJD.setToolTip("Po nacisnięciu zostanie policzna <b>data juliańska</b>")
        buttonMJD = QPushButton("Zmodyfikowana Data Juliańska", self)
        buttonMJD.setToolTip("Po nacisnięciu zostanie policzna <b>zmodyfikowana data juliańska</b>")
#        
        self.e1Edit = QLineEdit()
        self.e2Edit = QLineEdit()
        self.e3Edit = QLineEdit()
        self.e4Edit = QLineEdit()
        self.e5Edit = QLineEdit()
        self.e6Edit = QLineEdit()
        self.JDEdit = QLineEdit()
        self.MJDEdit = QLineEdit()
        
        self.JDEdit.setReadOnly(True) #tylko do odczytu, nie można wprowadzać zmian
        self.MJDEdit.setReadOnly(True)
        
        grid  = QGridLayout()
        grid2 = QHBoxLayout() 
        grid3 = QHBoxLayout()
        
        grid.addWidget(e1, 0, 1)
        grid.addWidget(self.e1Edit, 1, 1)
        
        
        grid.addWidget(e2, 0, 2)
        grid.addWidget(self.e2Edit, 1, 2)
        
        grid.addWidget(e3, 0, 3)
        grid.addWidget(self.e3Edit, 1, 3)
        
        
        grid.addWidget(e4, 0, 4)
        grid.addWidget(self.e4Edit, 1, 4)
        
        grid.addWidget(e5, 0, 5)    
        grid.addWidget(self.e5Edit, 1, 5)
        
        
        grid.addWidget(e6, 0, 6)
        grid.addWidget(self.e6Edit, 1, 6)
        
        grid2.addWidget(buttonJD)
        grid2.addWidget(buttonMJD)
        
        grid3.addWidget(self.JDEdit)
        grid3.addWidget(self.MJDEdit)
        
        grid.addLayout(grid2, 2, 0, 1, 8) 
        grid.addLayout(grid3, 3, 0, 1, 8) 
        
        self.setLayout(grid) 
        
        buttonJD.clicked.connect(self.dzialanie) # sygnał, łączy sie z funkcją "dzialanie"
        buttonMJD.clicked.connect(self.dzialanie)
#       
        
        
    def dzialanie(self):
        # funkcja odpowiadająca za działanie i wyswietlanie wynikóW
        
        nadawca = self.sender()
        
        try:
            rok      = float(self.e1Edit.text()) 
            miesiac  = float(self.e2Edit.text()) 
            dzien    = float(self.e3Edit.text())  
            godzina  = float(self.e4Edit.text())
            minuta   = float(self.e5Edit.text()) 
            sekunda  = float(self.e6Edit.text())
            wynik = None
            
            if nadawca.text() == "Data Juliańska":
                wynik = data_julianska(sekunda,minuta,godzina,dzien,miesiac,rok)
                self.JDEdit.setText(str(wynik)) 
                
            else:
                wynik2 = data_julianska(sekunda,minuta,godzina,dzien,miesiac,rok) - 2400000.5
                self.MJDEdit.setText(str(wynik2))
            
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
    okno = CDJD()
    sys.exit(app.exec_())
    
    
    