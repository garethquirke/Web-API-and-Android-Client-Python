# annoations allow us to define return types / inputs
# mainly used for docs

def info(name: str, age: int, weight: float) -> str:
    print("{} is {} years old and weighs {}kg".format(name, age, weight))

info("Gareth", 21, 75.2)

# this can be broken