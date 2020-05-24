# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wlambda.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Lambda(object):
    def setupUi(self, Lambda):
        Lambda.setObjectName("Lambda")
        Lambda.resize(400, 117)
        self.widget = QtWidgets.QWidget(Lambda)
        self.widget.setGeometry(QtCore.QRect(12, 12, 381, 89))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label1 = QtWidgets.QLabel(self.widget)
        self.label1.setObjectName("label1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label1)
        self.name = QtWidgets.QLineEdit(self.widget)
        self.name.setObjectName("name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name)
        self.label2 = QtWidgets.QLabel(self.widget)
        self.label2.setObjectName("label2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label2)
        self.boundaries = QtWidgets.QComboBox(self.widget)
        self.boundaries.setObjectName("boundaries")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.boundaries)
        self.label3 = QtWidgets.QLabel(self.widget)
        self.label3.setObjectName("label3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label3)
        self.hasAccessControl = QtWidgets.QComboBox(self.widget)
        self.hasAccessControl.setObjectName("hasAccessControl")
        self.hasAccessControl.addItem("")
        self.hasAccessControl.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.hasAccessControl)

        self.retranslateUi(Lambda)
        QtCore.QMetaObject.connectSlotsByName(Lambda)

    def retranslateUi(self, Lambda):
        _translate = QtCore.QCoreApplication.translate
        Lambda.setWindowTitle(_translate("Lambda", "Form"))
        self.label1.setText(_translate("Lambda", "Name"))
        self.label2.setText(_translate("Lambda", "inBoundary"))
        self.label3.setText(_translate("Lambda", "hasAccessControl"))
        self.hasAccessControl.setItemText(0, _translate("Lambda", "True"))
        self.hasAccessControl.setItemText(1, _translate("Lambda", "False"))

