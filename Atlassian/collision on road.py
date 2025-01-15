#Problem:Count Collision on road
#Link: https://leetcode.com/problems/count-collisions-on-a-road/

class Solution:
    def countCollisions(self, directions: str) -> int:
        directions= directions.lstrip('L').rstrip('R')
        c=0
        for co in directions:
            if co!='S':
                c+=1
        return c