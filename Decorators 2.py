# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()
#func: function as parameter
def greet(func):
    # storing the function in a variable
    #call "func" parameter
    greeting = func("""Hi, function passed as an argument.""")
    print (greeting)
#call the fuction using different fucntion parameters
greet(shout)
greet(whisper)







