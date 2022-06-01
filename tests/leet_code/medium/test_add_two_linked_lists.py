from algorithms.leet_code.medium.add_two_linked_lists import ListNode, Solution
from typing import List

def test_add_two_linked_lists():
    l1 = ListNode(1, ListNode(2, ListNode(3)))
    l2 = ListNode(1, ListNode(2, ListNode(3)))
    validateResult(Solution.add_two_numbers(l1, l2), [2, 4, 6])

    l1 = ListNode(1, ListNode(7, ListNode(3)))
    l2 = ListNode(1, ListNode(3, ListNode(3)))
    validateResult(Solution.add_two_numbers(l1, l2), [2, 0, 7])

    l1 = ListNode(1, ListNode(7))
    l2 = ListNode(1, ListNode(3, ListNode(3)))
    validateResult(Solution.add_two_numbers(l1, l2), [2, 0, 4])

    l1 = None
    l2 = ListNode(1, ListNode(3, ListNode(3)))
    validateResult(Solution.add_two_numbers(l1, l2), [1, 3, 3])

    l1 = ListNode(1, ListNode(3, ListNode(3)))
    l2 = None
    validateResult(Solution.add_two_numbers(l1, l2), [1, 3, 3])

    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    validateResult(Solution.add_two_numbers(l1, l2), [8, 9, 9, 9, 0, 0, 0, 1])

def validateResult(list: ListNode, digits: List[int]):
    runner = list
    i = 0

    while runner != None:
        assert runner.val == digits[i]
        i = i + 1
        runner = runner.next
