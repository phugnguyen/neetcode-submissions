# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # hold left and right nodes
        # set them equal to the inverttree of each other
        # base case is no root

        node = root
        if not node:
            return None

        left = node.left
        right = node.right 

        node.left = self.invertTree(right)
        node.right = self.invertTree(left)

        return node