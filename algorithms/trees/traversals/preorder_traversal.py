from typing import Optional, List
from ..tree_node import TreeNode

class Traversal:
    def preorder_traversal(node: Optional[TreeNode]) -> List[int]:
        result = []

        if node != None:
            Traversal.__traversal_helper(result, node)

        return result

    def __traversal_helper(result: List[int], node: TreeNode) -> None:
        result.append(node.val)
        
        if node.left != None:
            Traversal.__traversal_helper(result, node.left)

        if node.right != None:
            Traversal.__traversal_helper(result, node.right)

        return
