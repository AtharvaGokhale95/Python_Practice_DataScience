class Solution:
    def convertBinaryToDecimal(self, b:str) -> int:
        decimal = 0
        n = len(b)
        for idx, digit in enumerate(b):
            decimal = decimal + int(digit) * (2** (n - idx -1))
        return decimal
    
    def add_binary(self, a:str, b:str) -> str:
        # First we need to ensure that both the strings are of the same length
        width = max(len(a), len(b))
        a = a.zfill(width)
        b = b.zfill(width)
        
        # In binary addition, we have a result and a carry as two variable
        result = ""
        carry = 0
        
        # We need to traverse in the reverse direction for addition 
        for idx in range(width-1, -1, -1):  # Range starts from last char: width-1, Go up to -1th char means it will stop at 0th char, step = -1: Reverse direction 
            total = carry                                   # After every iteration we will be updating the total with carry to recursively update the total below
            total = total + int(a[idx]) + int(b[idx])       # Here, if we have 1 + 1, it will return 2. But to have binary addition, we have foll logic
            result = str(total % 2) + result                # Handle: 1 + 1 = carry = 1 and result = 0 
            carry = total // 2                              # This produces: 1 + 1 = 2//2 = 1, 1 + 1 + 1 = 3//2 = 1                          
        if carry:
            result = '1' + result
        return result
    
s = Solution()
#print(s.convertBinaryToDecimal("1010"))
print(s.add_binary("1101", ))

