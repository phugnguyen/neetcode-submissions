# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs
        # add right if there is a right
        # add left if there is a left
        # do nothing

        result = []
        queue = deque([root])

        while queue:
            level = []
            for i in range(len(queue)):
                current = queue.popleft()
                if current:
                    level.append(current.val)
                    queue.append(current.left)
                    queue.append(current.right)

            if level:
                result.append(level[-1])
        return result