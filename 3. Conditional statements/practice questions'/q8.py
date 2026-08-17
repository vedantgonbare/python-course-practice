"""
A shop gives discounts based on purchase amount:
Above 5000 → 20% discount
Above 2000 → 10% discount
Above 1000 → 5% discount
1000 or below → no discount
"""

purchase_amount = int(input("Enter your purchase amount = "))

if purchase_amount >= 5000:
    print("20% Dicount on this product!")
elif purchase_amount >= 2000:
    print("10% Dicount on this product!")
elif purchase_amount >= 1000:
    print("5% Dicount on this product!")
else:
    print("No discount on this product")