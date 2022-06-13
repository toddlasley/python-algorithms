from typing import List
from algorithms.leet_code.hard.merge_k_sorted_lists import ListNode, Solution
from typing import List

def test_merge_k_sorted_lists():
    a = ListNode(0, ListNode(1, ListNode(2)))
    b = ListNode(1, ListNode(2, ListNode(3)))
    c = ListNode(2, ListNode(3, ListNode(4)))
    d = ListNode(0, ListNode(1, ListNode(2)))
    e = ListNode(0, ListNode(1, ListNode(2)))
    f = ListNode(3, ListNode(4, ListNode(5)))
    g = ListNode(6, ListNode(7, ListNode(8)))
    h = ListNode(6, ListNode(7))

    assert linked_list_as_list(Solution.merge_k_sorted_lists([a, b, c])) == [0, 1, 1, 2, 2, 2, 3, 3, 4]
    assert linked_list_as_list(Solution.merge_k_sorted_lists([a, d, e])) == [0, 0, 0, 1, 1, 1, 2, 2, 2]
    assert linked_list_as_list(Solution.merge_k_sorted_lists([a, d, e])) == [0, 0, 0, 1, 1, 1, 2, 2, 2]
    assert linked_list_as_list(Solution.merge_k_sorted_lists([a, f, g])) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert linked_list_as_list(Solution.merge_k_sorted_lists([g, f, a])) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert linked_list_as_list(Solution.merge_k_sorted_lists([g, a, f])) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert linked_list_as_list(Solution.merge_k_sorted_lists([a, f, h])) == [0, 1, 2, 3, 4, 5, 6, 7]
    assert Solution.merge_k_sorted_lists([]) == None
    assert Solution.merge_k_sorted_lists([None]) == None
    assert Solution.merge_k_sorted_lists([None, None]) == None
    assert linked_list_as_list(Solution.merge_k_sorted_lists([None, a, None])) == [0, 1, 2]




def linked_list_as_list(node: ListNode) -> List:
    list = []

    while node is not None:
        list.append(node.val)
        node = node.next

    return list
