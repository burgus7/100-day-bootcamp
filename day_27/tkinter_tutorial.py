from tkinter import *

window = Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# make a label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
#my_label.pack(side="left")
my_label.grid(column=1, row=1)

# change text - two options:
my_label["text"] = "New Text"
my_label.config(text="New Text")

# make a button

def button_clicked():
    print("I got clicked")
    #my_label.config(text="Button Got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)
button = Button(text="I'm a new button", command=button_clicked)
button.grid(column=3, row=1)

# make an entry

input = Entry(width=10)
input.insert(END, string="{email}")
input.grid(column=4, row=3)
print(input.get())

# make a textbox
text = Text(height=5, width=30)
text.focus() # put cursor in box
text.insert(END, "This is an example of a multi-line text entry")
print(text.get("1.0", END)) # Get value in textbox at line 1, character 0
text.grid(column=1, row=4)

# make a spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column=2, row=4)

# make a scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.grid(column=3, row=4)

# make a checkbox
def checkbutton_used():
    #print 1 if checked, 0 if unchecked
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=4, row=4)

# make radiobutton
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=5, row=1)
radiobutton2.grid(column=5, row=2)

# make listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=5, row=3)


window.mainloop()

