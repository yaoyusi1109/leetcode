# Remove Duplicates from Sorted Array

# Slow-fast pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        count = 0
        while fast > len(nums):
            if nums[fast] != nums[slow]:
                nums[slow + 1] = nums[fast]
                count += 1
            if nums[fast] == nums[slow]:
                fast += 1
        return count, nums
        
        
            