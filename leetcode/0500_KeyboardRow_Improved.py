# knowledge: X
# concepts: Set
# comment: can use set for faster & easier initialization
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a=set('qwertyuiop')
        b=set('asdfghjkl')
        c=set('zxcvbnm')
        ans=[]
        for word in words:
            t=set(word.lower())
            if a&t==t:
                ans.append(word)
            if b&t==t:
                ans.append(word)
            if c&t==t:
                ans.append(word)
        return ans