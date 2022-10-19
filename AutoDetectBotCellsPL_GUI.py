# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutoDetectBotCellsPL_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(359, 249)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 3)
        self.writeROI = QtWidgets.QCheckBox(self.centralwidget)
        self.writeROI.setObjectName("writeROI")
        self.gridLayout.addWidget(self.writeROI, 1, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 3)
        self.GrayFactor = QtWidgets.QSpinBox(self.centralwidget)
        self.GrayFactor.setMaximum(999)
        self.GrayFactor.setProperty("value", 25)
        self.GrayFactor.setObjectName("GrayFactor")
        self.gridLayout.addWidget(self.GrayFactor, 2, 3, 1, 1)
        self.chooseFile = QtWidgets.QPushButton(self.centralwidget)
        self.chooseFile.setObjectName("chooseFile")
        self.gridLayout.addWidget(self.chooseFile, 0, 3, 1, 1)
        self.samplenumberstart = QtWidgets.QSpinBox(self.centralwidget)
        self.samplenumberstart.setMinimum(1)
        self.samplenumberstart.setMaximum(99999)
        self.samplenumberstart.setProperty("value", 1)
        self.samplenumberstart.setObjectName("samplenumberstart")
        self.gridLayout.addWidget(self.samplenumberstart, 3, 3, 1, 1)
        self.chosenFile = QtWidgets.QLineEdit(self.centralwidget)
        self.chosenFile.setObjectName("chosenFile")
        self.gridLayout.addWidget(self.chosenFile, 0, 0, 1, 3)
        self.ratioofroi = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ratioofroi.setDecimals(2)
        self.ratioofroi.setMaximum(1.0)
        self.ratioofroi.setSingleStep(0.1)
        self.ratioofroi.setProperty("value", 0.1)
        self.ratioofroi.setObjectName("ratioofroi")
        self.gridLayout.addWidget(self.ratioofroi, 4, 3, 1, 1)
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setObjectName("Start")
        self.gridLayout.addWidget(self.Start, 5, 0, 1, 4)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 359, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "AutoDetectBotCells-PL"))
        self.label.setText(_translate("mainWindow", "GrayFactor"))
        self.writeROI.setText(_translate("mainWindow", "write ROI"))
        self.label_3.setText(_translate("mainWindow", "Ratio of ROI"))
        self.label_2.setText(_translate("mainWindow", "Sample number start"))
        self.chooseFile.setText(_translate("mainWindow", "Choose file"))
        self.Start.setText(_translate("mainWindow", "Start"))

