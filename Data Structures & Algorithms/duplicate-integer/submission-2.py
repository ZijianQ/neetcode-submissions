class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tran = []
        n = len(nums)
        for i in range(0,n):
            if nums[i] not in tran:
                tran.append(nums[i])
            else:
                return True
        return False

        