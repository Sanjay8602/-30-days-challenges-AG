# Url: https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
# Title: Random Point in Non-overlapping Rectangles
# Using the same concept of prefix sum, we can solve this problem in O(logn) time complexity.


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = list(accumulate((x - a + 1) * (y - b + 1) for a, b, x, y in rects))

    def pick(self) -> List[int]:
        target = random.randint(1, self.areas[-1])
        rect_idx = next(i for i, area in enumerate(self.areas) if target <= area)
        a, b, x, y = self.rects[rect_idx]
        return [random.randint(a, x), random.randint(b, y)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()