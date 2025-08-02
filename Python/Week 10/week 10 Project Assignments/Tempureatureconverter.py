import tkinter as tk
from tkinter import messagebox

def convert_fahrenheit_to_celsius():
    try:
        f_value = float(fahrenheit_entry.get())
        c_value = (f_value - 32) * 5/9
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, f"{c_value:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for Fahrenheit.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def convert_celsius_to_fahrenheit():
    try:
        c_value = float(celsius_entry.get())
        f_value = c_value * 9/5 + 32
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, f"{f_value:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for Celsius.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x150")
root.resizable(False, False)

tk.Label(root, text="Fahrenheit:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
fahrenheit_entry = tk.Entry(root, width=15)
fahrenheit_entry.grid(row=1, column=0, padx=10, pady=5)
fahrenheit_entry.insert(0, "32.0")

tk.Label(root, text="Celsius:").grid(row=0, column=1, padx=10, pady=5, sticky="e")
celsius_entry = tk.Entry(root, width=15)
celsius_entry.grid(row=1, column=1, padx=10, pady=5)
celsius_entry.insert(0, "0.0")

tk.Button(root, text=">>>>", command=convert_fahrenheit_to_celsius).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="<<<<", command=convert_celsius_to_fahrenheit).grid(row=2, column=1, padx=10, pady=10)

root.mainloop()