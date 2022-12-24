import datetime
from peewee import *


database = SqliteDatabase('db/notes.db')


class Note(Model):
	id = IntegerField(primary_key=True)
	title = TextField()
	main_text = TextField()
	lucid = BooleanField()
	dream_date = DateField(default=datetime.datetime.now)
	changed_date = DateTimeField(default=datetime.datetime.now)

	

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

def new_note(title, main_text, lucid, dream_date):
	result = Note.insert(
		title=title,
		main_text=main_text,
		lucid=lucid,
		dream_date=dream_date,
		changed_date=datetime.datetime.now()
	).execute()

	return result

def delete_by_id_note(note_id):
	result = Note.delete().where(Note.id == note_id).execute()

def update_note(note_id, title, main_text, islucid, dream_date):
	Note.update(
		title=title,
		main_text=main_text,
		lucid=islucid,
		dream_date=dream_date,
		changed_date=datetime.datetime.now()

	).where(Note.id == note_id).execute()