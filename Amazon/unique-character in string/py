#Problem: Given a string, find the first non-repeating character in it and return its index.
#Problem link: https://leetcode.com/problems/first-unique-character-in-a-string/
#Technique: Hashing


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cc={}
        for i in s:
            cc[i]= cc.get(i,0)+1
        for i,j in enumerate(s):
            if cc[j]==1:
                return i
        return -1