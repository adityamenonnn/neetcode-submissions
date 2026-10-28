class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            #left sorted portion as in the graph
            if nums[l]<=nums[mid]:
                if target < nums[l] or target>nums[mid]:
                    l = mid + 1
                else: # target is less than the middle AND greater than the left, so it lies in the left sorted prition (DEMORGAN)
                    r = mid - 1
            #right sorted portion
            else:
                if target>nums[r] or target< nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


                