class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1
        res = nums[0]

        while l<=r:
            mid = (l+r)//2

            #if mid is bigger than the right end, the rotation point (min) is to the right
            if nums[mid]>nums[r]:
                l = mid+1

            #mid is smaller than right end, so mid itself could be the min
            #record it, then keep looking left for something smaller
            else:
                res = min(res,nums[mid])
                r = mid - 1

        return res