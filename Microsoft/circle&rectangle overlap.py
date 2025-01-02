#Problem: Circle and Rectangle Overlap
#Problem link: https://leetcode.com/problems/circle-and-rectangle-overlap/

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        cX = max(x1, min(xCenter, x2))
        cY = max(y1, min(yCenter, y2))
        ds = (cX - xCenter) ** 2 + (cY - yCenter) ** 2
        return ds <= radius ** 2