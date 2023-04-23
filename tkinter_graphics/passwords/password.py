import json
import random
from tkinter import *
from tkinter import messagebox

import pyperclip


def search():
    website = entry_website.get()
    try:
        with open("save_pwd.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Search Results", message=f"Email: {email}\nPassword|: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for the {website} exist")


def generate_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    entry_password.delete(first=0, last=END)
    entry_password.insert(index=0, string=password)
    pyperclip.copy(password)


def save_pwd():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    dict_json = {
        website: {
            "email": username,
            "password": password,
        }
    }
    if len(website) > 0 and len(password) > 0:
        try:
            with open(file="save_pwd.json", mode="r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open(file="save_pwd.json", mode="w") as f:
                json.dump(dict_json, f, indent=4)
        else:
            data.update(dict_json)
            with open(file="save_pwd.json", mode="w") as f:
                json.dump(data, f, indent=4)
        finally:
            entry_website.delete(first=0, last=END)
            entry_password.delete(first=0, last=END)
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")


window = Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Password Manager")
canvas = Canvas()
canvas.config(width=200, height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

label_website = Label()
label_website.config(text="Website:", bg="white")
label_website.grid(row=1, column=0)

label_username = Label()
label_username.config(text="Email/Username:", bg="white")
label_username.grid(row=2, column=0)

label_password = Label()
label_password.config(text="Password:", bg="white")
label_password.grid(row=3, column=0)

entry_website = Entry(width=31)
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=2, padx=2, pady=2)

entry_username = Entry(width=50)
entry_username.insert(index=END, string="anuj.nits@gmail.com")
entry_username.grid(row=2, column=1, columnspan=2, padx=2, pady=2)

entry_password = Entry(width=31)
entry_password.grid(row=3, column=1, padx=2, pady=2)

button_search = Button()
button_search.config(text="Search", command=search)
button_search.grid(row=1, column=2, padx=2, pady=2)

button_generate_pwd = Button()
button_generate_pwd.config(text="Generate Password", command=generate_pwd)
button_generate_pwd.grid(row=3, column=2, padx=2, pady=2)

button_add = Button(width=43)
button_add.config(text="Add", command=save_pwd)
button_add.grid(row=4, column=1, columnspan=2, padx=2, pady=2)

window.mainloop()

if __name__ == '__main__':
    print("Start")
