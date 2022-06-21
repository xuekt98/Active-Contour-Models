# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 402)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SelectImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.SelectImageButton.setGeometry(QtCore.QRect(30, 20, 150, 40))
        self.SelectImageButton.setObjectName("SelectImageButton")
        self.ClassicalSnakeButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClassicalSnakeButton.setGeometry(QtCore.QRect(30, 70, 150, 40))
        self.ClassicalSnakeButton.setObjectName("ClassicalSnakeButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 130, 161, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.CSParamsGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.CSParamsGrid.setContentsMargins(0, 0, 0, 0)
        self.CSParamsGrid.setObjectName("CSParamsGrid")
        self.CSweSB = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.CSweSB.setDecimals(3)
        self.CSweSB.setMaximum(10.0)
        self.CSweSB.setSingleStep(0.01)
        self.CSweSB.setProperty("value", 5.0)
        self.CSweSB.setObjectName("CSweSB")
        self.CSParamsGrid.addWidget(self.CSweSB, 5, 4, 1, 1)
        self.CSGammaSB = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.CSGammaSB.setDecimals(3)
        self.CSGammaSB.setMaximum(10.0)
        self.CSGammaSB.setSingleStep(0.01)
        self.CSGammaSB.setProperty("value", 1.5)
        self.CSGammaSB.setObjectName("CSGammaSB")
        self.CSParamsGrid.addWidget(self.CSGammaSB, 3, 4, 1, 1)
        self.CSwlSB = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.CSwlSB.setDecimals(3)
        self.CSwlSB.setMaximum(10.0)
        self.CSwlSB.setSingleStep(0.01)
        self.CSwlSB.setObjectName("CSwlSB")
        self.CSParamsGrid.addWidget(self.CSwlSB, 4, 4, 1, 1)
        self.CSwtSB = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.CSwtSB.setDecimals(3)
        self.CSwtSB.setMaximum(10.0)
        self.CSwtSB.setSingleStep(0.01)
        self.CSwtSB.setObjectName("CSwtSB")
        self.CSParamsGrid.addWidget(self.CSwtSB, 6, 4, 1, 1)
        self.CSAlphaSB = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.CSAlphaSB.setDecimals(3)
        self.CSAlphaSB.setMaximum(10.0)
        self.CSAlphaSB.setSingleStep(0.01)
        self.CSAlphaSB.setProperty("value", 0.1)
        self.CSAlphaSB.setObjectName("CSAlphaSB")
        self.CSParamsGrid.addWidget(self.CSAlphaSB, 1, 4, 1, 1)
        self.CSGammaLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CSGammaLabel.setObjectName("CSGammaLabel")
        self.CSParamsGrid.addWidget(self.CSGammaLabel, 3, 1, 1, 1)
        self.CSEdgeWeightLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CSEdgeWeightLabel.setObjectName("CSEdgeWeightLabel")
        self.CSParamsGrid.addWidget(self.CSEdgeWeightLabel, 5, 1, 1, 1)
        self.CSLineWeightLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CSLineWeightLabel.setObjectName("CSLineWeightLabel")
        self.CSParamsGrid.addWidget(self.CSLineWeightLabel, 4, 1, 1, 1)
        self.CSTermWeightLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CSTermWeightLabel.setObjectName("CSTermWeightLabel")
        self.CSParamsGrid.addWidget(self.CSTermWeightLabel, 6, 1, 1, 1)
        self.CSBetaLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CSBetaLabel.setObjectName("CSBetaLabel")
        self.CSParamsGrid.addWidget(self.CSBetaLabel, 2, 1, 1, 1)
        self.CSBetaSB = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.CSBetaSB.setDecimals(3)
        self.CSBetaSB.setMaximum(10.0)
        self.CSBetaSB.setSingleStep(0.01)
        self.CSBetaSB.setProperty("value", 3.0)
        self.CSBetaSB.setObjectName("CSBetaSB")
        self.CSParamsGrid.addWidget(self.CSBetaSB, 2, 4, 1, 1)
        self.CSAlphaLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CSAlphaLabel.setObjectName("CSAlphaLabel")
        self.CSParamsGrid.addWidget(self.CSAlphaLabel, 1, 1, 1, 1)
        self.GVFSnakeButton = QtWidgets.QPushButton(self.centralwidget)
        self.GVFSnakeButton.setGeometry(QtCore.QRect(380, 70, 150, 40))
        self.GVFSnakeButton.setObjectName("GVFSnakeButton")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(380, 130, 161, 91))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.GVFParamsGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.GVFParamsGrid.setContentsMargins(0, 0, 0, 0)
        self.GVFParamsGrid.setObjectName("GVFParamsGrid")
        self.GVFMuSB = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.GVFMuSB.setDecimals(3)
        self.GVFMuSB.setMaximum(10.0)
        self.GVFMuSB.setSingleStep(0.01)
        self.GVFMuSB.setProperty("value", 0.1)
        self.GVFMuSB.setObjectName("GVFMuSB")
        self.GVFParamsGrid.addWidget(self.GVFMuSB, 3, 4, 1, 1)
        self.GVFBetaLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.GVFBetaLabel.setObjectName("GVFBetaLabel")
        self.GVFParamsGrid.addWidget(self.GVFBetaLabel, 2, 1, 1, 1)
        self.GVFAlphaSB = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.GVFAlphaSB.setDecimals(3)
        self.GVFAlphaSB.setMaximum(10.0)
        self.GVFAlphaSB.setSingleStep(0.01)
        self.GVFAlphaSB.setProperty("value", 3.0)
        self.GVFAlphaSB.setObjectName("GVFAlphaSB")
        self.GVFParamsGrid.addWidget(self.GVFAlphaSB, 1, 4, 1, 1)
        self.GVFMuLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.GVFMuLabel.setObjectName("GVFMuLabel")
        self.GVFParamsGrid.addWidget(self.GVFMuLabel, 3, 1, 1, 1)
        self.GVFBetaSB = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.GVFBetaSB.setDecimals(3)
        self.GVFBetaSB.setMaximum(10.0)
        self.GVFBetaSB.setSingleStep(0.01)
        self.GVFBetaSB.setProperty("value", 1.75)
        self.GVFBetaSB.setObjectName("GVFBetaSB")
        self.GVFParamsGrid.addWidget(self.GVFBetaSB, 2, 4, 1, 1)
        self.GVFAlphaLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.GVFAlphaLabel.setObjectName("GVFAlphaLabel")
        self.GVFParamsGrid.addWidget(self.GVFAlphaLabel, 1, 1, 1, 1)
        self.SaveResultBox = QtWidgets.QCheckBox(self.centralwidget)
        self.SaveResultBox.setGeometry(QtCore.QRect(200, 30, 91, 19))
        self.SaveResultBox.setObjectName("SaveResultBox")
        self.CSDefaultBox = QtWidgets.QCheckBox(self.centralwidget)
        self.CSDefaultBox.setGeometry(QtCore.QRect(200, 80, 151, 19))
        self.CSDefaultBox.setObjectName("CSDefaultBox")
        self.GVFDefaultBox = QtWidgets.QCheckBox(self.centralwidget)
        self.GVFDefaultBox.setGeometry(QtCore.QRect(550, 80, 151, 19))
        self.GVFDefaultBox.setObjectName("GVFDefaultBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(380, 20, 151, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.MaxIterGrid = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.MaxIterGrid.setContentsMargins(0, 0, 0, 0)
        self.MaxIterGrid.setObjectName("MaxIterGrid")
        self.MaxIterLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.MaxIterLabel.setObjectName("MaxIterLabel")
        self.MaxIterGrid.addWidget(self.MaxIterLabel)
        self.MaxIterBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.MaxIterBox.setMaximum(300)
        self.MaxIterBox.setProperty("value", 100)
        self.MaxIterBox.setObjectName("MaxIterBox")
        self.MaxIterGrid.addWidget(self.MaxIterBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 711, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SelectImageButton.setText(_translate("MainWindow", "Select Image"))
        self.ClassicalSnakeButton.setText(_translate("MainWindow", "Run Classical Snake"))
        self.CSGammaLabel.setText(_translate("MainWindow", "gamma"))
        self.CSEdgeWeightLabel.setText(_translate("MainWindow", "edge weight"))
        self.CSLineWeightLabel.setText(_translate("MainWindow", "line weight"))
        self.CSTermWeightLabel.setText(_translate("MainWindow", "term weight"))
        self.CSBetaLabel.setText(_translate("MainWindow", "beta"))
        self.CSAlphaLabel.setText(_translate("MainWindow", "alpha"))
        self.GVFSnakeButton.setText(_translate("MainWindow", "Run GVF Snake"))
        self.GVFBetaLabel.setText(_translate("MainWindow", "beta"))
        self.GVFMuLabel.setText(_translate("MainWindow", "mu"))
        self.GVFAlphaLabel.setText(_translate("MainWindow", "alpha"))
        self.SaveResultBox.setText(_translate("MainWindow", "save result"))
        self.CSDefaultBox.setText(_translate("MainWindow", "use default parameters"))
        self.GVFDefaultBox.setText(_translate("MainWindow", "use default parameters"))
        self.MaxIterLabel.setText(_translate("MainWindow", "Max Iter"))