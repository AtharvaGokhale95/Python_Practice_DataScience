from typing import List
class Solution:
    def merge(self, nums1: List[int], m : int, nums2 : List[int], n:int) -> None:
        # Modify nums1 In-Place: Always start with the last element
        # For inplace update: Always maintain pointers and update them
        # The nums1 array will originally have the space to hold m elements from nums1 and n elements from nums2
        
        # Pointers
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        # Start updating the nums1 in the reverse direction, from p
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # This is when there are only zeros in nums1 and nums2 have values > 0
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

s = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)
            