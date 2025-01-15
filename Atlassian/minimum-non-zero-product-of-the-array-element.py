# Problem: minimum-non-zero-product-of-the-array-element
# Link: https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/


class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7
        def mod_exp(base, exp, mod):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result
        max_val = (1 << p) - 1 
        second_max = max_val - 1 
        power = (1 << (p - 1)) - 1 
        return (mod_exp(second_max, power, MOD) * max_val) % MOD




#Suggested by AI
def minNonZeroProduct(self, p: int) -> int:
    mod = 10**9 + 7
    return (pow(2**p-2, 2**(p-1)-1, mod) * (2**p-1)) % mod