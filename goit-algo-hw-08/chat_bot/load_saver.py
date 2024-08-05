import pickle
from addressbook import AddressBook	
from pathlib import Path
RECORDS_FILE_PATH = Path() / "goit-algo-hw-08/chat_bot/addressbook.pkl"


def save_data(book):
	with open(RECORDS_FILE_PATH, "wb") as f:
		pickle.dump(book,f)


def load_data():
	try:
		with open(RECORDS_FILE_PATH, "rb") as f:
			return pickle.load(f)
	except FileNotFoundError:
		return AddressBook()
