# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/diary.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 533)
        MainWindow.setStyleSheet("QLabel {\n"
"    border: 7px solid rgba(0, 0, 0, 0.02);\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"    text-transform: uppercase;\n"
"    color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"QMessageBox {\n"
"    background-color: rgb(97, 0, 97);\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"    border: none;\n"
"    font-size: 28px;\n"
"    font-style: normal;\n"
"    color: white;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background-color: rgb(97, 0, 97);\n"
"}\n"
"\n"
"QTextEdit, QLineEdit {\n"
"    background-color: rgb(97, 68, 97);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: pink;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QDialog QListView{\n"
"    background-color: rgb(97, 0, 97);\n"
"    color: rgb(203, 251, 255);\n"
"    padding-left: 7px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 12, 71, 41))
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.title_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.title_edit.setGeometry(QtCore.QRect(90, 20, 481, 31))
        self.title_edit.setObjectName("title_edit")
        self.main_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.main_edit.setGeometry(QtCore.QRect(10, 60, 561, 391))
        self.main_edit.setObjectName("main_edit")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(490, 460, 80, 23))
        self.save_button.setStyleSheet("text-transform: uppercase;\n"
"font-weight: 600;\n"
"border-radius: 10px;\n"
"border: 0.7px solid yellow;\n"
"color: rgb(217, 103, 255);\n"
"")
        self.save_button.setObjectName("save_button")
        self.lucid_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.lucid_checkbox.setGeometry(QtCore.QRect(10, 460, 181, 21))
        self.lucid_checkbox.setObjectName("lucid_checkbox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 20))
        self.menubar.setObjectName("menubar")
        self.menuNote = QtWidgets.QMenu(self.menubar)
        self.menuNote.setObjectName("menuNote")
        MainWindow.setMenuBar(self.menubar)
        self.actionSelect = QtWidgets.QAction(MainWindow)
        self.actionSelect.setObjectName("actionSelect")
        self.actionCreate = QtWidgets.QAction(MainWindow)
        self.actionCreate.setObjectName("actionCreate")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuNote.addAction(self.actionNew)
        self.menuNote.addAction(self.actionSelect)
        self.menuNote.addAction(self.actionDelete)
        self.menuNote.addSeparator()
        self.menuNote.addAction(self.actionClose)
        self.menubar.addAction(self.menuNote.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Title:"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.lucid_checkbox.setText(_translate("MainWindow", "Is dream lucid?"))
        self.menuNote.setTitle(_translate("MainWindow", "Note"))
        self.actionSelect.setText(_translate("MainWindow", "Select"))
        self.actionCreate.setText(_translate("MainWindow", "Create"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionClose.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
