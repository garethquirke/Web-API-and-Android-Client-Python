import random
# creating a random list filled with heads or tails
# after creating this list find the number of each side in the list
# heads: 53
# tails: 45

# the list
list = []

# populate the list
for i in range(1,101):
    list += random.choice(['H','T'])


print("Heads: ", list.count('H'))
print("Tails: ", list.count('T'))