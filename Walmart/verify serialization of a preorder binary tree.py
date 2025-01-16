#Problem: Verify Serialization of a Preorder Binary Tree
# Link: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        node= preorder.split(',')
        s=1
        for i in node:
            s-=1
            if s<0:
                return False
            if i != '#':
                s+=2
        return s==0