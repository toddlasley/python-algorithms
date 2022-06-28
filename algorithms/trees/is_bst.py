from typing import Optional
from ..trees.tree_node import TreeNode

def is_bst(node: TreeNode) -> bool:
    def is_bst_helper(node: TreeNode, lower_bound: Optional[int], upper_bound: Optional[int]) -> bool:
        if not node:
            return True
        
        if lower_bound != None and node.val <= lower_bound:
            return False

        if upper_bound != None and node.val >= upper_bound:
            return False

        return is_bst_helper(node.left, lower_bound, node.val) and is_bst_helper(node.right, node.val, upper_bound)

    return is_bst_helper(node, None, None)
