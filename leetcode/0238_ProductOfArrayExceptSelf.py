# knowledge: X
# concepts: product, array, one-pass
# comment: need to separate prefix and suffix -- may use this in other algorithms
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = list(accumulate(nums, mul))
        suf = list(accumulate(nums[::-1], mul))[::-1]
        n = len(nums)
        
        return [(pre[i-1] if i else 1) * (suf[i+1] if i+1 < n else 1) for i in range(n)]
    
    # better version
    def productExceptSelf(self, nums):
        ans, suf, pre = [1]*len(nums), 1, 1
        for i in range(len(nums)):
            ans[i] *= pre               # prefix product from one end
            pre *= nums[i]
            ans[-1-i] *= suf            # suffix product from other end
            suf *= nums[-1-i]
        return ans
        