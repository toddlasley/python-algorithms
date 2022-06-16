from algorithms.leet_code.medium.remove_nth_node import remove_nth_node, ListNode
from typing import List

def test_remove_nth_node():
    assert linked_list_as_list(remove_nth_node(ListNode(0, ListNode(1, ListNode(2))), 2)) == [0, 2]
    assert linked_list_as_list(remove_nth_node(ListNode(0, ListNode(1, ListNode(2, ListNode(3)))), 2)) == [0, 1, 3]
    assert linked_list_as_list(remove_nth_node(ListNode(0, ListNode(1, ListNode(2, ListNode(3)))), 1)) == [0, 1, 2]
    assert linked_list_as_list(remove_nth_node(ListNode(0, ListNode(1, ListNode(2, ListNode(3)))), 4)) == [1, 2, 3]

def linked_list_as_list(node: ListNode) -> List:
    list = []

    while node is not None:
        list.append(node.val)
        node = node.next

    return list
