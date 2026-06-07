class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        t, b = 0, n

        m = (t+b)//2
        row =0

        while t < b :
            m = (t+b)//2

            if  matrix[m][0]<=target <= matrix[m][-1]:
                row = m
                break
                
            elif target > matrix[m][-1]:
                
                t = m+1

            elif target < matrix[m][0]:
                
                b = m


        l,r = 0, len(matrix[0])-1
        while l <= r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True

        return False


            

        