class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L = 0
        maxCur = nums[0]
        cur = 0

        for R in range(len(nums)):
            if cur < 0 :
                cur = 0
                L = R

            cur += nums[R]

            if cur > maxCur :
                maxCur  = cur

        return maxCur


        