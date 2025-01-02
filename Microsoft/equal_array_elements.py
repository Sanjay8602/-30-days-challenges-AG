# Problem: 462. Minimum Moves to Equal Array Elements II
# Problem link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median= nums[len(nums)//2]
        move= sum(abs(i-median) for i in nums)
        return move