#Problem: 396. Rotate Function
# Link: https://leetcode.com/problems/rotate-function/


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n= len(nums)
        ts= sum(nums)
        F = sum(i * nums[i] for i in range(n))
        max_value = F
        for k in range(1, n):
        
            F += ts - n * nums[-k]
            max_value = max(max_value, F)
    
        return max_value