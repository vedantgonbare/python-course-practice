"""
Q74: Create a tuple of 5 of your favourite movies. Print the first, last, and middle one using indexing.
"""

fav_movies = ("Godfather", "Interstellar", "Inglorius Basterds", "Odysessy", "Tenet")

n = len(fav_movies)
print(f"first = {fav_movies[0]}")
print(f"Middle = {fav_movies[n//2]}")
print(f"last = {fav_movies[-1]}")
