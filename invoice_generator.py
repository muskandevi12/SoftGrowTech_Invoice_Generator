import tkinter as tk
from tkinter import messagebox


def generate_invoice():
    customer = customer_entry.get()
    item = item_entry.get()

    try:
        quantity = int(quantity_entry.get())
        price = float(price_entry.get())

        total = quantity * price

        invoice = (
            "========== INVOICE ==========\n"
            f"Customer Name: {customer}\n"
            f"Item Name: {item}\n"
            f"Quantity: {quantity}\n"
            f"Price per Item: Rs. {price:.2f}\n"
            "-----------------------------\n"
            f"Total Bill: Rs. {total:.2f}\n"
            "============================="
        )

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, invoice)

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid quantity and price."
        )


def clear_fields():
    customer_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    output_text.delete("1.0", tk.END)


# Main window
window = tk.Tk()
window.title("Invoice Generator")
window.geometry("500x550")
window.resizable(False, False)

# Heading
heading = tk.Label(
    window,
    text="Invoice Generator",
    font=("Arial", 22, "bold")
)
heading.pack(pady=20)

# Form frame
form_frame = tk.Frame(window)
form_frame.pack(pady=10)

tk.Label(
    form_frame,
    text="Customer Name:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10, pady=10, sticky="w")

customer_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12)
)
customer_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(
    form_frame,
    text="Item Name:",
    font=("Arial", 12)
).grid(row=1, column=0, padx=10, pady=10, sticky="w")

item_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12)
)
item_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(
    form_frame,
    text="Quantity:",
    font=("Arial", 12)
).grid(row=2, column=0, padx=10, pady=10, sticky="w")

quantity_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12)
)
quantity_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(
    form_frame,
    text="Price per Item:",
    font=("Arial", 12)
).grid(row=3, column=0, padx=10, pady=10, sticky="w")

price_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 12)
)
price_entry.grid(row=3, column=1, padx=10, pady=10)

# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=15)

generate_button = tk.Button(
    button_frame,
    text="Generate Invoice",
    font=("Arial", 11, "bold"),
    width=16,
    command=generate_invoice
)
generate_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 11, "bold"),
    width=10,
    command=clear_fields
)
clear_button.grid(row=0, column=1, padx=10)

# Invoice output
output_text = tk.Text(
    window,
    width=48,
    height=12,
    font=("Courier New", 11)
)
output_text.pack(pady=10)

window.mainloop()