from functools import reduce
# count words in sentence using reduce
def countwords(a,b):
    return a + 1

words = ["my", "name", "is", "gareth"]

result = reduce(countwords, filter(lambda i: i!= "my" and i != "is", words), 0)
print(result)