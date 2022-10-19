import sys
import cv2
import os
import numpy as np
import imutils
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Qt5Agg")
import pandas as pd
from PIL import Image
from AutoDetectBotCellsPL_GUI import Ui_mainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog


class AutoPL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        global DATA
        QtWidgets.QMainWindow.__init__(self, parent)
        
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        
        self.ui.chooseFile.clicked.connect(self.choosefile)
        self.ui.Start.clicked.connect(self.Start)
        
        
    def choosefile(self):
        file_path = QFileDialog.getOpenFileName(caption = 'Please select the file')[0]
        self.ui.chosenFile.setText(file_path)
        directory=os.path.dirname(os.path.abspath(file_path))
        os.chdir(directory)
        
    def Start(self):
        imagename=self.ui.chosenFile.text()
        ratioofROI=self.ui.ratioofroi.value()#0.1
        if self.ui.writeROI.isChecked():
            writeROI=True#False
        else:
            writeROI=False
        grayfactor=self.ui.GrayFactor.value()#25
        samplenumberstart=self.ui.samplenumberstart.value()#1
        
        img_src = cv2.imread(imagename)
        img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
        ret, img_bin = cv2.threshold(img_gray, grayfactor, 255,0)#, cv2.THRESH_BINARY)
        
        cnts = cv2.findContours(img_bin.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        img_result = img_src.copy()
        rect_points_list=[]
        rect_points_list2=[]
        allareas=[]
        for (i, c) in enumerate(cnts):
            min_rect = cv2.minAreaRect(c)
            rect_points = cv2.boxPoints(min_rect)
            rect_area = cv2.contourArea(c)
            if rect_area > 1000:
                allareas.append(rect_area)
                rect_points = np.int0(rect_points)
                rectptslist=rect_points.tolist()
                xmin=min([x[0] for x in rectptslist])
                xmax=max([x[0] for x in rectptslist])
                ymin=min([x[1] for x in rectptslist])
                ymax=max([x[1] for x in rectptslist])
                roiimage=img_src[ymin:ymax,xmin:xmax]
                
                height, width, channels = roiimage.shape
                roiimage2=roiimage[int(ratioofROI*height):int((1-ratioofROI)*height),int(ratioofROI*width):int((1-ratioofROI)*width)]
                
                cv2.line(img_result,(xmin+int(ratioofROI*width),ymin+int(ratioofROI*height)),(xmin+int(ratioofROI*width),ymax-int(ratioofROI*height)),(0, 255, 0), 2)
                cv2.line(img_result,(xmin+int(ratioofROI*width),ymax-int(ratioofROI*height)),(xmax-int(ratioofROI*width),ymax-int(ratioofROI*height)),(0, 255, 0), 2)
                cv2.line(img_result,(xmax-int(ratioofROI*width),ymax-int(ratioofROI*height)),(xmax-int(ratioofROI*width),ymin+int(ratioofROI*height)),(0, 255, 0), 2)
                cv2.line(img_result,(xmax-int(ratioofROI*width),ymin+int(ratioofROI*height)),(xmin+int(ratioofROI*width),ymin+int(ratioofROI*height)),(0, 255, 0), 2)
    
                cv2.line(img_result,(xmin,ymin),(xmin,ymax),(0, 255, 255), 2)
                cv2.line(img_result,(xmin,ymax),(xmax,ymax),(0, 255, 255), 2)
                cv2.line(img_result,(xmax,ymax),(xmax,ymin),(0, 255, 255), 2)
                cv2.line(img_result,(xmax,ymin),(xmin,ymin),(0, 255, 255), 2)
                
                try:
                    meanpixelvalue=int(roiimage2.mean())/255
                except ValueError:
                    meanpixelvalue=-1
                if writeROI:
                    cv2.imwrite('ROI'+str(len(rect_points_list)+samplenumberstart)+'.png',roiimage)
                    cv2.imwrite('ROI'+str(len(rect_points_list)+samplenumberstart)+'_'+'%.2f' % float(meanpixelvalue)+'.png',roiimage2)        
                rect_points_list.append([int((xmax+xmin)/2),int((ymax+ymin)/2),len(rect_points_list),rect_points,roiimage,roiimage2,meanpixelvalue,ymax-ymin])
                rect_points_list2.append(rect_points)
        
        #sorting
        rect_points_list_new = []
        keypoints_to_search = rect_points_list
        while len(keypoints_to_search) > 0:
            # print([keypoints_to_search[0][0],keypoints_to_search[0][1]])
            a = sorted(keypoints_to_search, key=lambda p: p[0]+p[1])[0]  # find upper left point
            b = sorted(keypoints_to_search, key=lambda p: p[0]-p[1])[-1]  # find upper right point
            # print('\n')
            # print([a[2],a[0],a[1]])
            # print([b[2],b[0],b[1]])
            # cv2.line(img_with_keypoints, (int(a.pt[0]), int(a.pt[1])), (int(b.pt[0]), int(b.pt[1])), (255, 0, 0), 1)
        
            # convert opencv keypoint to numpy 3d point
            a = np.array([a[0], a[1], 0])
            b = np.array([b[0], b[1], 0])
            
            row_points = []
            remaining_points = []
            for k in keypoints_to_search:
                p = np.array([k[0], k[1], 0])
                d = k[7]  # diameter of the keypoint (might be a theshold)
                dist = np.linalg.norm(np.cross(np.subtract(p, a), np.subtract(b, a))) / np.linalg.norm(b)   # distance between keypoint and line a->b
                if d/3 > dist:
                    row_points.append(k)
                else:
                    remaining_points.append(k)
            row_points=sorted(row_points, key=lambda h: h[0])
            # print('\n')
            # print([row_points[i][2] for i in range(len(row_points))])
            rect_points_list_new.extend(row_points)
            keypoints_to_search = remaining_points
        # print('\n\n')
        # print([[i+1,rect_points_list_new[i][0],rect_points_list_new[i][1]] for i in range(len(rect_points_list_new))])
        
        rect_points_list=rect_points_list_new
        
        
        #add labels
        for i in range(len(rect_points_list)):
            cv2.putText(img_result, 'Pad#: '+str(i+samplenumberstart), (rect_points_list[i][0]-60, rect_points_list[i][1]-40),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            # cv2.putText(img_result, str(rect_points_list[i][2]), (rect_points_list[i][0]-60, rect_points_list[i][1]),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            # cv2.drawContours(img_result, [rect_points_list2[rect_points_list[i][2]]], -1, (0, 255, 0), 1)
        
        df = pd.DataFrame()
        df['Pad#'] = [x+samplenumberstart for x in range(len(rect_points_list))]
        df['pixelValAvg/255']=['%.2f' % x[6] for x in rect_points_list]
        df.sort_values(by=["pixelValAvg/255"], inplace = True, ascending=False)
        
        padlist=list(df['Pad#'])
        # print(padlist)
        for j in range(len(padlist)):
            for i in range(len(rect_points_list)): 
                if padlist[j]==i+samplenumberstart:
                    cv2.putText(img_result, 'Rank: '+str(j+1), (rect_points_list[i][0]-60, rect_points_list[i][1]+60),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        cv2.imwrite('img_result.png',img_result)
        
        fig,ax = self.render_mpl_table(df,headerrows=range(1,len(rect_points_list)+1))#, header_columns=0, col_width=2.0)
        fig.savefig("table.png")
        plt.close(fig)
        
        img = cv2.imread("table.png")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        retval, thresh_gray = cv2.threshold(gray, thresh=100, maxval=255, type=cv2.THRESH_BINARY)
        points = np.argwhere(thresh_gray==0) 
        points = np.fliplr(points)
        x, y, w, h = cv2.boundingRect(points)
        x, y, w, h = x-10, y-10, w+20, h+20
        crop = gray[y:y+h, x:x+w]
        retval, thresh_crop = cv2.threshold(crop, thresh=200, maxval=255, type=cv2.THRESH_BINARY)
        cv2.imwrite('tablecropped.png',thresh_crop)
    
        cv2.waitKey()
        cv2.destroyAllWindows()
        
        images = list(map(Image.open, ["tablecropped.png",'img_result.png']))
        combo_2 = self.append_images(images, direction='horizontal', aligment='top',
                                bg_color=(255, 255, 255))
        combo_2.save(os.path.basename(imagename)[:-3]+'_withtable.png')
        
        os.remove("tablecropped.png")
        os.remove("img_result.png")
        os.remove("table.png")

    def append_images(self, images, direction='horizontal',bg_color=(255,255,255), aligment='center'):
        widths, heights = zip(*(i.size for i in images))
    
        if direction=='horizontal':
            new_width = sum(widths)
            new_height = max(heights)
        else:
            new_width = max(widths)
            new_height = sum(heights)
        
        new_im = Image.new('RGB', (new_width, new_height), color=bg_color)
    
        offset = 0
        for im in images:
            if direction=='horizontal':
                y = 0
                if aligment == 'center':
                    y = int((new_height - im.size[1])/2)
                elif aligment == 'bottom':
                    y = new_height - im.size[1]
                new_im.paste(im, (offset, y))
                offset += im.size[0]
            else:
                x = 0
                if aligment == 'center':
                    x = int((new_width - im.size[0])/2)
                elif aligment == 'right':
                    x = new_width - im.size[0]
                new_im.paste(im, (x, offset))
                offset += im.size[1]
        return new_im
    
    def render_mpl_table(self, data, col_width=4.0, row_height=0.625, font_size=14,
                         header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                         bbox=None, header_columns=0,headerrows=None,
                         ax=None, **kwargs):
        if ax is None:
            size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
            fig, ax = plt.subplots(figsize=size)
            ax.axis('off')
        mpl_table=ax.table(cellText=data.values, 
                            cellColours=None, 
                            cellLoc='left', 
                            colWidths=[0.15,0.3], 
                            rowLabels=headerrows, 
                            rowColours=None, 
                            rowLoc='left', 
                            colLabels=data.columns, 
                            colColours=None, 
                            colLoc='center', 
                            loc="center", 
                            bbox=None, 
                            edges='closed')
        mpl_table.auto_set_font_size(False)
        mpl_table.set_fontsize(font_size)
        mpl_table.scale(1, 1.5)
        return ax.get_figure(), ax


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = AutoPL()
    window.show()
    sys.exit(app.exec())