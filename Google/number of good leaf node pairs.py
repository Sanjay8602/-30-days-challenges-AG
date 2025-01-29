#Problem: Number of Good Leaf Nodes Pairs
#Problem: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        def dfs(node):
            if not node:
                return defaultdict(int)
            if not node.left and not node.right:
                return {1: 1}
            
            left_counts = dfs(node.left)
            right_counts = dfs(node.right)
            nonlocal result
            for d1, c1 in left_counts.items():
                for d2, c2 in right_counts.items():
                    if d1 + d2 <= distance:
                        result += c1 * c2 
            new_counts = defaultdict(int)
            for d, count in left_counts.items():
                if d + 1 <= distance:
                    new_counts[d + 1] += count
            for d, count in right_counts.items():
                if d + 1 <= distance:
                    new_counts[d + 1] += count

            return new_counts

        result = 0
        dfs(root)
        return result