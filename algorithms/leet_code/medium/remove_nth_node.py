# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from types import NoneType
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_node(head: 'ListNode', n: int) -> 'ListNode':
    def get_list_length(head: 'ListNode') -> int:
        length = 0
        point = head
        while point != None:
            length = length + 1
            point = point.next

        return length

    length = get_list_length(head)
    
    i = length - n
    point = head
    prev: 'ListNode' = None

    while i != 0:
        prev = point
        point = point.next
        i = i - 1
    
    if prev == None:
        head = head.next
    elif point.next == None:
        prev.next = None
    else:
        prev.next = point.next
    
    return head
