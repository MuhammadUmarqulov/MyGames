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
        self.setFixedSize(432,450)
        self.setWindowTitle("15 Numbers (created by Muhammad)")
        self.start()
    def font(self,ob):
        ob.setFont(QFont("Times New Roman",40))
    def start(self):
        vals = []
        while len(vals) != 15:
            i = random.randint(1,15)
            if i not in vals:
                vals.append(i)
        self.valls = vals
        self.valls.append(" ")            
        self.b1 = QPushButton(str(vals[0]),self,clicked = lambda: self.B1())
        self.font(self.b1)
        self.b1.setGeometry(20,20,91,91)
               
        self.b2 = QPushButton(str(vals[1]),self,clicked = lambda: self.B2())
        self.font(self.b2)
        self.b2.setGeometry(120,20,91,91)
            
        self.b3 = QPushButton(str(vals[2]),self,clicked = lambda: self.B3())
        self.font(self.b3)
        self.b3.setGeometry(220,20,91,91)
            
        self.b4 = QPushButton(str(vals[3]),self,clicked = lambda: self.B4())
        self.font(self.b4)
        self.b4.setGeometry(320,20,91,91)
            
        self.b5 = QPushButton(str(vals[4]),self,clicked = lambda: self.B5())
        self.font(self.b5)
        self.b5.setGeometry(20,120,91,91)
    
        self.b6 = QPushButton(str(vals[5]),self,clicked = lambda: self.B6())
        self.font(self.b6)
        self.b6.setGeometry(120,120,91,91)
            
        self.b7 = QPushButton(str(vals[6]),self,clicked = lambda: self.B7())
        self.font(self.b7)
        self.b7.setGeometry(220,120,91,91)
            
        self.b8 = QPushButton(str(vals[7]),self,clicked = lambda: self.B8())
        self.font(self.b8)
        self.b8.setGeometry(320,120,91,91)
            
        self.b9 = QPushButton(str(vals[8]),self,clicked = lambda: self.B9())
        self.font(self.b9)
        self.b9.setGeometry(20,220,91,91)
            
        self.b10 = QPushButton(str(vals[9]),self,clicked = lambda: self.B10())
        self.font(self.b10)
        self.b10.setGeometry(120,220,91,91)
            
        self.b11 = QPushButton(str(vals[10]),self,clicked = lambda: self.B11())
        self.font(self.b11)
        self.b11.setGeometry(220,220,91,91)
            
        self.b12 = QPushButton(str(vals[11]),self,clicked = lambda: self.B12())
        self.font(self.b12)
        self.b12.setGeometry(320,220,91,91)
            
        self.b13 = QPushButton(str(vals[12]),self,clicked = lambda: self.B13())
        self.font(self.b13)
        self.b13.setGeometry(20,320,91,91)
            
        self.b14 = QPushButton(str(vals[13]),self,clicked = lambda: self.B14())
        self.font(self.b14)
        self.b14.setGeometry(120,320,91,91)
            
        self.b15 = QPushButton(str(vals[14]),self,clicked = lambda: self.B15())
        self.font(self.b15) 
        self.b15.setGeometry(220,320,91,91)
            
        self.b16 = QPushButton(str(vals[15]),self,clicked = lambda: self.B16())
        self.font(self.b16)
        self.b16.setGeometry(320,320,91,91) 
            
        self.win = QLabel("You Win!!!",self)
        self.win.setGeometry(30,150,300,90)
        self.win.setFont(QFont("Arial",50))
        self.win.hide()
            
        self.about = QLabel("Start",self)
        self.about.move(25,420)            
    
    
    def B1(self):
        if self.valls[0+4] == " " or self.valls[0+1] == " ":
            self.probelFinder().setText(self.b1.text())
            self.b1.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[0] = self.valls[0], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b1)
    def B2(self):
        if self.valls[0] == " " or self.valls[5] == " " or self.valls[2] == " ":
            self.probelFinder().setText(self.b2.text())
            self.b2.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[1] = self.valls[1], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b2)
    def B3(self):
        if self.valls[3] == " " or self.valls[6] == " " or self.valls[1] == " ":
            self.probelFinder().setText(self.b3.text())
            self.b3.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[2] = self.valls[2], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b3)
    def B4(self):
        if self.valls[7] == " " or self.valls[2] == " ":
            self.probelFinder().setText(self.b4.text())
            self.b4.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[3] = self.valls[3], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b4)
    def B5(self):
        if self.valls[0] == " " or self.valls[8] == " " or self.valls[5] == " ":
            self.probelFinder().setText(self.b5.text())
            self.b5.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[4] = self.valls[4], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b5)
    def B6(self):
        if self.valls[4] == " " or self.valls[6] == " " or self.valls[1] == " " or self.valls[9] == " ":
            self.probelFinder().setText(self.b6.text())
            self.b6.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[5] = self.valls[5], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b6)
    def B7(self):
        if self.valls[7] == " " or self.valls[10] == " " or self.valls[2] == " " or self.valls[5] == " ":
            self.probelFinder().setText(self.b7.text())
            self.b7.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[6] = self.valls[6], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b7)
    def B8(self):
        if self.valls[3] == " " or self.valls[6] == " " or self.valls[11] == " ":
            self.probelFinder().setText(self.b8.text())
            self.b8.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[7] = self.valls[7], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b8)
    def B9(self):
        if self.valls[9] == " " or self.valls[12] == " " or self.valls[4] == " ":
            self.probelFinder().setText(self.b9.text())
            self.b9.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[8] = self.valls[8], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b9)
    def B10(self):
        if self.valls[8] == " " or self.valls[10] == " " or self.valls[13] == " " or self.valls[5] == " ":
            self.probelFinder().setText(self.b10.text())
            self.b10.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[9] = self.valls[9], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b10)
    def B11(self):
        if self.valls[9] == " " or self.valls[11] == " " or self.valls[14] == " " or self.valls[6] == " ":
            self.probelFinder().setText(self.b11.text())
            self.b11.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[10] = self.valls[10], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b11)
    def B12(self):
        if self.valls[7] == " " or self.valls[10] == " " or self.valls[15] == " ":
            self.probelFinder().setText(self.b12.text())
            self.b12.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[11] = self.valls[11], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b12)
    def B13(self):
        if self.valls[8] == " " or self.valls[13] == " ":
            self.probelFinder().setText(self.b13.text())
            self.b13.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[12] = self.valls[12], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b13)
    def B14(self):
        if self.valls[12] == " " or self.valls[14] == " " or self.valls[9] == " ":
            self.probelFinder().setText(self.b14.text())
            self.b14.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[13] = self.valls[13], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b14)
    def B15(self):
        if self.valls[15] == " " or self.valls[13] == " " or self.valls[10] == " ":
            self.probelFinder().setText(self.b15.text())
            self.b15.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[14] = self.valls[14], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b15)
    def B16(self):
        if self.valls[11] == " " or self.valls[14] == " ":
            self.probelFinder().setText(self.b16.text())
            self.b16.setText(" ")
            self.valls[self.valls.index(" ")], self.valls[15] = self.valls[15], self.valls[self.valls.index(" ")]
            self.checkWin()
        else:
            self.ErrorAnimation(self.b16)
    def checkWin(self):
        self.about.setText(f"Successfully moved!")
        self.about.adjustSize()
        if self.b1.text() == "1" and self.b2.text() == "2" and self.b3.text() == "3" and self.b4.text() == "4" and self.b5.text() == "5" and self.b6.text() == "6" and self.b7.text() == "7" and self.b8.text() == "8" and self.b9.text() == "9" and self.b10.text() == "10" and self.b11.text() == "11" and self.b12.text() == "12" and self.b13.text() == "13" and self.b14.text() == "14" and self.b15.text() == "15" :
            self.about.hide()
            self.b1.hide();self.b2.hide();self.b3.hide();self.b4.hide();self.b5.hide();self.b6.hide();self.b7.hide();self.b8.hide();self.b9.hide();self.b10.hide();self.b11.hide();self.b12.hide();self.b13.hide();self.b14.hide();self.b15.hide();self.b16.hide()
            self.win.show();self.win.adjustSize()
    def probelFinder(self):
        if self.b1.text() == ' ':return self.b1
        if self.b2.text() == ' ':return self.b2
        if self.b3.text() == ' ':return self.b3
        if self.b4.text() == ' ':return self.b4
        if self.b5.text() == ' ':return self.b5
        if self.b6.text() == ' ':return self.b6
        if self.b7.text() == ' ':return self.b7
        if self.b8.text() == ' ':return self.b8
        if self.b9.text() == ' ':return self.b9
        if self.b10.text() == ' ':return self.b10
        if self.b11.text() == ' ':return self.b11
        if self.b12.text() == ' ':return self.b12
        if self.b13.text() == ' ':return self.b13
        if self.b14.text() == ' ':return self.b14
        if self.b15.text() == ' ':return self.b15
        if self.b16.text() == ' ':return self.b16        
    def ErrorAnimation(self,name):
        self.about.setText(f"Failed to move!")
        self.about.adjustSize()
oyna=Window()
oyna.show()
sys.exit(app.exec_())
