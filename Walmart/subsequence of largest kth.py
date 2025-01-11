#Problem link: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/submissions/1505358013/
#Solution: Using indexed sort and then sorting the indexed list based on the index


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort(key=lambda x: x[0], reverse=True)
        top_k = sorted(indexed_nums[:k], key=lambda x: x[1])
        result = [num for num, _ in top_k]
        
        return result