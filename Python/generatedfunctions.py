def mult(num):return num * 2;

print(mult(2))

def do_math(function, num): return function(num)
print(do_math(mult, 2))


# return a function , dyanamically created function
# we are creating a function based on what is passed in
# inside our function we create and return a function
def getMutiplication(num):
    def multby(value):
        return num * value
    return multby

# first we generate a function, multby is now 5 times an parameter passed in
generatedfunction = getMutiplication(5)
# testing, expected value is 50
print(generatedfunction(10))

# using a list of functions
listOfFunctions = [mult, generatedfunction]
print(listOfFunctions[0](5))