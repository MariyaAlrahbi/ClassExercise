def decorator(func):
    def wrapper(n1,n2):
        # Decorated function return value
        print("before Execution")
        returned_value = func(n1,n2)
        print("after Execution")
        return returned_value
    return wrapper


@decorator # adding decorator 
def sum_two_numbers(a, b):
    return a + b


print("Sum =", sum_two_numbers(2, 3))





