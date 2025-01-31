#Problem: Max Sum of BST in Binary Tree
#Problem: https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (True, 0, float('inf'), float('-inf'), 0)  
            
            leftIsBST, leftSum, leftMin, leftMax, leftMaxSum = dfs(node.left)
            rightIsBST, rightSum, rightMin, rightMax, rightMaxSum = dfs(node.right)
            if leftIsBST and rightIsBST and leftMax < node.val < rightMin:
                currSum = leftSum + node.val + rightSum
                return (True, currSum, min(leftMin, node.val), max(rightMax, node.val), max(leftMaxSum, rightMaxSum, currSum))
            else:
                return (False, 0, 0, 0, max(leftMaxSum, rightMaxSum))

        return dfs(root)[4] 