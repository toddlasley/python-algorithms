# 2.4: Write code to partition a linked list around a value x, such that all
# nodes less than x come before all nodes greater than or equeal to x. The
# order of the values does not matter so long as values less than x come before
# those that are greater than or equal to x.

# Solution: p. 212

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def partition(head: 'ListNode', x: int) -> 'ListNode':
    point = head
    head = last = None
    right = None

    while point:
        if point.val >= x:
            temp = point
            point = point.next
            temp.next = right       
            right = temp
        else:
            if not last:
                last = point

            temp = point
            point = point.next
            temp.next = head
            head = temp

    if last:
        last.next = right
        return head
    else:
        return right
