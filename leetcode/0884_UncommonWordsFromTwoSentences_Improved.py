# knowledge: collections.Counter((A + B).split())
# concepts: counter
# comment: w,c are understandable enough
# runtime: X, not mine
# memory usage: X, not mine

def uncommonFromSentences(self, A, B):
    c = collections.Counter((A + " " + B).split())
    return [w for w in c if c[w] == 1]