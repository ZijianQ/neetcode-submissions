class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:return False

        row , col = len(matrix), len(matrix[0])

        l, r = 0, row*col -1

        while l <= r :
            m = (r+l)//2 
            ro, co = m// col, m % col

            if target == matrix[ro][co]:
                return True
            elif target > matrix[ro][co]:
                l = m +1
            else: r = m-1

        return False



        
            

        