import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Function to get real-time exchange rates
def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        print(result)
        rate = result["rates"].get(to_currency)
        return rate
    else:
        messagebox.showerror("Error", "Failed to fetch exchange rate.")
        return None


# Function to convert currency
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        rate = get_exchange_rate(from_curr, to_curr)
        if rate:
            converted = round(amount * rate, 2)
            result_label.config(text=f"{amount} {from_curr} = {converted} {to_curr}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid amount.")

# GUI setup
root = tk.Tk()
root.title("Currency Converter 💱")
root.geometry("400x300")
root.configure(bg="#f0f4f7")

# Title label
title_label = tk.Label(root, text="💸 Currency Converter", font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#333")
title_label.pack(pady=20)

# Entry and dropdowns
amount_entry = ttk.Entry(root, font=("Helvetica", 14))
amount_entry.pack(pady=10)

from_currency = ttk.Combobox(root, values=["USD", "INR", "EUR", "GBP", "JPY", "CAD"], state="readonly")
from_currency.set("USD")
from_currency.pack()

to_currency = ttk.Combobox(root, values=["USD", "INR", "EUR", "GBP", "JPY", "CAD"], state="readonly")
to_currency.set("INR")
to_currency.pack(pady=10)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#f0f4f7", fg="#222")
result_label.pack(pady=20)

root.mainloop()
