# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None or l2 == None:
            if l1 == None:
                return l2
            else:
                return l1
        
        longer: ListNode
        shorter: ListNode

        if Solution.get_linked_list_size(l1) < Solution.get_linked_list_size(l2):
            longer = l2
            shorter = l1
        else:
            longer = l1
            shorter = l2

        result = ListNode()
        runner = result
        remainder = 0
        
        while shorter != None:
            sum = longer.val + shorter.val + remainder
            remainder = 0

            if sum > 9:
                remainder = 1
                runner.val = sum - 10
            else:
                runner.val = sum

            shorter = shorter.next
            longer = longer.next

            if longer != None:
                runner.next = ListNode()
                runner = runner.next
        
        while longer != None:
            sum = longer.val + remainder
            remainder = 0

            if sum > 9:
                remainder = 1
                runner.val = sum - 10
            else:
                runner.val = sum

            longer = longer.next

            if longer != None:
                runner.next = ListNode()
                runner = runner.next
        
        if remainder == 1:
            runner.next = ListNode(1)

        return result

    def get_linked_list_size(list: ListNode) -> int:
        listSize = 0
        runner = list

        while runner != None:
            listSize = listSize + 1
            runner = runner.next
        
        return listSize
