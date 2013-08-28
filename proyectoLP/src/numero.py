'''
Created on 02/08/2013

@author: Keylis
'''
#QPushButtonGrid

from PyQt4.QtGui import QPushButton 


class numero(QPushButton): 
    
     
    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna
    
    def getNumReal(self):
        return self.numero_real
    
    def getNumeroAsignado(self):
        return self.numero_asignado
    
    def getColor(self):
        return self.color
    
    def getEsConstante(self):
        return self.esConstante
    
    def setFila(self,fila):
        self.fila = fila
        
    def setColumna(self,columna):
        self.columna = columna
        
    def setNumReal(self,numReal):
        self.numero_real = numReal
        
    def setNumeroAsignado(self,numAsignado):
        self.numero_asignado = numAsignado
        
    def setColor(self,color):
        self.color = color
    
    def setEsConstante(self,esConstante):
        self.esConstante = esConstante