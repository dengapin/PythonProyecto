# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaSudoku.ui'
#
# Created: Sun Aug  4 13:26:35 2013
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

class Ui_prueba(object):
    def setupUi(self, prueba):
        prueba.setObjectName(_fromUtf8("prueba"))
        prueba.resize(729, 544)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icono.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        prueba.setWindowIcon(icon)
        self.verticalLayoutWidget = QtGui.QWidget(prueba)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 440, 431, 91))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.seccioncronometro = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.seccioncronometro.setMargin(0)
        self.seccioncronometro.setObjectName(_fromUtf8("seccioncronometro"))
        self.gridLayoutWidget = QtGui.QWidget(prueba)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 150, 431, 271))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.taberosudoku = QtGui.QGridLayout(self.gridLayoutWidget)
        self.taberosudoku.setMargin(0)
        self.taberosudoku.setObjectName(_fromUtf8("taberosudoku"))
        self.textEdit = QtGui.QTextEdit(prueba)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(120, 30, 301, 81))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.groupBox = QtGui.QGroupBox(prueba)
        self.groupBox.setGeometry(QtCore.QRect(520, 50, 181, 241))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 151, 141))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.tableronumeros = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.tableronumeros.setMargin(0)
        self.tableronumeros.setObjectName(_fromUtf8("tableronumeros"))
        self.blimpiar = QtGui.QPushButton(self.groupBox)
        self.blimpiar.setGeometry(QtCore.QRect(60, 180, 75, 23))
        self.blimpiar.setObjectName(_fromUtf8("blimpiar"))
        self.groupBox_2 = QtGui.QGroupBox(prueba)
        self.groupBox_2.setGeometry(QtCore.QRect(520, 310, 181, 151))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.bnormal = QtGui.QRadioButton(self.groupBox_2)
        self.bnormal.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.bnormal.setObjectName(_fromUtf8("bnormal"))
        self.bhint = QtGui.QRadioButton(self.groupBox_2)
        self.bhint.setGeometry(QtCore.QRect(20, 60, 82, 17))
        self.bhint.setObjectName(_fromUtf8("bhint"))
        self.bclue = QtGui.QRadioButton(self.groupBox_2)
        self.bclue.setGeometry(QtCore.QRect(20, 90, 82, 17))
        self.bclue.setObjectName(_fromUtf8("bclue"))
        self.bsalir = QtGui.QPushButton(prueba)
        self.bsalir.setGeometry(QtCore.QRect(620, 480, 75, 23))
        self.bsalir.setObjectName(_fromUtf8("bsalir"))
        self.bguardar = QtGui.QPushButton(prueba)
        self.bguardar.setGeometry(QtCore.QRect(520, 480, 75, 23))
        self.bguardar.setObjectName(_fromUtf8("bguardar"))

        self.retranslateUi(prueba)
        QtCore.QMetaObject.connectSlotsByName(prueba)

    def retranslateUi(self, prueba):
        prueba.setWindowTitle(_translate("prueba", "Python Proyecto", None))
        self.textEdit.setHtml(_translate("prueba", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-style:italic; color:#00aaff;\">SUDOKU</span></p></body></html>", None))
        self.groupBox.setTitle(_translate("prueba", "Numeros", None))
        self.blimpiar.setText(_translate("prueba", "Limpiar", None))
        self.groupBox_2.setTitle(_translate("prueba", "Ayuda", None))
        self.bnormal.setText(_translate("prueba", "Normal", None))
        self.bhint.setText(_translate("prueba", "Hint", None))
        self.bclue.setText(_translate("prueba", "Clue", None))
        self.bsalir.setText(_translate("prueba", "Salir", None))
        self.bguardar.setText(_translate("prueba", "Guardar", None))

