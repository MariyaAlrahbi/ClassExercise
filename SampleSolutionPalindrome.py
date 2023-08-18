from QueueClass import Queue
from StackClass import Stack
def is_palindrome(input_string):
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_string = Queue()
    original_input = Stack()
    for char in input_string:
        if char.isalnum(): #add all alphanumeric chars in lower case, ignore special char
            cleaned_string.enqueue(char.lower())
            original_input.push(char.lower())
    matching = True
    
    # Compare the cleaned string with its reverse
    for i in range (original_input.size()):
        if original_input.pop() != cleaned_string.dequeue():
           matching = False
    return matching

# Test cases

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("12321"))  # Output: True
print(is_palindrome("python"))  # Output: False
