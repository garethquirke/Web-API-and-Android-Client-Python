# lambda is a way to make annoymous functions

average = lambda x, y, z:(x + y + z)/3
print(average(10,20,30))

eligbleVoter = lambda age: True if age>= 18 else False
print("i can vote when i am 17 years old.....")
print(eligbleVoter(17))


# binary -> powers of two
powerList = [lambda x: x**0,
             lambda x: x**1,
             lambda x: x**2,
             lambda x: x**3,
             lambda x: x**4]

# iterate through each function in the list
for func in powerList:
    print(func(2))