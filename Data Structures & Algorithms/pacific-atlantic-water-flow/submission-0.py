class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        results = []

        def canVisit(row, col, visited, prevHeight):
            if (row, col) in visited or row not in range(rows) or col not in range(cols) or heights[row][col] < prevHeight:
                return

            visited.add((row, col))
            for x, y in directions:
                canVisit(row + x, col + y, visited, heights[row][col])
        
        for col in range(cols):
            canVisit(0, col, pacific, heights[0][col])
            canVisit(rows - 1, col, atlantic, heights[rows - 1][col])

        for row in range(rows):
            canVisit(row, 0, pacific, heights[row][0])
            canVisit(row, cols - 1, atlantic, heights[row][cols - 1])

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    results.append([row, col])

        return results
            