queue = Queue()
print(queue.is_empty())  # Output: True

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.peek())  # Output: 1
print(queue.size())  # Output: 3

print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

print(queue.is_empty())  # Output: False
