#Import the tkinter library
from tkinter import *

#Create an instance of tkinter frame
win = Tk()
win.geometry("700x350")

#Create a Label to print the Name
label= Label(win, text="This is a New Line Text", font= ('Helvetica 14 bold'), foreground= "red3")
label.pack()
win.mainloop()