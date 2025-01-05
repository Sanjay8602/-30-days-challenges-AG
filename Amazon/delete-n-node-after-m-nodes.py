#problem: delete N nodes after M nodes of a linked list
#question link: https://practice.geeksforgeeks.org/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/1


# your task is to complete this Function
# Function shouldn't return anything

'''
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def linkdelete(self, head, n, m):
        if not head or n == 0:
            return head
        
        current = head
        
        while current:
            for _ in range(m - 1):
                if not current:
                    return head
                current = current.next
            if not current:
                return head
            temp = current.next
            for _ in range(n):
                if not temp:
                    break
                temp = temp.next
            current.next = temp
            current = temp
        
        return head