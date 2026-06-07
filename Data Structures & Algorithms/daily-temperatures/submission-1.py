class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        res = [0] * n
        
        for t in range(n - 1):
            l = 0
            for j in range(t + 1, n):
                l += 1
                if temperatures[j] > temperatures[t]:
                    res[t] = l
                    break
        
        return res



        