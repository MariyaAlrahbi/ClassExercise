import random

# A function that returns an integer in the range 0 to 99
def GetRandomNumber():
    # 1. Get a random number in the range 0..1
    number = random.random()
    number99 = lambda : int(number*100)
    # 3. Return an integer
    return number99()

num = GetRandomNumber()
print("num = ", num)