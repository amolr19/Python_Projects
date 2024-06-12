import tkinter as tk
from tkinter import messagebox
from Billing_soft.Backend.billing_logic import BillingSystem

class BillingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Billing Software")

        self.billing_system = BillingSystem()

        self.item_name_var = tk.StringVar()
        self.item_code_var = tk.StringVar()
        self.quantity_var = tk.IntVar()
        self.price_var = tk.DoubleVar()
        self.taxes_var = tk.DoubleVar()

        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self.master, text="Item Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.master, text="Item Code:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.master, text="Quantity:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self.master, text="Price:").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(self.master, text="Taxes:").grid(row=4, column=0, padx=10, pady=5)
        tk.Label(self.master, text="Bill Total:").grid(row=6, column=0, padx=10, pady=5)

        # Entry fields
        tk.Entry(self.master, textvariable=self.item_name_var).grid(row=0, column=1, padx=10, pady=5)
        tk.Entry(self.master, textvariable=self.item_code_var).grid(row=1, column=1, padx=10, pady=5)
        tk.Entry(self.master, textvariable=self.quantity_var).grid(row=2, column=1, padx=10, pady=5)
        tk.Entry(self.master, textvariable=self.price_var).grid(row=3, column=1, padx=10, pady=5)
        tk.Entry(self.master, textvariable=self.taxes_var).grid(row=4, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(self.master, text="Add Item", command=self.add_item).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Print Bill", command=self.print_bill).grid(row=5, column=1,columnspan=4,pady=10)
        tk.Button(self.master, text="Bill Generate", command=self.generate_bill).grid(row=5, column=3, pady=10)

        # Text box to display added items
        self.item_text = tk.Text(self.master, height=20, width=100)
        self.item_text.grid(row=10, column=0, columnspan=20, padx=10, pady=5)

        # Text field to display bill total
        self.bill_total_text = tk.Text(self.master, height=1, width=20, state=tk.DISABLED)
        self.bill_total_text.grid(row=6, column=1, padx=10, pady=5)

    def add_item(self):
        item_name = self.item_name_var.get()
        item_code = self.item_code_var.get()
        quantity = self.quantity_var.get()
        price = self.price_var.get()
        taxes = self.taxes_var.get()
        self.billing_system.add_item(item_name, item_code, quantity, price, taxes)
        self.update_item_text()  # Update text box with added items
        self.update_bill_total()  # Update bill total


    def update_item_text(self):
        self.item_text.delete(1.0, tk.END)
        self.item_text.insert(tk.END, "Bill Details:\n")
        self.item_text.insert(tk.END, "---------------------------------------------------------\n")
        self.item_text.insert(tk.END, "{:<20} {:<20} {:<10} {:<10} {:<10}\n".format("Item Name", "Item Code", "Quantity", "Price", "Total"))
        self.item_text.insert(tk.END, "---------------------------------------------------------\n")
        for item in self.billing_system.bill_items:
            self.item_text.insert(tk.END, "{:<20} {:<20} {:<10} {:<10} {:<10}\n".format(
                item["Item name"], item["Item code"], item["Quantity"], item["Price"], item["Bill Total"]))
        self.item_text.insert(tk.END, "---------------------------------------------------------\n")

    def update_bill_total(self):
        self.bill_total_text.config(state=tk.NORMAL)
        self.bill_total_text.delete(1.0, tk.END)
        self.bill_total_text.insert(tk.END, f"₹{self.billing_system.bill_total:.2f}")
        self.bill_total_text.config(state=tk.DISABLED)

    def print_bill(self):
        bill_items, bill_total = self.billing_system.generate_bill()
        messagebox.showinfo("Bill Details", f"Bill Items: {bill_items}\nBill Total: {bill_total}")
        self.item_text.delete(1.0, tk.END)  # Clear text box after printing bill
        self.bill_total_text.config(state=tk.NORMAL)
        self.bill_total_text.delete(1.0, tk.END)  # Clear bill total text field
        self.bill_total_text.config(state=tk.DISABLED)

    def generate_bill(self):
        self.billing_system.generate_bill()
        self.billing_system.clear_bill()
        messagebox.showinfo("Bill Generated", "Bill generated and saved to daily sales report.")
        self.item_text.delete(1.0, tk.END)  # Clear text box after generating bill
        self.bill_total_text.config(state=tk.NORMAL)
        self.bill_total_text.delete(1.0, tk.END)  # Clear bill total text field
        self.bill_total_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = BillingApp(root)
    root.geometry("900x700")  # Set the size of the window
    root.mainloop()

if __name__ == "__main__":
    main()
