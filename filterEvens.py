def is_even(L):
    evenList = []
    for num in L:
        if num%2 == 0: # even
            evenList.append(num)
    return evenList
numbers = [10, 2, 3, 14, 17, 29, 19, 18, 22, 26]
evens = is_even(numbers)
print("Numbers: ",numbers)
print("Even numbers: ", evens)
#using filter
evensUsingFilter = list(filter(lambda n: n%2==0 ,numbers))
print("Filterd evens: ", evensUsingFilter)
mapresult = list(map(lambda e: e*2 ,evensUsingFilter))
print("map:" , mapresult)





