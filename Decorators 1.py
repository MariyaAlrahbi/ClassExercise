# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()

#classical function call
print(shout('Hello'))

#assign function to an object (variable)
yell = shout   # no ()

print(yell('Hello'))




