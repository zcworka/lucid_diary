from gui.diary import *
from db_driver import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QListView, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import pyqtSlot
from re import match

def show_message(root, title, text, message_type):
    message = QMessageBox(root)
    message.setWindowTitle(title)
    message.setText(text)

    if message_type == "Okay":
        message.setStandardButtons(QMessageBox.Ok)
        message.show()



class Root(QtWidgets.QMainWindow ,Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        Root.show(self)

        self.current_note_index = None
        self.notes_buffer = {}

        self.screen_size = QApplication.primaryScreen().size()

        self.actionSelect.triggered.connect(lambda: self.select_action())
        self.actionSelect.setShortcut(QKeySequence("Ctrl+O"))

        self.actionNew.triggered.connect(lambda: self.new_action())
        self.actionNew.setShortcut(QKeySequence("Ctrl+N"))

        self.actionDelete.triggered.connect(lambda: self.delete_action())

        self.actionClose.triggered.connect(lambda: self.close_action())


        self.save_button.clicked.connect(lambda: self.save_button_event())
        self.save_button.setEnabled(False)


        self.lock()

    def lock(self):
        self.title_edit.setText("")
        self.main_edit.setText("")
        self.lucid_checkbox.setChecked(False)

        self.title_edit.setEnabled(False)
        self.main_edit.setEnabled(False)
        self.lucid_checkbox.setEnabled(False)
        self.save_button.setEnabled(False)

    def unlock(self):
        self.title_edit.setEnabled(True)
        self.main_edit.setEnabled(True)
        self.lucid_checkbox.setEnabled(True)
        self.save_button.setEnabled(True)


    def save_button_event(self):
        title = self.title_edit.text()
        text = self.main_edit.toPlainText()
        islucid = self.lucid_checkbox.isChecked()

        if self.note == "New":
            current_note_id = new_note(title, text, islucid)
            self.note = get_by_id_note(current_note_id)
            show_message(self, "Successfull", "Note is saved!", "Okay")
            return
        else:
            update_note(self.note.id, title, text, islucid)
            show_message(self, "Successfull", "Note is saved!", "Okay")  
            return

    def new_action(self):
        self.note = "New"

        self.title_edit.setText("")
        self.main_edit.setText("")
        self.lucid_checkbox.setChecked(False)

        self.save_button.setEnabled(True)
        self.unlock()

    def select_action(self):

        def select_button_click():
            item_index = notes_listview.currentIndex()
            note_item = notes_model.itemFromIndex(item_index).text()

            note_id = self.notes_buffer[item_index]

            self.note = get_by_id_note(int(note_id))
            select_dlg.close()
            self.save_button.setEnabled(True)

            self.title_edit.setText(self.note.title)
            self.main_edit.setText(self.note.main_text)

            if self.note.lucid == True:
                self.lucid_checkbox.setChecked(True)
            else:
                self.lucid_checkbox.setChecked(False)

            self.unlock()


        select_dlg = QDialog(self)
        select_dlg.setWindowTitle('Select dream title')

        notes_listview = QListView(select_dlg)
        notes_model = QtGui.QStandardItemModel()
        notes_listview.setModel(notes_model)

        for note in get_all_note():
            item = QtGui.QStandardItem(f"Title: {note.title}        {'Lucid' if note.lucid == True else ''}")
            notes_model.appendRow(item)
            self.notes_buffer[item.index()] = note.id


        select_button = QPushButton(select_dlg)
        select_button.setGeometry(175, 150, 80, 40)
        select_button.setText("Select")
        select_button.clicked.connect(lambda: select_button_click())

        select_dlg.show()

    def delete_action(self):
        delete_by_id_note(self.note.id)
        self.lock()

    def close_action(self):
        self.lock()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Root()
    sys.exit(app.exec_())