import random
from functools import reduce

# reduce is used to return a single result from a list
# in this case it finds the last value, 5, and adds it together
print(reduce((lambda x, y: x + y), range(1,5)))

# in this example i will reduce the list to the maximum value
# lambda is useful as it is more connected to the list we are addressing
maxvalue = lambda a,b: a if(a > b) else b
print(reduce(maxvalue, range(1,401)))


# Now calculate the stats from a random list
print('calculating stats from random list')
randomvalues = [random.randint(5,50) for _ in range(11)]
# min
print('min value: ', reduce(lambda min, current: current if current < min else min, randomvalues))
# max
print('max value: ', reduce(lambda max,current: current if current > max else max, randomvalues))
# average
average = reduce(lambda x,y: x + y, randomvalues) / len(randomvalues)
print('Average Value', int(average))