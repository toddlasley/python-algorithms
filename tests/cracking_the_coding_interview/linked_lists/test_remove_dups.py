from typing import List
from algorithms.cracking_the_coding_interview.linked_lists.remove_dups import remove_dups, ListNode

def test_remove_dups():
    assert remove_dups(None) == None
    assert linked_list_as_list(remove_dups(ListNode(0))) == [0]
    assert linked_list_as_list(remove_dups(ListNode(0, ListNode(1)))) == [0, 1]
    assert linked_list_as_list(remove_dups(ListNode(0, ListNode(1, ListNode(2))))) == [0, 1, 2]
    assert linked_list_as_list(remove_dups(ListNode(0, ListNode(1, ListNode(2, ListNode(3)))))) == [0, 1, 2, 3]
    assert linked_list_as_list(remove_dups(ListNode(1, ListNode(1)))) == [1]
    assert linked_list_as_list(remove_dups(ListNode(0, ListNode(1, ListNode(1))))) == [0, 1]
    assert linked_list_as_list(remove_dups(ListNode(0, ListNode(1, ListNode(1, ListNode(3)))))) == [0, 1, 3]
    assert linked_list_as_list(remove_dups(ListNode(0, ListNode(1, ListNode(1, ListNode(1)))))) == [0, 1]
    assert linked_list_as_list(remove_dups(ListNode(0, ListNode(0, ListNode(0, ListNode(0)))))) == [0]
    

def linked_list_as_list(node: ListNode) -> List:
    list = []

    while node is not None:
        list.append(node.val)
        node = node.next

    return list
