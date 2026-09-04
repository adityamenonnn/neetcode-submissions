class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #n^2 would be to take each of the elements and then checking, it would just overlook the logn of binary search
        # we know each row is sorted so we can just check if its greater than the greatest element or lesser than the least element

        top = 0 
        bottom = len(matrix)-1
        while top<=bottom:
            row = (top+bottom)//2

            #if target is greater than largest element in the curent row, then the actual row will be below
            if target>matrix[row][-1]:
                top = row +1

            #if the target is lesser than the lowest element, then the actual row is above
            elif target<matrix[row][0]:
                bottom = row -1

            else:
                break


        final_row = (top+bottom)//2 
        l=0
        r = len(matrix[final_row])-1
        while l<=r:
            mid = (l+r)//2
            if target > matrix[final_row][mid]:
                l = mid + 1
            elif target < matrix[final_row][mid]:
                r = mid - 1
            else:
                return True
        return False

