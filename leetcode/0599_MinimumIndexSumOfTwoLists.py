# knowledge: can create dictionary with generator
# concepts: list
# comment: just enumerate through dictionary, not a hard problem...
# runtime: X, not mine
# memory usage: X, not mine

def findRestaurant(self, A, B):
    aDict = {u: i for i, u in enumerate(A)}
    best, ans = 1e9, []

    for j, v in enumerate(B):
        i = aDict.get(v, 1e9)
        if i + j < best:
            best = i + j
            ans = [v]
        elif i + j == best:
            ans.append(v)
    return ans