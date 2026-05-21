# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is height of left and height of right added together
        # keep running total of maxDiameter
        # maxDepth with extra steps

        maxDiameter = 0

        def dfs(node):
            nonlocal maxDiameter
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            diameter = left + right

            maxDiameter = max(maxDiameter, diameter)

            return 1 + max(left, right)

        dfs(root)


        return maxDiameter