# knowledge: X
# concepts: binary search on rotated array
# comment: reference is very detailed; shrink the LR bounds to one value,
    # without ever disqualifying a possible minimum
# reference: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation

class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]