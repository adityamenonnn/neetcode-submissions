class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set (nums)
        maxLen = 0
        for i in nums:
            if i-1 not in numSet:
                curr = i 
                length = 1
                while curr+1 in numSet:
                    curr = curr+1
                    length +=1
                maxLen = max(length,maxLen)
        return maxLen 
                
            