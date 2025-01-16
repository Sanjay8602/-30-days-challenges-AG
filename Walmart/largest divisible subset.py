#Problem: Largest Divisible Subset
#https://leetcode.com/problems/largest-divisible-subset/


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        
        nums.sort() 
        dp = [1] * n
        prev = [-1] * n 
        
        max_size = 0
        max_index = -1
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]
        
        return result[::-1]