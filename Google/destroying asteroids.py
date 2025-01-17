#Problem: Destroying asteroids
#Link: https://leetcode.com/problems/destroying-asteroids/


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for i in asteroids:
            if mass >= i:
                mass += i
            else:
                return False
        return True