import tkinter as tk
from tkinter import messagebox

STANDARD_DEDUCTION = 10000.00
DEPENDENT_DEDUCTION_PER_CHILD = 3000.00
TAX_RATE = 0.20

def compute_tax():
    try:
        gross_income = float(gross_income_entry.get())
        dependents = int(dependents_entry.get())

        if gross_income < 0 or dependents < 0:
            messagebox.showerror("Input Error", "Gross income and dependents cannot be negative.")
            return

        taxable_income = gross_income - STANDARD_DEDUCTION - (dependents * DEPENDENT_DEDUCTION_PER_CHILD)

        if taxable_income < 0:
            taxable_income = 0

        total_tax = taxable_income * TAX_RATE

        total_tax_result.config(state="normal")
        total_tax_result.delete(0, tk.END)
        total_tax_result.insert(0, f"{total_tax:.2f}")
        total_tax_result.config(state="readonly")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for Gross income and Dependents.")
    except Exception as e:
        messagebox.showerror("An Error Occurred", f"An unexpected error occurred: {e}")

root = tk.Tk()
root.title("Tax Calculator")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="Gross income").grid(row=0, column=0, padx=10, pady=5, sticky="w")
gross_income_entry = tk.Entry(root, width=15)
gross_income_entry.grid(row=0, column=1, padx=10, pady=5)
gross_income_entry.insert(0, "0.0")

tk.Label(root, text="Dependents").grid(row=1, column=0, padx=10, pady=5, sticky="w")
dependents_entry = tk.Entry(root, width=15)
dependents_entry.grid(row=1, column=1, padx=10, pady=5)
dependents_entry.insert(0, "0")

tk.Button(root, text="Compute", command=compute_tax).grid(row=2, column=0, columnspan=2, pady=10)

tk.Label(root, text="Total tax").grid(row=3, column=0, padx=10, pady=5, sticky="w")
total_tax_result = tk.Entry(root, width=15, state="readonly")
total_tax_result.grid(row=3, column=1, padx=10, pady=5)
total_tax_result.insert(0, "0.0")

root.mainloop()