# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # keep track of maxVal as we're iterating through dfs
        # to determine if the node is good or not

        def dfs(node, maxVal):
            if not node:
                return 0
            
            result = 1 if node.val >= maxVal else 0

            maxVal = max(node.val, maxVal)

            result += dfs(node.left, maxVal)
            result += dfs(node.right, maxVal)

            return result


        return dfs(root, root.val)