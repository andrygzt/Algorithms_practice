"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def create_preorder_values_array(root, preorderArray = []):
            if root is None:
                return preorderArray
            
            preorderArray.append(root.val)
            for child in root.children:
                create_preorder_values_array(child, preorderArray)

            return preorderArray
        return create_preorder_values_array(root)
        