# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        interval = 1
        amount = len(lists)

        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = Solution.__merge_two_lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if amount > 0 else None


    def __merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
        head = point = ListNode()

        while l1 and l2:
            if (l1.val < l2.val):
                point.next = ListNode(l1.val)
                l1 = l1.next
            else:
                point.next = ListNode(l2.val)
                l2 = l2.next
            
            point = point.next
            
        if l1:
            point.next = l1
        else:
            point.next = l2

        return head.next
