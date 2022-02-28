# knowledge: X
# concepts: array sorting, sorting from the last element
# comment: X, understood solution but looked at discussion to solve
# runtime: 28 ms, faster than 99.33% of Python3 online submissions
# memory usage: 13.9 MB, less than 94.30% of Python3 online submissions

class Solution:
    def merge(self, nums1, m, nums2, n):
        while n > 0:
            if m <= 0 or nums2[n-1] >= nums1[m-1]: # compare last two elements
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1] # shift last real element to the end of the array
                m -= 1