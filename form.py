# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(922, 690)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 570, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 141, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(180, 90, 731, 31))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.site = QtWidgets.QLineEdit(Form)
        self.site.setGeometry(QtCore.QRect(180, 40, 731, 31))
        self.site.setReadOnly(False)
        self.site.setObjectName("site")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 40, 161, 31))
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 170, 901, 391))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, -1, 901, 361))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.l_count = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.l_count.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 215, 207);")
        self.l_count.setText("")
        self.l_count.setObjectName("l_count")
        self.verticalLayout_2.addWidget(self.l_count)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.graphicsView = PlotWidget(self.tab_3)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 901, 361))
        self.graphicsView.setObjectName("graphicsView")
        self.widget_2 = QtWidgets.QWidget(self.tab_3)
        self.widget_2.setGeometry(QtCore.QRect(710, 0, 191, 71))
        self.widget_2.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.widget_2.setObjectName("widget_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 191, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 1, 1, 1)
        self.maximum = QtWidgets.QLabel(self.gridLayoutWidget)
        self.maximum.setText("")
        self.maximum.setObjectName("maximum")
        self.gridLayout.addWidget(self.maximum, 0, 2, 1, 1)
        self.minimum = QtWidgets.QLabel(self.gridLayoutWidget)
        self.minimum.setText("")
        self.minimum.setObjectName("minimum")
        self.gridLayout.addWidget(self.minimum, 1, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.y_axis = QtWidgets.QLabel(self.tab_3)
        self.y_axis.setGeometry(QtCore.QRect(20, 0, 531, 17))
        self.y_axis.setStyleSheet("color: rgb(186, 189, 182);")
        self.y_axis.setText("")
        self.y_axis.setObjectName("y_axis")
        self.x_axis = QtWidgets.QLabel(self.tab_3)
        self.x_axis.setGeometry(QtCore.QRect(750, 300, 131, 20))
        self.x_axis.setStyleSheet("color: rgb(186, 189, 182);")
        self.x_axis.setText("")
        self.x_axis.setObjectName("x_axis")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.logs = QtWidgets.QTextEdit(Form)
        self.logs.setGeometry(QtCore.QRect(100, 570, 811, 111))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.logs.setFont(font)
        self.logs.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);")
        self.logs.setObjectName("logs")
        self.btn_file_db = QtWidgets.QPushButton(Form)
        self.btn_file_db.setGeometry(QtCore.QRect(10, 10, 181, 25))
        self.btn_file_db.setObjectName("btn_file_db")
        self.btn_file_token = QtWidgets.QPushButton(Form)
        self.btn_file_token.setGeometry(QtCore.QRect(210, 10, 181, 25))
        self.btn_file_token.setObjectName("btn_file_token")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(10, 30, 181, 91))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 180, 89))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_open = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setKerning(False)
        self.btn_open.setFont(font)
        self.btn_open.setDefault(False)
        self.btn_open.setFlat(True)
        self.btn_open.setObjectName("btn_open")
        self.verticalLayout.addWidget(self.btn_open)
        self.btn_save = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_save.setFlat(True)
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout.addWidget(self.btn_save)
        self.btn_file_csv = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_file_csv.setFlat(True)
        self.btn_file_csv.setObjectName("btn_file_csv")
        self.verticalLayout.addWidget(self.btn_file_csv)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 901, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_search = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_search.setEnabled(True)
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout.addWidget(self.btn_search)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_update = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_update.setObjectName("btn_update")
        self.horizontalLayout_2.addWidget(self.btn_update)
        self.rbtn_one1k = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbtn_one1k.setObjectName("rbtn_one1k")
        self.horizontalLayout_2.addWidget(self.rbtn_one1k)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.status = QtWidgets.QLabel(Form)
        self.status.setGeometry(QtCore.QRect(710, 160, 201, 31))
        self.status.setText("")
        self.status.setObjectName("status")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "АПИГВ"))
        self.label_3.setText(_translate("Form", "Детали:"))
        self.label_2.setText(_translate("Form", "Категории анализа:"))
        self.comboBox.setItemText(0, _translate("Form", "Показать текущую группу"))
        self.comboBox.setItemText(1, _translate("Form", "Показать всё"))
        self.comboBox.setItemText(2, _translate("Form", "Пол"))
        self.comboBox.setItemText(3, _translate("Form", "Возраст"))
        self.comboBox.setItemText(4, _translate("Form", "Кол-во \"banned\""))
        self.comboBox.setItemText(5, _translate("Form", "Кол-во \"deleted\""))
        self.label.setText(_translate("Form", "Ссылка на группу Вк:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Таблица"))
        self.label_5.setText(_translate("Form", "Минимум:"))
        self.label_4.setText(_translate("Form", "Максимум:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Линейный график"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Круговая диаграмма"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Столбчатый график"))
        self.btn_file_db.setText(_translate("Form", "Файл Базы данных"))
        self.btn_file_token.setText(_translate("Form", "Файл с токеном Vk Api"))
        self.btn_open.setText(_translate("Form", "Открыть файл"))
        self.btn_save.setText(_translate("Form", "Сохранить"))
        self.btn_file_csv.setText(_translate("Form", "Сохранить в csv формат"))
        self.btn_search.setText(_translate("Form", "Поиск"))
        self.btn_update.setText(_translate("Form", "Обновить базу"))
        self.rbtn_one1k.setText(_translate("Form", "Сканировать 1000 пользователей"))
from pyqtgraph import PlotWidget
