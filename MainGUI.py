# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainGui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 299)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_PLsorting = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_PLsorting.setObjectName("pushButton_PLsorting")
        self.gridLayout.addWidget(self.pushButton_PLsorting, 3, 1, 1, 1)
        self.pushButton_uvspectro = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_uvspectro.setObjectName("pushButton_uvspectro")
        self.gridLayout.addWidget(self.pushButton_uvspectro, 1, 0, 1, 1)
        self.pushButton_TMM = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_TMM.setObjectName("pushButton_TMM")
        self.gridLayout.addWidget(self.pushButton_TMM, 2, 0, 1, 1)
        self.pushButton_EQE = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_EQE.setObjectName("pushButton_EQE")
        self.gridLayout.addWidget(self.pushButton_EQE, 0, 1, 1, 1)
        self.pushButton_SolarSim = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SolarSim.setObjectName("pushButton_SolarSim")
        self.gridLayout.addWidget(self.pushButton_SolarSim, 0, 0, 1, 1)
        self.pushButton_NKtauc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_NKtauc.setObjectName("pushButton_NKtauc")
        self.gridLayout.addWidget(self.pushButton_NKtauc, 2, 1, 1, 1)
        self.pushButton_XRD = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_XRD.setObjectName("pushButton_XRD")
        self.gridLayout.addWidget(self.pushButton_XRD, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Solar Data Analyzer"))
        self.pushButton_PLsorting.setText(_translate("MainWindow", "PL images - bottom cell sorting"))
        self.pushButton_uvspectro.setText(_translate("MainWindow", "UV-vis spectrophotometry"))
        self.pushButton_TMM.setText(_translate("MainWindow", "Transfer Matrix Modeling"))
        self.pushButton_EQE.setText(_translate("MainWindow", "EQE"))
        self.pushButton_SolarSim.setText(_translate("MainWindow", "Solar Simulator"))
        self.pushButton_NKtauc.setText(_translate("MainWindow", "NK Tauc plot analysis"))
        self.pushButton_XRD.setText(_translate("MainWindow", "XRD"))

