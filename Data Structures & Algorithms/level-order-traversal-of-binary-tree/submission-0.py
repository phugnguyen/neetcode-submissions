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

        if not root:
            return result

        queue = deque([root])

        while queue:
            temp = []
            for i in range(len(queue)):
                current = queue.popleft()
                if current:
                    temp.append(current.val)
                    queue.append(current.left)
                    queue.append(current.right)
            if temp:
                result.append(temp)

        return result