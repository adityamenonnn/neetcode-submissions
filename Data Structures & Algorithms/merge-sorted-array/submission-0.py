class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = m-1
        y = n-1
        z = m+n-1

        while y>=0:
            while x>=0 and nums1[x]>nums2[y]:
                nums1[z]=nums1[x]
                x-=1
                z-=1
            else:
                nums1[z]=nums2[y]
                y-=1
                z-=1
        
        return nums1


        