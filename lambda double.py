def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)
mydoubler = myfunc(2) 
print(mytripler(11))
print(mydoubler(11)) 