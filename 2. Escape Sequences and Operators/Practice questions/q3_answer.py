# Take the users age as input and check weather they are eligible to vote (age >= 18) and weather they are a senior citizen (age >= 60).
#Print both results.

age = int(input("Enter your age ="))
can_vote = age >= 18
senior_citizen = age >= 60

print(f"User can vote {can_vote}")
print(f"User is a senior citizen {senior_citizen}")