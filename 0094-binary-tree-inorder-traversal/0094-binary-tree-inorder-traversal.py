# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def fillingArray(root: TreeNode, result = []):
            if root is None:
                return 
            fillingArray(root.left, result)
            result.append(root.val)
            fillingArray(root.right, result)

            return result
        return fillingArray(root)

        
        