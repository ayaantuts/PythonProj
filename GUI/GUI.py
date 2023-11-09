import tkinter
import mysql.connector

# Connect to database
def connect_db():
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="root",
		database="Library"
	)
	return mydb

def display_books(mydb):
	mycursor = mydb.cursor()
	mycursor.execute("select * from Books")
	myresult = mycursor.fetchall()
	return myresult

# Create window
def frame1():
	window = tkinter.Tk()
	window.title("Library")
	database = connect_db()
	books = display_books(database)
	
	# Create label
	label = tkinter.Label(window, text="Library", font=("Arial Bold", 20))
	label.grid(column=0, row=0)
	
	# Show books 10 at a time
	for i in range(10):
		book = tkinter.Label(window, text=books[i])
		book.grid(column=0, row=i+1)
	
	# Pagination
	# Create label
	label = tkinter.Label(window, text="Page 1", font=("Arial Bold", 20))
	label.grid(column=0, row=11)
	
	# Create button
	button = tkinter.Button(window, text="Add book", command=frame2)
	window.mainloop()

def frame2():
	pass

frame1()