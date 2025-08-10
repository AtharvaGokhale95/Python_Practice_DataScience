class Solution:
    def climbStairs_recursion(self, n:int) -> int:
        # Here we have 2 choices: To get to step n, I could have come from step n-1 or n-2
        # 1. Take 1 step -> reach n
        # 2. Take 2 steps -> reach n 
        # Total no of ways to reach step n: ways(n) = ways(n - 1) + ways(n - 2)
        # We set the anchor conditions for the recursion
        if n <= 0:
            return 1
        return self.climbStairs_recursion(n - 1) + self.climbStairs_recursion(n - 2)
    """"
    climbStairs(3)
├── climbStairs(2)
│   ├── climbStairs(1) → 1
│   └── climbStairs(0) → 1
├── climbStairs(1) → 1
    """

s = Solution()
print(s.climbStairs_recursion(3))

