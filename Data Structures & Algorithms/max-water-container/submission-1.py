class Solution:
    def maxArea(self, heights: List[int]) -> int:
        Area = 0
        l = 0 
        r = len(heights)-1

        while l<r:
            area = (r-l)* min(heights[r],heights[l])
            if area>Area:
                Area=area
            
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return Area