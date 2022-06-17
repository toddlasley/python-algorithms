from typing import Optional


# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's
# nodes (i.e., only nodes themselves may be changed.)

# https://leetcode.com/problems/swap-nodes-in-pairs/

class ListNode:
    def __init__(self, val=0, next: 'ListNode' = None):
        self.val = val
        self.next = next

def swap_linked_list_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None or head.next == None:
        return head
    else:
        a = head
        b = head.next
        c = head.next.next

        a.next = swap_linked_list_pairs(c)
        b.next = a

        return b
