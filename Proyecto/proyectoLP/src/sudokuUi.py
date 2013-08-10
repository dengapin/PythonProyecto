# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sudokuUi.ui'
#
# Created: Sat Aug 10 12:00:32 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Sudoku(object):
    def setupUi(self, Sudoku):
        Sudoku.setObjectName(_fromUtf8("Sudoku"))
        Sudoku.resize(886, 694)
        self.centralWidget = QtGui.QWidget(Sudoku)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 60, 551, 481))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.tablerosudoku = QtGui.QGridLayout(self.gridLayoutWidget)
        self.tablerosudoku.setMargin(0)
        self.tablerosudoku.setObjectName(_fromUtf8("tablerosudoku"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 550, 114, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 550, 551, 81))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.seccioncronometro = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.seccioncronometro.setMargin(0)
        self.seccioncronometro.setObjectName(_fromUtf8("seccioncronometro"))
        self.lcdNumber = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.seccioncronometro.addWidget(self.lcdNumber)
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(640, 20, 221, 271))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 40, 160, 151))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.tableronumeros = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.tableronumeros.setMargin(0)
        self.tableronumeros.setObjectName(_fromUtf8("tableronumeros"))
        self.nullButton = QtGui.QPushButton(self.groupBox)
        self.nullButton.setGeometry(QtCore.QRect(50, 210, 114, 32))
        self.nullButton.setObjectName(_fromUtf8("nullButton"))
        self.tablaAyuda = QtGui.QGroupBox(self.centralWidget)
        self.tablaAyuda.setEnabled(False)
        self.tablaAyuda.setGeometry(QtCore.QRect(690, 350, 120, 161))
        self.tablaAyuda.setObjectName(_fromUtf8("tablaAyuda"))
        self.hintButton = QtGui.QRadioButton(self.tablaAyuda)
        self.hintButton.setGeometry(QtCore.QRect(10, 70, 102, 20))
        self.hintButton.setObjectName(_fromUtf8("hintButton"))
        self.normalButton = QtGui.QRadioButton(self.tablaAyuda)
        self.normalButton.setGeometry(QtCore.QRect(10, 30, 102, 20))
        self.normalButton.setChecked(True)
        self.normalButton.setObjectName(_fromUtf8("normalButton"))
        self.clueButton = QtGui.QRadioButton(self.tablaAyuda)
        self.clueButton.setGeometry(QtCore.QRect(10, 110, 102, 20))
        self.clueButton.setObjectName(_fromUtf8("clueButton"))
        self.textEdit = QtGui.QTextEdit(self.centralWidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(220, 10, 161, 51))
        self.textEdit.setLineWidth(0)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        Sudoku.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(Sudoku)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 886, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        Sudoku.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(Sudoku)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        Sudoku.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(Sudoku)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        Sudoku.setStatusBar(self.statusBar)
        self.actionNew = QtGui.QAction(Sudoku)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(Sudoku)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(Sudoku)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionClose = QtGui.QAction(Sudoku)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionQuit = QtGui.QAction(Sudoku)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Sudoku)
        QtCore.QMetaObject.connectSlotsByName(Sudoku)

    def retranslateUi(self, Sudoku):
        Sudoku.setWindowTitle(_translate("Sudoku", "Sudoku", None))
        self.pushButton.setText(_translate("Sudoku", "Guardar", None))
        self.groupBox.setTitle(_translate("Sudoku", "Numeros ", None))
        self.nullButton.setText(_translate("Sudoku", "Limpiar", None))
        self.tablaAyuda.setTitle(_translate("Sudoku", "Ayuda", None))
        self.hintButton.setText(_translate("Sudoku", "Hint", None))
        self.normalButton.setText(_translate("Sudoku", "Normal", None))
        self.clueButton.setText(_translate("Sudoku", "Clue", None))
        self.textEdit.setHtml(_translate("Sudoku", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-style:italic; color:#00aaff;\">SUDOKU</span></p></body></html>", None))
        self.menuFile.setTitle(_translate("Sudoku", "File", None))
        self.actionNew.setText(_translate("Sudoku", "New", None))
        self.actionNew.setShortcut(_translate("Sudoku", "Ctrl+N", None))
        self.actionOpen.setText(_translate("Sudoku", "Open", None))
        self.actionOpen.setShortcut(_translate("Sudoku", "Ctrl+O", None))
        self.actionSave.setText(_translate("Sudoku", "Save", None))
        self.actionSave.setShortcut(_translate("Sudoku", "Ctrl+S", None))
        self.actionClose.setText(_translate("Sudoku", "Close", None))
        self.actionClose.setShortcut(_translate("Sudoku", "Ctrl+W", None))
        self.actionQuit.setText(_translate("Sudoku", "Quit", None))
        self.actionQuit.setShortcut(_translate("Sudoku", "Ctrl+P", None))

