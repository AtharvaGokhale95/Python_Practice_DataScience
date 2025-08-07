class Solution:
    def sqrt_builtin(self, n : int) -> int:
        return n**0.5
    
    def sqrt_heron(self, n : int, tolerance = 1e-10) -> int:
        x = n
        while True:
            root = 0.5 * (x + n/x)
            if abs(root - x) < tolerance:
                return root
            x = root
    
    def sqrt_binary(self, n:int) -> int:
        if n <2:
            return n
        
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2         # Determined the middle number between 1 and n
            if mid * mid == n:
                return mid
            if mid * mid < n:
                low = mid + 1
            else:
                high = mid - 1
        return high
            
        
s = Solution()
print(s.sqrt_builtin(25))
print(s.sqrt_heron(25))
print(s.sqrt_binary(25))