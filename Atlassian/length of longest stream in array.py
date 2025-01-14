# Problem: Length of Longest Subarray with At Most K Frequency
#Url: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int) 
        start = 0
        max_length = 0

        for end in range(len(nums)):
            freq[nums[end]] += 1
            while freq[nums[end]] > k:
                freq[nums[start]] -= 1
                if freq[nums[start]] == 0:
                    del freq[nums[start]] 
                start += 1
            max_length = max(max_length, end - start + 1)

        return max_length