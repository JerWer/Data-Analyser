# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XRDgui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1184, 849)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(5)
        self.splitter.setObjectName("splitter")
        self.mplwidget = QtWidgets.QWidget(self.splitter)
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
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.frame)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(5)
        self.splitter_2.setObjectName("splitter_2")
        self.frame_2 = QtWidgets.QFrame(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_3 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setHandleWidth(5)
        self.splitter_3.setObjectName("splitter_3")
        self.listWidget_samples = QtWidgets.QListWidget(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_samples.sizePolicy().hasHeightForWidth())
        self.listWidget_samples.setSizePolicy(sizePolicy)
        self.listWidget_samples.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_samples.setObjectName("listWidget_samples")
        self.listWidget_refpatt = QtWidgets.QListWidget(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_refpatt.sizePolicy().hasHeightForWidth())
        self.listWidget_refpatt.setSizePolicy(sizePolicy)
        self.listWidget_refpatt.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_refpatt.setObjectName("listWidget_refpatt")
        self.verticalLayout_2.addWidget(self.splitter_3)
        self.frame_3 = QtWidgets.QFrame(self.splitter_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 120))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_Xshift = QtWidgets.QPushButton(self.tab)
        self.pushButton_Xshift.setObjectName("pushButton_Xshift")
        self.gridLayout_3.addWidget(self.pushButton_Xshift, 0, 0, 1, 1)
        self.pushButton_Yshift = QtWidgets.QPushButton(self.tab)
        self.pushButton_Yshift.setObjectName("pushButton_Yshift")
        self.gridLayout_3.addWidget(self.pushButton_Yshift, 0, 1, 1, 1)
        self.pushButton_BkgRemovalPoly = QtWidgets.QPushButton(self.tab)
        self.pushButton_BkgRemovalPoly.setObjectName("pushButton_BkgRemovalPoly")
        self.gridLayout_3.addWidget(self.pushButton_BkgRemovalPoly, 0, 2, 1, 2)
        self.spinBox_PolyNumb = QtWidgets.QSpinBox(self.tab)
        self.spinBox_PolyNumb.setProperty("value", 12)
        self.spinBox_PolyNumb.setObjectName("spinBox_PolyNumb")
        self.gridLayout_3.addWidget(self.spinBox_PolyNumb, 0, 4, 1, 1)
        self.pushButton_SGfilter = QtWidgets.QPushButton(self.tab)
        self.pushButton_SGfilter.setObjectName("pushButton_SGfilter")
        self.gridLayout_3.addWidget(self.pushButton_SGfilter, 0, 5, 1, 2)
        self.pushButton_Backtooriginal = QtWidgets.QPushButton(self.tab)
        self.pushButton_Backtooriginal.setObjectName("pushButton_Backtooriginal")
        self.gridLayout_3.addWidget(self.pushButton_Backtooriginal, 0, 7, 1, 1)
        self.doubleSpinBox_Xshift = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_Xshift.setMinimum(-100000.0)
        self.doubleSpinBox_Xshift.setMaximum(100000.0)
        self.doubleSpinBox_Xshift.setSingleStep(1.0)
        self.doubleSpinBox_Xshift.setObjectName("doubleSpinBox_Xshift")
        self.gridLayout_3.addWidget(self.doubleSpinBox_Xshift, 1, 0, 1, 1)
        self.doubleSpinBox_Yshift = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_Yshift.setMinimum(-100000.0)
        self.doubleSpinBox_Yshift.setMaximum(100000.0)
        self.doubleSpinBox_Yshift.setSingleStep(1.0)
        self.doubleSpinBox_Yshift.setObjectName("doubleSpinBox_Yshift")
        self.gridLayout_3.addWidget(self.doubleSpinBox_Yshift, 1, 1, 1, 1)
        self.pushButton_rescale = QtWidgets.QPushButton(self.tab)
        self.pushButton_rescale.setObjectName("pushButton_rescale")
        self.gridLayout_3.addWidget(self.pushButton_rescale, 1, 2, 1, 1)
        self.doubleSpinBox_rescale = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_rescale.setDecimals(1)
        self.doubleSpinBox_rescale.setMaximum(10000.0)
        self.doubleSpinBox_rescale.setProperty("value", 1000.0)
        self.doubleSpinBox_rescale.setObjectName("doubleSpinBox_rescale")
        self.gridLayout_3.addWidget(self.doubleSpinBox_rescale, 1, 3, 1, 2)
        self.spinBox_SGfilter1 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_SGfilter1.setMaximum(999)
        self.spinBox_SGfilter1.setProperty("value", 31)
        self.spinBox_SGfilter1.setObjectName("spinBox_SGfilter1")
        self.gridLayout_3.addWidget(self.spinBox_SGfilter1, 1, 5, 1, 1)
        self.spinBox_SGfilter2 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_SGfilter2.setMaximum(999)
        self.spinBox_SGfilter2.setProperty("value", 5)
        self.spinBox_SGfilter2.setObjectName("spinBox_SGfilter2")
        self.gridLayout_3.addWidget(self.spinBox_SGfilter2, 1, 6, 1, 1)
        self.checkBox_showOrig = QtWidgets.QCheckBox(self.tab)
        self.checkBox_showOrig.setObjectName("checkBox_showOrig")
        self.gridLayout_3.addWidget(self.checkBox_showOrig, 1, 7, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy)
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(43, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkBox_legend = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_legend.setObjectName("checkBox_legend")
        self.horizontalLayout.addWidget(self.checkBox_legend)
        spacerItem1 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.checkBox_ylabel = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_ylabel.setObjectName("checkBox_ylabel")
        self.horizontalLayout.addWidget(self.checkBox_ylabel)
        self.checkBox_Qspace = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_Qspace.setObjectName("checkBox_Qspace")
        self.horizontalLayout.addWidget(self.checkBox_Qspace)
        spacerItem2 = QtWidgets.QSpacerItem(358, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_2, "")
        self.EditLegend = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EditLegend.sizePolicy().hasHeightForWidth())
        self.EditLegend.setSizePolicy(sizePolicy)
        self.EditLegend.setObjectName("EditLegend")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.EditLegend)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.EditLegend)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 878, 86))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_legend = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_legend.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_legend.setObjectName("verticalLayout_legend")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.EditLegend, "")
        self.tab_3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_3.sizePolicy().hasHeightForWidth())
        self.tab_3.setSizePolicy(sizePolicy)
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.doubleSpinBox_threshold = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_threshold.setSingleStep(0.01)
        self.doubleSpinBox_threshold.setProperty("value", 0.08)
        self.doubleSpinBox_threshold.setObjectName("doubleSpinBox_threshold")
        self.gridLayout_2.addWidget(self.doubleSpinBox_threshold, 2, 5, 1, 1)
        self.spinBox_MinDist = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_MinDist.setMaximum(999)
        self.spinBox_MinDist.setProperty("value", 20)
        self.spinBox_MinDist.setObjectName("spinBox_MinDist")
        self.gridLayout_2.addWidget(self.spinBox_MinDist, 2, 6, 1, 1)
        self.spinBox_A = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_A.setMaximum(999)
        self.spinBox_A.setProperty("value", 35)
        self.spinBox_A.setObjectName("spinBox_A")
        self.gridLayout_2.addWidget(self.spinBox_A, 2, 7, 1, 1)
        self.spinBox_B = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_B.setMaximum(999)
        self.spinBox_B.setProperty("value", 10)
        self.spinBox_B.setObjectName("spinBox_B")
        self.gridLayout_2.addWidget(self.spinBox_B, 2, 8, 1, 1)
        self.doubleSpinBox_ScherrerCst = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_ScherrerCst.setSingleStep(0.01)
        self.doubleSpinBox_ScherrerCst.setProperty("value", 0.89)
        self.doubleSpinBox_ScherrerCst.setObjectName("doubleSpinBox_ScherrerCst")
        self.gridLayout_2.addWidget(self.doubleSpinBox_ScherrerCst, 2, 3, 1, 1)
        self.spinBox_C = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_C.setMaximum(999)
        self.spinBox_C.setProperty("value", 80)
        self.spinBox_C.setObjectName("spinBox_C")
        self.gridLayout_2.addWidget(self.spinBox_C, 2, 9, 1, 1)
        self.checkBox_show = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_show.setObjectName("checkBox_show")
        self.gridLayout_2.addWidget(self.checkBox_show, 2, 10, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 2, 1, 1)
        self.checkBox_shownames = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_shownames.setObjectName("checkBox_shownames")
        self.gridLayout_2.addWidget(self.checkBox_shownames, 1, 10, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 9, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 7, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 8, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 6, 1, 1)
        self.pushButton_peaknames = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_peaknames.setObjectName("pushButton_peaknames")
        self.gridLayout_2.addWidget(self.pushButton_peaknames, 1, 2, 1, 2)
        self.checkBox_auto = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_auto.setObjectName("checkBox_auto")
        self.gridLayout_2.addWidget(self.checkBox_auto, 2, 1, 1, 1)
        self.pushButton_detectpeaks = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_detectpeaks.setObjectName("pushButton_detectpeaks")
        self.gridLayout_2.addWidget(self.pushButton_detectpeaks, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setMinimumSectionSize(10)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1184, 26))
        self.menubar.setObjectName("menubar")
        self.menuImport_export = QtWidgets.QMenu(self.menubar)
        self.menuImport_export.setObjectName("menuImport_export")
        self.menuExport = QtWidgets.QMenu(self.menubar)
        self.menuExport.setObjectName("menuExport")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionimport_data = QtWidgets.QAction(MainWindow)
        self.actionimport_data.setObjectName("actionimport_data")
        self.actionimport_ref = QtWidgets.QAction(MainWindow)
        self.actionimport_ref.setObjectName("actionimport_ref")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionexportWillHall = QtWidgets.QAction(MainWindow)
        self.actionexportWillHall.setObjectName("actionexportWillHall")
        self.actionmakeTimeGraph = QtWidgets.QAction(MainWindow)
        self.actionmakeTimeGraph.setObjectName("actionmakeTimeGraph")
        self.actionExport_export = QtWidgets.QAction(MainWindow)
        self.actionExport_export.setObjectName("actionExport_export")
        self.actionExportWillHall = QtWidgets.QAction(MainWindow)
        self.actionExportWillHall.setObjectName("actionExportWillHall")
        self.actionExport_as_Ref = QtWidgets.QAction(MainWindow)
        self.actionExport_as_Ref.setObjectName("actionExport_as_Ref")
        self.menuImport_export.addAction(self.actionimport_data)
        self.menuImport_export.addAction(self.actionimport_ref)
        self.menuExport.addAction(self.actionExport_export)
        self.menuExport.addAction(self.actionExportWillHall)
        self.menuExport.addAction(self.actionExport_as_Ref)
        self.menubar.addAction(self.menuImport_export.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XRD"))
        self.pushButton_Xshift.setText(_translate("MainWindow", "Xshift"))
        self.pushButton_Yshift.setText(_translate("MainWindow", "Yshift"))
        self.pushButton_BkgRemovalPoly.setText(_translate("MainWindow", "BkgRemovalPoly"))
        self.pushButton_SGfilter.setText(_translate("MainWindow", "SavitzkyGolayFilter"))
        self.pushButton_Backtooriginal.setText(_translate("MainWindow", "BackToOriginal"))
        self.pushButton_rescale.setText(_translate("MainWindow", "Rescale to:"))
        self.checkBox_showOrig.setText(_translate("MainWindow", "show Original"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tuning"))
        self.checkBox_legend.setText(_translate("MainWindow", "Legend?"))
        self.checkBox_ylabel.setText(_translate("MainWindow", "no y label"))
        self.checkBox_Qspace.setText(_translate("MainWindow", "q space"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Legend"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EditLegend), _translate("MainWindow", "EditLegend"))
        self.checkBox_show.setText(_translate("MainWindow", "show"))
        self.label_6.setText(_translate("MainWindow", "ScherrerCst"))
        self.checkBox_shownames.setText(_translate("MainWindow", "showNames"))
        self.label_5.setText(_translate("MainWindow", "diffLeftRight"))
        self.label_3.setText(_translate("MainWindow", "#points"))
        self.label_4.setText(_translate("MainWindow", "basepts"))
        self.label.setText(_translate("MainWindow", "Thres."))
        self.label_2.setText(_translate("MainWindow", "MinDist"))
        self.pushButton_peaknames.setText(_translate("MainWindow", "Confirm peak names"))
        self.checkBox_auto.setText(_translate("MainWindow", "Auto"))
        self.pushButton_detectpeaks.setText(_translate("MainWindow", "Detect Peaks"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "PeakDetection"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PeakName"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Position (2theta)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Position (q)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Intensity (a.u.)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "FWHM (2theta)"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "PeakArea"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "IntegralBreadth (2theta)"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Cryst.Size KI/Dcos(theta)(nm)"))
        self.menuImport_export.setTitle(_translate("MainWindow", "Import"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.actionimport_data.setText(_translate("MainWindow", "Import data"))
        self.actionimport_ref.setText(_translate("MainWindow", "Import ref"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionexportWillHall.setText(_translate("MainWindow", "exportWillHall"))
        self.actionmakeTimeGraph.setText(_translate("MainWindow", "makeTimeGraph"))
        self.actionExport_export.setText(_translate("MainWindow", "Export"))
        self.actionExportWillHall.setText(_translate("MainWindow", "ExportWillHall"))
        self.actionExport_as_Ref.setText(_translate("MainWindow", "Export as Ref"))

