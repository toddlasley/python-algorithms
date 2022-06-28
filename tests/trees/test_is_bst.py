from algorithms.trees.is_bst import is_bst, TreeNode

def test_none_returns_true():
    assert is_bst(None)

def test_single_node_returns_true():
    assert is_bst(TreeNode(0))

def test_complete_bst():
    # a complete binary tree (fills left to right)
    #           e(4)
    #          /    \
    #        d(2)   f(6)
    #       /  \      /
    #     b(1)  c(3) g(5)

    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(6)
    g = TreeNode(5)

    e.left = d
    e.right = f
    d.left = b
    d.right = c
    f.left = g

    assert is_bst(e)

def test_complete_non_bst():
    # a complete binary tree (fills left to right)
    #           e(4)
    #          /    \
    #        d(2)   f(6)
    #       /  \      /
    #     b(1)  c(3) g(10)

    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(6)
    g = TreeNode(10)

    e.left = d
    e.right = f
    d.left = b
    d.right = c
    f.left = g

    assert not is_bst(e)

def test_incomplete_bst():
    # an incomplete binary tree (doesn't fill left to right)
    #           e(4)
    #          /    \
    #        d(2)   f(5)
    #       /  \       \
    #     b(1)  c(3)    g(6)

    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(5)
    g = TreeNode(6)


    e.left = d
    e.right = f
    d.left = b
    d.right = c
    f.right = g

    assert is_bst(e)

def test_incomplete_non_bst():
    # an incomplete binary tree (doesn't fill left to right)
    #           e(4)
    #          /    \
    #        d(2)   f(5)
    #       /  \       \
    #     b(1)  c(10)    g(6)

    b = TreeNode(1)
    c = TreeNode(10)
    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(5)
    g = TreeNode(6)


    e.left = d
    e.right = f
    d.left = b
    d.right = c
    f.right = g

    assert not is_bst(e)

def test_full_bst():
    # a full binary tree (no node has one child)
    #           e(4)
    #          /    \
    #        d(3)   f(6)
    #               /  \
    #            b(5)  c(7)

    b = TreeNode(5)
    c = TreeNode(7)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(6)


    e.left = d
    e.right = f
    f.left = b
    f.right = c

    assert is_bst(e)

def test_full_non_bst():
    # a full binary tree (no node has one child)
    #           e(4)
    #          /    \
    #        d(10)   f(6)
    #               /  \
    #            b(5)  c(7)

    b = TreeNode(5)
    c = TreeNode(7)
    d = TreeNode(10)
    e = TreeNode(4)
    f = TreeNode(6)


    e.left = d
    e.right = f
    f.left = b
    f.right = c

    assert not is_bst(e)

def test_not_full_bst():
    # a not full binary tree (at least one node has one child)
    #           e(4)
    #          /    \
    #        d(2)   f(6)
    #         \       / \
    #          h(3) b(5) c(7)

    b = TreeNode(5)
    c = TreeNode(7)
    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(6)
    h = TreeNode(3)


    e.left = d
    e.right = f
    d.right = h
    f.left = b
    f.right = c

    assert is_bst(e)

def test_not_full_non_bst():
    # a not full binary tree (at least one node has one child)
    #           e(4)
    #          /    \
    #        d(2)   f(3)
    #         \       / \
    #          h(3) b(5) c(7)

    b = TreeNode(5)
    c = TreeNode(7)
    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(3)
    h = TreeNode(3)


    e.left = d
    e.right = f
    d.right = h
    f.left = b
    f.right = c

    assert not is_bst(e)
    
def test_perfect_bst():
    # a perfect (symmetrical) tree
    #           e(4)
    #          /    \
    #        d(2)   f(6)
    #       / \       / \
    #     i(1)  h(3) b(5) c(7)

    b = TreeNode(5)
    c = TreeNode(7)
    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(6)
    h = TreeNode(3)
    i = TreeNode(1)


    e.left = d
    e.right = f
    d.left = i
    d.right = h
    f.left = b
    f.right = c

    assert is_bst(e)

def test_perfect_non_bst():
    # a perfect (symmetrical) tree
    #           e(4)
    #          /    \
    #        d(2)   f(6)
    #       / \       / \
    #     i(1)  h(10) b(5) c(7)

    b = TreeNode(5)
    c = TreeNode(2)
    d = TreeNode(7)
    e = TreeNode(4)
    f = TreeNode(6)
    h = TreeNode(10)
    i = TreeNode(1)


    e.left = d
    e.right = f
    d.left = i
    d.right = h
    f.left = b
    f.right = c

    assert not is_bst(e)
