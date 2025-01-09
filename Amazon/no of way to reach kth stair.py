#Problem: number of ways to reach kth stair
# URL: https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

#Solution: First I coded from my way but some test cases were not passed. Then I saw the solution and coded it (converted to python).


class Solution:
    def __init__(self):
        self.memo = {}
        
    def waysToReachStair(self, k: int) -> int:
            return self.dp(1, k, 0, 0)

    def dp(self, position: int, k: int, direction: int, jump: int) -> int:
        if position < 0 or position > k + 1:
            return 0
        key = (position, direction, jump)
        if key in self.memo:
            return self.memo[key]
        ways = 1 if position == k else 0
        if position > 0 and direction != 1:
            ways += self.dp(position - 1, k, 1, jump)
        front_jump = position + (1 << jump)
        ways += self.dp(front_jump, k, 0, jump + 1)
        self.memo[key] = ways
        return ways