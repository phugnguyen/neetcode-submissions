class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        # with counter for each level (this is num of seconds)

        # multi source bfs with the starts of the rotted
        ROTTEN = 2
        FRESH = 1
        EMPTY = 0
        freshCount = 0

        q = deque([])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == ROTTEN:
                    q.append((row, col))
                elif grid[row][col] == FRESH:
                    freshCount += 1
                    
        seconds = 0
        seen = set(q)
        while q and freshCount > 0:
            seconds += 1
            for i in range(len(q)):
                currRow, currCol = q.popleft()
                for dr, dc in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                    row = currRow + dr
                    col = currCol + dc
                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row, col) not in seen and grid[row][col] == FRESH:
                        freshCount -= 1
                        seen.add((row, col))
                        grid[row][col] = ROTTEN
                        q.append((row, col))

        if freshCount == 0:
            return seconds
        else:
            return -1