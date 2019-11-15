# Программа находиться в стадии активной разработки.
# Из функции анализа работает только Возраст,
# Показать всё и выводиться в виде таблици и линейного графика.
# При анализе группы с 10к пользователями уже занимает время и ресурсы ЭВМ.
# Программа будет улучшаться в дальнейшем.

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from form import Ui_Form
import sys
import VkApiWorker
import SqlWorker
from Logger import *
from time import sleep


class Program(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        clearAll()  # Очитска логов
        self.db_file = None
        self.token = None
        self.vk = None
        self.widget.hide()  # Скрытие виджета, который отвечает за работу с файлами

        # Привызка нажатий клавишь к функциям
        self.btn_file_db.clicked.connect(self.openFileWidget)
        self.btn_search.clicked.connect(self.do_search)
        self.btn_update.clicked.connect(self.update_)
        self.btn_file_token.clicked.connect(self.openFileToken)
        # Конец привязки

    # Функция отображает текущие логи
    def show_logs(self):
        with open('apigv.log', 'r') as f:
            self.logs.setText(''.join(f.readlines()))

    # Функция выбора файла db
    def openFileWidget(self):
        self.widget.show()  # Отображение виджета

        #  Открытия диалогового окна выбора файла
        def open_():
            self.widget.hide()  # Скрытие виджета
            # Открытие диалогового окна и запись пути до файла в self.db_file
            self.db_file = QFileDialog.getOpenFileName(self, 'Выберете базу данных',
                                                       '', 'База данных (*.db)')[0]
            try:
                # Попытка Подключиться к этой базе
                self.sql = SqlWorker.SQL(self.db_file)
                self.sql.cur.execute('''SELECT * FROM users''')
            except Exception as e:
                addLog('|Main|: ' + str(e))
            # Возращение изначальной функции кнопки
            self.btn_file_db.clicked.connect(self.openFileWidget)

        def save():
            self.widget.hide()
            try:
                self.sql.con.commit()
                addLog('|Main|: Data saved.')
            except Exception as e:
                addLog('|Main|: ' + str(e))
            self.btn_file_db.clicked.connect(self.openFileWidget)

        # Функция повторного нажатия на кнопку закрывает виджет без каких либо действий
        def empty_click():
            self.widget.hide()
            self.btn_file_db.clicked.connect(self.openFileWidget)

        # Определение функций кнопок
        self.btn_file_db.clicked.connect(empty_click)  # Перезначение функции на повторное нажатие
        self.btn_open.clicked.connect(open_)
        self.btn_save.clicked.connect(save)

        self.show_logs()

    def openFileToken(self):
        path = QFileDialog.getOpenFileName(self, 'Файл с токеном vk', '', 'Текстовый файл (*.txt)')[0]
        try:
            with open(path, 'r') as f:
                for line in f:
                    self.token = line
                    break
            self.vk = VkApiWorker.VkParser(self.token)
        except Exception as e:
            addLog('|Main|: ' + str(e))

        self.show_logs()

    # Функция поиска данных в базе
    def do_search(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        group_id = self.site.text()[self.site.text().rfind(
            '/') + 1:] if 'vk.com/' in self.site.text() else None
        if self.db_file is not None:
            if self.comboBox.currentText() == 'Показать текущую группу':
                data = self.sql.get_curent(group_id)
                try:
                    self.tableWidget.setRowCount(len(data))
                    self.tableWidget.setColumnCount(len(data[0]))
                    for i, user in enumerate(data):
                        for j, elem in enumerate(user):
                            self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
                except Exception as e:
                    addLog('|Main|: ' + str(e))
            elif self.comboBox.currentText() == 'Показать всё':
                data = self.sql.get_all()
                try:
                    self.tableWidget.setRowCount(len(data))
                    self.tableWidget.setColumnCount(len(data[0]))
                    for i, user in enumerate(data):
                        for j, elem in enumerate(user):
                            self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
                except Exception as e:
                    addLog('|Main|: ' + str(e))
            elif self.comboBox.currentText() == 'Возраст':
                data = self.sql.get_age(group_id)
                try:
                    # Вывод в таблицу
                    self.tableWidget.setRowCount(len(data))
                    self.tableWidget.setColumnCount(len(data[0]))
                    for i, user in enumerate(data):
                        for j, elem in enumerate(user):
                            self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

                    # Построения графика возраста от кол-ва
                    self.y_axis.setText('Количество людей')
                    self.x_axis.setText('Возраст')
                    self.graphicsView.clear()
                    ages = sorted([2019 - int(str(user[-1]).split('.')[-1]) for user in data])
                    self.graphicsView.plot(sorted(list(set(ages))),
                                           [ages.count(age) for age in sorted(list(set(ages)))],
                                           pen='r')
                    maxx = max([ages.count(age) for age in sorted(list(set(ages)))])
                    minn = min([ages.count(age) for age in sorted(list(set(ages)))])
                    self.maximum.setText(str(maxx))
                    self.minimum.setText(str(minn))
                    self.graphicsView.plot(sorted(list(set(ages))),
                                           [maxx for _ in range(len(sorted(list(set(ages)))))],
                                           pen='g')
                    self.graphicsView.plot(sorted(list(set(ages))),
                                           [minn for _ in range(len(sorted(list(set(ages)))))],
                                           pen='b')
                except Exception as e:
                    addLog('|Main|: ' + str(e))
            elif self.comboBox.currentText() == 'Пол':
                data = self.sql.get_sex(group_id)
                # Вывод в таблицу
                self.tableWidget.setRowCount(len(data))
                self.tableWidget.setColumnCount(len(data[0]))
                for i, user in enumerate(data):
                    for j, elem in enumerate(user):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
            elif self.comboBox.currentText() == 'Кол-во \"banned\"':
                data = self.sql.get_banned(group_id)
                # Вывод в таблицу
                self.tableWidget.setRowCount(len(data))
                self.tableWidget.setColumnCount(len(data[0]))
                for i, user in enumerate(data):
                    for j, elem in enumerate(user):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
            elif self.comboBox.currentText() == 'Кол-во \"deleted\"':
                data = self.sql.get_deleted(group_id)
                # Вывод в таблицу
                self.tableWidget.setRowCount(len(data))
                self.tableWidget.setColumnCount(len(data[0]))
                for i, user in enumerate(data):
                    for j, elem in enumerate(user):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        else:
            addLog('|Main|: Didn\'t chosen db file.')
        self.show_logs()

    def update_(self):
        self.btn_file_db.setEnabled(False)
        self.btn_file_token.setEnabled(False)
        self.site.setEnabled(False)
        self.comboBox.setEnabled(False)
        self.btn_search.setEnabled(False)
        self.tabWidget.setEnabled(False)
        self.btn_update.setEnabled(False)
        self.status.setText('Обновление базы...')
        self.repaint()

        if self.db_file is not None:
            if self.vk is not None:
                for offset in range(0, self.vk.get_count(str(self.site.text())), 1000):
                    self.vk.getDataFromGroup(str(self.site.text()), offset)
                    self.vk.convertData()
                    if self.vk.data is not None:
                        for user in self.vk.data:
                            self.sql.add_user(user)
                        self.sql.con.commit()
                        self.vk.data = None
                        addLog('|Main|: Successful added users.')
                    else:
                        addLog('|Main|: Data is None.')
                    sleep(0.06)
            else:
                addLog('|Main|: Didn\'t chosen token file.')
        else:
            addLog('|Main|: Didn\'t chosen db file.')

        self.btn_file_db.setEnabled(True)
        self.btn_file_token.setEnabled(True)
        self.site.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.btn_search.setEnabled(True)
        self.tabWidget.setEnabled(True)
        self.btn_update.setEnabled(True)
        self.status.setText('')
        self.repaint()

        self.do_search()
        self.show_logs()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Program()
    prog.show()
    sys.exit(app.exec())
