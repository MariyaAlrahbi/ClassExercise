# Using default arguments in lambda expressions
# Lambda expression that takes 3 arguments by default
summ = lambda a=1, b=2, c=3: a+b+c

print("summ() = ", summ()) 
print("summ(10) = ", summ(b=10))
print("summ(10, 20) = ", summ(10,20))
print("summ(10, 20, 30) = ", summ(10,20,30))
print("summ(b=10, c=20,) = ", summ(b=10,c=20))

