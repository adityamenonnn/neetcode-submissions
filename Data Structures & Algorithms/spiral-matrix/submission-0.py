class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        left = 0 
        right = len(matrix[0])
        top = 0 
        bottom = len(matrix)
        res = []
        while left<right and top<bottom:
            #get all top column
            for i in range(left,right):  #r is not included, thats why we do r = len(matrix[0]) instead of it being len(matrix[0])-1
                res.append(matrix[top][i])
            top+=1

            #get rightmost now
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right-=1

            #handle a single column or a single row
            if not(left<right and top<bottom):
                break
            
            #get bottom most row
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1

            #get leftmost column
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left+=1

        return res

