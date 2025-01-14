#Problem: 718. Maximum Length of Repeated Subarray
# Link: https://leetcode.com/problems/maximum-length-of-repeated-subarray/


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [0] * (m + 1)
        max_length = 0
        for i in range(1, n + 1):
            prev = 0
            for j in range(1, m + 1):
                temp = dp[j]
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = prev + 1
                    max_length = max(max_length, dp[j])
                else:
                    dp[j] = 0
                prev = temp  
        return max_length