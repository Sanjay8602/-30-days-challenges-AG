# Problem: Kth Smallest Element Query
# Link: https://leetcode.com/problems/query-kth-smallest-trimmed-number/


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        result= []
        for k,j in queries:
            trimmed = [(num[-j:], i) for i, num in enumerate(nums)]
            trimmed.sort(key=lambda x: (x[0], x[1]))
            result.append(trimmed[k - 1][1])
        return result