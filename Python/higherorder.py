import random
from functools import reduce

#converting celsius to fahrenheit
def CelToFah(cel):return ((cel * 9 ) / 5) + 32

#convert fahrenheit to celsius
def FahToCel(fah):return ((fah - 32) * 5) / 9


# higher order funtion which accepts either function as a parameter aand a temperature value
def ConvertTemp(converter, value): return converter(value)

print(int(ConvertTemp(FahToCel, 90)))