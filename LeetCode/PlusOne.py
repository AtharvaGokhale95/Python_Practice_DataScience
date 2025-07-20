from typing import List
class Solution:
    def onePlus(self, digits : List[int]) -> List[int]:
        string = ""
        for digit in digits:
            string += str(digit)
        integer = int(string)
        integer_plusOne = integer + 1
        final_list = []
        for val in str(integer_plusOne):
            final_list.append(int(val))
        return final_list
    
    def onePlus_oneLiner(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        return list(map(int, str(num + 1)))
    
    def onePlus_function(self, digits: List[int]) -> List[int]:
        end = len(digits)
        for i in reversed(range(end)):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            # With the for loop running over it complete range in the reversed direction, the carry forward +1 will be added automatically
            
            # If command comes out of the for loop, i.e, the function never returns the list digits, then:
        return [1] + digits         # This add the carried over 1 if we encounter all 9s in the digits list
            
        
        
        
s = Solution()
print(s.onePlus([1,2,3]))
print(s.onePlus_oneLiner([9,9]))
print(s.onePlus_function([9,9,9]))