# knowledge: greedy algo
# concepts: double pointer
# comment: can rewrite without recursive part?
    # seems that you do need recursive part but for faster processing only go into recursive mode once you find deletable char
# runtime: 162 ms, faster than 62.92% of Python3 online submissions
# memory usage: 17.2 MB, less than 8.32% of Python3 online submissions

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def loopThrough(front: int, end: int, deleted: bool):
            while front < end:
                if s[front] != s[end]:
                    if deleted:
                        return False
                    else:
                        return loopThrough(front, end - 1, True) or loopThrough(front + 1, end, True)
                else:
                    front += 1
                    end -= 1
            return True
        
        return loopThrough(0, len(s) - 1, False)
    