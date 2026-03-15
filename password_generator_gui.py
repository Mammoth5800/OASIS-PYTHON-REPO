import tkinter as tk
from tkinter import messagebox
import random
import string


# --------------------------------
# GENERATE PASSWORD FUNCTION
# --------------------------------
def generate_password():

    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return

    except:
        messagebox.showerror("Error", "Enter a valid password length")
        return


    character_pool = ""

    if var_upper.get():
        character_pool += string.ascii_uppercase

    if var_lower.get():
        character_pool += string.ascii_lowercase

    if var_numbers.get():
        character_pool += string.digits

    if var_symbols.get():
        character_pool += string.punctuation


    if character_pool == "":
        messagebox.showerror("Error", "Select at least one character type")
        return


    password = ""

    # enforce strong password rule
    if var_upper.get():
        password += random.choice(string.ascii_uppercase)

    if var_lower.get():
        password += random.choice(string.ascii_lowercase)

    if var_numbers.get():
        password += random.choice(string.digits)

    if var_symbols.get():
        password += random.choice(string.punctuation)


    remaining_length = length - len(password)

    for i in range(remaining_length):
        password += random.choice(character_pool)


    password_list = list(password)
    random.shuffle(password_list)

    final_password = "".join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, final_password)



# --------------------------------
# COPY PASSWORD TO CLIPBOARD
# --------------------------------
def copy_password():

    password = password_entry.get()

    if password == "":
        messagebox.showerror("Error", "Generate a password first")
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo("Copied", "Password copied to clipboard!")


# --------------------------------
# CLEAR FUNCTION
# --------------------------------
def clear_fields():

    password_entry.delete(0, tk.END)



# --------------------------------
# GUI WINDOW
# --------------------------------
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("420x420")
root.resizable(False, False)



# --------------------------------
# TITLE
# --------------------------------
title = tk.Label(
    root,
    text="Advanced Password Generator",
    font=("Arial", 16, "bold")
)

title.pack(pady=10)



# --------------------------------
# PASSWORD LENGTH
# --------------------------------
length_label = tk.Label(root, text="Password Length:", font=("Arial", 12))
length_label.pack()

length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)



# --------------------------------
# CHECKBOX OPTIONS
# --------------------------------
var_upper = tk.IntVar()
var_lower = tk.IntVar()
var_numbers = tk.IntVar()
var_symbols = tk.IntVar()


check_upper = tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=var_upper)
check_upper.pack(anchor="w", padx=40)

check_lower = tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=var_lower)
check_lower.pack(anchor="w", padx=40)

check_numbers = tk.Checkbutton(root, text="Include Numbers (0-9)", variable=var_numbers)
check_numbers.pack(anchor="w", padx=40)

check_symbols = tk.Checkbutton(root, text="Include Symbols (!@#$)", variable=var_symbols)
check_symbols.pack(anchor="w", padx=40)



# --------------------------------
# GENERATE BUTTON
# --------------------------------
generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12),
    bg="green",
    fg="white",
    command=generate_password
)

generate_btn.pack(pady=15)



# --------------------------------
# PASSWORD DISPLAY
# --------------------------------
password_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    width=25
)

password_entry.pack(pady=10)



# --------------------------------
# BUTTON FRAME
# --------------------------------
button_frame = tk.Frame(root)
button_frame.pack(pady=10)


copy_btn = tk.Button(
    button_frame,
    text="Copy Password",
    bg="blue",
    fg="white",
    command=copy_password,
    width=14
)

copy_btn.grid(row=0, column=0, padx=5)


clear_btn = tk.Button(
    button_frame,
    text="Clear",
    bg="red",
    fg="white",
    command=clear_fields,
    width=10
)

clear_btn.grid(row=0, column=1, padx=5)



# --------------------------------
# FOOTER
# --------------------------------
footer = tk.Label(
    root,
    text="Secure Password Generator",
    font=("Arial", 10),
    fg="gray"
)

footer.pack(side="bottom", pady=10)



# --------------------------------
# RUN APPLICATION
# --------------------------------
root.mainloop()
