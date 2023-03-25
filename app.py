import os
from datetime import datetime

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QDate, QDateTime
from colorama import Fore, Style

import design
from MessagePack import print_info_msg, print_exception_msg
import xml.etree.ElementTree as Et
import numpy as np

from save_data import save_xlsx, save_xlsx_sheets

HEADER_MAP_DDU = ["дом", "тип", "квартира", "этаж", "площадь", "text_", "ods_", "название", "документ", "дата"]
HEADER_MAP_I = ["права", "название", "документ", "дата"]


class MainWindow(QMainWindow, design.Ui_MainWindow):
    def __init__(self, marker: str = ''):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
        self.setupUi(self)

        # ToolTips stylesheet
        self.setStyleSheet("""QToolTip {
                            border: 1px solid black;
                            padding: 3px;
                            border-radius: 3px;
                            opacity: 200;
                        }""")

        # self.ddu_list, self.i_list = [], []

        self.startButton.clicked.connect(self._start_click)
        self.selectFileButton.clicked.connect(self._select_file_path)

    def _select_file_path(self):
        print(os.getcwd())
        path = QFileDialog.getOpenFileName(self, 'Выберите файл', os.getcwd())[0]
        self.lineEditFile.setText(path)
        print_info_msg(f'path: {path}')

    def _check_file_name(self):
        name = self.lineEditFileName.text()
        names = []
        for root, dirs, files in os.walk("./result data"):
            for filename in files:
                names.append(filename.split(".")[0])
        print(names)
        if name == "":
            QMessageBox.question(self, 'Внимание!', 'Не указано название файла результата!.', QMessageBox.Ok)
            return None
        elif name in names:
            button = \
                QMessageBox.question(self, 'Внимание!',
                                     'Файл с таким именем уже существует. Хотите перезаписать существующий файл?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if button == QMessageBox.Yes:
                return name
            else:
                return None
        return name

    def _get_xml_file(self):
        xml_file = self.lineEditFile.text()
        if not xml_file.endswith('.xml'):
            QMessageBox.question(self, 'Внимание!', 'Расширение файла не .xml. Выберите другой файл.', QMessageBox.Ok)
            xml_file = None
        return xml_file

    @staticmethod
    def add_row_info(row, append_to, index_1=None, index_2=None):
        check = np.array(row)
        empty = True
        for cell in row:
            if cell != '':
                empty = False
                break
        if len(row) == 0 or empty:
            return
        for r in append_to:
            if np.array_equal(check, np.array(r)):
                return
        index_1 = '' if index_1 is None else Fore.BLUE + f'[{index_1}]'
        index_2 = '' if index_2 is None else Fore.BLUE + f'[{index_2}]'
        print(Fore.YELLOW + f'[PARSER]', index_1, index_2, Style.RESET_ALL + f'{row}')
        append_to.append(row)

    def _start_click(self):
        self.ddu_list, self.i_list = [], []
        file_name = self._check_file_name()
        if file_name is None:
            return
        xml_file = self._get_xml_file()
        if xml_file is None:
            return
        start_date = self.dateEdit_from.date()
        end_date = self.dateEdit_to.date()
        # create element tree object
        tree = Et.parse(xml_file)
        print(tree)

        # get root element
        root = tree.getroot()
        print(root)

        els = root.findall('./deal_records/deal_record')
        print(len(els))

        for el in els:
            house_, type_, flat_, floor_, area_, text_, ods_, doc_, date_, name_ = \
                '', '', '', '', '', '', '', '', '', ''
            try:
                doc_ = el.findall('./underlying_documents/underlying_document/document_number')[0].text
            except Exception as e:
                # print_exception_msg(str(e))
                pass
            if '/п' not in doc_.lower() and '-нп' not in doc_.lower() and '-п' not in doc_.lower():
                doc_date = None
                try:
                    date_ = el.findall('./underlying_documents/underlying_document/document_date')[0].text
                    y, m, d = date_.split('-')
                    doc_date = QDate(int(y), int(m), int(d))
                    # date_ = datetime(int(y), int(m), int(d))
                    date_ = f"{int(d)}.{int(m)}.{int(y)}"
                except Exception as e:
                    # print_exception_msg('date_, ' + str(e))
                    pass
                # print(start_date.toPyDate(), doc_date.toPyDate(), end_date.toPyDate())
                if doc_date and start_date <= doc_date <= end_date:
                    try:
                        name_ = el.findall('./underlying_documents/underlying_document/document_name')[0].text
                    except Exception as e:
                        # print_exception_msg('name_, ' + str(e))
                        pass
                    try:
                        house_ = el.findall('./deal_data/subject/share_subject_description/house_descriptions'
                                            '/house_description/house_number')[0].text
                    except Exception as e:
                        # print_exception_msg('house_, ' + str(e))
                        pass
                    try:
                        type_ = el.findall('./deal_data/subject/share_subject_description/house_descriptions'
                                           '/house_description/room_descriptions/room_description/room_name')[0].text
                    except Exception as e:
                        # print_exception_msg('type_, ' + str(e))
                        pass
                    try:
                        flat_ = el.findall('./deal_data/subject/share_subject_description/house_descriptions'
                                           '/house_description/room_descriptions/room_description/room_number')[0].text
                    except Exception as e:
                        # print_exception_msg('flat_, ' + str(e))
                        pass
                    try:
                        floor_ = el.findall('./deal_data/subject/share_subject_description/house_descriptions'
                                            '/house_description/room_descriptions/room_description/floor_number')[0].text
                    except Exception as e:
                        # print_exception_msg('floor_, ' + str(e))
                        pass
                    try:
                        area_ = el.findall('./deal_data/subject/share_subject_description/house_descriptions'
                                           '/house_description/room_descriptions/room_description/room_area')[0].text
                    except Exception as e:
                        # print_exception_msg('area_, ' + str(e))
                        pass
                    try:
                        text_ = el.findall('./deal_data/subject/share_subject_description/house_descriptions'
                                           '/house_description/room_descriptions/room_description/text_description')
                        if len(text_) > 0:
                            text_ = text_[0].text
                        else:
                            text_ = ''
                    except Exception as e:
                        # print_exception_msg('text_, ' + str(e))
                        pass
                    try:
                        ods_ = el.findall('./deal_data/subject/share_subject_description/ods_description')[0].text
                    except Exception as e:
                        # print_exception_msg('ods_, ' + str(e))
                        pass
                    row = [house_, type_, flat_, floor_, area_, text_, ods_, name_, doc_, date_]
                    self.add_row_info(row, self.ddu_list, 'ddu')

        self.ddu_list.insert(0, HEADER_MAP_DDU)

        els = root.findall('./restrict_records/restrict_record')
        print(len(els))

        for el in els:
            doc_, date_, name_, right_ = '', '', '', ''
            doc_date = None
            try:
                date_ = el.findall('./underlying_documents/underlying_document/document_date')[0].text
                y, m, d = date_.split('-')
                doc_date = QDate(int(y), int(m), int(d))
                # date_ = datetime(int(y), int(m), int(d))
                date_ = f"{int(d)}.{int(m)}.{int(y)}"
            except Exception as e:
                # print_exception_msg('date_, ' + str(e))
                pass
            if doc_date and start_date <= doc_date <= end_date:
                try:
                    doc_ = el.findall('./underlying_documents/underlying_document/document_number')[0].text
                except Exception as e:
                    # print_exception_msg('doc_, ' + str(e))
                    pass
                try:
                    name_ = el.findall('./underlying_documents/underlying_document/document_name')[0].text
                except Exception as e:
                    # print_exception_msg('name_, ' + str(e))
                    pass
                try:
                    right_ = el.findall('./right_holders/right_holder/legal_entity/entity/resident/name')[0].text
                except Exception as e:
                    # print_exception_msg('right_, ' + str(e))
                    pass

                row = [right_, name_, doc_, date_]
                self.add_row_info(row, self.i_list, 'ipoteka')

        self.i_list.insert(0, HEADER_MAP_I)

        data = {
            'дду': self.ddu_list,
            'ипотека': self.i_list
        }
        save_xlsx_sheets(data, file_name=file_name, folder=None, auto_start=True)
