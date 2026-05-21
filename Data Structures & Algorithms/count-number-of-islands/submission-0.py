class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        seen = set()

        def dfs(a, b):

            if a < 0 or a >= len(grid) or b < 0 or b >= len(grid[0]) or (a, b) in seen or grid[a][b] == "0":
                return

            seen.add((a, b))
            
            dfs(a + 1, b)
            dfs(a - 1, b)
            dfs(a, b + 1)
            dfs(a, b - 1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)


        return islands