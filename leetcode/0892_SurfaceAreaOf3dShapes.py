# knowledge: X
# concepts: 2D array
# comment: need simpler way to solve this problem without edge cases
# runtime: 135 ms, faster than 47.12% of Python3 online submissions
# memory usage: 14 MB, less than 25.96% of Python3 online submissions

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        # bottom + top (as long as > 0)
        # side (if at the edge or if surrounding blocks are smaller)
        
        n = len(grid)
        surface = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0: surface += 2
                if i == 0: surface += grid[i][j]
                if i == n - 1: surface += grid[i][j]
                if j == 0: surface += grid[i][j]
                if j == n - 1: surface += grid[i][j]
                
                if j != n - 1 and grid[i][j + 1] < grid[i][j]:
                    surface += grid[i][j] - grid[i][j + 1]
                    
                if j != 0 and grid[i][j - 1] < grid[i][j]:
                    surface += grid[i][j] - grid[i][j - 1]
                    
                if i != n - 1 and grid[i + 1][j] < grid[i][j]:
                    surface += grid[i][j] - grid[i + 1][j]
                    
                if i != 0 and grid[i - 1][j] < grid[i][j]:
                    surface += grid[i][j] - grid[i - 1][j]
                    
        return surface