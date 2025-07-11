'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: list[int], target:int ) -> list[int]:
        # This function definition says that nums is expected to be a list of int, target is a int variable and the function will return a list including int
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
    
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
                    
                
    