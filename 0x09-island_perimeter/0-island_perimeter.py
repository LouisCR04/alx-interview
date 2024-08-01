#!/usr/bin/python3
"""
LeetCode 463: Island Perimeter
"""


def island_perimeter(grid):
    """ Finds the perimeter of the island """
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(m, n):
        """ Recursive solution to finding perimeter of each cell """
        if (m < 0 or n < 0 or m >= rows or n >= cols or grid[m][n] == 0):
            return 1
        if [m, n] in visited:
            return 0

        visited.add([m, n])
        perimeter = dfs(m + 1, n) + dfs(m - 1, n) + dfs(m, n + 1) + dfs(m, n - 1)

        return perimeter

    for row in range(rows):
        for col in range(cols):
            return dfs(row, col)
