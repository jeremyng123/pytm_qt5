# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wactor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Actor(object):
    def setupUi(self, Actor):
        Actor.setObjectName("Actor")
        Actor.resize(400, 74)
        self.formLayout = QtWidgets.QFormLayout(Actor)
        self.formLayout.setObjectName("formLayout")
        self.Name = QtWidgets.QLabel(Actor)
        self.Name.setObjectName("Name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Name)
        self.name = QtWidgets.QLineEdit(Actor)
        self.name.setObjectName("name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name)
        self.inBoundary = QtWidgets.QLabel(Actor)
        self.inBoundary.setObjectName("inBoundary")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.inBoundary)
        self.boundaries = QtWidgets.QComboBox(Actor)
        self.boundaries.setObjectName("boundaries")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.boundaries)

        self.retranslateUi(Actor)
        QtCore.QMetaObject.connectSlotsByName(Actor)

    def retranslateUi(self, Actor):
        _translate = QtCore.QCoreApplication.translate
        Actor.setWindowTitle(_translate("Actor", "Form"))
        self.Name.setText(_translate("Actor", "Name"))
        self.inBoundary.setText(_translate("Actor", "inBoundary"))