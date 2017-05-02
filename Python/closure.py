# closures

# high order function
def exp(n):
    def raisetopower(x):
        return x ** n
    return raisetopower

square = exp(2)
cube = exp(3)

print(square(10))
print(cube(10))