from gui.diary import *
from db_driver import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QListView
from re import match



class Root(QtWidgets.QMainWindow ,Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        Root.show(self)
        self.screen_size = QApplication.primaryScreen().size()

        self.actionSelect.triggered.connect(lambda: self.select_action())

    def select_action(self):

        def select_button_click():
            item_index = notes_listview.currentIndex()
            note_item = notes_model.itemFromIndex(item_index).text()
            note_id = match(r'\d+', note_item).group()
            note_title = note_item.replace(f"{note_id}: ", "")

            self.note = get_by_id_note(int(note_id))
            select_dlg.close()
            


        select_dlg = QDialog(self)
        select_dlg.setWindowTitle('Select dream title')
        select_dlg.setGeometry(0, 0, self.geometry().width(), self.geometry().height())

        

        notes_listview = QListView(select_dlg)
        notes_model = QtGui.QStandardItemModel()
        notes_listview.setModel(notes_model)

        for note in get_all_note():
            item = QtGui.QStandardItem(f"{note.id}: {note.title}")
            notes_model.appendRow(item)


        select_button = QPushButton(select_dlg)
        select_button.setGeometry(175, 150, 80, 40)
        select_button.setText("Select")
        select_button.clicked.connect(lambda: select_button_click())

        select_dlg.exec()







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Root()
    sys.exit(app.exec_())