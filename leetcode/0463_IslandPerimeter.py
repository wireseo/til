# knowledge: X
# concepts: 2D array
# comment: not too difficult, but should be a more efficient way
# runtime: 547 ms, faster than 86.38% of Python3 online submissions
# memory usage: 14.3 MB, less than 73.18% of Python3 online submissions

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perim = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0:
                        perim += 1
                    if i == len(grid) - 1 or grid[i+1][j] == 0:
                        perim += 1
                    if j == 0 or grid[i][j-1] == 0:
                        perim += 1
                    if j == len(grid[0]) - 1 or grid[i][j+1] == 0:
                        perim += 1
                        
        return perim