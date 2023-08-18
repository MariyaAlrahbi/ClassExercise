def func1(fun):
    #define wrapper
    def wrapper():
        print("Hello")
        fun()
        print ("Welcome to Python")
    return wrapper

@func1
def func2():
    print ("Code Academy")

func2()