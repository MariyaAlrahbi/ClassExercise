def generator (): #generator definition
    yield 1
    yield 5
    yield 7

gen=generator()   #Call the generator

print (next(gen)) #print 1st element
print (next(gen)) #print 2nd element
print (next(gen)) #print 3rd element

