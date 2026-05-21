# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # good node if path has no nodes greater than current node
        # keep track of maxVal 

        def dfs(node, maxVal):
            if not node:
                return 0

            if node.val >= maxVal:
                result = 1
            else:
                result = 0
            
            # recompute maxVal 
            maxVal = max(node.val, maxVal)

            result += dfs(node.left, maxVal)
            result += dfs(node.right, maxVal)
            return result

        return dfs(root, root.val)