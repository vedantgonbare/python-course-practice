"""
Write a function tax_calculator(income) that takes annual income and returns
the tax amount based on these slabs:
* Up to 2,50,000 → No tax
* 2,50,001 to 5,00,000 → 5%
* 85,00,001 to 10,00,000 → 20%
* Above 10,00,000 → 30%

"""


def tax_calculator(income):
    if income <= 250000:
        return 0
    elif income >= 250001 and income <= 500000:
        return income * 5 / 100
    elif income <= 500001 and income >= 1000000:
        return income * 20 / 100
    else:
        return income * 30 / 100

print(tax_calculator(200000))
print(tax_calculator(500000))
print(tax_calculator(800000))
print(tax_calculator(1200000))
