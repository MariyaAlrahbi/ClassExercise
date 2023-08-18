def func1(fun):
    #define wrapper
    def wrapper():
        print("Hello")
        fun()
        print ("Welcome to Python")
    return wrapper

def func2():
    print ("Code Academy")
    
#object to fucn1
f=func1(func2)
f() #execute the object
