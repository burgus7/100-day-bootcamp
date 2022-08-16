from tkinter import *

window = Tk()
window.title('Miles to Km Converter')
window.minsize(300, 200)
window.config(padx=40, pady=40)

txt = Label(text="is equal to")
txt.grid(column=1, row=2)
txt.config(padx=20)

mi_txt = Label(text="miles")
mi_txt.grid(column=3, row=1)
mi_txt.config(padx=20)

km_txt = Label(text="kilometers")
km_txt.grid(column=3, row=2)
km_txt.config(padx=20)

km_val_txt = Label(text="0")
km_val_txt.grid(column=2, row=2)
km_val_txt.config(padx=20)

def calculate():
    in_val = int(mi_input.get())
    out_val = in_val * 1.609
    km_val_txt.config(text=out_val)

button = Button(text='Calculate',command=calculate)
button.grid(column=2, row=3)

mi_str = "0"
mi_input = Entry(width=20)
mi_input.insert(END, string=mi_str)
mi_input.grid(column=2, row=1)




window.mainloop()