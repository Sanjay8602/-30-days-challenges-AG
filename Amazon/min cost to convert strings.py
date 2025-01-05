#problem link: https://leetcode.com/problems/minimum-cost-to-convert-string-i/
#title: Minimum Cost to Convert String I


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        if n != len(target):
            return -1
        INF = float('inf')
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        for o, c, z in zip(original, changed, cost):
            dist[ord(o) - ord('a')][ord(c) - ord('a')] = min(dist[ord(o) - ord('a')][ord(c) - ord('a')], z)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            s_idx, t_idx = ord(s) - ord('a'), ord(t) - ord('a')
            if dist[s_idx][t_idx] == INF:
                return -1 
            total_cost += dist[s_idx][t_idx]
        
        return total_cost