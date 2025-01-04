# Url: https://leetcode.com/problems/repeated-dna-sequences/
# Title: Repeated DNA Sequences


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<10:
            return []
        char_to_bit = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    
        seen = set()
        repeated = set()
        bitmask = 0
        for i in range(len(s)):
            bitmask = ((bitmask << 2) | char_to_bit[s[i]]) & ((1 << 20) - 1)
            if i >= 9:
                if bitmask in seen:
                    repeated.add(s[i - 9:i + 1])  
                else:
                    seen.add(bitmask)
    
        return list(repeated)