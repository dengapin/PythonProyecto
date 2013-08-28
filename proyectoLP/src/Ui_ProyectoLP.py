# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_ProyectoLP.ui'
#
# Created: Mon Jul 29 23:59:19 2013
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(537, 399)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icono.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.titulo = QtGui.QTextEdit(Form)
        self.titulo.setEnabled(False)
        self.titulo.setGeometry(QtCore.QRect(140, 50, 281, 91))
        self.titulo.setObjectName(_fromUtf8("titulo"))
        self.beasy = QtGui.QRadioButton(Form)
        self.beasy.setGeometry(QtCore.QRect(70, 210, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.beasy.setFont(font)
        self.beasy.setObjectName(_fromUtf8("beasy"))
        self.bmedium = QtGui.QRadioButton(Form)
        self.bmedium.setGeometry(QtCore.QRect(220, 210, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bmedium.setFont(font)
        self.bmedium.setObjectName(_fromUtf8("bmedium"))
        self.bhard = QtGui.QRadioButton(Form)
        self.bhard.setGeometry(QtCore.QRect(370, 210, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bhard.setFont(font)
        self.bhard.setObjectName(_fromUtf8("bhard"))
        self.labellevels = QtGui.QLabel(Form)
        self.labellevels.setGeometry(QtCore.QRect(70, 170, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labellevels.setFont(font)
        self.labellevels.setObjectName(_fromUtf8("labellevels"))
        self.bclose = QtGui.QPushButton(Form)
        self.bclose.setGeometry(QtCore.QRect(320, 290, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bclose.setFont(font)
        self.bclose.setObjectName(_fromUtf8("bclose"))
        self.bplay = QtGui.QPushButton(Form)
        self.bplay.setGeometry(QtCore.QRect(150, 290, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bplay.setFont(font)
        self.bplay.setObjectName(_fromUtf8("bplay"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.bclose, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Sudoku en Python", None))
        self.titulo.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-style:italic; color:#00aaff;\">SUDOKU</span></p></body></html>", None))
        self.beasy.setText(_translate("Form", "Easy", None))
        self.bmedium.setText(_translate("Form", "Medium", None))
        self.bhard.setText(_translate("Form", "Hard", None))
        self.labellevels.setText(_translate("Form", "Levels", None))
        self.bclose.setText(_translate("Form", "CLOSE", None))
        self.bplay.setText(_translate("Form", "PLAY", None))

