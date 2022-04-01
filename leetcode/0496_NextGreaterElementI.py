# knowledge: use pop on lists, lambda map function
# concepts: monotonic stack
# comment: study monotonic stack structures
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st, d = [], {}

        for v in nums2:
            while len(st) and st[-1] < v:
                d[st.pop()] = v
            st.append(v)

        return map(lambda x: d.get(x, -1), nums1)