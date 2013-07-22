# -*- coding: utf-8 -*-
import sys
from PyQt4.QtGui import QApplication
from PyQt4 import uic

app= QApplication(sys.argv)

w= uic.loadUi('/Users/Dennise/Desktop/ProyectoLP.ui')
w.show()

sys.exit(app.exec_())