# knowledge: int() or // for integer results, arr.append(), array[-n], +=1 instead of ++
# concepts: odd/even, cover null scenarios, min() vs <=, creating new result array
# comment: need to understand problem better & faster, more intuitive naming for variables (medianIdx --> midpoint etc.)
    # midpoint odd/even is different from total length odd/even
# runtime:  139 ms, faster than 36.87% of Python3 online submissions
# memory usage: 14.3 MB, less than 90.76% of Python3 online submissions

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # add length of two arrays and get median index
        totalLength = len(nums1) + len(nums2)
        medianIdx = totalLength // 2
        result = []
        pointer1 = 0
        pointer2 = 0
        
        # if either of the lists are empty 
        if len(nums1) == 0:
            if totalLength % 2 == 1:
                return nums2[medianIdx]
            else:
                return ((nums2[medianIdx-1] + nums2[medianIdx]) / 2)

        elif len(nums2) == 0:
            if totalLength % 2 == 1:
                return nums1[medianIdx]
            else:
                return ((nums1[medianIdx] + nums1[medianIdx-1]) / 2)

        # otherwise
        while len(result) < (medianIdx + 1):
            # breakpoint for cases when one array runs out faster than the other
            if pointer1 >= len(nums1):
                while (len(result)) < (medianIdx + 1):
                    result.append(nums2[pointer2])
                    pointer2+=1
                break
            elif pointer2 >= len(nums2):
                while (len(result)) < (medianIdx + 1):
                    result.append(nums1[pointer1])
                    pointer1+=1
                break
                
            # else add minimum value to new result array
            if nums1[pointer1] <= nums2[pointer2]:
                result.append(nums1[pointer1])
                pointer1+=1
            else:
                result.append(nums2[pointer2])
                pointer2+=1
                    
        # if length is odd
        if totalLength % 2 == 1:
            return result[-1]
        
        # if length is even
        else:
            return (result[-1] + result[-2]) / 2
            