class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        slow = 0 
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break 
        
        slow2 = 0 
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow==slow2:
                return slow
                '''
        res = 0
        for i in nums:
            n = abs(i)
            if nums[n-1]<0:
                res = n
            nums[n-1]=-nums[n-1]
        return res
                