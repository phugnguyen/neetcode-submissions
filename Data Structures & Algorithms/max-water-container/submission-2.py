class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        while left < right:
            
            if (heights[left] <= heights[right]):
                currArea = heights[left]*(right - left)
                area = max(area, currArea)
                left += 1
            else:
                currArea = heights[right]*(right - left)
                area = max(area, currArea)
                right -= 1
        return area

