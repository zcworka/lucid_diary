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
        MainWindow.resize(600, 600)
        MainWindow.setStyleSheet("QLabel {\n"
"    border: 1px solid black;\n"
"    padding: 3px;\n"
"    border-radius: 5px;\n"
"    font-style: italic;\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"    border: none;\n"
"    font-size: 34px;\n"
"    font-style: normal;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.title_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.title_edit.setGeometry(QtCore.QRect(90, 20, 481, 31))
        self.title_edit.setObjectName("title_edit")
        self.main_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.main_edit.setGeometry(QtCore.QRect(10, 60, 561, 391))
        self.main_edit.setObjectName("main_edit")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(490, 460, 80, 23))
        self.save_button.setObjectName("save_button")
        self.lucid_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.lucid_checkbox.setGeometry(QtCore.QRect(10, 460, 131, 21))
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
        self.menuNote.addAction(self.actionSelect)
        self.menubar.addAction(self.menuNote.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Title"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.lucid_checkbox.setText(_translate("MainWindow", "Is dream lucid?"))
        self.menuNote.setTitle(_translate("MainWindow", "Note"))
        self.actionSelect.setText(_translate("MainWindow", "Select"))
        self.actionCreate.setText(_translate("MainWindow", "Create"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
