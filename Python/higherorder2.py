import string

def hello(name):
    print("hello " + name)

def goodbye(name):
    print("goodbye " + name)

hello("gareth")
goodbye("gareth")


def greeting(function):
    return function

greeting(hello("Gareth"))
greeting(lambda n: print("little lambda " + n, "expression"))


def splitfullname():
    def wholename(name):
        return name.split(' ')
    return wholename

name = splitfullname()
print(name("Gareth Quirke"))