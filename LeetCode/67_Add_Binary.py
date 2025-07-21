class Solution:
    def convertBinaryToDecimal(self, b:str) -> int:
        decimal = 0
        n = len(b)
        for idx, digit in enumerate(b):
            decimal = decimal + int(digit) * (2** (n - idx -1))
        return decimal

s = Solution()
print(s.convertBinaryToDecimal("1010"))