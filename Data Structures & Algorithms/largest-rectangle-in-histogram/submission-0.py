class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for right in range(n):
            cur_min = heights[right]
            for left in range(right, -1, -1):   # 向左扩展
                cur_min = min(cur_min, heights[left])
                width = right - left + 1
                max_area = max(max_area, cur_min * width)
        return max_area
        