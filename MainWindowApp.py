import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox,QAction
import socket
# try:
#     from pip import main as pipmain
# except ImportError:
#     from pip._internal import main as pipmain
    
# try:
#     import tkcolorpicker
# except ImportError:
#     pipmain(['install', 'tkcolorpicker'])
# try:
#     import peakutils
# except ImportError:
#     pipmain(['install', 'peakutils'])
# try:
#     import tmm
# except ImportError:
#     pipmain(['install', 'tmm'])
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

from TMsimulNew_Pyth36PyQT5_forExe import TMSimulation
from IVpyqt5_forExe import IVapp
from EQEpyqt5_ForExe import EQEapp
from Spectropyqt5_ForExe import Spectroapp
from XRDpyqt5_forExe import XRDapp
from nkTaucPlotAnalysis_ForExe import NKapp
from AutoDetectBotCellsPL_v2 import AutoPL

from PyQt5.uic import loadUiType
from MainGUI import Ui_MainWindow
import datetime
import win32com.client

systemcheck=''#'USB' #'USB', 'MAC'

expiracydate = datetime.datetime.strptime('31/12/2021 6:00', "%d/%m/%Y %H:%M")

class MainWindowAllApps(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.checkUSBFlashDrive()
        finish = QAction("Quit", self)
        finish.triggered.connect(lambda: self.closeEvent(1))
        
        self.ui.pushButton_SolarSim.clicked.connect(lambda: self.Launch(IVapp))
        self.ui.pushButton_uvspectro.clicked.connect(lambda: self.Launch(Spectroapp))
        self.ui.pushButton_NKtauc.clicked.connect(lambda: self.Launch(NKapp))
        self.ui.pushButton_TMM.clicked.connect(lambda: self.Launch(TMSimulation))
        self.ui.pushButton_EQE.clicked.connect(lambda: self.Launch(EQEapp))
        self.ui.pushButton_XRD.clicked.connect(lambda: self.Launch(XRDapp))
        self.ui.pushButton_PLsorting.clicked.connect(lambda: self.Launch(AutoPL))
        
    def Launch(self, Appfunction):
        self.w = Appfunction()
        self.w.show()
        # self.hide()
        
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
    def checkUSBFlashDrive(self):
        global usbflashdriveaddress, IPHostaddress, MACaddress, expiracydate
        # print('checking rights...')
        if systemcheck == 'USB':
            # print('usb address is ',usbflashdriveaddress)
            wmi = win32com.client.GetObject ("winmgmts:")
            for usb in wmi.InstancesOf ("Win32_USBHub"):
                if usbflashdriveaddress in usb.DeviceID: #for my usb : SanDisk
                    # print(usb.DeviceID)
                    # print('authorized use')
                    return 1
            # print('unauthorized use')
            # self.ui.textEdit_Keithley.append(QtCore.QDateTime.currentDateTime().toString()+': '+'We cannot find the proper usb flash drive connected. DEMO-mode-freepass')
            QMessageBox.information(self,'Unauthorized use', 'We cannot find the proper usb flash drive connected. Please connect it and try to restart the software.')
            app.quit()
            # window.close()
            sys.exit()

        # if socket.gethostname() == '19IKI50':
        #     # print('hostname is correct')
        #     pass
        # else:
        #     QMessageBox.information(self,'Unauthorized use - Fraud alert', 'It seems that you are trying to use this version on a non-recognized computer. Please contact your service provider.')
        #     app.quit()
        #     # window.close()
        #     sys.exit()
            
        if datetime.datetime.now() < expiracydate:
            # self.ui.textEdit_Keithley.append(QtCore.QDateTime.currentDateTime().toString()+': '+'Remaining validity time: '+str(expiracydate-datetime.datetime.now()))
            pass
        else:
            QMessageBox.information(self,'Unauthorized use - Fraud alert', 'It seems that you are trying to use an expired version. Please contact your service provider.')
            app.quit()
            # window.close()
            sys.exit()
#%%#############
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowAllApps()
    window.show()
    sys.exit(app.exec())
    
    # # code to check the usb flash drive name
    # wmi = win32com.client.GetObject ("winmgmts:")
    # for usb in wmi.InstancesOf ("Win32_USBHub"):
    #     print(usb.DeviceID)
    