# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nkgui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 631)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.mplwidget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwidget.sizePolicy().hasHeightForWidth())
        self.mplwidget.setSizePolicy(sizePolicy)
        self.mplwidget.setObjectName("mplwidget")
        self.verticalLayout_mplwidget = QtWidgets.QVBoxLayout(self.mplwidget)
        self.verticalLayout_mplwidget.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_mplwidget.setSpacing(5)
        self.verticalLayout_mplwidget.setObjectName("verticalLayout_mplwidget")
        self.frame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_SGFilter = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_SGFilter.setObjectName("pushButton_SGFilter")
        self.gridLayout_2.addWidget(self.pushButton_SGFilter, 0, 0, 1, 2)
        self.spinBox_SG1 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_SG1.setMaximum(999)
        self.spinBox_SG1.setProperty("value", 31)
        self.spinBox_SG1.setObjectName("spinBox_SG1")
        self.gridLayout_2.addWidget(self.spinBox_SG1, 1, 0, 1, 1)
        self.spinBox_SG2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_SG2.setMaximum(999)
        self.spinBox_SG2.setProperty("value", 5)
        self.spinBox_SG2.setObjectName("spinBox_SG2")
        self.gridLayout_2.addWidget(self.spinBox_SG2, 1, 1, 1, 1)
        self.pushButton_goback = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_goback.setObjectName("pushButton_goback")
        self.gridLayout_2.addWidget(self.pushButton_goback, 2, 0, 1, 2)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 127, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 1)
        self.spinBox_fontsize = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_fontsize.setProperty("value", 12)
        self.spinBox_fontsize.setObjectName("spinBox_fontsize")
        self.gridLayout_3.addWidget(self.spinBox_fontsize, 0, 1, 1, 1)
        self.comboBox_plottype = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_plottype.setObjectName("comboBox_plottype")
        self.comboBox_plottype.addItem("")
        self.comboBox_plottype.addItem("")
        self.comboBox_plottype.addItem("")
        self.comboBox_plottype.addItem("")
        self.comboBox_plottype.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_plottype, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.checkBox_showtangent = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_showtangent.setObjectName("checkBox_showtangent")
        self.gridLayout_3.addWidget(self.checkBox_showtangent, 2, 0, 1, 2)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.Samples = QtWidgets.QWidget()
        self.Samples.setObjectName("Samples")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Samples)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.Samples)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_legend = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_legend.setObjectName("checkBox_legend")
        self.gridLayout.addWidget(self.checkBox_legend, 0, 0, 1, 1)
        self.radioButton_topleft = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_topleft.setObjectName("radioButton_topleft")
        self.gridLayout.addWidget(self.radioButton_topleft, 1, 0, 1, 1)
        self.radioButton_topright = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_topright.setObjectName("radioButton_topright")
        self.gridLayout.addWidget(self.radioButton_topright, 1, 1, 1, 1)
        self.radioButton_bottomleft = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_bottomleft.setObjectName("radioButton_bottomleft")
        self.gridLayout.addWidget(self.radioButton_bottomleft, 2, 0, 1, 1)
        self.radioButton_bottomright = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_bottomright.setObjectName("radioButton_bottomright")
        self.gridLayout.addWidget(self.radioButton_bottomright, 2, 1, 1, 1)
        self.radioButton_outside = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_outside.setObjectName("radioButton_outside")
        self.gridLayout.addWidget(self.radioButton_outside, 3, 0, 1, 1)
        self.radioButton_best = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_best.setChecked(True)
        self.radioButton_best.setObjectName("radioButton_best")
        self.gridLayout.addWidget(self.radioButton_best, 3, 1, 1, 1)
        self.checkBox_addEgtoLeg = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_addEgtoLeg.setObjectName("checkBox_addEgtoLeg")
        self.gridLayout.addWidget(self.checkBox_addEgtoLeg, 0, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.listWidget = QtWidgets.QListWidget(self.Samples)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.tabWidget.addTab(self.Samples, "")
        self.EditLegend = QtWidgets.QWidget()
        self.EditLegend.setObjectName("EditLegend")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.EditLegend)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.EditLegend)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollArea_EditLegend = QtWidgets.QScrollArea(self.frame_3)
        self.scrollArea_EditLegend.setWidgetResizable(True)
        self.scrollArea_EditLegend.setObjectName("scrollArea_EditLegend")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 596, 507))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_EditLegend.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.addWidget(self.scrollArea_EditLegend, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.EditLegend, "")
        self.Tauc = QtWidgets.QWidget()
        self.Tauc.setObjectName("Tauc")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Tauc)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.Tauc)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea_Tauc = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea_Tauc.setWidgetResizable(True)
        self.scrollArea_Tauc.setObjectName("scrollArea_Tauc")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 596, 507))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_Tauc.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea_Tauc, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Tauc, "")
        self.EgSearch = QtWidgets.QWidget()
        self.EgSearch.setObjectName("EgSearch")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.EgSearch)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_recordEg = QtWidgets.QPushButton(self.EgSearch)
        self.pushButton_recordEg.setObjectName("pushButton_recordEg")
        self.gridLayout_8.addWidget(self.pushButton_recordEg, 0, 1, 1, 2)
        self.label_EgsearchSamplename = QtWidgets.QLabel(self.EgSearch)
        self.label_EgsearchSamplename.setObjectName("label_EgsearchSamplename")
        self.gridLayout_8.addWidget(self.label_EgsearchSamplename, 0, 0, 1, 1)
        self.doubleSpinBox_maxX = QtWidgets.QDoubleSpinBox(self.EgSearch)
        self.doubleSpinBox_maxX.setSingleStep(0.01)
        self.doubleSpinBox_maxX.setObjectName("doubleSpinBox_maxX")
        self.gridLayout_8.addWidget(self.doubleSpinBox_maxX, 5, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.EgSearch)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.EgSearch)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.EgSearch)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 5, 0, 1, 1)
        self.doubleSpinBox_verticalIP = QtWidgets.QDoubleSpinBox(self.EgSearch)
        self.doubleSpinBox_verticalIP.setReadOnly(False)
        self.doubleSpinBox_verticalIP.setDecimals(3)
        self.doubleSpinBox_verticalIP.setSingleStep(0.01)
        self.doubleSpinBox_verticalIP.setObjectName("doubleSpinBox_verticalIP")
        self.gridLayout_8.addWidget(self.doubleSpinBox_verticalIP, 2, 1, 1, 2)
        self.doubleSpinBox_Xcross = QtWidgets.QDoubleSpinBox(self.EgSearch)
        self.doubleSpinBox_Xcross.setReadOnly(True)
        self.doubleSpinBox_Xcross.setDecimals(3)
        self.doubleSpinBox_Xcross.setObjectName("doubleSpinBox_Xcross")
        self.gridLayout_8.addWidget(self.doubleSpinBox_Xcross, 3, 1, 1, 2)
        self.doubleSpinBox_minX = QtWidgets.QDoubleSpinBox(self.EgSearch)
        self.doubleSpinBox_minX.setSingleStep(0.01)
        self.doubleSpinBox_minX.setObjectName("doubleSpinBox_minX")
        self.gridLayout_8.addWidget(self.doubleSpinBox_minX, 5, 1, 1, 1)
        self.doubleSpinBox_EU = QtWidgets.QDoubleSpinBox(self.EgSearch)
        self.doubleSpinBox_EU.setReadOnly(True)
        self.doubleSpinBox_EU.setDecimals(3)
        self.doubleSpinBox_EU.setMaximum(999999.0)
        self.doubleSpinBox_EU.setObjectName("doubleSpinBox_EU")
        self.gridLayout_8.addWidget(self.doubleSpinBox_EU, 4, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.EgSearch)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 4, 0, 1, 1)
        self.tabWidget.addTab(self.EgSearch, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 923, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport_DATA = QtWidgets.QAction(MainWindow)
        self.actionImport_DATA.setObjectName("actionImport_DATA")
        self.actionExport_Graph = QtWidgets.QAction(MainWindow)
        self.actionExport_Graph.setObjectName("actionExport_Graph")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionExport_All_DATA = QtWidgets.QAction(MainWindow)
        self.actionExport_All_DATA.setObjectName("actionExport_All_DATA")
        self.menuFile.addAction(self.actionImport_DATA)
        self.menuFile.addAction(self.actionExport_Graph)
        self.menuFile.addAction(self.actionExport_All_DATA)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NK - plot & Egcalc"))
        self.pushButton_SGFilter.setText(_translate("MainWindow", "SavitzkyGolayFilter"))
        self.pushButton_goback.setText(_translate("MainWindow", "GoBack"))
        self.comboBox_plottype.setItemText(0, _translate("MainWindow", "Linear, nm"))
        self.comboBox_plottype.setItemText(1, _translate("MainWindow", "Linear, eV"))
        self.comboBox_plottype.setItemText(2, _translate("MainWindow", "Tauc (E*a*n)**m"))
        self.comboBox_plottype.setItemText(3, _translate("MainWindow", "Tauc (E*a)**m"))
        self.comboBox_plottype.setItemText(4, _translate("MainWindow", "Ln(a)"))
        self.label.setText(_translate("MainWindow", "Fontsize"))
        self.checkBox_showtangent.setText(_translate("MainWindow", "Show tangent"))
        self.groupBox.setTitle(_translate("MainWindow", "Legend"))
        self.checkBox_legend.setText(_translate("MainWindow", "legend?"))
        self.radioButton_topleft.setText(_translate("MainWindow", "TopLeft"))
        self.radioButton_topright.setText(_translate("MainWindow", "TopRight"))
        self.radioButton_bottomleft.setText(_translate("MainWindow", "BottomLeft"))
        self.radioButton_bottomright.setText(_translate("MainWindow", "BottomRight"))
        self.radioButton_outside.setText(_translate("MainWindow", "Outside"))
        self.radioButton_best.setText(_translate("MainWindow", "Best"))
        self.checkBox_addEgtoLeg.setText(_translate("MainWindow", "EgXcross?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Samples), _translate("MainWindow", "Samples"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EditLegend), _translate("MainWindow", "EditLegend"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tauc), _translate("MainWindow", "Tauc"))
        self.pushButton_recordEg.setText(_translate("MainWindow", "Record values"))
        self.label_EgsearchSamplename.setText(_translate("MainWindow", "samplename"))
        self.label_4.setText(_translate("MainWindow", "Eg: X-axis crossing of tg"))
        self.label_3.setText(_translate("MainWindow", "inflection point position"))
        self.label_2.setText(_translate("MainWindow", "X-axis range"))
        self.label_5.setText(_translate("MainWindow", "1/slope at IP (~Eu)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EgSearch), _translate("MainWindow", "EgSearch"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionImport_DATA.setText(_translate("MainWindow", "Import DATA"))
        self.actionExport_Graph.setText(_translate("MainWindow", "Export Graph"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionExport_All_DATA.setText(_translate("MainWindow", "Export All DATA"))

