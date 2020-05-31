from __future__ import unicode_literals
from PyQt5.QtGui import QIcon, QPixmap # wgranie widżetów umożliwiających dodanie ikony programu oraz obrazka
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QMessageBox # wgranie widżetów
from hirvonen import hirvonen 
from moje_metody import decimalDeg2dms 

class MetodaHirvonena(QWidget):
    
    def __init__(self):
        super().__init__()

        self.interfejs()
        self.interfejs_widgets()
        
    def interfejs(self):
        # główne okno
        self.setGeometry(500,500,150,130)          # miejsce wyswietlenia się na ekranie oraz szerokość i wysokość okna;
        self.setWindowIcon(QIcon('H.png'))        
        self.setWindowTitle("Metoda Hirvonena")    
        self.show()

    def interfejs_widgets(self):
        # umieszczenie i rozmieszczenie widżetów
        e1 = QLabel("X :", self)
        e2 = QLabel("Y :", self)
        e3 = QLabel("Z :", self)
        e7 = QLabel("Minuty :", self)
        e8 = QLabel("Stopnie :", self)
        e9 = QLabel("Sekundy :", self)
        e10 = QLabel("H :", self)
        
        self.l1 = QLineEdit()
        self.l2 = QLineEdit()
        self.l3 = QLineEdit()
        
        self.fistopnie = QLineEdit()
        self.fiminuty  = QLineEdit()
        self.fisekundy = QLineEdit()
        self.lambdastopnie = QLineEdit()
        self.lambdaminuty  = QLineEdit()
        self.lambdasekundy = QLineEdit()
        self.wysokosc = QLineEdit()
        
        self.fistopnie.setReadOnly(True)
        self.fiminuty.setReadOnly(True)
        self.fisekundy.setReadOnly(True)
        self.lambdastopnie.setReadOnly(True)
        self.lambdaminuty.setReadOnly(True)
        self.lambdasekundy.setReadOnly(True)
        self.wysokosc.setReadOnly(True)
        
        
        
        self.button = QPushButton(" ", self)
        self.button.setIcon(QIcon("strzalka w prawo.jpg"))
        self.clearbutton = QPushButton("Clear", self)
        self.clearbutton.setToolTip("Po nacisnięciu wszystkie pola zostaną <b>wyczyszczone</b>") # wskazówka
        

        fi      = QPixmap("fi.png") # symbol współrzędnej fi
        lambdaa =  QPixmap("lambda.png") # symbol współrzędnej lambda
        hirv    = QPixmap("metoda hirvonena.png") # rysunek
        
        filbl = QLabel(self)
        filbl.setPixmap(fi) # dodanie rysunku do widgetu
        
        lambdalbl = QLabel(self)
        lambdalbl.setPixmap(lambdaa) # dodanie rysunku do widgetu
        
        hirvlbl = QLabel(self)
        hirvlbl.setPixmap(hirv) # dodanie rysunku do widgetu
        
        grid  = QGridLayout()
        
        grid.addWidget(e1, 1, 0)
        grid.addWidget(e2, 2, 0)
        grid.addWidget(e3, 3, 0)
        
        grid.addWidget(self.l1, 1, 1)
        grid.addWidget(self.l2, 2, 1)
        grid.addWidget(self.l3, 3, 1)
        
        grid.addWidget(self.button, 2, 2)
        
        grid.addWidget(filbl, 1, 3)
        grid.addWidget(lambdalbl, 2, 3)
        grid.addWidget(e10, 3, 3)
        
        grid.addWidget(self.fistopnie, 1, 4)
        grid.addWidget(self.fiminuty, 1, 5)
        grid.addWidget(self.fisekundy, 1, 6)
        
        grid.addWidget(self.lambdastopnie, 2, 4)
        grid.addWidget(self.lambdaminuty, 2, 5)
        grid.addWidget(self.lambdasekundy, 2, 6)
        grid.addWidget(self.wysokosc, 3, 4, 1, 3)
        
        grid.addWidget(e7, 0, 4)
        grid.addWidget(e8, 0, 5)
        grid.addWidget(e9, 0, 6)
        grid.addWidget(self.clearbutton, 4, 0, 1, 7)
        grid.addWidget(hirvlbl, 5, 0, 1, 7)
        
        
        
        self.setLayout(grid)
        
        self.button.clicked.connect(self.dzialanie)
        self.clearbutton.clicked.connect(self.clear)
        
    def dzialanie(self):
        
        nadawca = self.sender()
        
        try:
            # pobranie współrzędnych
            X = float(self.l1.text()) 
            Y = float(self.l2.text())
            Z = float(self.l3.text())
            
            if nadawca.text() == " ":
                B, L, H = hirvonen(X, Y, Z, a = 6378137., e2 = 0.00669438002290) #wywolanie funkcji
                fi = decimalDeg2dms(B)
                la = decimalDeg2dms(L)
                
            #wyswietlenie wynikow   
            self.fistopnie.setText(str(fi[0]))
            self.fiminuty.setText(str(fi[1]))
            self.fisekundy.setText(str(round(fi[2],5)))
            
            self.lambdastopnie.setText(str(la[0]))
            self.lambdaminuty.setText(str(la[1]))
            self.lambdasekundy.setText(str(round(la[2],5)))
            
            self.wysokosc.setText(str(round(H,3)))
            
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Brak danych!", QMessageBox.Ok)
     
    def clear(self):
        self.fistopnie.clear()
        self.fiminuty.clear()
        self.fisekundy.clear()
        self.lambdastopnie.clear()
        self.lambdaminuty.clear()
        self.lambdasekundy.clear()
        self.wysokosc.clear()
        self.l1.clear()
        self.l2.clear()
        self.l3.clear()
                
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
    okno = MetodaHirvonena()
    sys.exit(app.exec_())