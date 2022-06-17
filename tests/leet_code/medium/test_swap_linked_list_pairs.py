from typing import List
from algorithms.leet_code.medium.swap_linked_list_pairs import swap_linked_list_pairs, ListNode

def test_swap_linked_list_pairs():
    assert linked_list_as_list(swap_linked_list_pairs(None)) == []
    assert linked_list_as_list(swap_linked_list_pairs(ListNode(0))) == [0]
    assert linked_list_as_list(swap_linked_list_pairs(ListNode(0, ListNode(1)))) == [1, 0]
    assert linked_list_as_list(swap_linked_list_pairs(ListNode(0, ListNode(1, ListNode(2))))) == [1, 0, 2]
    assert linked_list_as_list(swap_linked_list_pairs(ListNode(0, ListNode(1, ListNode(2, ListNode(3)))))) == [1, 0, 3, 2]

def linked_list_as_list(node: ListNode) -> List:
    list = []

    while node is not None:
        list.append(node.val)
        node = node.next

    return list
