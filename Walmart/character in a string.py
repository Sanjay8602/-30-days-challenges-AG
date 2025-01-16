#Problem: Extra Characters in a String
#Link: https://leetcode.com/problems/extra-characters-in-a-string/submissions/1510796469/


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        word_set = set(dictionary)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0 
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            for j in range(i + 1, n + 1):
                if s[i:j] in word_set:
                    dp[i] = min(dp[i], dp[j])        
        return dp[0]