import tkinter as tk
from tkinter import ttk

# -------------------- COLORS --------------------
BG_COLOR = "#F5F5F7"
CARD_COLOR = "white"
ACCENT = "#6C63FF"
ACCENT_HOVER = "#5848E5"
TEXT_COLOR = "#333333"

# -------------------- BUTTON HOVER EFFECT --------------------
def on_enter(e):
    e.widget['background'] = ACCENT_HOVER

def on_leave(e):
    e.widget['background'] = ACCENT

# -------------------- MAIN WINDOW --------------------
root = tk.Tk()
root.title("Password Manager")
root.geometry("420x420")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# -------------------- CARD FRAME --------------------
card = tk.Frame(root, bg=CARD_COLOR, bd=0, relief="flat")
card.place(relx=0.5, rely=0.5, anchor="center")

# -------------------- TITLE --------------------
title = tk.Label(card, text="MyPass", font=("Segoe UI", 22, "bold"), bg=CARD_COLOR, fg=ACCENT)
title.pack(pady=(20, 5))

subtitle = tk.Label(card, text="Secure. Simple. Smart.", font=("Segoe UI", 10), bg=CARD_COLOR, fg=TEXT_COLOR)
subtitle.pack(pady=(0, 20))

# -------------------- USERNAME --------------------
user_label = tk.Label(card, text="Username", font=("Segoe UI", 11), bg=CARD_COLOR, fg=TEXT_COLOR)
user_label.pack(anchor="w", padx=30)

user_entry = tk.Entry(card, font=("Segoe UI", 11), bd=1, relief="solid")
user_entry.pack(padx=30, pady=(0, 15), fill="x")

# -------------------- EMAIL --------------------
email_label = tk.Label(card, text="Email", font=("Segoe UI", 11), bg=CARD_COLOR, fg=TEXT_COLOR)
email_label.pack(anchor="w", padx=30)

email_entry = tk.Entry(card, font=("Segoe UI", 11), bd=1, relief="solid")
email_entry.pack(padx=30, pady=(0, 20), fill="x")

# -------------------- BUTTONS --------------------
btn_frame = tk.Frame(card, bg=CARD_COLOR)
btn_frame.pack(pady=(0, 25))

def make_button(text, command=None):
    btn = tk.Button(
        btn_frame,
        text=text,
        font=("Segoe UI", 11, "bold"),
        bg=ACCENT,
        fg="white",
        activebackground=ACCENT_HOVER,
        activeforeground="white",
        bd=0,
        padx=20,
        pady=8,
        cursor="hand2"
    )
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

save_btn = make_button("Save Password")
gen_btn = make_button("Generate Password")

save_btn.grid(row=0, column=0, padx=10)
gen_btn.grid(row=0, column=1, padx=10)

root.mainloop()
