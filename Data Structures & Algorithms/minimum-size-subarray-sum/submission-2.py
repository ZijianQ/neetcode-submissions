class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")

        value = 0
        L = 0
        for R in range(0, len(nums)):
            value+=nums[R]
            while value >= target:
                
                res = min(res, R-L+1)
                value -= nums[L]
                L +=1

            

            
        return res if res!= float("inf") else 0


        