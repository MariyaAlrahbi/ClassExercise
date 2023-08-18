def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    avg=total/len(numbers)
    return total,round(avg,1)

print(add(2, 3))
print(add(2, 3, 5))
print(add(2, 3, 5, 7))
print(add(2, 3, 5, 7, 9))


