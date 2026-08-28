class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)


        #[0,2,0,3,1,2]
        #ML=[0,0,2,2,3,3]
        #MR=[3,3,3,2,2,0]
        #finding the maximum element to the left of the index
        #the maximum left for the first will always be 0
        #the maximum right for the last element will alw3ays be 0 
        maxLeft = [0]*n
        maxRight = [0]*n

        maxLeft[0]=height[0]
        for i in range(1,n):
            maxLeft[i]=max(maxLeft[i-1],height[i])

        maxRight[-1]=height[-1]
        for i in range(n-2,-1,-1):
            maxRight[i]=max(maxRight[i+1],height[i])


        total = 0
        for i in range(n):
            diff = min(maxLeft[i],maxRight[i])-height[i]
            if diff>0:
                total+=diff
        
        return total


