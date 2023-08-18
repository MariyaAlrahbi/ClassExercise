#classical approach
def squire(l):
    for i in range(len(l)):
        l[i]=l[i]**2 
    return l

data = [1, 3, 5, 2, 7, 4, 10]
print(data)
l=squire(data)
print(l)

#using map function
data = [1, 3, 5, 2, 7, 4, 10]
d1 = list(map(lambda i: i**2, data))
print(d1)

