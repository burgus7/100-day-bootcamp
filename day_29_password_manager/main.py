from tkinter import *
from tkinter import messagebox
from random import sample, shuffle, randint
import pyperclip

WHITE = "#ffffff"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    chosen_letters = sample(letters, nr_letters)
    chosen_symbols = sample(symbols, nr_symbols)
    chosen_numbers = sample(numbers, nr_numbers)

    gen_pass_list = chosen_letters + chosen_numbers + chosen_symbols
    shuffle(gen_pass_list)

    gen_pass = ''.join(gen_pass_list)

    password_entry.delete(0, END)
    password_entry.insert(0, gen_pass)
    pyperclip.copy(gen_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:"
                                                      f"\n\tEmail: {email}"
                                                      f"\n\tPassword: {password}"
                                                      f"\nIs it okay to save? ")

        if is_ok:
            with open ("passwords.txt", "a") as file:
                print(website_entry.get())
                file.write(f"\n{website} | {email} | {password}")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=WHITE)
window.title("Password Manager")

canvas = Canvas(width=204, height=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img) # 100 100 is x and y pos of center of image
canvas.grid(column=1, row=0)

# Website Row
website_text = Label(text="Website:", bg=WHITE)
website_text.grid(column=0, row=1)

website_entry = Entry(width=54)
website_entry.grid(column=1, columnspan=2, row=1)

# Email/Username Row
email_text = Label(text="Email/Username:", bg=WHITE)
email_text.grid(column=0, row=2)

email_entry = Entry(width=54)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0, "shweta.burgula@gmail.com")

# Password Row
password_text = Label(text="Password:", bg=WHITE)
password_text.grid(column=0, row=3)

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

# Buttons
gen_password_btn = Button(text="Generate Password", command=generate_password)
gen_password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", command=save_password, width=46, highlightthickness=0)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()