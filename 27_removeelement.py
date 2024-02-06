# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a, b = 0, 0
        for a in range(len(nums)):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
        return b 
            
                
            
                
                
        
                
        