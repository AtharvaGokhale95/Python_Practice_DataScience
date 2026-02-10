# To manage data in the exact order it arrives (FIFO) -> Opposite of Stack 
# Used for loose coupling - Producer Consumer Problem


# Implementation using list in python:
# 2 operations to add an element to the list:
#   1. list.append(element): This add the element to the (right) end of the list
#   2. list.insert(0, element): This add the element at the (left) start of the list

# pop operation in Python - pop() always removes from the end of the list

# Thus, to implement Queue (FIFO) we will use list.insert(0, element)

# Python List : Queue
stock_price_queue = []

# Insert elements in the list
stock_price_queue.insert(0, 132.5)
stock_price_queue.insert(0, 135.0)
stock_price_queue.insert(0, 137.2)
# stock_price_queue = [137.2, 135.0, 132.5]

# Queue operations:

# pop()
# Handling the exception:
try:
    print("First element that will be popped:",stock_price_queue.pop())
    print("Second element that will be popped:",stock_price_queue.pop())
    print("Third element that will be popped:",stock_price_queue.pop())
    print("Trying to pop after the queue is empty:",stock_price_queue.pop())
except Exception as e:
    print("Exception Type:", type(e).__name__)


# Implementation using collections.deque
# collections is a built-in Python module that provides specialized container data types 
# deque (double-ended queue) is a class inside collections module
from collections import deque

# Create an object of class deque
q = deque()

# Append left: Insert objects in q:
q.appendleft(1)
q.appendleft(2)
q.appendleft(3)

try:
    while q:
        print(q.pop())
except Exception as e:
    print("Exception is:", type(e.__name__))
    
    
# Using collections.deque: Queue Class
