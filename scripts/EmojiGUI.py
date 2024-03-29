# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Karthik S\Desktop\EmojiGUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import os

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.setWindowModality(QtCore.Qt.ApplicationModal)
        StackedWidget.resize(1086, 515)
        StackedWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.first = QtWidgets.QWidget()
        self.first.setObjectName("first")
        self.label = QtWidgets.QLabel(self.first)
        self.label.setGeometry(QtCore.QRect(280, 20, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.first)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.filePath = QtWidgets.QLineEdit(self.first)
        self.filePath.setEnabled(False)
        self.filePath.setGeometry(QtCore.QRect(100, 90, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.filePath.setFont(font)
        self.filePath.setObjectName("filePath")
        self.fileBrowse = QtWidgets.QPushButton(self.first)
        self.fileBrowse.setGeometry(QtCore.QRect(440, 90, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fileBrowse.setFont(font)
        self.fileBrowse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fileBrowse.setObjectName("fileBrowse")
        self.label_3 = QtWidgets.QLabel(self.first)
        self.label_3.setGeometry(QtCore.QRect(550, 90, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.folderBrowse = QtWidgets.QPushButton(self.first)
        self.folderBrowse.setGeometry(QtCore.QRect(1000, 90, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.folderBrowse.setFont(font)
        self.folderBrowse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.folderBrowse.setObjectName("folderBrowse")
        self.folderPath = QtWidgets.QLineEdit(self.first)
        self.folderPath.setEnabled(False)
        self.folderPath.setGeometry(QtCore.QRect(660, 90, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.folderPath.setFont(font)
        self.folderPath.setObjectName("folderPath")
        self.label_4 = QtWidgets.QLabel(self.first)
        self.label_4.setGeometry(QtCore.QRect(100, 130, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.downsample = QtWidgets.QLineEdit(self.first)
        self.downsample.setEnabled(False)
        self.downsample.setGeometry(QtCore.QRect(230, 130, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.downsample.setFont(font)
        self.downsample.setObjectName("downsample")
        self.downscaleSlider = QtWidgets.QSlider(self.first)
        self.downscaleSlider.setGeometry(QtCore.QRect(100, 160, 160, 22))
        self.downscaleSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.downscaleSlider.setMinimum(1)
        self.downscaleSlider.setMaximum(10)
        self.downscaleSlider.setPageStep(1)
        self.downscaleSlider.setProperty("value", 2)
        self.downscaleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.downscaleSlider.setObjectName("downscaleSlider")
        self.label_5 = QtWidgets.QLabel(self.first)
        self.label_5.setGeometry(QtCore.QRect(310, 130, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.bilateralfilterSteps = QtWidgets.QLineEdit(self.first)
        self.bilateralfilterSteps.setEnabled(False)
        self.bilateralfilterSteps.setGeometry(QtCore.QRect(490, 130, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.bilateralfilterSteps.setFont(font)
        self.bilateralfilterSteps.setObjectName("bilateralfilterSteps")
        self.label_6 = QtWidgets.QLabel(self.first)
        self.label_6.setGeometry(QtCore.QRect(570, 130, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.sigmaBilateral = QtWidgets.QLineEdit(self.first)
        self.sigmaBilateral.setEnabled(False)
        self.sigmaBilateral.setGeometry(QtCore.QRect(760, 130, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.sigmaBilateral.setFont(font)
        self.sigmaBilateral.setObjectName("sigmaBilateral")
        self.label_7 = QtWidgets.QLabel(self.first)
        self.label_7.setGeometry(QtCore.QRect(840, 130, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.kernelSize = QtWidgets.QLineEdit(self.first)
        self.kernelSize.setEnabled(False)
        self.kernelSize.setGeometry(QtCore.QRect(930, 130, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.kernelSize.setFont(font)
        self.kernelSize.setObjectName("kernelSize")
        self.kernelSlider = QtWidgets.QSlider(self.first)
        self.kernelSlider.setGeometry(QtCore.QRect(820, 160, 160, 22))
        self.kernelSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kernelSlider.setMinimum(1)
        self.kernelSlider.setMaximum(30)
        self.kernelSlider.setSingleStep(3)
        self.kernelSlider.setPageStep(3)
        self.kernelSlider.setProperty("value", 3)
        self.kernelSlider.setOrientation(QtCore.Qt.Horizontal)
        self.kernelSlider.setObjectName("kernelSlider")
        self.sigmaSlider = QtWidgets.QSlider(self.first)
        self.sigmaSlider.setGeometry(QtCore.QRect(600, 160, 160, 22))
        self.sigmaSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sigmaSlider.setMinimum(1)
        self.sigmaSlider.setMaximum(30)
        self.sigmaSlider.setSingleStep(2)
        self.sigmaSlider.setPageStep(2)
        self.sigmaSlider.setProperty("value", 9)
        self.sigmaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sigmaSlider.setObjectName("sigmaSlider")
        self.bilateralslider = QtWidgets.QSlider(self.first)
        self.bilateralslider.setGeometry(QtCore.QRect(330, 160, 160, 22))
        self.bilateralslider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bilateralslider.setMinimum(10)
        self.bilateralslider.setMaximum(100)
        self.bilateralslider.setPageStep(1)
        self.bilateralslider.setProperty("value", 50)
        self.bilateralslider.setOrientation(QtCore.Qt.Horizontal)
        self.bilateralslider.setObjectName("bilateralslider")
        self.generate = QtWidgets.QPushButton(self.first)
        self.generate.setGeometry(QtCore.QRect(420, 190, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.generate.setFont(font)
        self.generate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generate.setObjectName("generate")
        self.saveImages = QtWidgets.QPushButton(self.first)
        self.saveImages.setGeometry(QtCore.QRect(420, 480, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.saveImages.setFont(font)
        self.saveImages.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveImages.setObjectName("saveImages")
        self.originalImage = QtWidgets.QGraphicsView(self.first)
        self.originalImage.setGeometry(QtCore.QRect(130, 270, 231, 191))
        self.originalImage.setObjectName("originalImage")
        self.edgesImage = QtWidgets.QGraphicsView(self.first)
        self.edgesImage.setGeometry(QtCore.QRect(420, 270, 231, 191))
        self.edgesImage.setObjectName("edgesImage")
        self.cartoonImage = QtWidgets.QGraphicsView(self.first)
        self.cartoonImage.setGeometry(QtCore.QRect(710, 270, 231, 191))
        self.cartoonImage.setObjectName("cartoonImage")
        self.label_8 = QtWidgets.QLabel(self.first)
        self.label_8.setGeometry(QtCore.QRect(130, 240, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.first)
        self.label_10.setGeometry(QtCore.QRect(420, 240, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.first)
        self.label_11.setGeometry(QtCore.QRect(710, 240, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.clearBtn = QtWidgets.QPushButton(self.first)
        self.clearBtn.setGeometry(QtCore.QRect(550, 480, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clearBtn.setFont(font)
        self.clearBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearBtn.setObjectName("clearBtn")
        self.resetBtn = QtWidgets.QPushButton(self.first)
        self.resetBtn.setGeometry(QtCore.QRect(550, 190, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.resetBtn.setFont(font)
        self.resetBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetBtn.setObjectName("resetBtn")
        self.warningLabel = QtWidgets.QLabel(self.first)
        self.warningLabel.setGeometry(QtCore.QRect(100, 220, 891, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.warningLabel.setFont(font)
        self.warningLabel.setText("")
        self.warningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.warningLabel.setObjectName("warningLabel")

        self.downsample.setText("2")
        self.bilateralfilterSteps.setText("50")
        self.sigmaBilateral.setText("9")
        self.kernelSize.setText("3")
        
        StackedWidget.addWidget(self.first)

        self.retranslateUi(StackedWidget)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)
        
        self.downscaleSlider.valueChanged.connect(self.valueChangedDownScale)
        self.bilateralslider.valueChanged.connect(self.valueChangedBilateralSlider)
        self.sigmaSlider.valueChanged.connect(self.valueChangedSigma)
        self.kernelSlider.valueChanged.connect(self.valueChangedKernelSize)
        
        self.fileBrowse.clicked.connect(self.browseFilePath)
        self.folderBrowse.clicked.connect(self.browseFolderPath)
        self.generate.clicked.connect(self.generateImages)
        self.resetBtn.clicked.connect(self.resetdata)
        self.saveImages.clicked.connect(self.callSaveImages)
        self.clearBtn.clicked.connect(self.callClear)
        
    def valueChangedDownScale(self):
        value = str(self.downscaleSlider.value())
        self.downsample.setText(value)
        
    def valueChangedBilateralSlider(self):
        value = str(self.bilateralslider.value())
        self.bilateralfilterSteps.setText(value)
    
    def valueChangedSigma(self):
        value = str(self.sigmaSlider.value())
        self.sigmaBilateral.setText(value)
        
    def valueChangedKernelSize(self):
        value = str(self.kernelSlider.value())
        self.kernelSize.setText(value)
    
    def browseFilePath(self):
        global imgPath
        imgPath = QtWidgets.QFileDialog.getOpenFileName(None, 'Single File', QtCore.QDir.rootPath() ,'*.jpg;*.png;*.jpeg;*.jfif')
        self.filePath.setText(str(imgPath[0]))
        return
        
    def browseFolderPath(self):
        global pathFolder
        pathFolder = QtWidgets.QFileDialog.getExistingDirectory()
        self.folderPath.setText(str(pathFolder))
    
    def generateImages(self):
        if(self.filePath.text()=="" or self.filePath.text()==None):
            self.warningLabel.clear()
            self.warningLabel.setStyleSheet("color: red")
            self.warningLabel.setText("Please Choose the Image file")
            self.filePath.clear()
        else:
            self.warningLabel.clear()
            img = cv2.imread(str(imgPath[0]))
            img = cv2.resize(img, (720,480))
            numDownSamples = int(self.downsample.text())
            numBilateralFilters = int(self.bilateralfilterSteps.text())
            img_color = img
            for _ in range(numDownSamples):
                img_color = cv2.pyrDown(img_color)
            
            sigmaColor = int(self.sigmaBilateral.text())
            for _ in range(numBilateralFilters):
                img_color = cv2.bilateralFilter(img_color, sigmaColor, sigmaColor, 7)
                
            for _ in range(numDownSamples):
                img_color = cv2.pyrUp(img_color)
                
            img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            
            kerSize = int(self.kernelSize.text())
            img_blur = cv2.medianBlur(img_gray, kerSize)
            
            img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                             cv2.ADAPTIVE_THRESH_MEAN_C,
                                             cv2.THRESH_BINARY, 9, 2)
            
            (x,y,z) = img_color.shape
            img_edge = cv2.resize(img_edge,(y,x)) 
            img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
            res = cv2.bitwise_and(img_color, img_edge)
            self.warningLabel.setStyleSheet("color: green")
            self.warningLabel.setText("Images Generated Successfully!")
            self.plotImages(img, img_edge, res)
        return
    
    def plotImages(self, originalImg, edgeImage, cartoonImage):
        
        cv2.imwrite("edgeDetected.png",edgeImage)
        cv2.imwrite("cartoonImage.jpg",cartoonImage)
        global edgeImages
        global cartoonImages
        
        edgeImages = edgeImage
        cartoonImages = cartoonImage
        ''' Original Image'''
        scene = QtWidgets.QGraphicsScene()
        scene.clear()
        self.originalImage.setScene(scene)
        pix = QtGui.QPixmap(imgPath[0]).scaled(225,185)
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)
        self.originalImage.setScene(scene)
        
        ''' Edge Detected Image '''
        edgeImagePath = str(os.getcwd())+"\edgeDetected.png"
        scene = QtWidgets.QGraphicsScene()
        scene.clear()
        self.edgesImage.setScene(scene)
        pix = QtGui.QPixmap(edgeImagePath).scaled(225,185)
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)
        self.edgesImage.setScene(scene)
        
        ''' Cartoon Image '''
        cartoonImagePath = str(os.getcwd())+"\cartoonImage.jpg"
        scene = QtWidgets.QGraphicsScene()
        scene.clear()
        self.cartoonImage.setScene(scene)
        pix = QtGui.QPixmap(cartoonImagePath).scaled(225,185)
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)
        self.cartoonImage.setScene(scene)
        return
    
    def resetdata(self):
        self.downsample.setText("2")
        self.bilateralfilterSteps.setText("50")
        self.sigmaBilateral.setText("9")
        self.kernelSize.setText("3")
        self.downscaleSlider.setProperty("value", 2)
        self.kernelSlider.setProperty("value", 3)
        self.bilateralslider.setProperty("value", 50)
        self.sigmaSlider.setProperty("value", 9)
        return
    
    def callSaveImages(self):
        if(self.folderPath.text()=="" or self.folderPath.text()==None):
            self.warningLabel.clear()
            self.warningLabel.setStyleSheet("color: red")
            self.warningLabel.setText("Please Choose the Output Directory")
            self.folderPath.clear()
        else:
            self.warningLabel.clear()
            currentDirectry = str(os.getcwd())
            os.chdir(str(pathFolder))
            if(os.path.exists(str(pathFolder)+"\Generated Images")):
                pass
            else:
                os.mkdir("Generated Images")
            os.chdir(str(pathFolder)+"\Generated Images\\")
            cv2.imwrite("Edge Detected.png",edgeImages)
            cv2.imwrite("Cartoon Image.jpg",cartoonImages)
            self.warningLabel.setStyleSheet("color: green")
            self.warningLabel.setText("Images are Saved in: "+"\""+str(os.getcwd())+"\"")
            os.chdir(currentDirectry)
            
        return
    
    def callClear(self):
        scene = QtWidgets.QGraphicsScene()
        scene.clear()
        self.originalImage.setScene(scene)
        
        scene = QtWidgets.QGraphicsScene()
        scene.clear()
        self.edgesImage.setScene(scene)
        
        scene = QtWidgets.QGraphicsScene()
        scene.clear()
        self.cartoonImage.setScene(scene)
        
        self.filePath.clear()
        self.folderPath.clear()
        self.warningLabel.clear()
        self.downsample.setText("2")
        self.bilateralfilterSteps.setText("50")
        self.sigmaBilateral.setText("9")
        self.kernelSize.setText("3")
        self.downscaleSlider.setProperty("value", 2)
        self.kernelSlider.setProperty("value", 3)
        self.bilateralslider.setProperty("value", 50)
        self.sigmaSlider.setProperty("value", 9)
        return

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.label.setText(_translate("StackedWidget", "Cartoon Generator from photo"))
        self.label_2.setText(_translate("StackedWidget", "File path:"))
        self.fileBrowse.setText(_translate("StackedWidget", "Browse"))
        self.label_3.setText(_translate("StackedWidget", "Output folder:"))
        self.folderBrowse.setText(_translate("StackedWidget", "Browse"))
        self.label_4.setText(_translate("StackedWidget", "Downscale Steps:"))
        self.label_5.setText(_translate("StackedWidget", "Bilateral Filtering Steps:"))
        self.label_6.setText(_translate("StackedWidget", "Sigma for Bilateral filter:"))
        self.label_7.setText(_translate("StackedWidget", "Kernel Size:"))
        self.generate.setText(_translate("StackedWidget", "Generate"))
        self.saveImages.setText(_translate("StackedWidget", "Save Images"))
        self.label_8.setText(_translate("StackedWidget", "Original Image"))
        self.label_10.setText(_translate("StackedWidget", "Edges Image"))
        self.label_11.setText(_translate("StackedWidget", "Cartoon Image"))
        self.clearBtn.setText(_translate("StackedWidget", "Clear"))
        self.resetBtn.setText(_translate("StackedWidget", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StackedWidget = QtWidgets.QStackedWidget()
    ui = Ui_StackedWidget()
    ui.setupUi(StackedWidget)
    StackedWidget.show()
    sys.exit(app.exec_())

