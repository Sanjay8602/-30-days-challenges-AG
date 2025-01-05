# Problem: Excel Sheet Column Title
#problem link: https://leetcode.com/problems/excel-sheet-column-title/


class Solution:
    def convertToTitle(self, cn: int) -> str:
        r = []
        while cn > 0:
            cn -= 1
            r.append(chr(cn % 26 + ord('A')))
            cn //= 26
        return ''.join(r[::-1])