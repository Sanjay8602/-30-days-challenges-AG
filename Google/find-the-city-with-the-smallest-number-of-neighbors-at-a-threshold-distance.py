#Problem: find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance
#Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF= float('inf')
        graph = [[INF] * n for _ in range(n)]

        for i in range(n):
            graph[i][i]=0
        
        for u, v, weight in edges:
            graph[u][v] = weight
            graph[v][u] = weight
    
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        min_reachable = float('inf')
        result_city = -1

        for i in range(n):
            count = sum(1 for j in range(n) if graph[i][j] <= distanceThreshold)
            if count < min_reachable or (count == min_reachable and i > result_city):
                min_reachable = count
                result_city = i

        return result_city