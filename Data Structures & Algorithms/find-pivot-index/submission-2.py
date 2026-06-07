class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return -1
        prefixSum = [0] * n 
        prefixSum[0] = nums[0]
        for i in range(1,n):
            prefixSum[i ] = prefixSum[i-1] + nums[i]

        for i in range(n):
            leftSum = prefixSum[i-1]if i > 0 else 0
            rightSum = prefixSum[-1] - prefixSum[i]
            if leftSum == rightSum:
                return i
        return -1
        