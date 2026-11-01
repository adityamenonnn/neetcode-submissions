class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def robline(houses):
            dp = [0,0]+houses
            for i in range(2,len(dp)):
                dp[i]= max(dp[i-1],dp[i]+dp[i-2])
            return dp[-1]
        n = len(nums)
        return max(robline(nums[0:n-1]),robline(nums[1:n]))
