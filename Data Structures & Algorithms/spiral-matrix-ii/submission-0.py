class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
    


        res = [[0]*n for _ in range(n)]
        top, bottom = 0 , n-1
        left, right = 0, n-1
        num = 1
        while top<= bottom and left<=right :
            for j in range(left, right+1):
                res[top][j] =num
                num +=1
            top +=1

            for  j in range(top, bottom+1):
                res[j][right] = num
                num +=1
            right-=1

            
            if top <= bottom:
                for i in range(right, left-1, -1):
                    res[bottom][i] = num
                    num +=1
                    
                bottom -=1

            if left <= right:
                for j in range(bottom, top-1, -1):
                    res[j][left] = num
                    num +=1
                left +=1
        
        return res