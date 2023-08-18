#if we define a list as a stack
# list can be randomly accessed
# Thus, use stack object
from StackClass import Stack
stack = Stack()
print(stack.is_empty())  # Output: True

stack.push('A')
stack.push('D')
stack.push('R')

print(stack.peek())  # Output: R
print(stack.size())  # Output: 3

print(stack.pop())  # Output: R
print(stack.pop())  # Output: D

print(stack.is_empty())  # Output: False

