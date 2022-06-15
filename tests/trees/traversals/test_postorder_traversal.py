from algorithms.trees.traversals.postorder_traversal import Traversal
from algorithms.trees.tree_node import TreeNode


def test_complete_tree():
    # a complete binary tree (fills left to right)
    #           e(4)
    #          /    \
    #        d(3)   f(5)
    #       /  \      /
    #     b(1)  c(2) g(6)

    b = TreeNode(1)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(5)
    g = TreeNode(6)

    e.left = d
    e.right = f
    d.left = b
    d.right = c
    f.left = g


    assert Traversal.postorder_traversal(e) == [1, 2, 3, 6, 5, 4]

def test_incomplete_tree():
    # an incomplete binary tree (doesn't fill left to right)
    #           e(4)
    #          /    \
    #        d(3)   f(5)
    #       /  \       \
    #     b(1)  c(2)    g(6)

    b = TreeNode(1)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(5)
    g = TreeNode(6)


    e.left = d
    e.right = f
    d.left = b
    d.right = c
    f.right = g


    assert Traversal.postorder_traversal(e) == [1, 2, 3, 6, 5, 4]

def test_full_tree():
    # a full binary tree (no node has one child)
    #           e(4)
    #          /    \
    #        d(3)   f(5)
    #               /  \
    #            b(1)  c(2)

    b = TreeNode(1)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(5)


    e.left = d
    e.right = f
    f.left = b
    f.right = c


    assert Traversal.postorder_traversal(e) == [3, 1, 2, 5, 4]

def test_not_full_tree():
    # a not full binary tree (at least one node has one child)
    #           e(4)
    #          /    \
    #        d(3)   f(5)
    #         \       / \
    #          h(7) b(1) c(2)

    b = TreeNode(1)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(5)
    h = TreeNode(7)


    e.left = d
    e.right = f
    d.right = h
    f.left = b
    f.right = c


    assert Traversal.postorder_traversal(e) == [7, 3, 1, 2, 5, 4]

def test_perfect_tree():
    # a perfect (symmetrical) tree
    #           e(4)
    #          /    \
    #        d(3)   f(5)
    #       / \       / \
    #     i(8)  h(7) b(1) c(2)

    b = TreeNode(1)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(5)
    h = TreeNode(7)
    i = TreeNode(8)


    e.left = d
    e.right = f
    d.left = i
    d.right = h
    f.left = b
    f.right = c


    assert Traversal.postorder_traversal(e) == [8, 7, 3, 1, 2, 5, 4]

def test_no_children():
    assert Traversal.postorder_traversal(TreeNode(0)) == [0]

def test_empty_tree():
    assert Traversal.postorder_traversal(None) == []
