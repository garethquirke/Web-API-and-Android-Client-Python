import random
from functools import reduce

# generate 6 different lottery numbers
numbers = [x for x in range(1,50)]
random.shuffle(numbers)

lotterypicks = [numbers[0], numbers[1], numbers[2], numbers[3],numbers[4], numbers[5]]
print(lotterypicks)