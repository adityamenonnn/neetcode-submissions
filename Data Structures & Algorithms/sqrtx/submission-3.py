class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0 
        l=0
        r = x
        while l<=r:
            mid = (l+r)//2
            if mid**2>x:
                r = mid - 1
            elif mid**2<x:
                res = mid
                l = mid +1
            else:
                return mid
        
        return res
