# Find the Index of the FIrst Occurence in a String

# Given two strings needle and haystack, return the index of the first 
# occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i 
        return -1
        
        