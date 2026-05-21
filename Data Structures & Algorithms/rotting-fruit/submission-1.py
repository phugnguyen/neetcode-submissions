class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs the rotten fruit
        # if fresh fruit is adjacent to rotten fruit, make rotten and decrement freshFruit
        
        # keep track of all fresh fruit
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        freshFruit = 0
        minutes = 0

        queue = deque()

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == FRESH:
                    freshFruit += 1
                if grid[r][c] == ROTTEN:
                    queue.append([r, c])


        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        while queue and freshFruit > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nrows, ncols = r + dr, c + dc
                    if nrows in range(rows) and ncols in range(cols) and grid[nrows][ncols] == FRESH:
                        queue.append([nrows, ncols])
                        grid[nrows][ncols] = ROTTEN
                        freshFruit -= 1



            minutes += 1

        
        if freshFruit > 0:
            return -1
        else:
            return minutes



