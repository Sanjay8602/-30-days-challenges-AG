# URL: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# Solution: Using binary search to find the distance between two arrays

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count= 0
        for i in arr1:
            l= i-d
            r= i+d
            left_idx = bisect_left(arr2, l)
            right_idx = bisect_right(arr2, r)
            if left_idx == right_idx:
                count += 1
        return count
