def evenElem(L):
    l1=[]
    for i in L:
        if (i % 2 == 0):
             l1.append(i)
    return l1

data = [1, 3, 5, 2, 7, 4, 10]
l=evenElem(data)
print(data)
print(l)

