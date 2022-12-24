import datetime
from peewee import *


database = SqliteDatabase('db/notes.db')


class Note(Model):
	id = IntegerField(primary_key=True)
	title = TextField()
	main_text = TextField()
	changed_date = DateTimeField(default=datetime.datetime.now)
	lucid = BooleanField()

	class Meta:
		database = database
		order_by = id


def create_note_table():
	database.create_tables([Note])

def get_by_id_note(note_id):
	result = Note.select().where(Note.id == note_id).get()

	return result

def get_all_note():
	return [note for note in Note.select()]

def new_note(title, main_text, lucid):
	result = Note.insert(title=title, main_text=main_text, lucid=lucid).execute()
	return result

def delete_by_id_note(note_id):
	result = Note.delete().where(Note.id == note_id).execute()

def update_note(note_id, title, main_text, islucid):
	Note.update(title=title, main_text=main_text, lucid=islucid).where(Note.id == note_id).execute()