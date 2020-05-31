from __future__ import unicode_literals
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QMessageBox
from metody import data_gregorianska 

class JDCD(QWidget): 
    
    def __init__(self):
        super().__init__()

        self.interfejs()
        self.interfejs_widgets()
        
    def interfejs(self):
        # główne okno
        self.setGeometry(500,500,250,160)                       # miejsce wyswietlenia się na ekranie oraz szerokość i wysokość okna
        self.setWindowIcon(QIcon('kalendarz2.png'))             
        self.setWindowTitle("JDCD")                             
        self.show()

    def interfejs_widgets(self):
        # umieszczenie i rozmieszczenie widżetów
        
        e1       = QLabel("Data Juliańska :", self)
        buttonCD = QPushButton("Data gregoriańska", self)
        e3       = QLabel("Rok :", self)
        e4       = QLabel("Miesiąc:", self)
        e5       = QLabel("Dzień :", self)
        e6       = QLabel("Godzina :", self)
        e7       = QLabel("Minuta :", self)
        e8       = QLabel("Sekunda :", self)
        
        self.e1Edit = QLineEdit()
        self.e3Edit = QLineEdit()
        self.e4Edit = QLineEdit()
        self.e5Edit = QLineEdit()
        self.e6Edit = QLineEdit()
        self.e7Edit = QLineEdit()
        self.e8Edit = QLineEdit()
        
        self.e3Edit.setReadOnly(True) # tylko do odczytu
        self.e4Edit.setReadOnly(True)
        self.e5Edit.setReadOnly(True)
        self.e6Edit.setReadOnly(True)
        self.e7Edit.setReadOnly(True)
        self.e8Edit.setReadOnly(True)
        
        grid  = QGridLayout()
        grid.addWidget(e1, 0, 0)
        grid.addWidget(self.e1Edit, 0, 1)
        grid.addWidget(buttonCD, 1, 0, 1, 2)
        grid.addWidget(e3, 3, 0)
        grid.addWidget(e4, 4, 0)
        grid.addWidget(e5, 5, 0)
        grid.addWidget(e6, 6, 0)
        grid.addWidget(e7, 7, 0)
        grid.addWidget(e8, 8, 0)
        
        grid.addWidget(self.e3Edit, 3, 1)
        grid.addWidget(self.e4Edit, 4, 1)
        grid.addWidget(self.e5Edit, 5, 1)
        grid.addWidget(self.e6Edit, 6, 1)
        grid.addWidget(self.e7Edit, 7, 1)
        grid.addWidget(self.e8Edit, 8, 1)
        
        self.setLayout(grid)
        
        buttonCD.clicked.connect(self.dzialanie) # sygnał, łączy sie z funkcją "dzialanie"
        
    def dzialanie(self):
        # funkcja odpowiadająca za działanie i wyswietlanie wyników
        
        nadawca = self.sender()
        
        try:
            data_julianska = float(self.e1Edit.text()) 
            
            if nadawca.text() == "Data gregoriańska":
                wynik   = data_gregorianska(data_julianska)
                
            self.e3Edit.setText(str(wynik[5])) 
            self.e4Edit.setText(str(wynik[4]))
            self.e5Edit.setText(str(wynik[3]))
            self.e6Edit.setText(str(wynik[2]))
            self.e7Edit.setText(str(wynik[1]))
            self.e8Edit.setText(str(wynik[0]))
            
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
    okno = JDCD()
    sys.exit(app.exec_())
    