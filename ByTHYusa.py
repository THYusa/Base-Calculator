#By THYusa
import tkinter as tk
from tkinter import messagebox
import math

def calculate_simple_interest(principal, rate, time):
    return principal * (1 + (rate / 100) * time)

def calculate_compound_interest(principal, rate, time, compounds_per_year=1):
    return principal * (1 + rate / (100 * compounds_per_year)) ** (compounds_per_year * time)

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero!")
                return
            result = num1 / num2
        elif operation == '**':
            result = num1 ** num2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def calculate_simple_interest_ui():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())
        result = calculate_simple_interest(principal, rate, time)
        label_result.config(text=f"Total after {time} years: {result:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid values")

def calculate_compound_interest_ui():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())
        compounds_per_year = int(entry_compounds.get())
        result = calculate_compound_interest(principal, rate, time, compounds_per_year)
        label_result.config(text=f"Total after {time} years: {result:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid values")

root = tk.Tk()
root.title("Calculator")

bg_color = "#b3d9ff"
root.config(bg=bg_color)

frame_basic = tk.Frame(root, bg=bg_color)
frame_basic.pack(pady=10)

label_num1 = tk.Label(frame_basic, text="First number:", bg=bg_color)
label_num1.grid(row=0, column=0)

entry_num1 = tk.Entry(frame_basic)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(frame_basic, text="Second number:", bg=bg_color)
label_num2.grid(row=1, column=0)

entry_num2 = tk.Entry(frame_basic)
entry_num2.grid(row=1, column=1)

operation_var = tk.StringVar(value='+')
operation_menu = tk.OptionMenu(frame_basic, operation_var, '+', '-', '*', '/', '**')
operation_menu.grid(row=2, column=0, columnspan=2)

btn_calculate = tk.Button(frame_basic, text="Calculate", command=calculate, bg="#99ccff")
btn_calculate.grid(row=3, column=0, columnspan=2)

frame_interest = tk.Frame(root, bg=bg_color)
frame_interest.pack(pady=10)

label_principal = tk.Label(frame_interest, text="Principal amount:", bg=bg_color)
label_principal.grid(row=0, column=0)

entry_principal = tk.Entry(frame_interest)
entry_principal.grid(row=0, column=1)

label_rate = tk.Label(frame_interest, text="Interest rate (%):", bg=bg_color)
label_rate.grid(row=1, column=0)

entry_rate = tk.Entry(frame_interest)
entry_rate.grid(row=1, column=1)

label_time = tk.Label(frame_interest, text="Time (years):", bg=bg_color)
label_time.grid(row=2, column=0)

entry_time = tk.Entry(frame_interest)
entry_time.grid(row=2, column=1)

label_compounds = tk.Label(frame_interest, text="Compounds per year:", bg=bg_color)
label_compounds.grid(row=3, column=0)

entry_compounds = tk.Entry(frame_interest)
entry_compounds.grid(row=3, column=1)

btn_simple_interest = tk.Button(frame_interest, text="Simple Interest", command=calculate_simple_interest_ui, bg="#99ccff")
btn_simple_interest.grid(row=4, column=0)

btn_compound_interest = tk.Button(frame_interest, text="Compound Interest", command=calculate_compound_interest_ui, bg="#99ccff")
btn_compound_interest.grid(row=4, column=1)

label_result = tk.Label(root, text="Result:", bg=bg_color)
label_result.pack(pady=10)

root.mainloop()
#By THYusa
