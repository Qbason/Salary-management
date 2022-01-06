from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Salary-managment")
root.geometry("480x640")

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)

my_frame1 = Frame(my_notebook, width=500, height=500, bg="green")
my_frame2 = Frame(my_notebook, width=500, height=500, bg="pink")

my_frame1.pack(fill="both",expand=1)
my_frame2.pack(fill="both",expand=1)

my_notebook.add(my_frame1, text="Tab1")
my_notebook.add(my_frame2, text="Tab2")

root.mainloop()