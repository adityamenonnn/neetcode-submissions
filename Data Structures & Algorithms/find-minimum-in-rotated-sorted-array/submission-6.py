class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("infinity")
        l = 0 
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2

            if nums[mid]>nums[r]:
                l = mid+1
            else:
                res = min(nums[mid],res)
                r = mid -1
        return res