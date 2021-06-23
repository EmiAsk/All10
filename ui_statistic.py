# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_statistic.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(872, 699)
        Form.setStyleSheet("QWidget {background-color: #1581e6; color: white; font-family: \"Days\";}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_today = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setFamily("Days")
        font.setPointSize(18)
        self.btn_today.setFont(font)
        self.btn_today.setChecked(True)
        self.btn_today.setObjectName("btn_today")
        self.mode_of_sorting = QtWidgets.QButtonGroup(Form)
        self.mode_of_sorting.setObjectName("mode_of_sorting")
        self.mode_of_sorting.addButton(self.btn_today)
        self.horizontalLayout.addWidget(self.btn_today)
        self.btn_month = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setFamily("Days")
        font.setPointSize(18)
        self.btn_month.setFont(font)
        self.btn_month.setObjectName("btn_month")
        self.mode_of_sorting.addButton(self.btn_month)
        self.horizontalLayout.addWidget(self.btn_month)
        self.btn_year = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setFamily("Days")
        font.setPointSize(18)
        self.btn_year.setFont(font)
        self.btn_year.setObjectName("btn_year")
        self.mode_of_sorting.addButton(self.btn_year)
        self.horizontalLayout.addWidget(self.btn_year)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.profile_table = QtWidgets.QTableWidget(Form)
        self.profile_table.setStyleSheet("QHeaderView::section {background-color:rgb(21, 129, 230)}\n"
"QHeaderView { font-size: 16pt; }\n"
"")
        self.profile_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.profile_table.setObjectName("profile_table")
        self.profile_table.setColumnCount(0)
        self.profile_table.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.profile_table)
        self.profile_graph = PlotWidget(Form)
        self.profile_graph.setObjectName("profile_graph")
        self.horizontalLayout_4.addWidget(self.profile_graph)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_table = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setFamily("Days")
        font.setPointSize(18)
        self.btn_table.setFont(font)
        self.btn_table.setChecked(True)
        self.btn_table.setObjectName("btn_table")
        self.table_graph = QtWidgets.QButtonGroup(Form)
        self.table_graph.setObjectName("table_graph")
        self.table_graph.addButton(self.btn_table)
        self.horizontalLayout_2.addWidget(self.btn_table, 0, QtCore.Qt.AlignRight)
        self.btn_graph = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setFamily("Days")
        font.setPointSize(18)
        self.btn_graph.setFont(font)
        self.btn_graph.setChecked(False)
        self.btn_graph.setObjectName("btn_graph")
        self.table_graph.addButton(self.btn_graph)
        self.horizontalLayout_2.addWidget(self.btn_graph)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Статистика"))
        self.btn_today.setText(_translate("Form", "Сегодня"))
        self.btn_month.setText(_translate("Form", "За месяц"))
        self.btn_year.setText(_translate("Form", "За год"))
        self.btn_table.setText(_translate("Form", "Таблица"))
        self.btn_graph.setText(_translate("Form", "График"))
from pyqtgraph import PlotWidget
