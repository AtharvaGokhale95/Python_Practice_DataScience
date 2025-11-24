# Stack is LIFO data-structure (LIFO)
# Used to restore the previous stage

# We push a element in stack; when we pop, it returns the last element pushed
# push/ pop: O(1)
# Search element by value: O(n)

# Implementations in Python: List(Array), collections.deque, queue.LifoQueue

# Implementation using list:
s = []
s.append("https://www.cnn.com/")            # First element pushed in the list
s.append("https://www.cnn.com/world")
s.append("https://www.cnn.com/india")
s.append("https://www.cnn.com/china")       # Last element pushed in the list
# print(s)

# Pop out the element:
# s.pop()                 # Pops the last element pushed ("https://www.cnn.com/china")
# print(s)

# s.pop()                 # Pops the second-last element pushed ("https://www.cnn.com/india")
# print(s)

# s.pop()
# s.pop()
# # Now the list is empty

# while s:
#     print(s.pop())
#     if not s:
#         print("The list is now empty and we cannot pop a element from an empty list")



# Implementation using collections.deque - Implemented using doubly linked list
from collections import deque

# stack = deque()                                 # Initialized a stack using deque method
# stack.append("https://www.cnn.com/")            # First element pushed in the stack 
# stack.append("https://www.cnn.com/world")       # Second element will be pushed to the right of the initial element by default
# stack.append("https://www.cnn.com/india")
# stack.append("https://www.cnn.com/china")       # Last element pushed in the stack
# # print(stack)

# Structured Implementation:
class stack:
    def __init__(self):
        self.container = deque()                    # Object of deque class
        
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def length(self):
        return len(self.container)
    
if __name__ == "__main__":
    s = stack()
    
    s.push("https://www.cnn.com/")
    s.push("https://www.cnn.com/world")
    s.push("https://www.cnn.com/india")
    s.push("https://www.cnn.com/china")
    
    print(s.pop())                          # https://www.cnn.com/china is already popped out of the stack
    
    print(s.peek())                         # The element at the top now is https://www.cnn.com/india
    
    print(s.is_empty())
    
    print(s.length())                       # Only https://www.cnn.com/china is popped out - So we have 3 elements in the stack now