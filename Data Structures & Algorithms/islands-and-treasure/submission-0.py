class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        TREASURE = 0
        WATER = -1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == TREASURE:
                    queue.append([r, c])
                    visited.add((r, c))

        def addRoom(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == WATER:
                return

            visited.add((r, c))
            queue.append([r, c])

        distance = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = distance

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            distance += 1

