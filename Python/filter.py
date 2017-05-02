import random
# filter allows us to select items from a list based on a function
# lets filter out the even values
print(list(filter((lambda x: x %2), range(1,20))))

# multiples of 9 from a list of 100 values ranging from 1 to 500
randomlist = list(random.randint(1,500) for i in range(100))
print(list(filter((lambda x: x%9 == 0), randomlist)))