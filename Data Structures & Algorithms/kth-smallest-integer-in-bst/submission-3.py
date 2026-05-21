# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal with a stack
        # set current = current.left
        # append current to stack
        # iterate counter to look for k

        i = 0
        result = 0

        def dfs(node):
            nonlocal i, result
            if not node:
                return
            
            dfs(node.left)
            i += 1
            if i == k:
                result = node.val
            dfs(node.right)
            

        dfs(root)
        return result


