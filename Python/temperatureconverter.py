import random
from functools import reduce

#converting celsius to fahrenheit
def CelToFah(cel):return ((cel * 9 ) / 5) + 32

#convert fahrenheit to celsius
def FahToCel(fah):return ((fah - 32) * 5) / 9

# ouputting two different types of conversions
# casting to int(removes trailing numbers afer decimal point)
print(int(CelToFah(32)))
print(int(FahToCel(82)))