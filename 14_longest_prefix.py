# Write a function to find the longest common prefix string 
# amongst an array of strings. If there is no common prefix, 
# return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:    
        
        shortest = min(strs, key = len)
        
        if len(shortest) == 0:
            return ""
        
        for index, val in enumerate(shortest):
            for words in strs:
                if words[index] != val:
                    return shortest[:index]
        return shortest
    
def main():
    s = Solution()
    strs = ["ab", "a"]
    result = s.longestCommonPrefix(strs)
    print(result)

if __name__ == "__main__":
    main()
