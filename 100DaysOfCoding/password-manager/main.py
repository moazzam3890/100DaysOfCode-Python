from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- Search Data ------------------------------- #


def search_data():
    website = website_entry.get()
    try:
        with open("data_file.json", "r") as data_file:
            data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="There is no such file in DB")
    except KeyError:
        messagebox.showerror(title="Error", message="Please enter correct website")
    else:
        messagebox.showinfo(title=f"{website_entry.get()}", message=f"Email: {email}/n Password: {password}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    passwords = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": passwords,
        }
    }

    if len(website) == 0 or len(passwords) == 0:
        messagebox.showerror(title="OOPS", message="Don't leave any field empty!")
    else:
        is_ok = messagebox.askyesno(title=website, message=f"You have entered \nEmail: {email}\n"
                                                           f"Password: {passwords}\n"
                                                   f"Do you want to proceed")

        if is_ok:
            try:
                with open("data_file.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data_file.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data_file.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

            messagebox.showinfo(title="Congrats!", message="Entered data saved successfully.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=20)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "moaadi3890@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

search_button = Button(text="Search", width=8, command=search_data)
search_button.grid(row=1, column=2)

gen_pass_button = Button(text="Generate Password", width=13, font=("Arial", 9), command=pass_gen)
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
