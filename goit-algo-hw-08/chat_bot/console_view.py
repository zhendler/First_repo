from user_view import UserView


class ConsoleView(UserView):

	def display_massage(self, message):
		print(message)

	def get_input(self, prompt):
		return input(prompt)
	
	def display_contacts(self, contacts):
		for contact in contacts.values():
			print(contact)

	def display_contact(self, contact):
		print(contact)

	def display_help(self):
		print("""
		Available commands:
		- add [name] [phone number]: Add a new contact or phone number
		- change [name] [old phone number] [new phone number]: Change the phone number of a contact
		- show [name]: Show details of a contact
		- all: Show all contacts
		- add-birthday [name] [date of birth]: Add a birthday to a contact
		- show-birthday [name]: Show the birthday of a contact
		- birthdays: Show upcoming birthdays
		- exit: Exit the application
		""")

