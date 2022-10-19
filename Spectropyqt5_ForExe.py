import sys
import os
from pathlib import Path
import numpy as np
from math import factorial
from scipy.interpolate import UnivariateSpline
import csv

# import pip
# def import_or_install(package):
#     try:
#         __import__(package)
#     except ImportError:
#         pip.main(['install', package]) 

# import_or_install('tkcolorpicker')
# import_or_install('peakutils')
#%%######################################################################################################
import matplotlib
matplotlib.use("Qt5Agg")
#%%######################################################################################################
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QColorDialog, QAction
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import copy
# from matplotlib.ticker import MaxNLocator
# from matplotlib.transforms import Bbox
# import pickle
# import six
from functools import partial
# import darktolight as DtoL
import os.path
# import shutil
# from dateutil import parser
# from scipy import stats
# from statistics import mean
# from scipy.interpolate import interp1d
# from XRD_NREL import savitzky_golay
# from PyQt5.uic import loadUiType
# Ui_MainWindow, QMainWindow = loadUiType('spectrogui.ui')
# Ui_MainWindow, QMainWindow = loadUiType(r'C:\Users\serjw\Documents\nBox\PythonScripts\SERIS-pythonscripts\executables\All\spectrogui.ui')
from spectrogui import Ui_MainWindow
exedirectory=str(Path(os.path.abspath(__file__)).parent)

LARGE_FONT= ("Verdana", 16)
SMALL_FONT= ("Verdana", 10)

echarge = 1.60218e-19
planck = 6.62607e-34
lightspeed = 299792458
DATAspectro={}
SpectlegendMod=[]
titSpect=0
Patternsamplenameslist=[]
takenforplot=[]
listofanswer=[]
listoflinestyle=[]
listofcolorstyle=[]
listoflinewidthstyle=[]
colorstylelist = ['black', 'red', 'blue', 'brown', 'green','cyan','magenta','olive','navy','orange','gray','aliceblue','antiquewhite','aqua','aquamarine','azure','beige','bisque','blanchedalmond','blue','blueviolet','brown','burlywood','cadetblue','chartreuse','chocolate','coral','cornflowerblue','cornsilk','crimson','darkblue','darkcyan','darkgoldenrod','darkgray','darkgreen','darkkhaki','darkmagenta','darkolivegreen','darkorange','darkorchid','darkred','darksalmon','darkseagreen','darkslateblue','darkslategray','darkturquoise','darkviolet','deeppink','deepskyblue','dimgray','dodgerblue','firebrick','floralwhite','forestgreen','fuchsia','gainsboro','ghostwhite','gold','goldenrod','greenyellow','honeydew','hotpink','indianred','indigo','ivory','khaki','lavender','lavenderblush','lawngreen','lemonchiffon','lightblue','lightcoral','lightcyan','lightgoldenrodyellow','lightgreen','lightgray','lightpink','lightsalmon','lightseagreen','lightskyblue','lightslategray','lightsteelblue','lightyellow','lime','limegreen','linen','magenta','maroon','mediumaquamarine','mediumblue','mediumorchid','mediumpurple','mediumseagreen','mediumslateblue','mediumspringgreen','mediumturquoise','mediumvioletred','midnightblue','mintcream','mistyrose','moccasin','navajowhite','navy','oldlace','olive','olivedrab','orange','orangered','orchid','palegoldenrod','palegreen','paleturquoise','palevioletred','papayawhip','peachpuff','peru','pink','plum','powderblue','purple','red','rosybrown','royalblue','saddlebrown','salmon','sandybrown','seagreen','seashell','sienna','silver','skyblue','slateblue','slategray','snow','springgreen','steelblue','tan','teal','thistle','tomato','turquoise','violet','wheat','white','whitesmoke','yellow','yellowgreen']


def savitzky_golay(y, window_size, order, deriv=0, rate=1):
    try:
        window_size = np.abs(np.int(window_size))
        order = np.abs(np.int(order))
    except ValueError:
        raise ValueError("window_size and order have to be of type int")
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
    # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid')

class Spectroapp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.DATA={}
        self.fig = Figure()
        self.Spectrograph = self.fig.add_subplot(111)
        self.addmpl(self.fig,self.ui.verticalLayout_mplwidget, self.ui.mplwidget)
        
        finish = QAction("Quit", self)
        finish.triggered.connect(lambda: self.closeEvent(1))
        
        self.ui.actionHelp.triggered.connect(self.Helpcall)
        self.ui.actionImport_DATA.triggered.connect(self.GetSpectroDATA)
        self.ui.actionExport_All_DATA.triggered.connect(self.sortandexportspectro)
        self.ui.actionExport_Graph.triggered.connect(self.ExportGraph)
        
        self.ui.pushButton_SGFilter.clicked.connect(self.SavitzkyGolayFiltering)
        self.ui.pushButton_goback.clicked.connect(self.backtoOriginal)

        self.ui.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ui.listWidget.itemClicked.connect(self.UpdateGraph0)
        
        self.ui.checkBox_legend.toggled.connect(self.UpdateGraph0)
        self.ui.radioButton_topleft.toggled.connect(self.UpdateGraph0)
        self.ui.radioButton_topright.toggled.connect(self.UpdateGraph0)
        self.ui.radioButton_bottomleft.toggled.connect(self.UpdateGraph0)
        self.ui.radioButton_bottomright.toggled.connect(self.UpdateGraph0)
        self.ui.radioButton_outside.toggled.connect(self.UpdateGraph0)
        self.ui.radioButton_best.toggled.connect(self.UpdateGraph0)
        self.ui.spinBox_fontsize.valueChanged.connect(self.UpdateGraph0)
        self.ui.comboBox_plottype.currentTextChanged.connect(self.UpdateGraph0)
        self.ui.checkBox_showtangent.toggled.connect(self.UpdateGraph0)
        self.ui.checkBox_addEgtoLeg.toggled.connect(self.UpdateGraph0)
        self.ui.pushButton_recordEg.clicked.connect(self.RecordEg)
        
        self.ui.tabWidget.currentChanged.connect(self.onclicklegendtab)
        
        self.ui.doubleSpinBox_verticalIP.valueChanged.connect(lambda:self.plotEgsearch(self.ui.label_EgsearchSamplename.text()))
        self.ui.doubleSpinBox_minX.valueChanged.connect(lambda:self.plotEgsearch(self.ui.label_EgsearchSamplename.text()))
        self.ui.doubleSpinBox_maxX.valueChanged.connect(lambda:self.plotEgsearch(self.ui.label_EgsearchSamplename.text()))
        # self.ui.doubleSpinBox_minY.valueChanged.connect(lambda:self.plotEgsearch(self.ui.label_EgsearchSamplename.text()))
        # self.ui.doubleSpinBox_maxY.valueChanged.connect(lambda:self.plotEgsearch(self.ui.label_EgsearchSamplename.text()))

    def closeEvent(self, event):
        
        """ what happens when close the program"""
        
        close = QMessageBox.question(self,
                                     "QUIT",
                                     "Are you sure?",
                                      QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
            try:
                app.quit()
            except:
                pass
        else:
            event.ignore()

    def addmpl(self, fig, whereLayout, whereWidget):
        self.canvas = FigureCanvas(fig)
        whereLayout.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, 
                whereWidget, coordinates=True)
        whereLayout.addWidget(self.toolbar)
        
    def Helpcall(self):
        self.w = Help()
        self.w.show()
    
    def onclicklegendtab(self,indexoftab):
        # print(indexoftab)   
        if indexoftab==1 and self.ui.checkBox_legend.isChecked():
            self.populate()
        elif indexoftab==3:
            self.initialEgsearch()
            
    def initialEgsearch(self):
        global takenforplot
        if takenforplot!=[]:
            
            # self.Spectrograph.clear()
            # self.fig.canvas.draw_idle()
            foundA=0
            for item in takenforplot:
                if self.DATA[item][1]=='A':
                    foundA=1
                    break
            if foundA:
                self.ui.label_EgsearchSamplename.setText(item)
                # minimumY=min(self.DATA[item][13])
                # self.ui.doubleSpinBox_minY.setValue(minimumY/(10**19))
                # maximumY=max(self.DATA[item][13])
                # self.ui.doubleSpinBox_maxY.setValue(maximumY/(10**19))
                minimumX=min(self.DATA[item][10])
                self.ui.doubleSpinBox_minX.setValue(minimumX)
                maximumX=max(self.DATA[item][10])
                self.ui.doubleSpinBox_maxX.setValue(maximumX)
                self.ui.doubleSpinBox_verticalIP.setValue(minimumX+(maximumX-minimumX)/2)
                
                self.plotEgsearch(item)
    
    def RecordEg(self):
        self.DATA[self.ui.label_EgsearchSamplename.text()][14]=self.ui.doubleSpinBox_verticalIP.value()
        self.DATA[self.ui.label_EgsearchSamplename.text()][15]=self.ui.doubleSpinBox_Xcross.value()
        self.DATA[self.ui.label_EgsearchSamplename.text()][16]=self.xtg
        self.DATA[self.ui.label_EgsearchSamplename.text()][17]=self.ytg
            
    def plotEgsearch(self, samplename):
        DATAx=self.DATA
        # print('plot')
        i=samplename
        if i!='samplename' and self.ui.doubleSpinBox_minX.value()<self.ui.doubleSpinBox_maxX.value():
            self.Spectrograph.clear()
            # print('plot2')
            if self.ui.doubleSpinBox_verticalIP.value()<self.ui.doubleSpinBox_minX.value() or self.ui.doubleSpinBox_verticalIP.value()>self.ui.doubleSpinBox_maxX.value():
                self.ui.doubleSpinBox_verticalIP.setValue(self.ui.doubleSpinBox_minX.value()+(self.ui.doubleSpinBox_maxX.value()-self.ui.doubleSpinBox_minX.value())/2)
            x=[]
            y=[]
            for item in range(len(DATAx[i][10])):
                if DATAx[i][10][item] >self.ui.doubleSpinBox_minX.value() and DATAx[i][10][item]<=self.ui.doubleSpinBox_maxX.value():
                    x.append(DATAx[i][10][item])
                    y.append(DATAx[i][13][item])
            # print(DATAx[i][10])
            # print(x)
            xhighslope=self.ui.doubleSpinBox_verticalIP.value()
            spl=UnivariateSpline(x, y, s=0)
            splder = spl.derivative(n=1)
            slopeatIP=splder(xhighslope)
            
            self.xtg = np.linspace(min(x),max(x),3)
            self.ytg = slopeatIP*self.xtg+spl(xhighslope)-slopeatIP*xhighslope
            xcrossing=(-spl(xhighslope)+slopeatIP*xhighslope)/slopeatIP
            self.ui.doubleSpinBox_Xcross.setValue(xcrossing)
            # print(1/slopeatIP)
            # self.ui.doubleSpinBox_Eu.setValue(1/slopeatIP)
            
            
            if self.ui.checkBox_legend.isChecked():
                self.Spectrograph.plot(x,y,label=DATAx[i][6],linestyle=DATAx[i][7],color=DATAx[i][8],linewidth=DATAx[i][9])
                self.Spectrograph.plot(self.xtg,self.ytg,linestyle='--', color='r',linewidth=DATAx[i][9], label='tangente to IP')
                self.Spectrograph.plot([xhighslope,xcrossing],[spl(xhighslope),0], 'ro')
            else:
                self.Spectrograph.plot(x,y,linestyle=DATAx[i][7],color=DATAx[i][8],linewidth=DATAx[i][9])
                self.Spectrograph.plot(self.xtg,self.ytg,linestyle='--', color='r',linewidth=DATAx[i][9])
                self.Spectrograph.plot([xhighslope,xcrossing],[spl(xhighslope),0], 'ro')
                
            self.Spectrograph.set_ylabel('(eV*A/t)^n')
            self.Spectrograph.set_xlabel('Energy (eV)')
            self.Spectrograph.set_xlim([self.ui.doubleSpinBox_minX.value(),self.ui.doubleSpinBox_maxX.value()])
            # self.Spectrograph.set_ylim([self.ui.doubleSpinBox_minY.value()*(10**19),self.ui.doubleSpinBox_maxY.value()*(10**19)])
            if self.ui.checkBox_legend.isChecked():
                if self.ui.radioButton_topleft.isChecked():
                    self.leg=self.Spectrograph.legend(loc=2, fontsize = self.ui.spinBox_fontsize.value())
                elif self.ui.radioButton_topright.isChecked():
                    self.leg=self.Spectrograph.legend(loc=1, fontsize = self.ui.spinBox_fontsize.value())
                elif self.ui.radioButton_bottomleft.isChecked():
                    self.leg=self.Spectrograph.legend(loc=3, fontsize = self.ui.spinBox_fontsize.value())
                elif self.ui.radioButton_bottomright.isChecked():
                    self.leg=self.Spectrograph.legend(loc=4, fontsize = self.ui.spinBox_fontsize.value())
                elif self.ui.radioButton_outside.isChecked():
                    self.leg=self.Spectrograph.legend(bbox_to_anchor=(1, 1), loc='upper left', ncol=1, fontsize = self.ui.spinBox_fontsize.value())
                elif self.ui.radioButton_best.isChecked():
                    self.leg=self.Spectrograph.legend(loc=0, fontsize = self.ui.spinBox_fontsize.value())
                    
            for item in ([self.Spectrograph.title, self.Spectrograph.xaxis.label, self.Spectrograph.yaxis.label] +
                             self.Spectrograph.get_xticklabels() + self.Spectrograph.get_yticklabels()):
                item.set_fontsize(self.ui.spinBox_fontsize.value())
            
            self.fig.canvas.draw_idle()

    def populate(self):
        global takenforplot
        global colorstylelist
        global listofanswer
        global listoflinestyle
        global listofcolorstyle, listoflinewidthstyle
        DATAx=self.DATA
        listofanswer=[]
        # sampletotake=[]
        # if takenforplot!=[]:
        #     for item in takenforplot:
        #         sampletotake.append(DATAx[item])
                
        listoflinestyle=[]
        listofcolorstyle=[]
        listoflinewidthstyle=[]
        for item in DATAx.keys():
            listoflinestyle.append(DATAx[item][7])
            listofcolorstyle.append(DATAx[item][8])
            listofanswer.append(DATAx[item][6])
            listoflinewidthstyle.append(str(DATAx[item][9]))
            
        self.clearLayout(self.ui.gridLayout_6)
        self.ui.scrollArea_EditLegend = QtWidgets.QScrollArea(self.ui.frame_3)
        self.ui.scrollArea_EditLegend.setWidgetResizable(True)
        self.ui.scrollArea_EditLegend.setObjectName("scrollArea_EditLegend")
        self.ui.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.ui.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.ui.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.ui.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.ui.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ui.scrollAreaWidgetContents_2)
        self.ui.verticalLayout_3.setObjectName("verticalLayout_3")
        
        item1=0
        for itemm in DATAx.keys():
            if itemm in takenforplot:
                #print(itemm)
                self.frame = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_2)
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
                self.horizontalLayout.setObjectName("horizontalLayout")
                
                label = QtWidgets.QLabel(self.frame)
                label.setText(itemm)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
                label.setSizePolicy(sizePolicy)
                self.horizontalLayout.addWidget(label)
                
                listofanswer[item1]=QtWidgets.QLineEdit(self.frame)
                listofanswer[item1].setText(DATAx[itemm][6])
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(listofanswer[item1].sizePolicy().hasHeightForWidth())
                listofanswer[item1].setSizePolicy(sizePolicy)
                self.horizontalLayout.addWidget(listofanswer[item1])
                listofanswer[item1].textChanged.connect(self.UpdateSpectroLegMod)
                
                listoflinestyle[item1] = QtWidgets.QComboBox(self.frame)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(listoflinestyle[item1].sizePolicy().hasHeightForWidth())
                listoflinestyle[item1].setObjectName("comboBox_matname"+str(item1))
                listoflinestyle[item1].addItems(["-","--","-.",":"])
                listoflinestyle[item1].setCurrentText(DATAx[itemm][7])
                self.horizontalLayout.addWidget(listoflinestyle[item1])
                listoflinestyle[item1].currentTextChanged.connect(self.UpdateSpectroLegMod)
                
                colstyle = QtWidgets.QPushButton('Select Color', self.frame)
                colstyle.setStyleSheet("color:"+str(listofcolorstyle[item1])+";")
                self.horizontalLayout.addWidget(colstyle)
                colstyle.clicked.connect(partial(self.getColor,item1))
                
                listoflinewidthstyle[item1] = QtWidgets.QSpinBox(self.frame)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(listoflinewidthstyle[item1].sizePolicy().hasHeightForWidth())
                listoflinewidthstyle[item1].setSizePolicy(sizePolicy)
                listoflinewidthstyle[item1].setMaximum(9999999)
                listoflinewidthstyle[item1].setObjectName("spinBox_"+str(item1))
                listoflinewidthstyle[item1].setValue(DATAx[itemm][9])
                self.horizontalLayout.addWidget(listoflinewidthstyle[item1])
                listoflinewidthstyle[item1].valueChanged.connect(self.UpdateSpectroLegMod)
                
                self.ui.verticalLayout_3.addWidget(self.frame)
            
            else:
                listofanswer[item1]=str(DATAx[itemm][6])
                listoflinestyle.append(str(DATAx[itemm][7]))
                listofcolorstyle.append(str(DATAx[itemm][8]))
                listoflinewidthstyle.append(str(DATAx[itemm][9]))
            
            item1+=1
        
        self.ui.scrollArea_EditLegend.setWidget(self.ui.scrollAreaWidgetContents_2)
        self.ui.gridLayout_6.addWidget(self.ui.scrollArea_EditLegend, 0, 0, 1, 1)
    
    def getColor(self,rowitem):
        global listofcolorstyle
        color = QColorDialog.getColor()
        listofcolorstyle[rowitem]=color.name()
        self.UpdateSpectroLegMod()
        self.populate()
        
    def UpdateSpectroLegMod(self):
        global listofanswer
        global listoflinestyle
        global listofcolorstyle,listoflinewidthstyle
        # print('')
        # print(listofanswer)
        DATAx=self.DATA
        
        leglist=[]
        for e in listofanswer:
            if type(e)!=str:
                leglist.append(e.text())
            else:
                leglist.append(e)
        # print(leglist)
        item=0
        for itemm in DATAx.keys():
            DATAx[itemm][6]=leglist[item]
            item+=1
        leglist=[]
        for e in listoflinestyle:
            if type(e)!=str:
                leglist.append(e.currentText())
            else:
                leglist.append(e)
        item=0
        for itemm in DATAx.keys():
            DATAx[itemm][7]=leglist[item]
            item+=1
        leglist=[]
        for e in listofcolorstyle:
            if type(e)!=str:
                leglist.append(e.get())
            else:
                leglist.append(e)
        item=0
        for itemm in DATAx.keys():
            DATAx[itemm][8]=leglist[item]
            item+=1
        leglist=[]
        for e in listoflinewidthstyle:
            if type(e)!=str:
                leglist.append(e.value())
            else:
                leglist.append(e)
        item=0
        for itemm in DATAx.keys():
            DATAx[itemm][9]=int(leglist[item])
            item+=1
                
        
        self.UpdateGraph(0)
    
    def UpdateGraph0(self,a):
        global titSpect
        global SpectlegendMod, takenforplot
        
        # takenforplot = [self.listboxsamples.get(idx) for idx in self.listboxsamples.curselection()]
        items = self.ui.listWidget.selectedItems()
        takenforplot = []
        for i in range(len(items)):
            takenforplot.append(str(self.ui.listWidget.selectedItems()[i].text()))
        # print(takenforplot)
        self.UpdateGraph(0)
        
    def UpdateGraph(self,a):
        global titSpect
        global SpectlegendMod, takenforplot
#        try:
        if self.DATA!={}:        
            DATAx=self.DATA
    #            sampletotake=[]
    #            namelist=[self.listboxsamples.get(idx) for idx in self.listboxsamples.curselection()]
    #            for name, var in namelist:
    #                sampletotake.append(var.get())
    #            sampletotake=[i for i,x in enumerate(sampletotake) if x == 1]
            if takenforplot!=[]:
                sampletotake=takenforplot
            else:
                sampletotake=[]
#            print('UpdateGraph')
            # print(sampletotake)
    #            else:
    #            sampletotake = [self.listboxsamples.get(idx) for idx in self.listboxsamples.curselection()]
    #            takenforplot=sampletotake
    #            if takenforplot!=[]:
    #                sampletotake=takenforplot
#            print(DATAx.keys())
            if self.ui.comboBox_plottype.currentText()=="Linear":
                self.Spectrograph.clear()
                for i in sampletotake:
                    x = DATAx[i][2]
                    y = DATAx[i][3]
                    if self.ui.checkBox_legend.isChecked():
                        if DATAx[i][1]=='A' and DATAx[i][15]!=0 and self.ui.checkBox_addEgtoLeg.isChecked():
                            self.Spectrograph.plot(x,y,label=DATAx[i][6]+' - '+'EgTauc: %.2f' % DATAx[i][15],linestyle=DATAx[i][7],color=DATAx[i][8],linewidth=DATAx[i][9])
                        else:
                            self.Spectrograph.plot(x,y,label=DATAx[i][6],linestyle=DATAx[i][7],color=DATAx[i][8],linewidth=DATAx[i][9])
                    else:
                        m=DATAx[i][7]
                        mm=DATAx[i][8]
                        mmm=DATAx[i][9]
                        self.Spectrograph.plot(x,y,linestyle=m,color=mm,linewidth=mmm)        
                
                self.Spectrograph.set_ylabel('Intensity (%)')
                self.Spectrograph.set_xlabel('Wavelength (nm)')
                    
            elif self.ui.comboBox_plottype.currentText()=="Tauc":
                self.Spectrograph.clear()
                for i in sampletotake:
                    if DATAx[i][1]=='A':
                        x = DATAx[i][10]
                        y = DATAx[i][13]
                        if self.ui.checkBox_legend.isChecked():
                            if DATAx[i][1]=='A' and DATAx[i][15]!=0 and self.ui.checkBox_addEgtoLeg.isChecked():
                                self.Spectrograph.plot(x,y,label=DATAx[i][6]+' - '+'EgTauc: %.2f' % DATAx[i][15],linestyle=DATAx[i][7],color=DATAx[i][8],linewidth=DATAx[i][9])
                            else:
                                self.Spectrograph.plot(x,y,label=DATAx[i][6],linestyle=DATAx[i][7],color=DATAx[i][8],linewidth=DATAx[i][9])
                        else:
                            m=DATAx[i][7]
                            mm=DATAx[i][8]
                            mmm=DATAx[i][9]
                            self.Spectrograph.plot(x,y,linestyle=m,color=mm,linewidth=mmm)
                        if self.ui.checkBox_showtangent.isChecked():
                            self.Spectrograph.plot(DATAx[i][16],DATAx[i][17],linestyle='--', color=DATAx[i][8])
                
                self.Spectrograph.set_ylabel('(eV*A/t)^n')
                self.Spectrograph.set_xlabel('Energy (eV)')
                
            if self.ui.checkBox_legend.isChecked():
                if self.ui.radioButton_topleft.isChecked():
                    self.leg=self.Spectrograph.legend(loc=2, fontsize = self.ui.spinBox_fontsize.value())
                elif self.ui.radioButton_topright.isChecked():
                    self.leg=self.Spectrograph.legend(loc=1, fontsize = self.ui.spinBox_fontsize.value())
                elif self.ui.radioButton_bottomleft.isChecked():
                    self.leg=self.Spectrograph.legend(loc=3, fontsize = self.ui.spinBox_fontsize.value())
                elif self.ui.radioButton_bottomright.isChecked():
                    self.leg=self.Spectrograph.legend(loc=4, fontsize = self.ui.spinBox_fontsize.value())
                elif self.ui.radioButton_outside.isChecked():
                    self.leg=self.Spectrograph.legend(bbox_to_anchor=(1, 1), loc='upper left', ncol=1, fontsize = self.ui.spinBox_fontsize.value())
                elif self.ui.radioButton_best.isChecked():
                    self.leg=self.Spectrograph.legend(loc=0, fontsize = self.ui.spinBox_fontsize.value())
                    
            for item in ([self.Spectrograph.title, self.Spectrograph.xaxis.label, self.Spectrograph.yaxis.label] +
                             self.Spectrograph.get_xticklabels() + self.Spectrograph.get_yticklabels()):
                item.set_fontsize(self.ui.spinBox_fontsize.value())

        self.fig.canvas.draw_idle()
        
    def GetSpectroDATA(self):
        global Patternsamplenameslist, colorstylelist, DATAspectro
        
        file_path = QFileDialog.getOpenFileNames(caption = 'Please select the spectro files')[0]
        
        directory = str(Path(file_path[0]).parent.parent)+'\\resultFilesSpectro'
        
        if not os.path.exists(directory):
            os.makedirs(directory)
            os.chdir(directory)
        else :
            os.chdir(directory)
        
        try:
            DATA=self.DATA
        except:
            DATA = {}
        
        for item in range(len(file_path)):
            if os.path.splitext(file_path[item])[1] ==".csv":
                with open(file_path[item], encoding='ISO-8859-1') as csvfile:
                    readCSV = list(csv.reader(csvfile, delimiter=','))
                    
                    samplenames=readCSV[0]
                    dataWaveInt=readCSV[2:]
                    print(len(dataWaveInt))
                    for item in range(len(samplenames)):
                        if samplenames[item]!='':
                            dataWave = []
                            dataInt = []
                            discard=1
#                            print(samplenames[item])
                            if '_TT' in samplenames[item]:
                                curvetype="TT"
                                samplenameshort = samplenames[item][:-3]
                            elif '_TR' in samplenames[item]:
                                curvetype="TR"
                                samplenameshort = samplenames[item][:-3]
                            elif "Baseline" in samplenames[item]:
                                discard=0
                            if discard:
#                                print(samplenames[item])
                                for item1 in range(len(dataWaveInt)):
#                                    print(dataWaveInt[item1])
#                                    if dataWaveInt[item1][0]=='':
                                    try:
                                        if dataWaveInt[item1]==[]:
                                            break
                                    except:
                                        pass
                                    try:
                                        if dataWaveInt[item1][0]=='':
                                            break
                                    except:
                                        pass
#                                    print(dataWaveInt[item1][item])
                                    if dataWaveInt[item1][item]=='':
                                        break
                                    dataWave.append(dataWaveInt[item1][item])
                                    dataInt.append(dataWaveInt[item1][item+1])
                                dataWave=list(map(float,dataWave))
                                dataWaveEV=list(map(lambda x: 1240/x, dataWave))
                                dataInt=list(map(float,dataInt))
                                
                                #[0 samplenameshort, 1 curvetype, 2 dataWave, 3 dataInt, 4 dataIntorig, 5 longnameorig, 6 longnamemod, 7 linestyle, 8 linecolor, 9 linewidth, 10 XineV, 11 thickness (100nm default), 12 TaucExp, 13 YTauc]
                                DATA[samplenames[item]] = [samplenameshort, curvetype, dataWave, dataInt,dataInt,samplenames[item],samplenames[item],'-',colorstylelist[len(DATA.keys())],int(2),dataWaveEV,100,2,dataInt]
                                Patternsamplenameslist.append(samplenames[item])
#                                print(samplenameshort)
            # elif os.path.splitext(file_path[item])[1] ==".txt": 
             
            #     file = open(file_path[item], encoding='ISO-8859-1')
            #     filedat = file.readlines()
            #     OceanOpticsYesNo=0
            #     for row in range(0, len(filedat)):
            #         if ">>>>>Begin Spectral Data<<<<<" in filedat[row]:
            #             OceanOpticsYesNo=row
                        
            #     if OceanOpticsYesNo:
            #         samplename=os.path.splitext(os.path.basename(file_path[item]))[0]
            #         wave=[]
            #         absorb=[]
            #         for item1 in range(OceanOpticsYesNo+1,len(filedat)):
            #             wave.append(float(filedat[item1].split('\t')[0]))
            #             absorb.append(1*(100-float(filedat[item1].split('\t')[1])))
                    
            #         DATA[samplename+'_A']=[samplename,'A',wave,absorb,absorb,samplename+'_A',samplename+'_A','-',colorstylelist[len(DATA.keys())],int(2)]
            #         Patternsamplenameslist.append(samplename+'_A')
            #     elif "Theta Device (for lockin measurement)" in filedat[0]: #
            #         samplename=os.path.splitext(os.path.basename(file_path[item]))[0]
            #         wave=[]
            #         absorb=[]
            #         for item1 in range(2,len(filedat)):
            #             wave.append(float(filedat[item1].split('\t')[0]))
            #             absorb.append(100*(1-float(filedat[item1].split('\t')[1])))
                    
            #         DATA[samplename+'_A']=[samplename,'A',wave,absorb,absorb,samplename+'_A',samplename+'_A','-',colorstylelist[len(DATA.keys())],int(2)]
            #         Patternsamplenameslist.append(samplename+'_A')
            #     else:
            #         samplename=filedat[0].split(' ')[0]
            #         wave=[]
            #         absorb=[]
            #         for item1 in range(2,len(filedat)):
            #             wave.append(float(filedat[item1].split('\t')[0]))
            #             absorb.append(float(filedat[item1].split('\t')[1]))
                    
            #         DATA[samplename+'_A']=[samplename,'A',wave,absorb,absorb,samplename+'_A',samplename+'_A','-',colorstylelist[len(DATA.keys())],int(2)]
            #         Patternsamplenameslist.append(samplename+'_A')
                     
                            
#                    dataWave=list(map(float,dataWave[1:]))
#                    dataInt=list(map(float,dataInt[1:]))
        
#        if os.path.splitext(file_path[0])[1] ==".asc": #for files .Sample.Raw.asc , file with spectro info at beginning, data starts after occurence of #DATA
#            DATA = []
#            for item in range(len(file_path)):                
#                if os.path.split(file_path[item])[1][-15:]==".Sample.Raw.asc":
#                    samplename=os.path.split(file_path[item])[1][:-15]
#                else:
#                    samplename=os.path.split(file_path[item])[1][:-4]
#            
#                if samplename[-3:]=="_TT" or samplename[-3:]=="-TT": 
#                    curvetype="TT"
#                    samplenameshort = samplename[:-3]
#                elif samplename[-2:]=="_T" or samplename[-2:]=="-T":
#                    curvetype="TT"
#                    samplenameshort = samplename[:-2]
#                elif samplename[-3:]=="_TR" or samplename[-3:]=="-TR":
#                    curvetype="TR" 
#                    samplenameshort = samplename[:-3]
#                elif  samplename[-2:]=="_R" or samplename[-2:]=="-R":
#                    curvetype="TR" 
#                    samplenameshort = samplename[:-2]
#                elif samplename[-3:]=="_DR" or samplename[-3:]=="-DR" :
#                    curvetype="DR" 
#                    samplenameshort = samplename[:-3]
#                elif samplename[-3:]=="_DT" or samplename[-3:]=="-DT" :
#                    curvetype="DT"
#                    samplenameshort = samplename[:-3]
#                
#                file1 = open(file_path[item])
#                content = file1.readlines()
#                file1.close()
#                
#                dataCurve = content[(content.index('#DATA\n') + 1):len(content)]
#                dataWave = []
#                dataInt = []
#                for i in range(len(dataCurve)):
#                    pos = dataCurve[i].find('\t')
#                    dataWave.append(dataCurve[i][:pos])
#                    dataInt.append(dataCurve[i][pos+1:-1])
#                dataWave=list(map(float,dataWave[1:]))
#                dataInt=list(map(float,dataInt[1:]))
#                datadict = [samplenameshort, curvetype, dataWave, dataInt]
#                DATA.append(datadict)
#                
#        elif os.path.splitext(file_path[0])[1] ==".csv":   #for excel files .Sample.Raw.csv (only two columns, data starts at second line)
#            DATA = []
#            for item in range(len(file_path)):
#                samplename=os.path.split(file_path[item])[1][:-15]
#                        
#                if samplename[-3:]=="_TT" or samplename[-3:]=="-TT": 
#                    curvetype="TT"
#                    samplenameshort = samplename[:-3]
#                elif samplename[-2:]=="_T" or samplename[-2:]=="-T":
#                    curvetype="TT"
#                    samplenameshort = samplename[:-2]
#                elif samplename[-3:]=="_TR" or samplename[-3:]=="-TR":
#                    curvetype="TR" 
#                    samplenameshort = samplename[:-3]
#                elif  samplename[-2:]=="_R" or samplename[-2:]=="-R":
#                    curvetype="TR" 
#                    samplenameshort = samplename[:-2]
#                elif samplename[-3:]=="_DR" or samplename[-3:]=="-DR" :
#                    curvetype="DR" 
#                    samplenameshort = samplename[:-3]
#                elif samplename[-3:]=="_DT" or samplename[-3:]=="-DT" :
#                    curvetype="DT"
#                    samplenameshort = samplename[:-3]
#                    
#                with open(file_path[item]) as csvfile:
#                    readCSV = csv.reader(csvfile, delimiter=',')
#                    
#                    dataWave = []
#                    dataInt = []
#                    for row in readCSV:
#                        dataWave.append(row[0])
#                        dataInt.append(row[1])
#                    dataWave=list(map(float,dataWave[1:]))
#                    dataInt=list(map(float,dataInt[1:]))
#                datadict = [samplenameshort, curvetype, dataWave, dataInt]
#                DATA.append(datadict)    

#DATA[samplenames[item]] = [samplenameshort, curvetype, dataWave, dataInt,dataInt,samplenames[item],samplenames[item],'-',colorstylelist[len(DATA.keys())],int(2)]
        
        try:
            DATADICTtot = self.DATADICTtot
        except:
#            print("exception")
            DATADICTtot = []
        Taucnames=[]
        if os.path.splitext(file_path[0])[1] !=".txt": 
            DATA2 = copy.deepcopy(DATA)
            while DATA != {}:
                listpositions = []
                names=list(DATA.keys())
                name = DATA[names[0]][0]
                for i in names:
                    if DATA[i][0] == name:
                        listpositions.append(i)
    
                datadict = {'Name': name, 'Wave': DATA[names[0]][2], 'TR': [],'TT':[],'A':[],'DR':[],'DT':[]}
                for i in listpositions:
                    if DATA[i][1]=='TR':
                        datadict['TR']=DATA[i][3]
                    elif DATA[i][1]=='TT':
                        datadict['TT']=DATA[i][3]
                    elif DATA[i][1]=='DR':
                        datadict['DR']=DATA[i][3]
                    elif DATA[i][1]=='DT':
                        datadict['DT']=DATA[i][3]
                if datadict['TR']!=[] and datadict['TT']!=[]:   
                    # print(name)
                    refl = [float(i) for i in datadict['TR']]
                    trans = [float(i) for i in datadict['TT']]
                    absorpt = [float(i) for i in [100 - (x + y) for x, y in zip(refl, trans)]]
#                    print(absorpt)
                    datadict['A']=absorpt
                    dataWaveEV=list(map(lambda x: 1240/x, DATA[names[0]][2]))
                    dataIntTauc=[(datadict['A'][i]*dataWaveEV[i]/100E-9)**2 for i in range(len(dataWaveEV))]
                    #[0 samplenameshort, 1 curvetype, 2 dataWave, 3 dataInt, 4 dataIntorig, 5 longnameorig, 6 longnamemod, 7 linestyle, 8 linecolor, 9 linewidth, 10 XineV, 11 thickness (100nm default), 12 TaucExp, 13 YTauc, 14 EGIP, 15 EgXcross, 16 xtg, 17 ytg]
                    DATA2[name+'_A']=[name,'A',DATA[names[0]][2],absorpt,absorpt,name+'_A',name+'_A','-',colorstylelist[len(DATA2.keys())],int(2),dataWaveEV,100,2,dataIntTauc,0,0,[],[]]
                    Patternsamplenameslist.append(name+'_A')
                    Taucnames.append(name+'_A')
                DATADICTtot.append(datadict)
                for index in sorted(listpositions, reverse=True):
                    del DATA[index]
            self.DATADICTtot=DATADICTtot
            self.DATA=DATA2
        else:
            self.DATA=DATA
#        print(self.DATA.keys())
        
        #update the listbox
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(Patternsamplenameslist)
        
        #update Tauc scroll area
        
        self.clearLayout(self.ui.gridLayout_4)
        self.ui.scrollArea_Tauc = QtWidgets.QScrollArea(self.ui.frame_2)
        self.ui.scrollArea_Tauc.setWidgetResizable(True)
        self.ui.scrollArea_Tauc.setObjectName("scrollArea_Tauc")
        self.ui.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.ui.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.ui.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.ui.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.ui.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.ui.verticalLayout_2.setObjectName("verticalLayout_2")
        
        item1=0
        for itemm in Taucnames:
            # print(item1)
            self.frame = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents)
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
            self.horizontalLayout.setObjectName("horizontalLayout")
            
            label = QtWidgets.QLabel(self.frame)
            label.setText(itemm)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
            label.setSizePolicy(sizePolicy)
            self.horizontalLayout.addWidget(label)
            
            self.spinBox_thickness = QtWidgets.QSpinBox(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.spinBox_thickness.sizePolicy().hasHeightForWidth())
            self.spinBox_thickness.setSizePolicy(sizePolicy)
            self.spinBox_thickness.setMaximum(9999999)
            self.spinBox_thickness.setObjectName("spinBox_thickness"+str(item1))
            self.spinBox_thickness.setValue(self.DATA[itemm][11])
            self.horizontalLayout.addWidget(self.spinBox_thickness)
            self.spinBox_thickness.valueChanged.connect(partial(self.TaucThicknessChanged,itemm))
            
            self.comboBox_TaucExp = QtWidgets.QComboBox(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.comboBox_TaucExp.sizePolicy().hasHeightForWidth())
            self.comboBox_TaucExp.setObjectName("comboBox_TaucExp"+str(item1))
            self.comboBox_TaucExp.addItems(['2','2/3','1/2','1/3'])
            self.comboBox_TaucExp.setCurrentText('2')
            self.horizontalLayout.addWidget(self.comboBox_TaucExp)
            self.comboBox_TaucExp.currentTextChanged.connect(partial(self.TaucExpchanged,itemm))
            
            item1+=1
            self.ui.verticalLayout_2.addWidget(self.frame)
        self.ui.scrollArea_Tauc.setWidget(self.ui.scrollAreaWidgetContents)
        self.ui.gridLayout_4.addWidget(self.ui.scrollArea_Tauc, 0, 0, 1, 1)
         
    def TaucThicknessChanged(self,name,new):
        self.DATA[name][11]=new
        self.updateTaucdat(name)
        self.UpdateGraph0(0)
        
    def TaucExpchanged(self,name,new):
        self.DATA[name][12]=float(eval(new))
        self.updateTaucdat(name)
        self.UpdateGraph0(0)
        
    def updateTaucdat(self,name):
        dataIntTauc=[((10**(9))*self.DATA[name][3][i]*self.DATA[name][10][i]/self.DATA[name][11])**self.DATA[name][12] for i in range(len(self.DATA[name][10]))]
        self.DATA[name][13]=dataIntTauc
        
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())
                    
    def sortandexportspectro(self):
        
        keyslist=list(self.DATA.keys())
        namesshort=list(dict.fromkeys([self.DATA[item][0] for item in keyslist]))
        
        for name in namesshort:
            l=[]
            for i in keyslist:
                if self.DATA[i][0]==name:
                    l.append(['Wavelength']+['nm']+self.DATA[i][2])
                    l.append([self.DATA[i][1]]+['%']+self.DATA[i][3])
                    if self.DATA[i][1]=='A' and list(self.DATA[i][16])!=[]:
                        l.append(['Energy']+['eV']+self.DATA[i][10])
                        l.append(['Tauc']+['(eV*A/'+str(self.DATA[i][11])+'E-9)^'+str(self.DATA[i][12])+'n']+self.DATA[i][13])
                
            content=np.array(l).T.tolist()
            content1=[]
            for j in range(len(content)):
                strr=''
                for k in range(len(content[j])):
                    strr = strr + str(content[j][k])+'\t'
                strr = strr[:-1]+'\n'
                content1.append(strr)
                        
            file = open(name + '.txt','w', encoding='ISO-8859-1')
            file.writelines("%s" % item for item in content1)
            file.close()
            
    def ExportGraph(self):

        path = QFileDialog.getSaveFileName(self, 'Save graph', ".png", "graph file (*.png);; All Files (*)")[0]

        if self.ui.checkBox_legend.isChecked():
            self.fig.savefig(path, dpi=300, bbox_extra_artists=(self.leg,))#, transparent=True)
        else:
            self.fig.savefig(path, dpi=300)#, transparent=True)
            
#     def AbsCoeffAndTauc(self):
#         self.AbsCoeffAndTaucWin = tk.Toplevel()
#         self.AbsCoeffAndTaucWin.wm_title("AbsCoeff, Tauc plot")
#         self.AbsCoeffAndTaucWin.geometry("280x250")
# #        center(self.AbsCoeffAndTaucWin)
        
#         #names=self.SampleNames(self.DATA)
        
# #        names=[item[0]+'-'+item[1] for item in self.DATA]
# #        
# #        namesshort=[]
# #        for item in names:
# #            if item.split("-")[0] not in namesshort:
# #                namesshort.append(item.split("-")[0])
        
#         names=list(self.DATA.keys())
#         namesshort=list(dict.fromkeys([self.DATA[item][0] for item in names]))
        
#         label = tk.Label(self.AbsCoeffAndTaucWin, text="Select:", font=12, bg="white",fg="black")
#         label.pack(fill=tk.X, expand=1)
        
#         self.RTchoice=StringVar()
#         self.dropMenuTauc = OptionMenu(self.AbsCoeffAndTaucWin, self.RTchoice, *namesshort, command=())
#         self.dropMenuTauc.pack(expand=1)
#         self.RTchoice.set("")
        
#         label = tk.Label(self.AbsCoeffAndTaucWin, text="Thickness:", font=12, bg="white",fg="black")
#         label.pack(fill=tk.X, expand=1)
        
#         self.thickness = tk.DoubleVar()
#         Entry(self.AbsCoeffAndTaucWin, textvariable=self.thickness,width=5).pack()
#         self.thickness.set(100)
        
#         label = tk.Label(self.AbsCoeffAndTaucWin, text="Transition type:", font=12, bg="white",fg="black")
#         label.pack(fill=tk.X, expand=1)

#         transitions=["1/2 for direct allowed", "3/2 for direct forbidden", "2 for indirect allowed", "3 for indirect forbidden"]
#         self.TransitionChoice=StringVar()
#         self.dropMenuTaucTrans = OptionMenu(self.AbsCoeffAndTaucWin, self.TransitionChoice, *transitions, command=())
#         self.dropMenuTaucTrans.pack(expand=1)
#         self.TransitionChoice.set(transitions[0])
        
#         ExportTauc = Button(self.AbsCoeffAndTaucWin, text="Export",width=15, command = self.AbsCoeffAndTaucSave)
#         ExportTauc.pack(fill=tk.X, expand=1)
        
#         label = tk.Label(self.AbsCoeffAndTaucWin, text="AbsCoeff=-Log(TT/(1-TR))/thickness;", font=("Verdana", 8), bg="white",fg="black")
#         label.pack(fill=tk.BOTH, expand=1)
#         label = tk.Label(self.AbsCoeffAndTaucWin, text="Tauc=(AbsCoeff * energy)^TransitionCoeff;", font=("Verdana", 8), bg="white",fg="black")
#         label.pack(fill=tk.BOTH, expand=1)
        
        

#     def AbsCoeffAndTaucSave(self):
        
#         if self.RTchoice.get()!="":
#             if self.thickness.get()!=0:
            
#                 reflectance=[]
#                 transmittance=[]
#                 absorptance=[]
#                 wavelength=[]
#                 sampletotake=[]
                
#                 keysData=list(self.DATA.keys())
# #                names=[self.DATA[item][0]+'-'+self.DATA[item][1] for item in keysData]
#                 sampletotake=[i for i in keysData if self.RTchoice.get()==self.DATA[i][0]]
                
#                 if len(sampletotake)>0:
#                     wavelength=self.DATA[sampletotake[0]][2]
#                     for item in sampletotake:
#                         if "_TR" in item:
#                             reflectance=self.DATA[item][3]
#                         elif "_TT" in item:
#                             transmittance=self.DATA[item][3]
#                         elif "_A" in item:
#                             absorptance=self.DATA[item][3]  
                
#                 if reflectance!=[] and transmittance != [] and absorptance!=[] and wavelength!=[]:
#                     f = filedialog.asksaveasfilename(defaultextension=".txt",initialfile= self.DATA[sampletotake[0]][0]+"_AbscoefTauc.txt", filetypes = (("text file", "*.txt"),("All Files", "*.*")))
            
#                     c = lightspeed
#                     h = 4.1e-15
#                     dataFactor=0.01
                    
#                     transition=0.5
#                     if self.TransitionChoice.get()=="1/2 for direct allowed":
#                         transition=0.5
#                     elif self.TransitionChoice.get()=="3/2 for direct forbidden":
#                         transition=1.5
#                     elif self.TransitionChoice.get()=="2 for indirect allowed":
#                         transition=2
#                     elif self.TransitionChoice.get()=="3 for indirect forbidden":
#                         transition=3
                    
#                     energy=[(c*h)/(float(x)/1e9) for x in wavelength]
#                     m=[dataFactor*float(x) for x in transmittance]
#                     n=[1-dataFactor*float(x) for x in reflectance]
#                     o=list(map(div, m,n))
#                     o=[abs(x) for x in o]
#                     o=list(map(log,o))
#                     abscoeff=[-float(x)/(self.thickness.get()*1e-7) for x in o]
#                     ahc=[pow(abs(abscoeff[i]*energy[i]),float(transition)) for i in range(len(energy))]
#                     logalpha=[log(abs(i)) for i in abscoeff]
                    
#                     taucdata=[]
#                     taucdata.append(wavelength)
#                     taucdata.append(energy)
#                     taucdata.append(reflectance)
#                     taucdata.append(transmittance)
#                     taucdata.append(absorptance)
#                     taucdata.append(logalpha)
#                     taucdata.append(abscoeff)
#                     taucdata.append(ahc)
                    
#                     taucdata=list(map(list,zip(*taucdata)))
                    
#                     taucdata=[["Wavelength","Energy","Reflectance","Transmittance","Absorptance","LogAlpha","AbsCoeff","Tauc"]]+taucdata
            
#                     file = open(f,'w', encoding='ISO-8859-1')
#                     file.writelines("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % tuple(item) for item in taucdata)
#                     file.close()
#                 else:
#                     print("cannot find the corresponding TR and TT files")
#             else:
#                 print("the thickness should be non-zero")
#         else:
#             print("choose a sample")
        
    def SavitzkyGolayFiltering(self):
        
        if self.ui.spinBox_SG1.value()>self.ui.spinBox_SG2.value() and self.ui.spinBox_SG1.value()%2==1:
            if self.ui.listWidget.selectedItems()!=():
                samplestakenforplot = [str(self.ui.listWidget.selectedItems()[i].text()) for i in range(len(self.ui.listWidget.selectedItems()))]
                if samplestakenforplot!=[]:
                    for item in samplestakenforplot:
                        y = self.DATA[item][3]
                        y=np.array(y)
                        self.DATA[item][3] = savitzky_golay(y, window_size=self.ui.spinBox_SG1.value(), order=self.ui.spinBox_SG2.value())
                
                self.UpdateGraph(0)
        else:
            QMessageBox.information('Information', "the SG window-size must be larger than the SG order, positive and odd.")

    def backtoOriginal(self):
        
        samplestakenforplot = [str(self.ui.listWidget.selectedItems()[i].text()) for i in range(len(self.ui.listWidget.selectedItems()))]
        if samplestakenforplot!=[]:
            for item in samplestakenforplot:
                self.DATA[item][3]=self.DATA[item][4]
        
        self.UpdateGraph(0)        
            
#%%#############
class Help(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        global matnamelist
        
        self.resize(1000, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(900, 200))
        self.setWindowTitle("Information")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.label = QtWidgets.QLabel()
        self.label.setText("""
                           \nHow do I name my files?\nTotal reflectance: _TR\tTotal transmittance: _TT\tDiffuse reflectance: _DR\tDiffuse transmittance: _DT\n
                           \nBy ending your measurement names with _TR, _TT, _DR or _DT, the program will be able to \nrecognise them, group them, and calculate the total absorptance.\n\n
                           For Tauc, it is a plot of (alpha * h * v)**r, where r is 2 for direct, 2/3 for direct forbidden, 1/2 for indirect, 1/3 for indirect forbidden transitions.\n
                           the layer thickness also needs to be defined for every sample.
                           """)

        self.gridLayout.addWidget(self.label)
#%%#############
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Spectroapp()
    window.show()
    sys.exit(app.exec())

