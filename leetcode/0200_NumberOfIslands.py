# knowledge: map(function, list of tuple[0]s, list of tuple[1]s)
    #  map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
# concepts: DFS
# comment: is there a faster way?
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def numIslands(self, grid):
            def sink(i, j):
                if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    sink(i+1, j)
                    sink(i-1, j)
                    sink(i, j+1)
                    sink(i, j-1)
                    return 1
                
            return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == '1')