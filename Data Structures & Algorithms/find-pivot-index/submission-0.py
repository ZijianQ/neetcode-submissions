class Solution:
    def prefix(self, nums):
        res =[]
        total =0
        for n in nums:
            total +=n
            res.append(total)

        return res

    def pivotIndex(self, nums: List[int]) -> int:
        pre = self.prefix(nums)
        R = 0
        for L in range(len(nums)):
            
            right = pre[-1]
            if pre[L] -nums[L] == right - pre[L]:
                return L


        return -1
        