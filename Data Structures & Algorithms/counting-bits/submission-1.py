class Solution:
    def countBits(self, n: int) -> List[int]:
        res= [0] * (n+1)


        for i in range(1,n+1):
            n = i
            
            while n !=0:
                n &= (n- 1)
                res[i]+=1
            

        return res

        
        