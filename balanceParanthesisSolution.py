from StackClass import Stack
def is_balanced(parentheses_string):
    stack = Stack()

    for char in parentheses_string:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()

    return stack.is_empty()

# Test cases
print(is_balanced("(())"))  # Output: True
print(is_balanced("(()))"))  # Output: False
print(is_balanced("((()()()))"))  # Output: True
print(is_balanced("())("))  # Output: False
