#Problem: amount-of-time-for-binary-tree-to-be-infected
# Link: https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def buildGraph(node, parent):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                buildGraph(node.left, node)
                buildGraph(node.right, node)
        
        graph = defaultdict(list)
        buildGraph(root, None)
        queue, visited, minutes = deque([start]), set([start]), 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            if queue: minutes += 1

        return minutes