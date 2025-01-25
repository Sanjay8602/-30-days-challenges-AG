#Problem: Sum of scores of built strings
#Link: https://leetcode.com/problems/sum-of-scores-of-built-strings/
class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        Z = [0] * n
        l, r, k = 0, 0, 0
        
        for i in range(1, n):
            if i <= r:
                Z[i] = min(r - i + 1, Z[i - l])
            while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
                Z[i] += 1
            if i + Z[i] - 1 > r:
                l, r = i, i + Z[i] - 1
        
        return sum(Z) + n