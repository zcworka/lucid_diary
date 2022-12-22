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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
