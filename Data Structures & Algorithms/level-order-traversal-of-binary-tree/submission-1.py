# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        # queue with root
        # for items in queue, construct a list, then append to result lsut

        result = []
        q = deque([root])

        while q:
            level = []
            lenq = len(q)

            for i in range(lenq):
                current = q.popleft()
                if current:
                    level.append(current.val)
                    q.append(current.left)
                    q.append(current.right)
            if level:
                result.append(level)

        return result