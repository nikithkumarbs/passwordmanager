from  tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

def password_generator():

    alphabate = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z",
                 "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]

    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "[", "]", "{", "}", "|", ":", ";",
               "<", ">", ".", "/", "?", "~", "`", "", ",", ".", "/", "?", ";", ":"]

    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    # accepting inputs from users and storing in variables
    no_of_letters = randint(8, 10)
    no_of_symbols = randint(2, 4)
    no_of_numbers = randint(2, 4)

    generated_password = [choice(alphabate) for _ in range(0, no_of_letters)]
    generated_password += [choice(symbols) for _ in range(0, no_of_symbols)]
    generated_password += [choice(numbers) for _ in range(0, no_of_numbers)]

    # shuffling list
    shuffle(generated_password)

    # converting list item to string
    generated_password = "".join(generated_password)

    password_entry.delete(0,END)
    password_entry.insert(0,string=f"{generated_password}")
    pyperclip.copy(text=f"{generated_password}")

def entry_field_check():

    if website_entry.get() == "":
        messagebox.showinfo("website", "website name is missing")
        website_entry.focus()
        return False
    if password_entry.get() == "":
        messagebox.showinfo("password", "website password is missing")
        password_entry.focus()
        return False
    if email_entry.get() == "":
        messagebox.showinfo("email", "website email is missing")
        email_entry.focus()
        return False

    return True

def evaluate_email():
    gmail = email_entry.get()
    if "@gmail.com" in gmail or "@outlook.com" in gmail:
        return True
    messagebox.showinfo("message", "invalid email ")
    email_entry.focus()

def delete_entries():

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()

def password_manager():

        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        if entry_field_check():

            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                                     f"Email:{email}\nPassword:{password}\n"
                                                                     f"Is it ok to save?")
            if is_ok:

                # saving password to file
                with open(file="passwords.txt",mode="a") as file:
                    file.write(f"website:{website} | email:{email} "
                               f"| password:{password}\n")
                messagebox.showinfo("message", "password saved succesfully!...")

                delete_entries()

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="password.png")

canvas.create_image(100,100,image=image)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0,row=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

website_entry = Entry(width=56, borderwidth=0, relief="ridge", border=2)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=56,borderwidth=0,relief="ridge",border=2)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0,string="sundarnikith@gmail.com")
password_entry = Entry(width=38,borderwidth=0,relief="ridge",border=2)
password_entry.grid(row=3,column=1)

generate_password_btn = Button(text="Generate Password",relief="ridge",highlightthickness=0,command=password_generator)
generate_password_btn.grid(row=3,column=2)
add_btn = Button(text="Add",width=48,relief="ridge",highlightthickness=0,command=password_manager)
add_btn.grid(row=4,column=1,columnspan=2)

window.mainloop()
