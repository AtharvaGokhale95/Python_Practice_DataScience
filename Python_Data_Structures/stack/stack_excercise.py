# Write a function in python that can reverse a string using stack data structure
# Using the collections.deque class

from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self, val):
        return self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def reverse_string(self, string):
        for char in string:
            self.push(char)
        
        print(self.container)
        
        output_str = ""
        while self.container():
            output_str += self.container.pop()
        return output_str           
        
            
# if __name__ == "__main__":
    
#     # Created an object of class stack:
#     s = Stack()
    
#     reverse_str = s.reverse_string("We will conquer COVID-19")
#     print(reverse_str)
    
    
# Write a function in python that checks if parenthesis in the string are balanced or not. Possible parentheses are "{}',"()" or "[]"
# Logic: E.g.: [(a+b)] -> If I see a closing bracket, it must match the most recent opening bracket in the stack
# 1. char = '[' -> As this is a opening bracket, we push this in the stack
# 2. char = '(' -> As this is a opening bracket, we push this in the stack
# 3. Now, stack = ['(', '[']
# 4. char = ')' -> closing bracket -> Needs to match with the last char pushed / first char in the stack to maintain the balance -> If it matches then pop it out
# 5. Now, stack = ['[']
# 6. char = ']' -> closing bracket -> This needs to match with the first char in the stack to maintain the balance -> If it matches then pop it out

def is_match(closing_bracket, opening_bracket):
    # Here we keep the closing bracket as the key and opening bracket as the value
    # This is because, in the is_balanced logic, if we get a opening bracket we push it in the stack, 
    # But if we get a closing bracket, we use that char as the key and pass it to the is_match function to find its value and then determine the match
    match_dict = {
        '}' : '{',
        ')' : '(',
        ']' : '['
    }
    return match_dict[closing_bracket] == opening_bracket           # Returns a boolean value: True/ False if the condition is satisfied

# print(is_match('{', '}'))                 # This returns True

def is_balanced(string):                    # returns a boolean value: True/ False
    stack  = Stack()                        # Created an obj of class Stack
    opening = set("{([]")
    closing = set('})]')
    for char in string:
        if char in opening:       # If it is a opening parenthesis then push that char in the stack
            stack.push(char)
        if char in closing:       # If the the char is a closing parenthesis, we pass it to is_match function to check for its val
            if stack.size() == 0:
                return False                        # There is a closing bracket without any corresponding opening bracket remaining in the stack -> Not balanced
            if not is_match(char, stack.pop()):     # If is_match is True then we just pop the matching opening bracket and we move the the next char
                # However, even if one pair is not matching we can directly return False
                return False
            
    return stack.size() == 0                # This condition ensures that we have found a match for all the opening brackets that were pushed in the stack

print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("((a+g))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))