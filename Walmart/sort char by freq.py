# Problem: Sort Characters By Frequency
# Source: https://leetcode.com/problems/sort-characters-by-frequency/


class Solution:
    def frequencySort(self, s: str) -> str:
        f= Counter(s)
        sorted_chars = sorted(f.items(), key=lambda x: -x[1])
        result = ''.join(char * count for char, count in sorted_chars)
        return result