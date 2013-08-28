# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sudoku.ui'
#
# Created: Fri Aug  2 04:47:11 2013
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
        Sudoku.setStyleSheet(_fromUtf8("background-color:white;"))
        self.centralWidget = QtGui.QWidget(Sudoku)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 80, 511, 461))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.radioButton = QtGui.QRadioButton(self.centralWidget)
        self.radioButton.setEnabled(False)
        self.radioButton.setGeometry(QtCore.QRect(840, 540, 21, 20))
        self.radioButton.setText(_fromUtf8(""))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 600, 114, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 550, 511, 81))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(640, 20, 221, 271))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 40, 160, 151))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.numberPad = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.numberPad.setMargin(0)
        self.numberPad.setObjectName(_fromUtf8("numberPad"))
        self.nullButton = QtGui.QPushButton(self.groupBox)
        self.nullButton.setGeometry(QtCore.QRect(50, 210, 114, 32))
        self.nullButton.setObjectName(_fromUtf8("nullButton"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QtCore.QRect(690, 350, 120, 161))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.hintButton = QtGui.QRadioButton(self.groupBox_2)
        self.hintButton.setGeometry(QtCore.QRect(10, 70, 102, 20))
        self.hintButton.setObjectName(_fromUtf8("hintButton"))
        self.normalButton = QtGui.QRadioButton(self.groupBox_2)
        self.normalButton.setGeometry(QtCore.QRect(10, 30, 102, 20))
        self.normalButton.setChecked(True)
        self.normalButton.setObjectName(_fromUtf8("normalButton"))
        self.clueButton = QtGui.QRadioButton(self.groupBox_2)
        self.clueButton.setGeometry(QtCore.QRect(10, 110, 102, 20))
        self.clueButton.setObjectName(_fromUtf8("clueButton"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(80, 0, 511, 73))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textEdit = QtGui.QTextEdit(self.gridLayoutWidget_3)
        self.textEdit.setEnabled(False)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
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
        self.actionOpen = QtGui.QAction(Sudoku)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(Sudoku)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionClose = QtGui.QAction(Sudoku)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionQuit = QtGui.QAction(Sudoku)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionMedium = QtGui.QAction(Sudoku)
        self.actionMedium.setObjectName(_fromUtf8("actionMedium"))
        self.actionHard = QtGui.QAction(Sudoku)
        self.actionHard.setObjectName(_fromUtf8("actionHard"))
        self.actionEasy_2 = QtGui.QAction(Sudoku)
        self.actionEasy_2.setObjectName(_fromUtf8("actionEasy_2"))
        self.actionMedium_2 = QtGui.QAction(Sudoku)
        self.actionMedium_2.setObjectName(_fromUtf8("actionMedium_2"))
        self.actionHard_2 = QtGui.QAction(Sudoku)
        self.actionHard_2.setObjectName(_fromUtf8("actionHard_2"))
        self.actionNew = QtGui.QAction(Sudoku)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
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
        self.pushButton.setText(_translate("Sudoku", "PushButton", None))
        self.groupBox.setTitle(_translate("Sudoku", "Number Pad", None))
        self.nullButton.setText(_translate("Sudoku", "PushButton", None))
        self.groupBox_2.setTitle(_translate("Sudoku", "Game Mode", None))
        self.hintButton.setText(_translate("Sudoku", "Hint", None))
        self.normalButton.setText(_translate("Sudoku", "Normal", None))
        self.clueButton.setText(_translate("Sudoku", "Clue", None))
        self.textEdit.setHtml(_translate("Sudoku", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; color:#00aaff;\">SUDOKU</span></p></body></html>", None))
        self.menuFile.setTitle(_translate("Sudoku", "File", None))
        self.actionOpen.setText(_translate("Sudoku", "Open", None))
        self.actionOpen.setShortcut(_translate("Sudoku", "Ctrl+O", None))
        self.actionSave.setText(_translate("Sudoku", "Save", None))
        self.actionSave.setShortcut(_translate("Sudoku", "Ctrl+S", None))
        self.actionClose.setText(_translate("Sudoku", "Close", None))
        self.actionClose.setShortcut(_translate("Sudoku", "Ctrl+W", None))
        self.actionQuit.setText(_translate("Sudoku", "Quit", None))
        self.actionQuit.setShortcut(_translate("Sudoku", "Ctrl+P", None))
        self.actionMedium.setText(_translate("Sudoku", "Medium", None))
        self.actionMedium.setShortcut(_translate("Sudoku", "Ctrl+2", None))
        self.actionHard.setText(_translate("Sudoku", "Hard", None))
        self.actionHard.setShortcut(_translate("Sudoku", "Ctrl+3", None))
        self.actionEasy_2.setText(_translate("Sudoku", "Easy", None))
        self.actionEasy_2.setShortcut(_translate("Sudoku", "Ctrl+1", None))
        self.actionMedium_2.setText(_translate("Sudoku", "Medium", None))
        self.actionMedium_2.setShortcut(_translate("Sudoku", "Ctrl+2", None))
        self.actionHard_2.setText(_translate("Sudoku", "Hard", None))
        self.actionHard_2.setShortcut(_translate("Sudoku", "Ctrl+3", None))
        self.actionNew.setText(_translate("Sudoku", "New", None))

