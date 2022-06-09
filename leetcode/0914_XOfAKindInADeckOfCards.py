# knowledge: X
# concepts: GCD
# comment: need to realize it's a greatest common divisor problem
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    # def hasGroupsSizeX(self, deck: List[int]) -> bool:
    #     vals = Counter(deck).values()
    #     return all([x >= 2 for x in vals]) and len(set(vals)) == 1

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        mini = min(count.values())
        
        if mini < 2:
            return False
        
        for i in range(mini+1,1,-1):
            res = all(value % i == 0 for value in count.values())
            if res: 
                return True
            
        return False        