class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        for i in range(n):

            right_most = i 
            while right_most+1 <n and  heights[right_most+1] >= heights[i]:
                right_most +=1
            left_most = i
            while left_most-1 >= 0 and  heights[left_most-1] >= heights[i]:
                left_most -=1
            max_area = max(max_area, heights[i]*(right_most - left_most+1))
        return max_area


        