#Problem: Find in mountain array
#Link: https://leetcode.com/problems/find-in-mountain-array/


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def findPeak(mountainArr):
            left, right = 0, mountainArr.length() - 1
            while left < right:
                mid = (left + right) // 2
                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def binarySearch(mountainArr, target, left, right, isIncreasing):
            while left <= right:
                mid = (left + right) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                if isIncreasing:
                    if val < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if val > target:
                        left = mid + 1
                    else:
                        right = mid - 1
            return -1
        peak = findPeak(mountainArr)
        leftResult = binarySearch(mountainArr, target, 0, peak, True)
        if leftResult != -1:
            return leftResult
        return binarySearch(mountainArr, target, peak + 1, mountainArr.length() - 1, False)