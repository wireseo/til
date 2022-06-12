# knowledge: deque: pop/append from both ends
# concepts: deque manipulation, two pointer
# comment: use deque to implement stack/queue
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = collections.deque()
        l, r = 0, len(nums) - 1
        
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
                
        return list(answer)