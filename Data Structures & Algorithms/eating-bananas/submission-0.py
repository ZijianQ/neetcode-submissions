class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def total_hour(k: int) -> int:
            total = 0
            for p in piles:
                total += (p + k - 1) // k
            return total

        l, r = 1, max(piles)  # 二分的是速度 k，不是 piles 下标

        while l < r:
            m = (l+r) // 2
            if total_hour(m) <= h:
                r = m          #
            else:
                l = m + 1      
        return l


        




            

            
        