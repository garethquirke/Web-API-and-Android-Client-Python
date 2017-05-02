import random
from functools import reduce
# create three funtions
# 1. euro to dollar
# 2. euro to japanese yen
# 3. dollar to sterling
# 4. higher order function to accept any function as a paramter
# 5. generate a list of 5 random double amounts (1 - 1000 range)
# 6. calculate the average on this list
# 7. calculate the minium on this list
# 8. calculate the max of this list
# 9  treat the amounts as it is in Euro and use map to convert the
#    list to dollars (through the high order functions)
# 10. use a loop to output the top 3 values in order
# 11. find the number of odd numbers in the list and output that
#     comparison to even numbers
# 12. now create a function to truncate the trailing points after the decimal
#     and check the number of even/odd in the list

# euro to dollar
def euroToDollar(amount):
    return amount  * 1.09

# euro to yen
def euroToYen(amount):
    return amount * 122.19 

# dollar to £
def dollarToSterling(amount):
    return amount * 0.77

def currencyConversion(function, amount):
    return function(amount)

print('50 to dollars ' , int(euroToDollar(50)))
print("100 euro  to yen " , int(euroToYen(100)))
print("80 dollars to pounds" ,  int(dollarToSterling(80)))
print("higher order euro to yen", int(currencyConversion(euroToYen, 20)))


# generate 5 random values in range 1 to 100, 2 decimal places
values = [round(random.uniform(1.0,1000.0), 2) for i in range(5)]
print(values)

# get the average of the list
average = reduce(lambda a,b: a + b, values) / len(values)
print("Average value: ", round(average,2))

# get the minium of the list
minval = reduce(lambda min, current: current if current < min else min, values)
print("Min value: ", minval)

# get the maximum value of the list
maxval = reduce(lambda max, current: current if current > max else max, values)
print("Max value: ", maxval)



# use map to convert the list to dollars (through the high order functions)
listToDollars = list(map(lambda x: round(currencyConversion(euroToDollar,x),2), values))
print("List converted to dollars ", listToDollars)

# use a loop to output all of the values
for i in listToDollars:
    print(i, ",")


# list of the top 3 values 
print(sorted(zip(listToDollars), reverse = True)[:3])


# find the number of odd in the list output that compared to the number of even
comparison = []
othercomparison = []

for i in values:
    if i % 2 == 0: comparison += 'E'
    else: comparison += 'O'

print("Even numbers: " , comparison.count("E"))
print("Odd numbers: " , comparison.count("O"))

# truncate after decimal point and check again for number of even or odd
def numbertypes(list):
    compared = []
    for i in list:
        i = int(i)
        if i % 2 == 0:
            compared += 'E'
        else: compared += 'O'
    return compared


othercomparison = numbertypes(values)
print("Even numbers: " , othercomparison.count('E'))
print("Odd numbers: " , othercomparison.count('O'))