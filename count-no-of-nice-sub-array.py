# URL: https://leetcode.com/problems/count-number-of-nice-subarrays/
#problem: Count Number of Nice Subarrays


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmostk(nums, k):
            l=0
            c=0
            odd_count=0
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    odd_count += 1
                while odd_count > k:
                    if nums[l] % 2 != 0:
                        odd_count -= 1
                    l += 1
                c += i-l+1
            return c
        return atmostk(nums, k) - atmostk(nums, k - 1)


        