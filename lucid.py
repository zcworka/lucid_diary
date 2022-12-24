import datetime
from gui.diary import *
from db_driver import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QListView, QMessageBox, QShortcut, QDialogButtonBox, QVBoxLayout, QLabel
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import pyqtSlot, QDate
from re import match

def do_nothing():
    pass


def show_message(root, title, text, message_type):
    message = QMessageBox(root)
    message.setWindowTitle(title)
    message.setText(text)

    if message_type == "Okay":
        message.setStandardButtons(QMessageBox.Ok)
        message.show()

class ConrifmDialog(QDialog):
    def __init__(self, text, title='Confirmation'):

        super().__init__()

        self.title = title
        self.text = text

        self.setWindowTitle(self.title)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel(self.text)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)




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

        self.dateEdit.setDate(datetime.datetime.now().date())

        self.actionNew.triggered.connect(lambda: self.new_action())
        self.actionNew.setShortcut(QKeySequence("Ctrl+N"))

        self.actionDelete.triggered.connect(lambda: self.delete_action())

        self.actionClose.triggered.connect(lambda: self.close_action())
        self.actionClose.setShortcut(QKeySequence("Ctrl+Q"))


        self.save_button.clicked.connect(lambda: self.save_button_event())
        self.save_button.setEnabled(False)

        self.lock()

        # comfort
        self.setLucidSC = QShortcut(QKeySequence('Ctrl+L'), self)
        self.setLucidSC.activated.connect(
            lambda: \
            (
                self.lucid_checkbox.setChecked(True) \
                if not self.lucid_checkbox.isChecked() \
                else self.lucid_checkbox.setChecked(False)) \
            if self.lucid_checkbox.isEnabled() else do_nothing() 
            ) # is this absolute shit code? 

        self.testSC = QShortcut(QKeySequence('Ctrl+Z'), self)
        self.testSC.activated.connect(lambda: self.testing())

    def testing(self):
        print()
    

    def lock(self):
        self.title_edit.setText("")
        self.main_edit.setText("")
        self.lucid_checkbox.setChecked(False)
        self.dateEdit.setDate(datetime.datetime.strptime('01.01.2000', '%d.%m.%Y').date())

        self.title_edit.setEnabled(False)
        self.main_edit.setEnabled(False)
        self.lucid_checkbox.setEnabled(False)
        self.save_button.setEnabled(False)
        self.dateEdit.setEnabled(False)

    def unlock(self):
        self.title_edit.setEnabled(True)
        self.main_edit.setEnabled(True)
        self.lucid_checkbox.setEnabled(True)
        self.save_button.setEnabled(True)
        self.dateEdit.setEnabled(True)

    def is_locked(self):
        return not all([
                self.main_edit.isEnabled(),
                self.title_edit.isEnabled(),
                self.lucid_checkbox.isEnabled(),
                self.save_button.isEnabled()
        ])


    def save_button_event(self):
        title = self.title_edit.text()
        text = self.main_edit.toPlainText()
        islucid = self.lucid_checkbox.isChecked()
        dream_date = datetime.datetime.strptime(self.dateEdit.text(), '%d.%m.%Y').date()

        if self.note == "New":
            current_note_id = new_note(title, text, islucid, dream_date)
            self.note = get_by_id_note(current_note_id)
            show_message(self, "Successfull", "Note is saved!", "Okay")
            return
        else:
            update_note(self.note.id, title, text, islucid, dream_date)
            show_message(self, "Successfull", "Note is saved!", "Okay")  
            return

    def new_action(self):
        self.note = "New"

        self.title_edit.setText("")
        self.main_edit.setText("")
        self.lucid_checkbox.setChecked(False)
        self.dateEdit.setDate(datetime.datetime.now().date())

        self.save_button.setEnabled(True)
        self.unlock()

    def select_action(self):

        def select_button_click():
            item_index = notes_listview.currentIndex()

            if not item_index.data():
                if ConrifmDialog('Create new note?').exec():
                    self.new_action()
                    select_dlg.close()
                return

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

            self.dateEdit.setDate(self.note.dream_date)

            self.unlock()


        select_dlg = QDialog(self)
        select_dlg.setWindowTitle('Select dream title')

        notes_listview = QListView(select_dlg)
        notes_model = QtGui.QStandardItemModel()
        notes_listview.setModel(notes_model)

        for note in get_all_note()[::-1]:
            item = QtGui.QStandardItem(f"Title: {note.title}        {'Lucid' if note.lucid == True else ''}")
            notes_model.appendRow(item)
            self.notes_buffer[item.index()] = note.id


        select_button = QPushButton(select_dlg)
        select_button.setGeometry(175, 150, 80, 40)
        select_button.setText("Select")
        select_button.clicked.connect(lambda: select_button_click())

        select_dlg.show()

    def delete_action(self):
        if not self.is_locked():
            if ConrifmDialog('Are you sure you want to delete this note?').exec():
                delete_by_id_note(self.note.id)
                self.lock()
            return
        show_message(self, 'Warning', 'First select note', 'Okay')

    def close_action(self):
        if not self.is_locked():
            if ConrifmDialog('Are you sure you want to close?\nAll changes will be discarded').exec():
                self.lock()    
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Root()
    sys.exit(app.exec_())