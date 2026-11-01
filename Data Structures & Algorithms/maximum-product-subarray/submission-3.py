class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) #[-1] cant keep res = 0
        currMax, currMin = 1,1
        for i in nums:
            if i==0:
                currMax, currMin = 1,1
                continue
            temp = currMax*i
            currMax = max(currMax*i,currMin*i,i) #[-1,8]
            currMin = min(temp,currMin*i,i)
            res = max(res, currMax)
        return res

            

