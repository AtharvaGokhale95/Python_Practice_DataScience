'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
from typing import List
class Solution:

#     def twoSum(self, nums:list[int], target:int ) -> list[int]:
#         # This function definition says that nums is expected to be a list of int, target is a int variable and the function will return a list including int
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
#         return []
    
# sol = Solution()
# print(sol.twoSum([2, 7, 11, 15], 9))
# # Time complexity: O(n^2)


# Using dictionary: Time complexity: O(n)

    def twoSum(self, nums:List[int], target:int) -> List[int]:
        num_dict = {}                                               # This dict will be empty for the first iteration
        for i, num in enumerate(nums):                              # This for loop runs over each key-value pair using the enumerate
            diff = target - num                                     # calculate diff 
            if diff in num_dict:                                    # if value of diff is already present in num_dict then we have found the other value
                return [num_dict[diff], i]              
            num_dict[num] = i                                       # if diff is not already present in num_dict, we save the key(index) - value(value at the index) in dict 
            #print(num_dict)
        return []

    
sol = Solution()                                                    # Created a object of the class Solution
print(sol.twoSum([2, 7, 11, 15], 17))                               # Called method twoSum using the instance of the Class



# When we call a method using object.method(), the self parameter is assigned to object


        

                    
    
                
    