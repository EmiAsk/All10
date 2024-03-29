# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pretest.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1150, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1150, 640))
        Form.setMaximumSize(QtCore.QSize(1150, 640))
        Form.setStyleSheet("QWidget {background-color: #1581e6; color: white; font-family: \"Days\";}\n"
"QPushButton:hover {border-style: solid; border-width: 3px; border-color: white;} QPushButton:pressed {border-style: solid; border-width: 3px; border-color: rgb(14, 80, 158);} QPushButton {background-color: rgb(255, 230, 31); color: rgb(14, 80, 158); border-radius: 10px;}")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(490, 170, 491, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(42)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Days")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btn_make_test = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_make_test.sizePolicy().hasHeightForWidth())
        self.btn_make_test.setSizePolicy(sizePolicy)
        self.btn_make_test.setMinimumSize(QtCore.QSize(250, 70))
        font = QtGui.QFont()
        font.setFamily("Days")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_make_test.setFont(font)
        self.btn_make_test.setStyleSheet("")
        self.btn_make_test.setObjectName("btn_make_test")
        self.verticalLayout.addWidget(self.btn_make_test)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 331, 411))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/Секундомер.png"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Начать тестирование"))
        self.label.setText(_translate("Form", "Набери небольшой текст. Проверь, сколько знаков в минуту ты печатаешь на русском языке"))
        self.btn_make_test.setText(_translate("Form", "Пройти тест печати"))
