from functools import reduce
data = [1, 3, 5, 2, 7, 4, 10]
result = reduce(lambda total, value: total + value, data)
print(result)

letters=['C','O', 'D', 'E', ' ', 'A', 'C', 'A','D', 'E', 'M', 'Y']
word=reduce(lambda x,y:x+y, letters)
print(word)


fact=[5,4,3,2,1]
result=reduce(lambda x,y:x*y, fact)
print(result)


