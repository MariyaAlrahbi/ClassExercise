from functools import reduce

emplo = ['Ali', 'Ahmed', 'Mohammed', 'Hamed']
hoursWorked = [1,     3,        5,          7] # number of hours each emply works
payPerHour = [2,     4,        6,          8] #how much per hour is paid
result = list(map(lambda hours, pay: hours * pay, hoursWorked, payPerHour))
print(result)
totalPayment = reduce( lambda a, b: a+ b, result)
print("total:", totalPayment)
total = 0
for n in result:
     total += n
print("t:", total)
"""
doubePay = list(map( lambda pay: pay * 2,payPerHour))

print(doubePay)
result = list(map(lambda hours, pay: hours * pay, hoursWorked, doubePay))
print("after double:", result)
"""