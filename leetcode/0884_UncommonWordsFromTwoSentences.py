# knowledge: return statement = generator!
# concepts: dict
# comment: need faster solution not using didct
# runtime: 43 ms, faster than 48.94% of Python3 online submissions
# memory usage: 13.9 MB, less than 19.84% of Python3 online submissions

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lst = s1.split(" ") + s2.split(" ")
        words = dict()
        
        for word in lst:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
                
        return [word for word,count in words.items() if count == 1]
                