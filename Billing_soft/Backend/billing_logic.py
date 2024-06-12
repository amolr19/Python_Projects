class BillingSystem:
    def __init__(self):
        self.bill_items = []
        self.bill_total = 0
        self.bill_number = 1

    def add_item(self, item_name, item_code, quantity, price, taxes):
        total_without_taxes = quantity * price
        total_with_taxes = total_without_taxes + (total_without_taxes * taxes / 100)
        self.bill_items.append({
            "Sr no.": len(self.bill_items) + 1,
            "Item name": item_name,
            "Item code": item_code,
            "Quantity": quantity,
            "Price": price,
            "Taxes": taxes,
            "Total Without Taxes": total_without_taxes,
            "Bill Total": total_with_taxes
        })
        self.bill_total += total_with_taxes

    def generate_bill(self):
        # Save the bill to daily sales report
        with open("daily_sales_report.txt", "a") as f:
            f.write(f"Bill Number: {self.bill_number}\n")
            for item in self.bill_items:
                f.write(f"{item}\n")
            f.write(f"Bill Total: {self.bill_total}\n\n")
        self.bill_number += 1
        return self.bill_items, self.bill_total

    def clear_bill(self):
        self.bill_items = []
        self.bill_total = 0
