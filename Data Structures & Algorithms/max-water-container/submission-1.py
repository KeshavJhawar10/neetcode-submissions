class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            width = r - l 
            height = min(heights[l], heights[r])
            area = width * height
            max_area = max(max_area, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1
        return max_area

