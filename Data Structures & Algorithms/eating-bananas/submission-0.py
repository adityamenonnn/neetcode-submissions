class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 # min speed
        r = max(piles) #max speed

        while l<=r:
            mid = (l+r)//2
            hours = 0 
            for p in piles:
                hours+=math.ceil(p/mid) #if speed greater than number of banana, max 1 hour
            
            if hours<=h: #if its valid
                k = mid
                #check if there can be a minimum one
                r = mid - 1
            else:
                l = mid +1
        
        return k
