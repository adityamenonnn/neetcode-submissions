class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)
        r = sum(weights)
        res = r
        while l<=r:
            mid = (l+r)//2

            count = 1
            s = 0 
            for w in weights:
                if s+w>mid:
                    count+=1
                    s = 0 
                s+=w
            

            
            if count<=days:
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid+1
        
        return res

        