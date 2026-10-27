class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0 
        bottom = len(matrix)-1
        
        while top<=bottom:
            mid = (top+bottom)//2
            if target>matrix[mid][-1]:
                top = mid + 1
            elif target<matrix[mid][0]:
                bottom = mid - 1
            else:
                break
        
        finalrow = matrix[mid]
        l = 0 
        r = len(finalrow)-1
        while l<=r:
            mid = (l+r)//2
            if finalrow[mid]<target:
                l= mid+1
            elif finalrow[mid]>target:
                r  = mid-1
            else:
                return True
        return False
        


        