class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set (nums)

        for i in nums:
            if i-1 not in numSet:
                current = i 
                length = 1
                while current + 1 in numSet:
                    current+=1
                    length+=1
                
                if length>longest:
                    longest = length
            
        return longest