#problem: https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/


class Solution:
    def maxProduct(self, s: str) -> int:
        def is_palindrome(subsequence):
            return subsequence == subsequence[::-1]
    
        n = len(s)
        max_product = 0
        subseq_lengths = {}
        for mask in range(1, 1 << n):
            subseq = ''.join(s[i] for i in range(n) if mask & (1 << i))
            if is_palindrome(subseq):
                subseq_lengths[mask] = len(subseq)
        for mask1 in subseq_lengths:
            for mask2 in subseq_lengths:
                if mask1 & mask2 == 0:  
                    max_product = max(max_product, subseq_lengths[mask1] * subseq_lengths[mask2])
        
        return max_product