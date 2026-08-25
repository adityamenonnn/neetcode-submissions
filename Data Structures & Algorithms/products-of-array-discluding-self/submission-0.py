class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)

        result = [1]*n

        prefix = 1
        for i in range (n):
            result[i]=prefix #sets the first element to 1
            prefix = prefix * nums[i]
        
        suffix = 1
        #from the back
        for i in range(n-1,-1,-1):
            result[i]*=suffix
            suffix = suffix * nums[i]

        return result

            

