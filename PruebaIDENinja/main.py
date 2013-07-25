# -*- coding: utf-8 -*-
import sys
from PyQt4.QtGui import QApplication
from PyQt4 import QtGui
from PyQt4 import uic

app= QApplication(sys.argv)

w= uic.loadUi('/Users/Dennise/Desktop/ProyectoLP.ui')
w.setGeometry(300,300,250,150)
w.setWindowTitle('Proyecto')
w.setWindowIcon(QtGui.QIcon('icono.jpg'))

w.show()
sys.exit(app.exec_())