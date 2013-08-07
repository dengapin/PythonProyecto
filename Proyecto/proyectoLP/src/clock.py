# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clock.ui'
#
# Created: Mon Aug  5 12:22:52 2013
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

class Ui_clock(object):
    def setupUi(self, clock):
        clock.setObjectName(_fromUtf8("clock"))
        clock.resize(400, 300)

        self.retranslateUi(clock)
        QtCore.QMetaObject.connectSlotsByName(clock)

    def retranslateUi(self, clock):
        clock.setWindowTitle(_translate("clock", "Form", None))

