class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        for L in range(n):
            cur = heights[L]
            for R in range(L, n):
                cur = min(cur , heights[R])   # 这里还要一个循环去找最小值
                max_area = max(max_area, cur * (R - L + 1))
        return max_area
        