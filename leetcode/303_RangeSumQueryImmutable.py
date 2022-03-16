# knowledge: X
# concepts: prefix sum algorithm (generate sum array)
# comment: need to use append rather than idx assignment when adding items to list
# runtime: 137 ms, faster than 52.43% of Python3 online submissions
# memory usage: 17.6 MB, less than 61.72% of Python3 online submissions

class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [nums[0]]
        for idx in range(1, len(nums)):
            self.sums.append(self.sums[idx - 1] + nums[idx])

    def sumRange(self, left: int, right: int) -> int:
        if left:
            return self.sums[right] - self.sums[left - 1]
        else:
            return self.sums[right]
            

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)