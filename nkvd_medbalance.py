# TODO
# взять файл
# определить его расширение
# zip распаковать и взять из него csv, а csv сразу пустить в работу
# взять инфу в список из нужных колонок
# сделать новые списке относительно алгоритма подсчёта остатков
import difflib
import os
import sys
# import openpyxl
# import openpyxl.utils
# import openpyxl.styles
import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtCore
import PyQt5.QtGui
# новые импорты для чтения архива, работы в файлами, временем и csv
# import datetime
# import shutil
# import psutil
import csv
import zipfile
import difflib
import locale


# класс главного окна
class WindowMain(PyQt5.QtWidgets.QMainWindow):
    """Класс главного окна"""

    # описание главного окна
    def __init__(self):
        super().__init__()

        # главное окно, надпись на нём и размеры
        self.setWindowTitle('Помощник проверки остатков')
        self.setGeometry(150, 150, 1000, 400)
        self.setWindowFlags(PyQt5.QtCore.Qt.WindowStaysOnTopHint)

        # переменные
        self.info_extention_open_file = 'Файлы (*.zip; *.csv)'
        self.info_path_open_file = None
        self.info_for_open_file = 'Выберите файл (.ZIP) или (.CSV)'
        self.text_empty_path_file = 'файл пока не выбран'
        self.selected_file = None

        # ОБЪЕКТЫ НА ФОРМЕ
        # label_prompt_select_file
        self.label_prompt_select_file = PyQt5.QtWidgets.QLabel(self)
        self.label_prompt_select_file.setObjectName('label_prompt_select_file')
        self.label_prompt_select_file.setText('Выберите файл ZIP или CSV')
        self.label_prompt_select_file.setGeometry(PyQt5.QtCore.QRect(10, 10, 150, 40))
        font = PyQt5.QtGui.QFont()
        font.setPointSize(12)
        self.label_prompt_select_file.setFont(font)
        self.label_prompt_select_file.adjustSize()
        self.label_prompt_select_file.setToolTip(self.label_prompt_select_file.objectName())

        # button_select_file
        self.button_select_file = PyQt5.QtWidgets.QPushButton(self)
        self.button_select_file.setObjectName('button_select_file')
        self.button_select_file.setText('...')
        self.button_select_file.setGeometry(PyQt5.QtCore.QRect(10, 40, 50, 20))
        self.button_select_file.setFixedWidth(50)
        self.button_select_file.clicked.connect(self.select_file)
        self.button_select_file.setToolTip(self.button_select_file.objectName())

        # label_path_selected_file
        self.label_path_selected_file = PyQt5.QtWidgets.QLabel(self)
        self.label_path_selected_file.setObjectName('label_path_selected_file')
        self.label_path_selected_file.setEnabled(False)
        self.label_path_selected_file.setText(self.text_empty_path_file)
        self.label_path_selected_file.setGeometry(PyQt5.QtCore.QRect(10, 70, 400, 40))
        font = PyQt5.QtGui.QFont()
        font.setPointSize(10)
        self.label_path_selected_file.setFont(font)
        self.label_path_selected_file.adjustSize()
        self.label_path_selected_file.setToolTip(self.label_path_selected_file.objectName())

        # тут место табличному виджету
        #

        # button_report_to_xls
        self.button_report_to_xls = PyQt5.QtWidgets.QPushButton(self)
        self.button_report_to_xls.setObjectName('button_report_to_xls')
        self.button_report_to_xls.setEnabled(False)
        self.button_report_to_xls.setText('Создать отчёт "Остатки на складе"')
        self.button_report_to_xls.setGeometry(PyQt5.QtCore.QRect(10, 230, 260, 25))
        self.button_report_to_xls.clicked.connect(self.report_to_xls)
        self.button_report_to_xls.setToolTip(self.button_report_to_xls.objectName())

        # button_exit
        self.button_exit = PyQt5.QtWidgets.QPushButton(self)
        self.button_exit.setObjectName('button_exit')
        self.button_exit.setText('Выход')
        self.button_exit.setGeometry(PyQt5.QtCore.QRect(10, 300, 100, 25))
        # self.button_exit.setFixedWidth(50)
        self.button_exit.clicked.connect(self.click_on_btn_exit)
        self.button_exit.setToolTip(self.button_exit.objectName())

    # событие - нажатие на кнопку выбора файла
    def select_file(self):
        # переменная для хранения информации из окна выбора файла
        data_of_open_file_name = None

        # запоминание старого значения пути выбора файлов
        old_path_of_selected_file = self.label_path_selected_file.text()

        # непосредственное окно выбора файла и переменная для хранения пути файла
        data_of_open_file_name = PyQt5.QtWidgets.QFileDialog.getOpenFileName(self,
                                                                             self.info_for_open_file,
                                                                             self.info_path_open_file,
                                                                             self.info_extention_open_file)
        # выбираю только путь из data_of_open_file_name
        selected_file_full_path = data_of_open_file_name[0]

        # нажата или не нажата кнопка выбора файла
        if selected_file_full_path == '':
            # если не выбран файл
            old_path_of_selected_file = self.label_path_selected_file.text()
            if self.label_path_selected_file.text() == self.text_empty_path_file:
                self.selected_file = None
            else:
                self.selected_file = old_path_of_selected_file
            self.label_path_selected_file.setText(old_path_of_selected_file)
            self.label_path_selected_file.adjustSize()
        else:
            # если выбран файл
            old_path_of_selected_file = self.label_path_selected_file.text()
            self.selected_file = os.path.normcase(selected_file_full_path)
            self.label_path_selected_file.setText(selected_file_full_path)
            self.label_path_selected_file.adjustSize()

        # активация и деактивация объектов на форме зависящее от выбора файла
        if self.text_empty_path_file not in self.label_path_selected_file.text():
            self.button_report_to_xls.setEnabled(True)

            self.parse_selected_file()

    # функция создания отчёта
    def parse_selected_file(self):
        file_full_path = self.selected_file
        file_full_name = os.path.basename(self.selected_file)
        file_name = os.path.basename(self.selected_file).rsplit('.', 1)[0]
        file_ext = os.path.basename(self.selected_file).rsplit('.', 1)[1]

        file_kit = (file_full_path, file_full_name, file_name, file_ext)

        if file_ext == 'zip':
            self.take_zip(file_kit)
        elif file_ext == 'csv':
            self.take_csv(file_kit)
        else:
            # не могу определить расширение файла
            pass

    # функция создания отчёта
    def take_zip(self, file_kit):
        # print(self.take_zip.__name__)
        # print(file_kit)
        # print()

        # работа с zip файлом
        if not zipfile.is_zipfile(file_kit[0]):
            # информационное окно про полное заполнение колонки
            PyQt5.QtWidgets.QMessageBox.information(self,'Ошибка', f'Файл\n{file_kit[0]}\n не является архивом zip')
        else:
            # файл экземпляр ZipFile
            zf = zipfile.ZipFile(file_kit[0])
            # print(zf.filename)
            # print(zf.filelist)
            # print(zf.namelist())
            # print(zf.infolist())

            # поиск файла csv в архиве
            flag_csv_ext = False
            for file_in_zf in zf.infolist():
                # print(file_in_zf)
                # print(file_in_zf.filename)
                # print(file_in_zf.is_dir())
                if not file_in_zf.is_dir():
                    # print(file_in_zf.filename)
                    if file_in_zf.filename.rsplit('.', 1)[1].lower() == 'csv':
                        diff_ratio_file_names = difflib.SequenceMatcher(None, file_kit[2],
                                                                        file_in_zf.filename.rsplit('.', 1)[0]).ratio()
                        if diff_ratio_file_names < 0.9:
                            PyQt5.QtWidgets.QMessageBox.information(self, 'Ошибка',
                                f'Имя файла zip не совпадает с именам внутри архива.\n'
                                f'Выберите непереименованный файл скачанный с сайта\n'
                                f'или выберите другой.')
                        else:
                            flag_csv_ext = True

                            with zf.open(file_in_zf.filename) as file_csv:
                                # text = file_csv.readlines()
                                text = file_csv.read()
                            # print(text)
                            # print(text.decode('utf-8'))
                            # print(text.decode('cp1251'))

                            print(locale.getpreferredencoding())
                            sys_lcl = locale.getpreferredencoding()

                            reader_object = csv.reader(text.decode(sys_lcl),
                                                       delimiter=";",
                                                       # doublequote=False,
                                                       # quotechar='',
                                                       # lineterminator='\n'
                                                       # skipinitialspace=True,
                                                       # strict=False
                                                       )
                            for cell in reader_object:
                                print(cell, end='')
                            print()

                            # for csv_str in text:
                            #     pass
                            #     print(csv_str)
                            #     print(csv_str.decode('utf-8'))
                            #     print('------------------')
                            #     reader_object = csv.reader(csv_str.decode('utf-8'), delimiter=',', doublequote=True)
                            #     for cell in reader_object:
                            #         print(cell, end=' ... ')
                            #     print()


                            # # reader_object = csv.reader(csv_str.decode('utf-8'), delimiter=",", quotechar='"', doublequote=True)
                            # reader_object = csv.reader(text)
                            # for row in reader_object:
                            #     print(row)


            zf.close()





    # функция создания отчёта
    def take_csv(self, file_kit):
        print(self.take_csv.__name__)

    # функция создания отчёта
    def report_to_xls(self):
        pass

    # событие - нажатие на кнопку Выход
    @staticmethod
    def click_on_btn_exit():
        sys.exit()


# создание основного окна
def main_app():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app_window_main = WindowMain()
    app_window_main.show()
    sys.exit(app.exec_())


# запуск основного окна
if __name__ == '__main__':
    main_app()
