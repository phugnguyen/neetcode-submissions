class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        seen = set()
        # have a seen set to keep track of where we've been
        # use max to determine what the rolling area should be area = max(area, dfs(i, j))
        # dfs
        # # return 0 when coords are out of bounds, seen, or location is a 0
        # # return 1 + dfs (surrounding coords)

        def dfs(a, b):
            if a < 0 or a >= len(grid) or b < 0 or b >= len(grid[0]) or (a, b) in seen or grid[a][b] == 0:
                return 0
            

            seen.add((a, b))

            return 1 + dfs(a + 1, b) + dfs(a - 1, b) + dfs(a, b + 1) + dfs(a, b - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen or grid[i][j] == 1:
                    area = max(area, dfs(i, j))
        

        return area