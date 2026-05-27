# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # use a range to determine if correct
        def valid(node, leftBound, rightBound):
            if not node:
                return True
            if not (leftBound < node.val < rightBound):
                return False
            return valid(node.left, leftBound, node.val) and valid(node.right, node.val, rightBound)
        return valid(root, float("-inf"), float("inf"))
        
        