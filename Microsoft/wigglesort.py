# Problem: 324. Wiggle Sort II
# Problem link: https://leetcode.com/problems/wiggle-sort-ii/


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()
        mid = (n - 1) // 2
        left = nums[:mid + 1]  
        right = nums[mid + 1:]
        for i in range(n):
            if i % 2 == 0:
                nums[i] = left.pop()  
            else:
                nums[i] = right.pop()