from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtWidgets import QPushButton,QRadioButton,QComboBox,QLabel
from PyQt5.QtGui import QFont
import sys
import random
import time
app=QApplication(sys.argv)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,450,450)
        self.setFixedSize(340,360)
        self.setWindowTitle("TicTac Toe")
        self.start()
    def font(self,ob):
        ob.setFont(QFont("Times New Roman",40))
    def start(self):
        self.k = 0            
        self.b1 = QPushButton("",self,clicked = lambda: self.B1())
        self.font(self.b1)
        self.b1.setGeometry(10,10,100,100)
                
        self.b2 = QPushButton("",self,clicked = lambda: self.B2())
        self.font(self.b2)
        self.b2.setGeometry(120,10,100,100)
                
        self.b3 = QPushButton("",self,clicked = lambda: self.B3())
        self.font(self.b3)
        self.b3.setGeometry(230,10,100,100)
                
        self.b4 = QPushButton("",self,clicked = lambda: self.B4())
        self.font(self.b4)
        self.b4.setGeometry(10,120,100,100)
                
        self.b5 = QPushButton("",self,clicked = lambda: self.B5())
        self.font(self.b5)
        self.b5.setGeometry(120,120,100,100)
        
        self.b6 = QPushButton("",self,clicked = lambda: self.B6())
        self.font(self.b6)
        self.b6.setGeometry(230,120,100,100)
                
        self.b7 = QPushButton("",self,clicked = lambda: self.B7())
        self.font(self.b7)
        self.b7.setGeometry(10,230,100,100)
                
        self.b8 = QPushButton("",self,clicked = lambda: self.B8())
        self.font(self.b8)
        self.b8.setGeometry(120,230,100,100)
                
        self.b9 = QPushButton("",self,clicked = lambda: self.B9())
        self.font(self.b9)
        self.b9.setGeometry(230,230,100,100)
        
        self.words = QLabel("O's turn",self)
        self.words.setGeometry(125,340,120,20)
        self.words.setFont(QFont("Times",15))
        self.draw = 0
                               
    def B1(self):
        self.k+=1
        if self.k % 2 == 0:
            self.addXO(self.b1,1)
        if self.k % 2 != 0:
            self.addXO(self.b1,2)
        self.result()        
    def B2(self):
        self.k+=1
        if self.k % 2 == 0:
            self.addXO(self.b2,1)
        if self.k % 2 != 0:
            self.addXO(self.b2,2)
        self.result()            
    def B3(self):
        self.k+=1
        if self.k % 2 == 0:
            self.addXO(self.b3,1)
        if self.k % 2 != 0:
            self.addXO(self.b3,2)
        self.result()
    def B4(self):
        self.k+=1
        if self.k % 2 == 0:
            self.addXO(self.b4,1)
        if self.k % 2 != 0:
            self.addXO(self.b4,2)
        self.result()
    def B5(self):
        self.k+=1
        if self.k % 2 == 0:
            self.addXO(self.b5,1)
        if self.k % 2 != 0:
            self.addXO(self.b5,2)
        self.result()
    def B6(self):
        self.k+=1
        if self.k % 2 == 0:
            self.addXO(self.b6,1)
        if self.k % 2 != 0:
            self.addXO(self.b6,2)
        self.result()
    def B7(self):
        self.k+=1
        if self.k % 2 == 0:
            self.addXO(self.b7,1)
        if self.k % 2 != 0:
            self.addXO(self.b7,2)
        self.result()
    def B8(self):
        self.k+=1
        if self.k % 2 == 0:
            self.addXO(self.b8,1)
        if self.k % 2 != 0:
            self.addXO(self.b8,2)
        self.result()        
    def B9(self):
        self.k+=1
        if self.k % 2 == 0:
            self.addXO(self.b9,1)
        if self.k % 2 != 0:
            self.addXO(self.b9,2)
        self.result()  
              
    def addXO(self,Bname,ind):
        if Bname.text()=="" and ind==1:
            self.words.setText("O's turn")
            Bname.setText("X")            
        if Bname.text()=="" and ind==2:
            self.words.setText("X's turn")
            Bname.setText("O")
    def result(self):
        if self.b1.text() == 'X' and self.b2.text() == 'X' and self.b3.text() == 'X' or self.b4.text() == 'X' and self.b5.text() == 'X' and self.b6.text() == 'X' or self.b7.text() == 'X' and self.b8.text() == 'X' and self.b9.text() == 'X' or self.b1.text() == 'X' and self.b4.text() == 'X' and self.b7.text() == 'X' or self.b2.text() == 'X' and self.b5.text() == 'X' and self.b8.text() == 'X' or self.b3.text() == 'X' and self.b5.text() == 'X' and self.b9.text() == 'X' or self.b1.text() == 'X' and self.b5.text() == 'X' and self.b9.text() == 'X' or self.b3.text() == 'X' and self.b5.text() == 'X' and self.b7.text() == 'X' or self.b3.text() == 'X' and self.b6.text() == 'X' and self.b9.text() == 'X':
            self.b1.hide();self.b2.hide();self.b3.hide();self.b4.hide();self.b5.hide();self.b6.hide();self.b7.hide();self.b8.hide();self.b9.hide()
            self.words.setText("X is won!")
            self.font(self.words)
            self.words.setGeometry(50,50,270,80)
        elif self.b1.text() == 'O' and self.b2.text() == 'O' and self.b3.text() == 'O' or self.b4.text() == 'O' and self.b5.text() == 'O' and self.b6.text() == 'O' or self.b7.text() == 'O' and self.b8.text() == 'O' and self.b9.text() == 'O' or self.b1.text() == 'O' and self.b4.text() == 'O' and self.b7.text() == 'O' or self.b2.text() == 'O' and self.b5.text() == 'O' and self.b8.text() == 'O' or self.b3.text() == 'O' and self.b5.text() == 'O' and self.b7.text() == 'O' or self.b1.text() == 'O' and self.b5.text() == 'O' and self.b9.text() == 'O' or self.b3.text() == 'O' and self.b5.text() == 'O' and self.b7.text() == 'O' or self.b3.text() == 'O' and self.b6.text() == 'O' and self.b9.text() == 'O':
            self.words.setText("0 is won!")
            self.font(self.words)
            self.words.setGeometry(50,50,270,80)
            self.b1.hide();self.b2.hide();self.b3.hide();self.b4.hide();self.b5.hide();self.b6.hide();self.b7.hide();self.b8.hide();self.b9.hide()
        else:
            self.draw+=1
        if self.draw == 9:
            self.words.setText("Draw!")
            self.font(self.words)
            self.words.setGeometry(90,50,270,80)            
oyna=Window()
oyna.show()
sys.exit(app.exec_())
