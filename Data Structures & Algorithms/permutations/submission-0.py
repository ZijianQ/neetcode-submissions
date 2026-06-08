class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) ==1:
            return [nums]
        res = []

        perm =  self.permute( nums[1:])

        for p in perm:
            for j in range(len(p)+1):

                p.insert(j, nums[0])

                res.append(p.copy())

                p.pop(j)


        return res


        

        