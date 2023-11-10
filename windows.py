import tkinter 
import random 

names = ["Sarah", "James", "Mike", "Angela", "Chris", "Madeline", "Jorge", "Anna"]
window = tkinter.Tk() 

def random_name():
    generated_name.configure(text="The name is " + random.choice(names))

my_title = tkinter.Label(window, text="Random Name Generator",font="Helvetica 17 italic")
my_title.pack()

my_button = tkinter.Button(window, text="Generate name!", command=random_name) 
my_button.pack()

generated_name = tkinter.Label(window, font="Helvetica 14")
generated_name.pack()

window.mainloop()
