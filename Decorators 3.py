# Functions can return another function
#upper function
def create_adder(x):
    #inner fuction
    def adder(y):
        #note:Inner can access outer's paramenters "x"
        print (x,y)
        return x+y
    #return the inner function
    return adder

add_15 = create_adder(15)

print(add_15(10))
