"""
Q81: Product Price Lookup (HW)
Construct a dictionary containing four product names and their
prices. Prompt the user to enter a product name. Use the in
keyword to check if it exists; if so, display its price. Otherwise,
inform the user "Product not found."

"""

product = {
    "Bag": 20,
    "Table": 50,
    "Chair": 45,
    "Desk": 80,
}

item = input("Enter item name = ")
if item in product:
    print(product[item])
else:
    print("Product not found.")