from audioop import add
import email
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ("Arial", 12, "bold")
FILE_SAVES = 'Day29/passwords.json'
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":username,
            "password":password
        }
    }
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            with open(FILE_SAVES, mode='r') as password_file:
                #json.dump(new_data, password_file, indent=4)
                data = json.load(password_file)
        except json.decoder.JSONDecodeError:
            data = {}
            pass
        except FileNotFoundError:
            with open(FILE_SAVES, mode='w') as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            with open(FILE_SAVES, mode='w') as password_file:
                data.update(new_data)
                print(data)
                json.dump(data, password_file, indent=4)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #
def search():
    try:
        with open(FILE_SAVES, mode='r') as password_file:
            data = json.load(password_file)
            password = data[website_entry.get()]["password"]
            username = data[website_entry.get()]["email"]
            password_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.insert(0,password)
            username_entry.insert(0,username)
    except FileNotFoundError:
        pass
    except IndexError:
        pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='Day29/logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


website_lbl = Label(text="Website:", font=FONT)
website_lbl.grid(row=1, column=0)
username_lbl = Label(text="Email/Username:", font=FONT)
username_lbl.grid(row=2, column=0)
password_lbl = Label(text="Password:", font=FONT)
password_lbl.grid(row=3, column=0)


website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
username_entry = Entry(width=50)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "franperezfolgado@outlook.com")
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

search_btn = Button(text='Search', width=15, command=search)
search_btn.grid(row=1, column=2)

generate_pass_btn = Button(text='Generate Password',
                           width=15, command=generate_password)
generate_pass_btn.grid(row=3, column=2)
add_btn = Button(text='Add', width=40, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()