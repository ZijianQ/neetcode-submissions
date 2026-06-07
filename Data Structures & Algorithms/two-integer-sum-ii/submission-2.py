class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(0, n):
            s = target - numbers[i]
            for j in range(n-1, i, -1):  # 从后往前找
                if numbers[j] == s:  # 用 == 比较
                    return [i+1, j+1]
            