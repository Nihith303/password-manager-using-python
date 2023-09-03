from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy
import json


# ----------------------------      Search      ---------------------------------#
def search():
    wed = website.get()
    try:
        with open("Nihilistic.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="There is no file existing to search\nFirst create a file.")
    else:
        if wed in data:
            email = data[wed]["email"]
            password1 = data[wed]["password"]
            copy(password1)
            messagebox.showinfo(title="Password Data", message=f"Email:{email}\nPassword:{password1}")
        else:
            messagebox.showinfo(title="Oops!", message=f"There are No Details saved for {wed} Website")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    Password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_char = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_symbols+password_char+password_numbers

    shuffle(password_list)
    password = ''.join(password_list)
    Password.insert(0, password)
    copy(password)


# ---------------------------- SAVE PASSWORD ----------------------------#
def Save():
    wed = website.get()
    em = username.get()
    pa = Password.get()
    new_dict = {wed: {"email": em, "password": pa}}
    if len(wed) == 0 or len(pa) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        ok = messagebox.askokcancel(title="Info box", message=f"Website:{wed}\nPassword:{pa}\nEmail:{em}\n is it ok?")
        if ok:
            try:
                with open("Nihilistic.json", "r") as f:
                    # Reading old data.
                    data = json.load(f)
            except FileNotFoundError:
                with open("Nihilistic.json", "w") as f:
                    json.dump(new_dict, f, indent=4)
            else:
                # Updating Json files old data.
                data.update(new_dict)
                with open("Nihilistic.json", "w") as f:
                    # Writing to Json File updated data.
                    json.dump(data, f, indent=4)
            finally:
                website.delete(0, END)
                Password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

window.config(padx=40, pady=40)
# Entry of Website.
label1 = Label(text="Website:")
label1.grid(row=1, column=0)
website = Entry(width=26)
website.grid(row=1, column=1)
website.focus()

# Search button.
Search = Button(text="Search", width=12, command=search)
Search.grid(row=1, column=2)

# Entry of Username.
label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)
username = Entry(width=44)
username.grid(row=2, column=1, columnspan=2)
username.insert(0, "jonnalagaddanihith@gmail.com")

# Entry of Password.
label3 = Label(text="Password:")
label3.grid(row=3, column=0)
Password = Entry(width=26)
Password.grid(row=3, column=1)

# Password Generator Button.
passwordgenerator = Button(text="Generate Password", command=generate_password)
passwordgenerator.grid(row=3, column=2)
Add = Button(text="Add", width=36, command=Save)
Add.grid(row=5, column=1, columnspan=2)

# Inserting the lock PNG.
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

window.mainloop()
