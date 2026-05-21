class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # similar to pacific atlantic
        # dfs to find all o's that connect to a border o
        # mark them #

        # then pass through and mark those that are not connected
        # to border

        # then pass again to flip # to o

        rows, cols = len(board), len(board[0])
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

        SEEN = '#'
        X = 'X'
        O = 'O'

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != O:
                return
            
            board[row][col] = SEEN

            for r, c in directions:
                dfs(row + r, col + c)

        for row in range(rows):
            if board[row][0] == O:
                dfs(row, 0)
            if board[row][cols - 1] == O:
                dfs(row, cols - 1)

        for col in range(cols):
            if board[0][col] == O:
                dfs(0, col)
            if board[rows - 1][col] == O:
                dfs(rows - 1, col)

        def markGrid(grid: List[List[str]], marker: str, antiMarker: str) -> None:
            rows, cols = len(grid), len(grid[0])

            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] != antiMarker:
                        grid[row][col] = marker
        
        markGrid(board, X, SEEN)
        markGrid(board, O, X)


