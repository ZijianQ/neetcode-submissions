class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}   # 普通 dict 就够了

        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if tmp in mp:
                return [mp[tmp], i + 1]   # 1-indexed
            mp[numbers[i]] = i + 1

        return []

        