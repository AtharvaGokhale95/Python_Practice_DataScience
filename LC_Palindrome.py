'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''


# Using list reversal
class Solution:
    def isPalindrome_reverse(self, x:int) -> bool:
        x_list = [str(char) for char in str(x)]
        x_list_reverse = x_list[::-1]
        if x_list == x_list_reverse:
            return True
        return False
    
    # Using while loop:
    def isPalindrome_while(self, x):
        x_str = str(x)                              # Type casted int to str
        if len(x_str) == 1:
            return True
        
        head = 0
        tail = len(x_str) - 1
        
        while head < tail:          # This while loop ensure the comparing values are not the same and 
                                    # We exactly keep comparing one value from the front and other from the back of the string while head < tail               
            if x_str[head] == x_str[tail]:
                return True
            else:
                return False
            head += 1
            tail -= 1
            
    
obj = Solution()
print(obj.isPalindrome_while(1212))
# print(obj.isPalindrome(121))
        



