from typing import List

# This solution does not remove the duplicates in place - It requires a new list
class Solution:
    def remove_duplicates(self, nums:List[int]) -> int:
        out_arr = []
        for idx in range(len(nums)):
            if nums[idx] in out_arr:
                pass
            else:
                out_arr.append(nums[idx])
        return len(out_arr), out_arr
    
    # In-place update of nums array:
    def remove_duplicates_inplace(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        write_idx = 1                                       # There will be at least 1 unique element in every array which is not empty. Thus initialize write_idx = 1
        for read_idx in range(1, len(nums)):                # We iterate from the 2nd element in nums array as we have already considered that the 1st element is unique
            if nums[read_idx] != nums[read_idx - 1]:        # Compare current value with the previous value
                nums[write_idx] = nums[read_idx]            # We will add the value at the current_idx to the nums array - This is how we update the array in place
                write_idx += 1                              # We add 1 to the count of unique elements in the nums array
                print(nums)
                # The first k elements in the list k are unique
                # After the last iteration, we will still see the last duplicate present in nums as, when read_idx reached to (len(nums) - 1)th idx, and the if the control doesn't enter the if loop, it returns the read_idx and leave the last duplicate in the nums arr as is
                print(list(set(nums)))                      # List without any duplicates
        return write_idx
    
    # In place update of non-sorted array:
    def remove_duplicates_inplace_nonsorted(self, nums:List[int]) -> int:
        if not nums:
            return 0
        
        seen = set()                                        # Declared a empty set
        write_idx = 0                                       # Initialize the count of unique elements to 0
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[write_idx] = num                       # Inplace update
                write_idx += 1
        return write_idx, nums[:write_idx]                  # Values in nums upto (write_idx)th index are already updated in place with the unique values 

s = Solution()
# print(s.remove_duplicates([1, 2, 2]))
# print(s.remove_duplicates_inplace([1,2,3,4,4,5,6,7,7]))
print(s.remove_duplicates_inplace_nonsorted([1,2,3,4,4,55,5,6,7,7]))      


        