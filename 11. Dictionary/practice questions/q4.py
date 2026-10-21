"""
Q82: World Capitals (HW)
Create a dictionary mapping five countries to their capital cities. Iterate
through this dictionary using the items() method and print each pair in
the format: Country → Capital.

"""

World = {
    "Germany": "Berlin",
    "India": "Delhi",
    "France": "Paris",
    "Spain": "Madrid",
    "Russia": "Moscow",
}

for Country, Capital in World.items():
    print(f"{Country} = {Capital}")