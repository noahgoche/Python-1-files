"""
* Name         : M10 T2: Invoice Class Assignment
* Author       : Noah Goche
* Created      : 7/16/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.129.1
* Description  : Class creates invoice objects that take a invoice id, customer id, and a dictionary of items from the user.
Includes methods to get and set and print the information out. 
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""
"""
CIS189 Module 10 invoice Class assignment script.

Remove all instances of `pass` before testing/running.
"""

class Invoice:
    def __init__(self, invoice_id, customer_id, items = dict()):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.ditems = dict(items)
        self.ditems = {key: f"{value:.2f}" for key, value in self.ditems.items()}

    @property
    def invoice_id(self):
        return self._invoice_id
    
    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value

    @property
    def customer_id(self):
        return self._customer_id
    
    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    
    def add_item (self, item, price):
        self.ditems[item] = price

    def print_invoice(self):
        print("CUSTOMER: {}\nINVOICE: {}".format(self.customer_id, self.invoice_id))

        for key, value in sorted(self.ditems.items()):
            print(f"\t{key}: {value} ")
        
    def __str__(self):
        return "Invoice ID: " + self.invoice_id + "\nCustomer ID: " + self.customer_id + f"\nItems\n{self.ditems}"



def main():

    invoices_list = [
        {"invoice_id": "A554GFT-117", "customer_id": "98676867", "items": [("ipad", 499.99), ("mouse", 29.97), ("monitor", 229.08)]},
        {"invoice_id": "J244GFT-283", "customer_id": "77594872", "items": [("router", 267.78), ("hdmi-cable", 24.77)]},
        {"invoice_id": "R943RXC-476", "customer_id": "54092341", "items": [("laptop", 1399.54), ("warranty", 199.94), ("snickers", 2.49)]},
        {"invoice_id": "J712WQR-888", "customer_id": "43908134", "items": [("amplifier", 749.00), ("speaker-cable", 42.75)]}
    ]

    # Iterate over invoices_list. After items have been added to instance dictionary,
    # call print_invoice.
    invoice_object_list = []
    # Iterate over invoices_list, and create a new invoice instance 
    for invoice in invoices_list:
        #takes the dictionary key values as keyword args to create each employee object then adds to a list of employees then prints the display function
        new_Invoice = Invoice(**invoice)
        invoice_object_list.append(new_Invoice)
        print(f"{(str(new_Invoice))}\n")   
        new_Invoice.print_invoice()

    

if __name__ == "__main__":

    main()

