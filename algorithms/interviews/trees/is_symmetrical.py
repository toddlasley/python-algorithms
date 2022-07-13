# Given a binary tree, determine whether it is symmetrical with respect to its values.
from typing import List


class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetrical(root: 'TreeNode') -> bool:
    def is_symmetrical_helper(left: List['TreeNode'], right: List['TreeNode']):
        left_children = []
        right_children = []
        left_count = 0
        right_count = 0

        for i, left_node in enumerate(left):
            right_node = right[i]

            if (left_node and right_node and left_node.val != right_node.val) or (not left_node and right_node) or (not right_node and left_node):
                return False
            
            if left_node:
                left_children.append(left_node.left)
                left_children.append(left_node.right)

                if left_node.left:
                    left_count += 1
                
                if left_node.right:
                    left_count += 1
            else:
                left_children.append(None)
                left_children.append(None)

            if right_node:
                right_children.append(right_node.right)
                right_children.append(right_node.left)

                if right_node.right:
                    right_count += 1
                
                if right_node.left:
                    right_count += 1
            else:
                right_children.append(None)
                right_children.append(None)
            
        if left_count == right_count == 0:
            return True
        else:
            return is_symmetrical_helper(left_children, right_children)

    if root != None:
        return is_symmetrical_helper([root.left], [root.right])
    else:
        return True
