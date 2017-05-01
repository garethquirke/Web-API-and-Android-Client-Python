# PROBLEM
# produce a list of odd numbers from 1 to 20
# first make a function that checks whether a number is odd or not
# create a function to accept a list of numbers and a function
# use the function passed in (odd number checker) to return a complete list of odd numbers


# odd number function
def isOdd(num):
    if num %2 == 0:
        return False
    else:
        return True


# function to return a list of odd numbers, append is used to pop values to array
def changeList(list, function):
    oddList = []
    for i in list: 

        if function(i):
            oddList.append(i)
    return oddList

list = range(1,20)
print(changeList(list, isOdd))