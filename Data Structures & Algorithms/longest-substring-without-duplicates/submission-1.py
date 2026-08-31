class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        CharSet = set()
        result = 0 
        l = 0
        
        for r in range(len(s)):
            #duplicates 
            while s[r] in CharSet:
                CharSet.remove(s[l])
                l+=1
            CharSet.add(s[r])
            result = max(result, r-l+1)
        return result