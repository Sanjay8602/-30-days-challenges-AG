# Problem: Count number of square free subsets
# Source: https://leetcode.com/problems/count-number-of-square-free-subsets/

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        prime_masks = {}
        for num in range(1, 31):
            mask = 0
            square_free = True
            for i, prime in enumerate(primes):
                if num % (prime * prime) == 0: 
                    square_free = False
                    break
                if num % prime == 0:
                    mask |= (1 << i)
            if square_free:
                prime_masks[num] = mask
        dp = [0] * (1 << len(primes))
        dp[0] = 1  
        
        for num in nums:
            if num not in prime_masks:
                continue
            num_mask = prime_masks[num]
            for mask in range((1 << len(primes)) - 1, -1, -1):
                if mask & num_mask == 0: 
                    dp[mask | num_mask] = (dp[mask | num_mask] + dp[mask]) % MOD
 
        return (sum(dp) - 1) % MOD