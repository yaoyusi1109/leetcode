# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a, b = 0, 1
        k = 0
        for b in range(1, len(nums)):
            if nums[a] == val:
                nums[a] = nums[b]
            a += 1
        for i in nums:
            if i != val:
                k += 1
        return k 
            
                
            
                
                
        
                
        