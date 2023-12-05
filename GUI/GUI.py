import tkinter as tk
import mysql.connector as m

(WIDTH, HEIGHT) = (500, 500)

root = tk.Tk()
root.title("Events Management System")
root.geometry("600x600")

small_font = ("Montserrat", 10)
font = ("Montserrat", 14)
heading_font = ("Montserrat", 18)
button_bg = "#4CAF50"
button_fg = "#FFFFFF"
text = "#212121"

def destroy():
	for i in root.winfo_children():
		i.destroy()

def connect_db():
	db = m.connect(
		host="localhost",
		user="root",
		passwd="root",
		database="Events"
	)
	return db

def select_db(attr = "*"):
	db = connect_db()
	cursor = db.cursor()
	cursor.execute("SELECT {attr} FROM Events".format(attr=attr))
	result = cursor.fetchall()
	return result

def insert_db(title, description, date, fees):
	db = connect_db()
	cursor = db.cursor()
	cursor.execute("INSERT INTO Events (title, description, date, fees) VALUES (%s, %s, %s, %s)", (title, description, date, fees))
	db.commit()
	print(cursor.rowcount, "record(s) inserted.")

def update_db(price, id):
	db = connect_db()
	cursor = db.cursor()
	cursor.execute("UPDATE Events SET fees = %s WHERE id = %s", (price, id))
	db.commit()
	print(cursor.rowcount, "record(s) updated.")

def delete_db(id):
	db = connect_db()
	cursor = db.cursor()
	cursor.execute("DELETE FROM Events WHERE id = %s", (id,))
	db.commit()
	print(cursor.rowcount, "record(s) deleted.")

def checkNewEvent(title, description, date, fees):
	if title and description and date and fees:
		insert_db(title, description, date, fees)
	else:
		print("Please fill all the fields")

def checkUpdateEvent(price, id):
	if price:
		update_db(price, id)
	else:
		print("Please fill all the fields")

def updateEvent():
	destroy()
	updateEvent_frame = tk.Frame(root, width=WIDTH, height=HEIGHT)
	updateEvent_frame.pack()

	# Ids of Events
	event_details = select_db("id, title")
	for event in event_details:
		(id, title) = event
		# Id
		event_id = tk.Label(updateEvent_frame, text=id, font=small_font)
		event_id.grid(row=id, column=0)

		# Title
		event_title = tk.Label(updateEvent_frame, text=title, font=small_font)
		event_title.grid(row=id, column=1)

	# Form
	form = tk.Frame(updateEvent_frame)
	form.grid(padx=10, pady=10, columnspan=2)

	# Id
	id_label = tk.Label(form, text="Enter Id: ", font=font)
	id_label.grid(row=0, column=0, sticky=tk.E)

	id_entry = tk.Entry(form, font=font)
	id_entry.grid(row=0, column=1, sticky=tk.E)

	# Price
	price_label = tk.Label(form, text="Enter new Price: ", font=font)
	price_label.grid(row=1, column=0, sticky=tk.E)

	price_entry = tk.Entry(form, font=font)
	price_entry.grid(row=1, column=1, sticky=tk.E)

	# Buttons
	btn_update = tk.Button(updateEvent_frame, text="Update", font=font, bg=button_bg, fg=button_fg, command=lambda: checkUpdateEvent(price_entry.get(), id_entry.get()))
	btn_update.grid(columnspan=2, padx=10, pady=10, ipadx=10, ipady=10)

	btn_back = tk.Button(updateEvent_frame, text="Back", font=font, bg=button_bg, fg=button_fg, command=landing_page)
	btn_back.grid(columnspan=2, padx=10, pady=10, ipadx=10, ipady=10)

def showEvent():
	destroy()
	# Show Event
	show_frame = tk.Frame(root, width=WIDTH, height=HEIGHT)
	show_frame.pack()

	# Title
	title = tk.Label(show_frame, text="Events", font=heading_font)
	title.pack(padx=10, pady=10)
	
	# Event Card
	events = select_db()
	for event in events:
		(id, title, description, date, fees) = event
		event_card = tk.Frame(show_frame, width=WIDTH, height=HEIGHT, bd=1, relief=tk.SOLID)
		event_card.pack(padx=10, pady=10, ipadx=10, ipady=10)

		# Title
		event_title = tk.Label(event_card, text=title, font=font)
		event_title.pack(anchor=tk.W)

		# Description
		event_description = tk.Label(event_card, text=description, font=font)
		event_description.pack(side=tk.LEFT, )

		# Date
		event_date = tk.Label(event_card, text=date, font=font)
		event_date.pack(side=tk.LEFT, )

		event_fees_label = tk.Label(event_card, text="Fees: ", font=font)
		event_fees_label.pack(side=tk.LEFT)

		# Fees
		event_fees = tk.Label(event_card, text=fees, font=font)
		event_fees.pack(side=tk.LEFT)

	# Buttons
	btn_back = tk.Button(show_frame, text="Back", font=font, bg=button_bg, fg=button_fg, command=landing_page)
	btn_back.pack(padx=10, pady=10, ipadx=10, ipady=10)

def newEvent():
	destroy()
	newEvent_frame = tk.Frame(root, width=WIDTH, height=HEIGHT)
	newEvent_frame.pack()

	# Title
	title = tk.Label(newEvent_frame, text="Add a new Event", font=heading_font)
	title.pack(padx=10, pady=10)

	# Form
	form = tk.Frame(newEvent_frame)
	form.pack(padx=10, pady=10)

	# Title
	title_label = tk.Label(form, text="Title: ", font=font)
	title_label.grid(row=0, column=0, sticky=tk.E)

	title_entry = tk.Entry(form, font=font)
	title_entry.grid(row=0, column=1, sticky=tk.E)

	# Description
	description_label = tk.Label(form, text="Description: ", font=font)
	description_label.grid(row=1, column=0, sticky=tk.E)

	description_entry = tk.Entry(form, font=font)
	description_entry.grid(row=1, column=1, sticky=tk.E)

	# Date
	date_label = tk.Label(form, text="Date: ", font=font)
	date_label.grid(row=2, column=0, sticky=tk.E)

	date_entry = tk.Entry(form, font=font)
	date_entry.grid(row=2, column=1, sticky=tk.E)

	# Fees
	fees_label = tk.Label(form, text="Fees: ", font=font)
	fees_label.grid(row=3, column=0, sticky=tk.E)

	fees_entry = tk.Entry(form, font=font)
	fees_entry.grid(row=3, column=1, sticky=tk.E)

	# Buttons
	btn_add = tk.Button(newEvent_frame, text="Add", font=font, bg=button_bg, fg=button_fg, command=lambda: checkNewEvent(title_entry.get(), description_entry.get(), date_entry.get(), fees_entry.get()))
	btn_add.pack(padx=10, pady=10, ipadx=10, ipady=10)

	btn_back = tk.Button(newEvent_frame, text="Back", font=font, bg=button_bg, fg=button_fg, command=landing_page)
	btn_back.pack(padx=10, pady=10, ipadx=10, ipady=10)

def deleteEvent():
	destroy()
	deleteEvent_frame = tk.Frame(root, width=WIDTH, height=HEIGHT)
	deleteEvent_frame.pack()

	# Ids of Events
	event_details = select_db("id, title")
	for event in event_details:
		(id, title) = event
		# Id
		event_id = tk.Label(deleteEvent_frame, text=id, font=small_font)
		event_id.grid(row=id, column=0)

		# Title
		event_title = tk.Label(deleteEvent_frame, text=title, font=small_font)
		event_title.grid(row=id, column=1)

	# Title
	title = tk.Label(deleteEvent_frame, text="Delete an Event", font=heading_font)
	title.grid(columnspan=2, padx=10, pady=10)

	# Form
	form = tk.Frame(deleteEvent_frame)
	form.grid(columnspan=2, padx=10, pady=10)

	# Id
	id_label = tk.Label(form, text="Enter Id: ", font=font)
	id_label.grid(columnspan=2, row=0, column=0)

	id_entry = tk.Entry(form, font=font)
	id_entry.grid(columnspan=2, row=0, column=2)

	# Buttons
	btn_delete = tk.Button(deleteEvent_frame, text="Delete", font=font, bg=button_bg, fg=button_fg, command=lambda: delete_db(id_entry.get()))
	btn_delete.grid(columnspan=2, padx=10, pady=10, ipadx=10, ipady=10)

	btn_back = tk.Button(deleteEvent_frame, text="Back", font=font, bg=button_bg, fg=button_fg, command=landing_page)
	btn_back.grid(columnspan=2, padx=10, pady=10, ipadx=10, ipady=10)

def landing_page():
	destroy()
	# Landing Page
	landing_frame = tk.Frame(root)
	landing_frame.pack()

	# Title
	title = tk.Label(landing_frame, text="Events Management System", font=heading_font)
	title.pack(padx=10, pady=10)

	# Buttons
	btn_select = tk.Button(landing_frame, text="Select", font=font, bg=button_bg, fg=button_fg, command=showEvent)
	btn_select.pack(padx=10, pady=10, ipadx=10, ipady=10)

	btn_insert = tk.Button(landing_frame, text="Insert", font=font, bg=button_bg, fg=button_fg, command=newEvent)
	btn_insert.pack(padx=10, pady=10, ipadx=10, ipady=10)

	btn_update = tk.Button(landing_frame, text="Update", font=font, bg=button_bg, fg=button_fg, command=updateEvent)
	btn_update.pack(padx=10, pady=10, ipadx=10, ipady=10)

	btn_delete = tk.Button(landing_frame, text="Delete", font=font, bg=button_bg, fg=button_fg, command=deleteEvent)
	btn_delete.pack(padx=10, pady=10, ipadx=10, ipady=10)

	# Footer
	footer = tk.Label(landing_frame, text="Developed by: Ayaan and Aldrin", font=font)
	footer.pack(side=tk.BOTTOM, padx=10, pady=10)

landing_page()
root.mainloop()