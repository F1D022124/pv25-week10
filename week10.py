# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'week1-.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import sqlite3

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(406, 331)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 411, 331))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 170, 381, 91))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Judul", "Pengarang", "Tahun"])
        self.tableWidget.setRowCount(0)
        # Agar bisa edit sel table langsung (untuk update data)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)

        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(70, 20, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(60, 80, 47, 13))
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 50, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 140, 381, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(160, 110, 75, 23))
        self.pushButton.setStyleSheet("background-color: #A9A9A9; color: black; border-radius: 5px;")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 270, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: #ffff00; color: black; border-radius: 5px;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.label_4.setStyleSheet("color: grey;")
        self.label_4.setObjectName("label_4")

        
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 120, 301, 21))
        self.pushButton_3.setStyleSheet("background-color: #A9A9A9; color: black; border-radius: 5px;")
        self.pushButton_3.setObjectName("pushButton_3")

        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Week 10 - Ida Ayu Vinaya Anindya(F1D022124)"))
        self.label.setText(_translate("Form", "Judul :"))
        self.label_2.setText(_translate("Form", "Pengarang :"))
        self.label_3.setText(_translate("Form", "Tahun :"))
        self.pushButton.setText(_translate("Form", "Simpan"))
        self.pushButton_2.setText(_translate("Form", "Hapus Data"))
        self.label_4.setText(_translate("Form", "Cari judul..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Data Buku"))
        self.pushButton_3.setText(_translate("Form", "Ekspor ke CSV"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Ekspor"))

class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Koneksi database SQLite, buat tabel jika belum ada
        self.conn = sqlite3.connect("buku.db")
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS buku (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            judul TEXT NOT NULL,
            pengarang TEXT NOT NULL,
            tahun TEXT NOT NULL
        )""")
        self.conn.commit()

        # Load data dari database ke tabel saat aplikasi mulai
        self.load_data()

        # Connect tombol dan event
        self.pushButton.clicked.connect(self.tambah_data)
        self.pushButton_2.clicked.connect(self.hapus_data)
        self.lineEdit_4.textChanged.connect(self.cari_data)
        self.pushButton_3.clicked.connect(self.eksport_csv)
        self.tableWidget.itemChanged.connect(self.edit_data)

    def load_data(self):
        
        self.tableWidget.setRowCount(0)
        self.c.execute("SELECT id, judul, pengarang, tahun FROM buku")
        for row_data in self.c.fetchall():
            id_, judul, pengarang, tahun = row_data
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
           
            item_judul = QtWidgets.QTableWidgetItem(judul)
            item_judul.setData(QtCore.Qt.UserRole, id_)
            self.tableWidget.setItem(rowPosition, 0, item_judul)
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(pengarang))
            self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(tahun))

    def tambah_data(self):
        judul = self.lineEdit.text().strip()
        pengarang = self.lineEdit_2.text().strip()
        tahun = self.lineEdit_3.text().strip()

        if not judul or not pengarang or not tahun:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Semua kolom harus diisi!")
            return

       
        self.c.execute("INSERT INTO buku (judul, pengarang, tahun) VALUES (?, ?, ?)", (judul, pengarang, tahun))
        self.conn.commit()

        
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()

        
        self.load_data()

    def hapus_data(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            item = self.tableWidget.item(selected_row, 0)
            if item:
                id_ = item.data(QtCore.Qt.UserRole)
                if id_:
                    
                    self.c.execute("DELETE FROM buku WHERE id = ?", (id_,))
                    self.conn.commit()
                    self.tableWidget.removeRow(selected_row)
                else:
                    QtWidgets.QMessageBox.warning(self, "Peringatan", "Data tidak valid!")
        else:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Pilih baris data yang akan dihapus!")

    def cari_data(self):
        keyword = self.lineEdit_4.text().strip().lower()
       
        query = "SELECT id, judul, pengarang, tahun FROM buku WHERE LOWER(judul) LIKE ?"
        self.c.execute(query, ('%' + keyword + '%',))
        rows = self.c.fetchall()

        self.tableWidget.setRowCount(0)
        for row_data in rows:
            id_, judul, pengarang, tahun = row_data
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            item_judul = QtWidgets.QTableWidgetItem(judul)
            item_judul.setData(QtCore.Qt.UserRole, id_)
            self.tableWidget.setItem(rowPosition, 0, item_judul)
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(pengarang))
            self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(tahun))

    def eksport_csv(self):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Simpan CSV", "", "CSV Files (*.csv)")
        if path:
            with open(path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                headers = [self.tableWidget.horizontalHeaderItem(col).text() for col in range(self.tableWidget.columnCount())]
                writer.writerow(headers)
                for row in range(self.tableWidget.rowCount()):
                    rowdata = []
                    for col in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, col)
                        rowdata.append(item.text() if item else "")
                    writer.writerow(rowdata)
            QtWidgets.QMessageBox.information(self, "Sukses", "Data berhasil diekspor ke CSV!")

    def edit_data(self, item):
       
        row = item.row()
        col = item.column()
        id_item = self.tableWidget.item(row, 0)
        if id_item:
            id_ = id_item.data(QtCore.Qt.UserRole)
            if id_:
                # Ambil nilai di setiap kolom untuk update
                judul = self.tableWidget.item(row, 0).text()
                pengarang = self.tableWidget.item(row, 1).text() if self.tableWidget.item(row, 1) else ""
                tahun = self.tableWidget.item(row, 2).text() if self.tableWidget.item(row, 2) else ""
                self.c.execute("UPDATE buku SET judul=?, pengarang=?, tahun=? WHERE id=?", (judul, pengarang, tahun, id_))
                self.conn.commit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
