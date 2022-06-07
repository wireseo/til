# knowledge: X
# concepts: two pointer
# comment: need to choose which one to iterate and which one to manually increase
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
            
        return i == len(name)