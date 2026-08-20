"""
Write a function called discount_price that takes original_price
and discount_percent as parameters and prints the final
price after discount.

"""


def discount_price(original_price, discount_percent):
    discount_amount = discount_percent / 100 * original_price
    final_amount = original_price - discount_amount
    print(f"The final price after discount is ₹ {final_amount}")


a = float(input("Enter the original price = "))
b = float(input("Enter the discount percent = "))

discount_price(a, b)
