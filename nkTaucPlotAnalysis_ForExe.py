import sys
import os
from pathlib import Path
import numpy as np
# from statistics import mean
from math import factorial, log, pi
from scipy.interpolate import UnivariateSpline
import xlsxwriter
#%%######################################################################################################
import matplotlib
matplotlib.use("Qt5Agg")
#%%######################################################################################################
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QColorDialog,QAction
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
# import copy
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
# Ui_MainWindow, QMainWindow = loadUiType('nkgui.ui')
# Ui_MainWindow, QMainWindow = loadUiType(r'C:\Users\serjw\Documents\nBox\PythonScripts\SERIS-pythonscripts\executables\All\nkgui.ui')
from nkgui import Ui_MainWindow
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

class NKapp(QtWidgets.QMainWindow):
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
                if self.DATA[item][1]=='k':
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
        if self.ui.comboBox_plottype.currentText()=="Tauc (E*a*n)**m":
            self.DATA[self.ui.label_EgsearchSamplename.text()][14]=self.ui.doubleSpinBox_verticalIP.value()
            self.DATA[self.ui.label_EgsearchSamplename.text()][15]=self.ui.doubleSpinBox_Xcross.value()
            self.DATA[self.ui.label_EgsearchSamplename.text()][16]=self.xtg
            self.DATA[self.ui.label_EgsearchSamplename.text()][17]=self.ytg
        elif self.ui.comboBox_plottype.currentText()=="Tauc (E*a)**m":
            self.DATA[self.ui.label_EgsearchSamplename.text()][19]=self.ui.doubleSpinBox_verticalIP.value()
            self.DATA[self.ui.label_EgsearchSamplename.text()][20]=self.ui.doubleSpinBox_Xcross.value()
            self.DATA[self.ui.label_EgsearchSamplename.text()][21]=self.xtg
            self.DATA[self.ui.label_EgsearchSamplename.text()][22]=self.ytg
        elif self.ui.comboBox_plottype.currentText()=="Ln(a)":
            self.DATA[self.ui.label_EgsearchSamplename.text()][24]=self.ui.doubleSpinBox_verticalIP.value()
            self.DATA[self.ui.label_EgsearchSamplename.text()][25]=self.ui.doubleSpinBox_EU.value()
            self.DATA[self.ui.label_EgsearchSamplename.text()][26]=self.xtg
            self.DATA[self.ui.label_EgsearchSamplename.text()][27]=self.ytg
        
            
    def plotEgsearch(self, samplename):
        DATAx=self.DATA
        # print('plot')
        i=samplename
        if i!='samplename' and self.ui.doubleSpinBox_minX.value()<self.ui.doubleSpinBox_maxX.value():
            self.Spectrograph.clear()
            if self.ui.doubleSpinBox_verticalIP.value()<self.ui.doubleSpinBox_minX.value() or self.ui.doubleSpinBox_verticalIP.value()>self.ui.doubleSpinBox_maxX.value():
                self.ui.doubleSpinBox_verticalIP.setValue(self.ui.doubleSpinBox_minX.value()+(self.ui.doubleSpinBox_maxX.value()-self.ui.doubleSpinBox_minX.value())/2)
            x=[]
            y=[]
            for item in range(len(DATAx[i][10])):
                if DATAx[i][10][item] >self.ui.doubleSpinBox_minX.value() and DATAx[i][10][item]<=self.ui.doubleSpinBox_maxX.value():
                    x.append(DATAx[i][10][item])
                    if self.ui.comboBox_plottype.currentText()=="Tauc (E*a*n)**m":
                        y.append(DATAx[i][13][item])
                        self.Spectrograph.set_ylabel('(E*a*n)^m')
                    elif self.ui.comboBox_plottype.currentText()=="Tauc (E*a)**m":
                        y.append(DATAx[i][18][item])
                        self.Spectrograph.set_ylabel('(E*a)^m')
                    elif self.ui.comboBox_plottype.currentText()=="Ln(a)":
                        y.append(DATAx[i][23][item])
                        self.Spectrograph.set_ylabel('Ln(a)')
                    
            if y!=[]:
                xhighslope=self.ui.doubleSpinBox_verticalIP.value()
                spl=UnivariateSpline(x, y, s=0)
                splder = spl.derivative(n=1)
                slopeatIP=splder(xhighslope)
                self.ui.doubleSpinBox_EU.setValue(1/slopeatIP)
                
                self.xtg = np.linspace(min(x),max(x),3)
                self.ytg = slopeatIP*self.xtg+spl(xhighslope)-slopeatIP*xhighslope
                xcrossing=(-spl(xhighslope)+slopeatIP*xhighslope)/slopeatIP
                self.ui.doubleSpinBox_Xcross.setValue(xcrossing)
                
                
                if self.ui.checkBox_legend.isChecked():
                    self.Spectrograph.plot(x,y,label=DATAx[i][6],linestyle=DATAx[i][7],color=DATAx[i][8],linewidth=DATAx[i][9])
                    self.Spectrograph.plot(self.xtg,self.ytg,linestyle='--', color='r',linewidth=DATAx[i][9], label='tangente to IP')
                    self.Spectrograph.plot([xhighslope,xcrossing],[spl(xhighslope),0], 'ro')
                else:
                    self.Spectrograph.plot(x,y,linestyle=DATAx[i][7],color=DATAx[i][8],linewidth=DATAx[i][9])
                    self.Spectrograph.plot(self.xtg,self.ytg,linestyle='--', color='r',linewidth=DATAx[i][9])
                    self.Spectrograph.plot([xhighslope,xcrossing],[spl(xhighslope),0], 'ro')
                    
    
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
        # print(listoflinestyle)
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
            if takenforplot!=[]:
                sampletotake=takenforplot
            else:
                sampletotake=[]
                
            if self.ui.comboBox_plottype.currentText()=="Linear, nm":
                self.Spectrograph.clear()
                for i in sampletotake:
                    x = DATAx[i][2]
                    y = DATAx[i][3]
                    if self.ui.checkBox_legend.isChecked():
                        if DATAx[i][1]=='k' and DATAx[i][15]!=0 and self.ui.checkBox_addEgtoLeg.isChecked():
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
            
            elif self.ui.comboBox_plottype.currentText()=="Linear, eV":
                self.Spectrograph.clear()
                for i in sampletotake:
                    x = DATAx[i][10]
                    y = DATAx[i][3]
                    if self.ui.checkBox_legend.isChecked():
                        if DATAx[i][1]=='k' and DATAx[i][15]!=0 and self.ui.checkBox_addEgtoLeg.isChecked():
                            self.Spectrograph.plot(x,y,label=DATAx[i][6]+' - '+'EgTauc: %.2f' % DATAx[i][15],linestyle=DATAx[i][7],color=DATAx[i][8],linewidth=DATAx[i][9])
                        else:
                            self.Spectrograph.plot(x,y,label=DATAx[i][6],linestyle=DATAx[i][7],color=DATAx[i][8],linewidth=DATAx[i][9])
                    else:
                        m=DATAx[i][7]
                        mm=DATAx[i][8]
                        mmm=DATAx[i][9]
                        self.Spectrograph.plot(x,y,linestyle=m,color=mm,linewidth=mmm)        
                
                self.Spectrograph.set_ylabel('Intensity (%)')
                self.Spectrograph.set_xlabel('Energy (eV)')
                    
            elif self.ui.comboBox_plottype.currentText()=="Tauc (E*a*n)**m":
                self.Spectrograph.clear()
                for i in sampletotake:
                    if DATAx[i][1]=='k':
                        x = DATAx[i][10]
                        y = DATAx[i][13]
                        if self.ui.checkBox_legend.isChecked():
                            if DATAx[i][1]=='k' and DATAx[i][15]!=0 and self.ui.checkBox_addEgtoLeg.isChecked():
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
                
                self.Spectrograph.set_ylabel('(E*a*n)^m')
                self.Spectrograph.set_xlabel('Energy (eV)')
                
            elif self.ui.comboBox_plottype.currentText()=="Tauc (E*a)**m":
                self.Spectrograph.clear()
                for i in sampletotake:
                    if DATAx[i][1]=='k':
                        x = DATAx[i][10]
                        y = DATAx[i][18]
                        if self.ui.checkBox_legend.isChecked():
                            if DATAx[i][1]=='k' and DATAx[i][20]!=0 and self.ui.checkBox_addEgtoLeg.isChecked():
                                self.Spectrograph.plot(x,y,label=DATAx[i][6]+' - '+'EgTauc: %.2f' % DATAx[i][20],linestyle=DATAx[i][7],color=DATAx[i][8],linewidth=DATAx[i][9])
                            else:
                                self.Spectrograph.plot(x,y,label=DATAx[i][6],linestyle=DATAx[i][7],color=DATAx[i][8],linewidth=DATAx[i][9])
                        else:
                            m=DATAx[i][7]
                            mm=DATAx[i][8]
                            mmm=DATAx[i][9]
                            self.Spectrograph.plot(x,y,linestyle=m,color=mm,linewidth=mmm)
                        if self.ui.checkBox_showtangent.isChecked():
                            self.Spectrograph.plot(DATAx[i][21],DATAx[i][22],linestyle='--', color=DATAx[i][8])
                
                self.Spectrograph.set_ylabel('(E*a)^m')
                self.Spectrograph.set_xlabel('Energy (eV)')
                
            elif self.ui.comboBox_plottype.currentText()=="Ln(a)":
                self.Spectrograph.clear()
                for i in sampletotake:
                    if DATAx[i][1]=='k':
                        x = DATAx[i][10]
                        y = DATAx[i][23]
                        if self.ui.checkBox_legend.isChecked():
                            if DATAx[i][1]=='k' and DATAx[i][25]!=0 and self.ui.checkBox_addEgtoLeg.isChecked():
                                self.Spectrograph.plot(x,y,label=DATAx[i][6]+' - '+'1/slope: %.2f' % DATAx[i][25],linestyle=DATAx[i][7],color=DATAx[i][8],linewidth=DATAx[i][9])
                            else:
                                self.Spectrograph.plot(x,y,label=DATAx[i][6],linestyle=DATAx[i][7],color=DATAx[i][8],linewidth=DATAx[i][9])
                        else:
                            m=DATAx[i][7]
                            mm=DATAx[i][8]
                            mmm=DATAx[i][9]
                            self.Spectrograph.plot(x,y,linestyle=m,color=mm,linewidth=mmm)
                        if self.ui.checkBox_showtangent.isChecked():
                            self.Spectrograph.plot(DATAx[i][26],DATAx[i][27],linestyle='--', color=DATAx[i][8])
                
                self.Spectrograph.set_ylabel('Ln(a)')
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
        global Patternsamplenameslist, echarge, planck, lightspeed
        
        file_path = QFileDialog.getOpenFileNames(caption = 'Please select the nk text files')[0]

        directory = str(Path(file_path[0]).parent.parent)+'\\resultNK'
        
        if not os.path.exists(directory):
            os.makedirs(directory)
            os.chdir(directory)
        else :
            os.chdir(directory)
        
        try:
            DATA=self.DATA    
        except:
            DATA = {}
        Taucnames=[]  
        for item in range(len(file_path)):
            if os.path.splitext(file_path[item])[1] ==".txt":
                file = open(file_path[item], encoding='ISO-8859-1')
                filedat = file.readlines()
                
                filename=os.path.basename(os.path.normpath(file_path[item]))[:-4]
                if 'thick' in filename:
                    thickness=float(filename.split('_')[1][5:])
                    filename=filename.split('_')[0]
                else:
                    thickness=1
                
                
                lambdalist=[]
                nlist=[]
                klist=[]
                for item1 in filedat:
                    lambdalist.append(float(item1.split('\t')[0]))
                    nlist.append(float(item1.split('\t')[1]))
                    klist.append(float(item1.split('\t')[2]))
                lambdalisteV=[(planck*lightspeed)/(echarge*x*0.000000001) for x in lambdalist]
                DATA[filename+'_n'] = [filename, 'n',lambdalist,nlist,nlist,filename+'_n', filename+'_n','-',colorstylelist[len(DATA.keys())],int(2),lambdalisteV]
                Patternsamplenameslist.append(filename+'_n')
                print(filename+'_n')
                
                
                alpha= [(4*pi*klist[i]/lambdalist[i])*1E7 for i in range(len(klist))]
                
                TaucExp=2
                
                YTaucn=[(alpha[i]*lambdalisteV[i]*lambdalist[i])**TaucExp for i in range(len(alpha))]
                EGIPn=0
                EgXcrossn=0
                xtgn=[]
                ytgn=[]
                
                YTaucnn=[(alpha[i]*lambdalisteV[i])**TaucExp for i in range(len(alpha))]
                EGIPnn=0
                EgXcrossnn=0
                xtgnn=[]
                ytgnn=[]
                LnAlpha=[]
                for i in range(len(alpha)):
                    try:
                        LnAlpha.append(log(alpha[i]))
                    except ValueError:
                        LnAlpha.append(0)
                    
                EUip=0
                EUipSlopeinv=0
                xtgEU=[]
                ytgEU=[]
                
                
                DATA[filename+'_k'] = [filename, 'k',lambdalist,klist,klist,filename+'_k', filename+'_k','-',colorstylelist[len(DATA.keys())],int(2),lambdalisteV, thickness, TaucExp, YTaucn, EGIPn, EgXcrossn, xtgn, ytgn, YTaucnn, EGIPnn, EgXcrossnn, xtgnn, ytgnn, LnAlpha, EUip, EUipSlopeinv, xtgEU, ytgEU]
                Taucnames.append(filename+'_k')
                Patternsamplenameslist.append(filename+'_k')
                print(filename+'_k')
               
            else:
                QMessageBox.information('Information', 'not .txt files')

                # print('not .txt files')#to be replaced by popup messagebox
          
        self.DATA=DATA
        
        #update the listbox
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
            
            # self.spinBox_thickness = QtWidgets.QSpinBox(self.frame)
            # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
            # sizePolicy.setHorizontalStretch(0)
            # sizePolicy.setVerticalStretch(0)
            # sizePolicy.setHeightForWidth(self.spinBox_thickness.sizePolicy().hasHeightForWidth())
            # self.spinBox_thickness.setSizePolicy(sizePolicy)
            # self.spinBox_thickness.setMaximum(9999999)
            # self.spinBox_thickness.setObjectName("spinBox_thickness"+str(item1))
            # self.spinBox_thickness.setValue(int(self.DATA[itemm][11]))
            # self.horizontalLayout.addWidget(self.spinBox_thickness)
            # self.spinBox_thickness.valueChanged.connect(partial(self.TaucThicknessChanged,itemm))
            
            self.comboBox_TaucExp = QtWidgets.QComboBox(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.comboBox_TaucExp.sizePolicy().hasHeightForWidth())
            self.comboBox_TaucExp.setObjectName("comboBox_TaucExp"+str(item1))
            self.comboBox_TaucExp.addItems(['2','2/3','1/2','1/3'])
            self.comboBox_TaucExp.setCurrentText(str(self.DATA[itemm][12]))
            self.horizontalLayout.addWidget(self.comboBox_TaucExp)
            self.comboBox_TaucExp.currentTextChanged.connect(partial(self.TaucExpchanged,itemm))
            self.comboBox_TaucExp.setToolTip("2 \tdirect bandgap\n1/2 \tindirect bandgap")
            
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
        klist=self.DATA[name][3]
        lambdalist=self.DATA[name][2]
        lambdalisteV=self.DATA[name][10]
        TaucExp=self.DATA[name][12]
        alpha= [(4*pi*klist[i]/lambdalist[i])*1E7 for i in range(len(klist))]
        YTaucn=[(alpha[i]*lambdalisteV[i]*lambdalist[i])**TaucExp for i in range(len(alpha))]
        self.DATA[name][13]=YTaucn
        YTaucnn=[(alpha[i]*lambdalisteV[i])**TaucExp for i in range(len(alpha))]
        self.DATA[name][18]=YTaucnn
        LnAlpha=[]
        for i in range(len(alpha)):
            try:
                LnAlpha.append(log(alpha[i]))
            except ValueError:
                LnAlpha.append(0)
        self.DATA[name][23]=LnAlpha
        
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
            workbook = xlsxwriter.Workbook(name+'.xlsx')
            for i in keyslist:
                if self.DATA[i][0]==name:
                    worksheet = workbook.add_worksheet(self.DATA[i][1])
                    for item in range(len(self.DATA[i])):
                        if type(self.DATA[i][item])==list:
                            for row in range(len(self.DATA[i][item])):
                                worksheet.write(row+1,item,self.DATA[i][item][row])
                        elif type(self.DATA[i][item])==np.ndarray: 
                            for row in range(len(list(self.DATA[i][item]))):
                                worksheet.write(row+1,item,list(self.DATA[i][item])[row])
                        else:
                            worksheet.write(1,item,self.DATA[i][item])
                    if self.DATA[i][1]=='n':
                        listofheadingsN=["samplenameshort", "curvetype", "dataWave", "dataInt", "dataIntorig", "longnameorig", "longnamemod", "linestyle", "linecolor", "linewidth", "X eV"]
                        for item in range(len(listofheadingsN)):
                            worksheet.write(0,item,listofheadingsN[item])
                    elif self.DATA[i][1]=='k':
                        listofheadingsN=["samplenameshort", "curvetype", "dataWave", "dataInt", "dataIntorig", "longnameorig", "longnamemod", "linestyle", "linecolor", "linewidth", "X eV","thickness","TaucExp", "YTauc", "EGIP", "EgXcross", "xtg", "ytg", "YTauc NoN", "EGIP NoN", "EgXcross NoN", "xtg NoN", "ytg NoN", "Ln(Alpha)", "Eip", "Eip_Slopeinv", "xtgEU", "ytgEU"]
                        for item in range(len(listofheadingsN)):
                            worksheet.write(0,item,listofheadingsN[item])
            workbook.close()
            
    def ExportGraph(self):
        
        #add export data in txt file
        
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
        self.label.setText("""""")
                            # \nHow do I name my files?\nTotal reflectance: _TR\tTotal transmittance: _TT\tDiffuse reflectance: _DR\tDiffuse transmittance: _DT\n
                            # \nBy ending your measurement names with _TR, _TT, _DR or _DT, the program will be able to \nrecognise them, group them, and calculate the total absorptance.\n\n
                            # """)

        self.gridLayout.addWidget(self.label)
#%%#############
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = NKapp()
    window.show()
    sys.exit(app.exec())

