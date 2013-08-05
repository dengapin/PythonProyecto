'''
Created on 31/07/2013

@author: Keylis
'''

import sys,os

from PyQt4 import QtCore, QtGui, uic
from numero import *
from sudoku import Ui_Sudoku
    
class Main(QtGui.QMainWindow):
    
    
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
       # uifile = os.path.join(os.path.abspath(os.path.dirname(__file__)),"sudoku.ui")
       # uic.loadUi(uifile, self)
        self.ui = Ui_Sudoku()
        self.ui.setupUi(self)
        self.initGui()
   
     
              
    def initGui(self):
        global coorX
        global coorY
        global encriptar
        global celdaSeleccionada
        global casilla
        global valorPad
        casilla = [[0 for j in range(9)] for i in range(9)]
        valorPad = [0 for j in range(9)]
        coorX = -1
        coorY = -1
        
        flag = False
                  
        for i in range(0,9):    
            for j in range(0,9):
               celda = numero()
               celda.setFila(i)
               celda.setColumna(j)
               celda.setNumReal(0)
               celda.setNumAsignado(0)
               celda.setEsConstante(False)
               
               if(flag):
                   celda.setColor(0)
                   celda.setStyleSheet('QPushButton {background-color: red}' )
               else:
                   celda.setColor(1)
                   celda.setStyleSheet('QPushButton {background-color: blue}' )
               casilla [i][j]= celda
               self.ui.gridLayout.addWidget(celda,i,j)
               
               if(j % 3 == 2):
                    flag = not(flag)
            if(i % 3 != 2):
                flag = not (flag)
                  
        for i in range(0,9):
            numSelec = QPushButton(str(i+1))
            valorPad [i] = numSelec
            self.ui.numberPad.addWidget(numSelec,i/3, i%3)
            numSelec.setStyleSheet('QPushButton {background-color: black; color: white}')
    
        self.ui.nullButton.setText('Borrar')
        self.ui.nullButton.setEnabled(False)
        #self.ui.nullButton.setStyleSheet('QPushButton {background-color: black; color: white}')
        celdaSeleccionada = False
        self.ventanaInvalida()
        
    def ventanaInvalida(self):
        coorX = -1
        coorY = -1
        celda = numero()
        for i in range(0,9):
            for j in range(0,9):
                celda = casilla[i][j]
                celda.setEnabled(False)
                if(celda.getColor() == 0):
                    celda.setStyleSheet('QPushButton {background-color: red}')
                else:
                    celda.setStyleSheet('QPushButton {background-color: blue}')
            numSelec = QPushButton()
            numSelec = valorPad[i]
            numSelec.setEnabled(False)
        
        self.ui.nullButton.setEnabled(False)
        self.ui.radioButton.setChecked(False)
        celdaSeleccionada = False
        
        self.ui.groupBox_2.setEnabled(False)        
                    
    def celdaClicked(self):
        if(not(celdaSeleccionada)):
            celdaSeleccionada = True
        else:
            celda = casilla[coorX][coorY]
            if(celda.getColor == 0):
                celda.setStyleSheet('QPushButton {background-color: red}')
            else:
                celda.setStyleSheet('QPushButton {background-color: blue}')
        celda = numero()
        celda.sender()
        coorX = celda.getFila()
        coorY = celda.getColumna()
        
        if (celda.getNumReal() == celda.getNumeroAsignado()):
            self.ui.radioButton.setChecked(True)
        else:
            self.ui.radioButton.setChecked(False)
            numSelec = QPushButton() 
        for i in range(0,9):
            numSelec = valorPad[i] 
            numSelec.setEnabled(True)
        if(self.ui.radioButton.isChecked()):
            self.validarCelda()
        
        celda.setStyleSheet('QPushButton {background-color: orange}')
            
    def validarCelda(self):
        centerX = coorX/3
        centerY = coorY/3
        celda = numero()
        for i in range(0,9):
            for j in range(0,9):
                if(i == coorX | j == coorY | (i/3 == centerX & j/3 == centerY )):
                    celda = casilla[i][j]
                    if (celda.getNumeroAsignado()):
                        numSelec = QPushButton()
                        valor = celda.getNumeroAsignado()
                        numSelec = valorPad[valor -1]
                        numSelec.setEnabled(False)
        
        celda = casilla[coorX][coorY]
        if(not(celda.getNumeroAsignado())):
            self.ui.nullButton.setEnabled(False)
        else:
            self.ui.nullButton.setEnabled(True)
            
if __name__ == "__main__":
    app= QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())