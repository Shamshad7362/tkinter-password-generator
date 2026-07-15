import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tkinter Password Manager")
window.geometry("500x500")

value=messagebox.showinfo("Password Manager", "Password Manager has been created")
print(value)

window.mainloop()