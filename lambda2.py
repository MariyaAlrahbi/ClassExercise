def oddEven(n):
    if n%2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
oddEven1= lambda n:(n%2 and 'ODD' or 'EVEN')


print(oddEven1(14))
print(oddEven1(15))
