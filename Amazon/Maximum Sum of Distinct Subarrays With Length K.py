#Problem Link: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
#Title: Maximum Sum of Distinct Subarrays With Length K


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        cs = 0
        ms = 0
        seen = set()
        
        for end in range(len(nums)):
            cs += nums[end]
            
            while nums[end] in seen:
                seen.remove(nums[s])
                cs -= nums[s]
                s += 1
            
            seen.add(nums[end])
            
            if end - s + 1 == k:
                ms = max(ms, cs)
                seen.remove(nums[s])
                cs -= nums[s]
                s += 1
        
        return ms