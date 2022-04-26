# knowledge: sum() to sum record
# concepts: X
# comment: accepted solution!
# runtime: 44 ms, faster than 80.69% of Python3 online submissions
# memory usage: 13.9 MB, less than 99.69% of Python3 online submissions

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        
        for op in ops:
            if op == '+':
                record.append(record[-1] + record[-2])
            elif op == 'D':
                record.append(record[-1] * 2)
            elif op == 'C':
                record.pop()
            else:
                record.append(int(op))
                
        return sum(record)