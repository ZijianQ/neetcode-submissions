class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        for L in range(n):
            for R in range(L, n):
                h = min(heights[L:R+1])   # 这里还要一个循环去找最小值
                max_area = max(max_area, h * (R - L + 1))
        return max_area
        