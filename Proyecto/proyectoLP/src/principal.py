import os, sys

from PyQt4 import QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_ProyectoLP import Ui_Form

class Main(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)

        uifile = os.path.join(os.path.abspath(os.path.dirname(__file__)),"UI_ProyectoLP.ui")
        uic.loadUi(uifile, self)
    
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.connect(self.ui.beasy, SIGNAL('clicked()'),self.callSudoku)
            
    def mensajeprueba(self):
        QMessageBox.warning(self, 'title','Mensaje de Prueba')
           
    def callSudoku(self):
        self.ui.bclose.hide()
        self.ui.beasy.hide()
        self.ui.bhard.hide()
        self.ui.labellevels.hide()
        self.ui.bplay.hide()
        self.ui.bmedium.hide()
        
        self.ui.setupUi(self)
        
    
    
        

def main():
    app= QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()