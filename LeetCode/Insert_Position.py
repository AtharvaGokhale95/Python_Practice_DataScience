from typing import List
class Solution:
    # Time Complexity: O(n)
    def searchInsert(self, nums:List[int], target:int) -> int:
        for idx in range(0, len(nums)):
            if nums[idx] >= target:
                return idx                  # This is applicable if the target <= nums[len(nums) - 1], less than the last element in nums
        return len(nums)                    # If target > nums[len(nums) - 1], greater than the last element in nums, it will be inserted at the last idx, nums[len(nums)]
    
    # Time Complexity: O(log n) - Binary Search     
    def search_insert_binary(self, nums: List[int], target:int) -> int:
        left, right = 0, len(nums) - 1      # Initialized left to the 0th idx and right to the last idx of the nums array
        
        while left <= right:
            mid = (left + right) // 2         # a // b returns the quotient , mid returns the centre idx of  the nums array
            
            if nums[mid] == target:             # If the target value is found at the (mid)th idx in nums, then return mid
                return mid
        
            elif nums[mid] < target:              # Search the Right - Half of the array
                left = mid + 1
            elif nums[mid] > target:              # Search the Left - Half of the array
                right = mid - 1

        return left                         # left is that idx which we will be updating and then use to insert the new value in the list
        

s = Solution()
print(s.searchInsert([1, 3, 5, 6], 7))
print(s.search_insert_binary([1, 7, 19, 86, 177, 353, 798], 436))
                
                
            