# code for testing decorator chaining
def decorator1(func):
    def wrapper():
        x = func()
        return x * x
    return wrapper

def decorator2(func):
    def wrapper():
        x = func()
        return 2 * x
    return wrapper

@decorator1 #then run decorator1
@decorator2 #start with decorator2
def num():
    return 10

print(num())



