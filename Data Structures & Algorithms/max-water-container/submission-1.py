class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lentgh = len(heights)
        left = 0
        right = lentgh - 1
        result = []

        for i in range(lentgh):
            height = min(heights[left], heights[right])
            area = height * (right - left)
            result.append(area)
            if heights[left] <= heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1

        return max(result)
