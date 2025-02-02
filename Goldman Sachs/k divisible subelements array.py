#Problem: K divisible subelements array
#Link: https://leetcode.com/problems/k-divisible-elements-subarrays/description/


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        seen = set()
        for i in range(len(nums)):
            divisible_count = 0
            subarray = []
            
            for j in range(i, len(nums)):
                subarray.append(nums[j])
                if nums[j] % p == 0:
                    divisible_count += 1
                if divisible_count > k:
                    break
                seen.add(tuple(subarray))
        
        return len(seen)