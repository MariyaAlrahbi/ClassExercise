def is_even(i):
    return i % 2 == 0

data = [1, 3, 5, 2, 7, 4, 10]

# Filter for even numbers using a lambda function
d1 = list(filter(lambda i: i % 2 == 0, data))
d2 = list(filter(is_even, data))
print(data)
print(d1)


