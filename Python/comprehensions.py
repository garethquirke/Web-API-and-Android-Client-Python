# comprehensions are a way of initializing a list or dictionary or set
data = list(range(1,10))

# square all of the odd numbers in the odd list declared above
oddsquared = map(lambda x: x**2, filter(lambda i: i %2 == 1, data))
print(list(oddsquared))

# carry out the same process but this time use list comprehension
oddsquared = [d**2 for d in data if d % 2 == 1]
print(oddsquared)