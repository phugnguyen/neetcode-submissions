class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            diff = right - left
            area = diff * min(heights[left], heights[right])
            result = max(area, result)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1


        return result