# Find the maximum number of your content children that can be satisfied given the cookies.
# Problem Link: https://leetcode.com/problems/assign-cookies/

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child, cookie = 0, 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        
        return child