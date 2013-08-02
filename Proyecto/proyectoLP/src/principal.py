import os, sys

from PyQt4 import QtCore, QtGui, uic

class Main(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)

        uifile = os.path.join(os.path.abspath(os.path.dirname(__file__)),"UI_ProyectoLP.ui")
        uic.loadUi(uifile, self)

def main():
    app= QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
   main()