from algorithms.interviews.trees.is_symmetrical import TreeNode, is_symmetrical

def test_is_symmetrical():
    assert is_symmetrical(None)
    assert is_symmetrical(TreeNode(0))
    #           a(0)
    #          /    \
    #        b(1)   c(1)
    #       / \       / \
    #     d(1)  e(1) f(1) g(1)

    a = TreeNode(0)
    b = TreeNode(1)
    c = TreeNode(1)
    d = TreeNode(1)
    e = TreeNode(1)
    f = TreeNode(1)
    g = TreeNode(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    
    assert is_symmetrical(a)

    d.val = 2

    assert not is_symmetrical(a)

    g.val = 2

    assert is_symmetrical(a)
    
    b.left = None

    assert not is_symmetrical(a)

    c.right = None

    assert is_symmetrical(a)

    c.left = None

    assert not is_symmetrical(a)
