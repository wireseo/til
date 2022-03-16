# knowledge: X
# concepts: prefix sum algorithm (generate sum array)
# comment: better index assignment for clear code, also can use += instead of append to list
    # as long as you use tuple (num,) to extend the array
# runtime: X, not mine
# memory usage: X, not mine

class NumArray(object):
    def __init__(self, nums: List[int]):
        self.sums = [0]
        for num in nums: 
            self.sums += self.sums[-1] + num,

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]