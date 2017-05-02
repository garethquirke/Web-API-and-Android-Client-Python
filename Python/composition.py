# returning a function which composes f and g
def compose(f, g):
    return lambda x: f(g(x))

add2 = compose(lambda a: a + 1, lambda a: a + 1)
x = add2(10)
print(x)