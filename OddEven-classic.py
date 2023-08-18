def OddEven (x):
    if x%2 == 0:
        return "Even"
    else:
        return "Odd"
print (OddEven(100))
print (OddEven(33))

"""
OddEven=lambda x:(x % 2 and 'odd' or 'even')

print (OddEven(100))
print (OddEven(33))
"""