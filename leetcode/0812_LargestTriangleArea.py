# knowledge: itertools.combinations
# concepts: math, brute force
# comment: X
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(0.5 * abs(xa*yb + xb*yc + xc*ya - xb*ya - xc*yb - xa*yc)
                   for (xa, ya), (xb, yb), (xc, yc) in itertools.combinations(points, 3))