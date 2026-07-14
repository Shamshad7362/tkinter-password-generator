# ---------------------------- IMPORT ------------------------------- #
import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '&', '*']


def generate_password():
    num = random.choices(numbers, k=4)
    lett_up = random.choices(uppercase_letters, k=4)
    lett_low = random.choices(lowercase_letters, k=4)
    sym = random.choices(symbols, k=4)
    password = num + lett_up + lett_low + sym
    random.shuffle(password)
    final_password = "".join(password)
    pass_ent.delete(0, 'end')
    pass_ent.insert(END, final_password)
    pyperclip.copy(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website_text = website_ent.get()
    email_text = email_ent.get()
    pass_text = pass_ent.get()
    new_data= {
        website_text:{
            'email':email_text,
            'password':pass_text
        }
    }

    if len(website_text)>0 and len(email_text)>0 and len(pass_text)>0:
        is_ok = messagebox.askokcancel(title=website_text,
                                       message=f'These are the details entered: \nEmail: {email_text}\nPassword: {pass_text}\nDo want to save the details?')
        if is_ok:
            try:
                with open(file="password.json", mode='r') as file:
                    data=json.load(file)

            except (FileNotFoundError,json.JSONDecodeError):
                with open(file="password.json", mode='w') as file:
                    json.dump(new_data, file,indent=4)

            else:
                data.update(new_data)
                with open(file="password.json", mode='w') as file:
                    json.dump(data, file,indent=4)
            finally:
                website_ent.delete(0, 'end')
                pass_ent.delete(0, 'end')
    else:
        messagebox.showinfo("Password Manager", "Please enter all details")

# ---------------------------- Search ------------------------------- #
def search():
    website_text=website_ent.get()
    try:
        with open("password.json") as file:
            data = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        messagebox.showinfo("File Error", "You have not any saved details")
    else:
        if website_text in data:
            messagebox.showinfo("Password Details", f"Email : {data[website_text]['email']}\nPassword : {data[website_text]['password']}")
        else:
            messagebox.showinfo("Password Manager", "Website not found")


            # email_ent.insert(index=0, string=website['email'])
            # pass_ent.insert(0, website['password'])
            # messagebox.showinfo("Password Details", f"Website : {website_ent.get()}\nEmail : {email_ent.get()}\nPassword : {pass_ent.get()}")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.geometry("500x500")
window.title("Password Manager")
window.config(bg="#F5F5F7")

my_style = {
    'bd': 0,
    'relief': 'solid',
    'highlightbackground': '#cccccc',
    'highlightthickness': 1,
    'highlightcolor': '#cccccc'
}

font = ('Times New Roman', 15, 'italic')
password_img = PhotoImage(file="logo.png")
canvas = Canvas(window, width=200, height=200, highlightthickness=2, highlightbackground='red')
canvas.create_image(100, 100, image=password_img, anchor="c")
canvas.grid(row=0, column=1, pady=20, padx=20)

Label(window, text="Website :").grid(row=2, column=0)
website_ent = Entry(window, **my_style, font=font)
website_ent.grid(row=2, column=1, sticky='ew', pady=10)

search_button=Button(window,text='Search',command=search)
search_button.grid(row=2, column=2, pady=20, padx=20)

Label(window, text="Email :").grid(row=3, column=0)
email_ent = Entry(window, **my_style, font=font)
email_ent.grid(row=3, column=1, sticky='ew', columnspan=2, pady=10)
email_ent.insert(0, "ansarisamsad@gmail.com")

Label(window, text="Password :").grid(row=4, column=0)
pass_ent = Entry(window, **my_style, font=font)
pass_ent.grid(row=4, column=1, sticky='ew', pady=10)

Button(window, text='Generate Password', command=generate_password).grid(row=4, column=2, padx=10)
Button(window, text='Save Password', command=save_password).grid(row=5, column=1)

window.mainloop()
