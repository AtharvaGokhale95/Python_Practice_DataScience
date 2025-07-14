class Solution:
    dict = {'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}
    
    # def roman_To_Int_partial(self, s:str) -> int:
    #     val = 0
    #     for char in s:
    #         val += dict[char]
    #     return val
    
    
    def roman_To_Int_complete(self, s:str) -> int:
        previous_value = 0
        total_value = 0
        for char in reversed(s):
            current_value = self.dict[char]
            if current_value >= previous_value:
               total_value += current_value
               
            else:                                   # current_value is less than previous_value
               total_value -= current_value
            previous_value = current_value          # previous_value is updated only after if - else is completed
        return total_value

obj = Solution()
print(obj.roman_To_Int_complete('LVIII'))