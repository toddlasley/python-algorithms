from typing import List
from algorithms.cracking_the_coding_interview.linked_lists.delete_node import delete_node, ListNode


def test_delete_node():
    a = ListNode(0)
    b = ListNode(1)
    c = ListNode(2)
    d = ListNode(3)
    e = ListNode(4)

    a.next = b
    b.next = c
    delete_node(b)
    assert linked_list_as_list(a) == [0, 2]

    b.val = 1
    a.next = b
    b.next = c
    c.next = d
    delete_node(b)
    assert linked_list_as_list(a) == [0, 2, 3]

    b.val = 1
    a.next = b
    b.next = c
    c.next = d
    delete_node(c)
    assert linked_list_as_list(a) == [0, 1, 3]

    c.val = 2
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    delete_node(b)
    assert linked_list_as_list(a) == [0, 2, 3, 4]

    b.val = 1
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    delete_node(d)
    assert linked_list_as_list(a) == [0, 1, 2, 4]


def linked_list_as_list(node: ListNode) -> List:
    nodes = []

    while node:
        nodes.append(node.val)
        node = node.next

    return nodes
