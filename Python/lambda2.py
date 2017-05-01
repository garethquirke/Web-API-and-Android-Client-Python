import random
# dictionary of functions with lambda

tricks = {"ollie": (lambda : print("ollie")),
          "kickflip": (lambda : print("kickflip")),
          "heelflip": (lambda : print("heelflip")),
          "pop shuv": (lambda : print("pop shuv"))}

tricks["heelflip"]()


# now do a random trick for the boys
tricknumber = random.choice(list(tricks.keys()))
tricks[tricknumber]()