class Solution:
    dict = {'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}
    
    # def roman_To_Int_partial(self, s:str) -> int:
    #     val = 0
    #     for char in s:
    #         val += dict[char]
    #     return val
    
    
    def roman_To_Int_complete(self, s:str) -> int:
        prev = 0
        total = 0
        for char in reversed(s):
            val = self.dict[char]
            if val > prev:
               total += val
               
            else:               # val is less than prev
               total -= val
            prev = val          # prev is updated only after if - else is completed
        return total

obj = Solution()
print(obj.roman_To_Int_complete('IX'))