from typing import List
class Solution:
    def remove_element(self, nums:List[int], val:int) -> int:
        if not nums:
            return 0
        
        write_idx = 0
        for read_idx in range(0, len(nums)):
            if nums[read_idx] != val:
                nums[write_idx] = nums[read_idx]
                write_idx += 1
        return write_idx

        del nums[write_idx:]

s = Solution()
print(s.remove_element([1,2,3,1,5], 1))