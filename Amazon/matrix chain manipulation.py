#Problem: Matrix Chain Malipulation
# URL: https://practice.geeksforgeeks.org/problems/brackets-in-matrix-chain-multiplication1024/1


#User function Template for python3

class Solution:
    def matrixChainOrder(self, arr):
        # code here
        n = len(arr)
        dp = [[0] * n for _ in range(n)] 
        split = [[-1] * n for _ in range(n)]
        for length in range(2, n):  
            for i in range(1, n - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")  
                for k in range(i, j):  
                    cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        split[i][j] = k
        def buildOptimalOrder(i, j):
            if i == j:
                return chr(65 + i - 1)  
            k = split[i][j]
            left = buildOptimalOrder(i, k)
            right = buildOptimalOrder(k + 1, j)
            return f"({left}{right})"
        optimal_order = buildOptimalOrder(1, n - 1)
        return optimal_order