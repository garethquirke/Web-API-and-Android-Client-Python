# map functions allow us to exectute a function on each item of a list

# simple 1 to ten list and outputted in for loop
onetoten = list(range(1,11))
print(onetoten)

def doublenum(num):
    return num *2

# creating a new list, mapping a function to it and a original list(onetoten)
multiplesoftwo = list(map(doublenum, onetoten))
print(multiplesoftwo)

# now we will square each element by itself
# to create a list of powers
def squarenum(num):
    return num * num

squarelist = list(map(squarenum,onetoten))
print(squarelist)

# example with lambda as a parameter in the map function
cubedlist = list(map((lambda x: x**3), onetoten))
print(cubedlist)

# another lambda example
addtwoarrays = list(map((lambda x,y: x + y), [1,2,3], [1,2,3]))
print(addtwoarrays)