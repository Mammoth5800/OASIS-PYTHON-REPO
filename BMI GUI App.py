import tkinter as tk
from tkinter import messagebox


# -----------------------------
# BMI CALCULATION FUNCTION
# -----------------------------
def calculate_bmi():

    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Weight and height must be positive numbers.")
            return

        bmi = weight / (height ** 2)

        # Determine BMI Category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal Weight"
        elif bmi < 29.9:
            category = "Overweight"
        elif bmi < 34.9:
            category = "Obese"
        else:
            category = "Extremely Obese"

        # Display result
        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


# -----------------------------
# CLEAR INPUT FUNCTION
# -----------------------------
def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")


# -----------------------------
# MAIN WINDOW
# -----------------------------
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x300")
root.resizable(False, False)

# -----------------------------
# TITLE
# -----------------------------
title = tk.Label(root, text="BMI Calculator", font=("Arial", 18, "bold"))
title.pack(pady=10)


# -----------------------------
# WEIGHT INPUT
# -----------------------------
weight_label = tk.Label(root, text="Enter Weight (kg):", font=("Arial", 12))
weight_label.pack()

weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.pack(pady=5)


# -----------------------------
# HEIGHT INPUT
# -----------------------------
height_label = tk.Label(root, text="Enter Height (meters):", font=("Arial", 12))
height_label.pack()

height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.pack(pady=5)


# -----------------------------
# BUTTON FRAME
# -----------------------------
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

calc_button = tk.Button(
    button_frame,
    text="Calculate BMI",
    command=calculate_bmi,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11),
    width=12
)

calc_button.grid(row=0, column=0, padx=5)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    bg="#f44336",
    fg="white",
    font=("Arial", 11),
    width=8
)

clear_button.grid(row=0, column=1, padx=5)


# -----------------------------
# RESULT DISPLAY
# -----------------------------
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    fg="blue"
)

result_label.pack(pady=20)


# -----------------------------
# RUN APPLICATION
# -----------------------------
root.mainloop()
