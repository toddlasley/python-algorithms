# 2.3: Implement an algorithm to delete a node in the middle, given only access to that node.

# Solution: p. 211

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def delete_node(node: 'ListNode') -> None:
    if node and node.next:
        node.val = node.next.val
        node.next = node.next.next
