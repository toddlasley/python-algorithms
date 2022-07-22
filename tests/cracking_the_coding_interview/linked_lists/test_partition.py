from typing import List
from algorithms.cracking_the_coding_interview.linked_lists.partition import partition, ListNode

def test_partition():
    assert linked_list_as_list(partition(ListNode(0, ListNode(1, ListNode(2, ListNode(3)))), 4)) == [3, 2, 1, 0]
    assert linked_list_as_list(partition(ListNode(0, ListNode(1, ListNode(2, ListNode(3)))), 0)) == [3, 2, 1, 0]
    assert linked_list_as_list(partition(ListNode(4, ListNode(3, ListNode(2, ListNode(1, ListNode(0))))), 1)) == [0, 1, 2, 3, 4]
    assert linked_list_as_list(partition(ListNode(4, ListNode(3, ListNode(2, ListNode(1, ListNode(0))))), 2)) == [0, 1, 2, 3, 4]
    assert linked_list_as_list(partition(ListNode(4, ListNode(3, ListNode(2, ListNode(1, ListNode(0))))), 3)) == [0, 1, 2, 3, 4]
    a = ListNode(3, ListNode(5, ListNode(8, ListNode(5, ListNode(10, ListNode(2, ListNode(1)))))))
    assert linked_list_as_list(partition(a, 5)) == [1, 2, 3, 10, 5, 8, 5]
    
    
def linked_list_as_list(node: ListNode) -> List:
    values = []

    while node is not None:
        values.append(node.val)
        node = node.next

    return values
