# knowledge: X
# concepts: 2D array
# comment: wayyy too difficult and complicated... still don't understand fully; need to study 2D algorithms
    # Prepend and append a zero, find the pairs that don't match, count the number of pairs that don't match (this is the number of shorelines between cells in this row):
    # Now do this for every row and column in the grid and sum the results:
    # grid contains all the rows
    # map(list, zip(*grid)) contains all the columns (zip(*rows) is a trick to transpose a 2D array, but you have to do map(list, ...) as zip produces tuples rather than lists)
    # grid + map(list, zip(*grid)) contains all the rows and all the columns 
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def islandPerimeter(self, grid):
        return sum(sum(map(operator.ne, [0] + row, row + [0]))
                for row in grid + map(list, zip(*grid)))