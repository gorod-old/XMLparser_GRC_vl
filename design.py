# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 200)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 240))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.selectFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectFileButton.setMinimumSize(QtCore.QSize(160, 0))
        self.selectFileButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.selectFileButton.setObjectName("selectFileButton")
        self.gridLayout.addWidget(self.selectFileButton, 4, 1, 1, 1)
        self.lineEditFileName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFileName.setMinimumSize(QtCore.QSize(400, 28))
        self.lineEditFileName.setObjectName("lineEditFileName")
        self.gridLayout.addWidget(self.lineEditFileName, 3, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setMinimumSize(QtCore.QSize(160, 0))
        self.startButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startButton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 4, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 3)
        self.lineEditFile = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFile.setMinimumSize(QtCore.QSize(400, 28))
        self.lineEditFile.setObjectName("lineEditFile")
        self.gridLayout.addWidget(self.lineEditFile, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(150, 25, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 36))
        self.label_3.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.dateEdit_from = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_from.setMinimumSize(QtCore.QSize(160, 36))
        self.dateEdit_from.setMaximumSize(QtCore.QSize(160, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit_from.setFont(font)
        self.dateEdit_from.setObjectName("dateEdit_from")
        self.horizontalLayout.addWidget(self.dateEdit_from)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 36))
        self.label_4.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.dateEdit_to = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_to.setMinimumSize(QtCore.QSize(160, 36))
        self.dateEdit_to.setMaximumSize(QtCore.QSize(160, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit_to.setFont(font)
        self.dateEdit_to.setObjectName("dateEdit_to")
        self.horizontalLayout.addWidget(self.dateEdit_to)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Парсер данных из XML в Excel"))
        self.selectFileButton.setText(_translate("MainWindow", "выберите файл"))
        self.startButton.setText(_translate("MainWindow", "Старт"))
        self.label_2.setText(_translate("MainWindow", "<<<   введите название файла для результата"))
        self.label_3.setText(_translate("MainWindow", "Дата от:"))
        self.label_4.setText(_translate("MainWindow", "до"))
