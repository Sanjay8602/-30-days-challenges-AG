# Problem: Combination Sum III
# Link: https://leetcode.com/problems/combination-sum-iii/


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def backtrack(start, remaining_sum, combination):
            if len(combination) == k and remaining_sum == 0:
                result.append(combination[:])
                return
            if len(combination) > k or remaining_sum < 0:
                return
            for i in range(start, 10):
                combination.append(i)
                backtrack(i + 1, remaining_sum - i, combination)
                combination.pop()
        backtrack(1, n, [])
        return result