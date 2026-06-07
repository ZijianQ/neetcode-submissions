class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        medium = set(nums)
        res = 0

        for num in medium:
            if (num-1) not in medium:
                length = 1
                while (num+length) in medium:
                    length +=1
                res = max(length, res)
        return res


        