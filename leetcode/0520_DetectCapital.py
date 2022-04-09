# knowledge: isupper(), islower()
# concepts: string manipulation
# comment: too easy; maybe shouldn't use isupper and islower
# runtime: 32 ms, faster than 88.20% of Python3 online submissions
# memory usage: 13.8 MB, less than 61.38% of Python3 online submissions

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or word[0].isupper() and word[1:].islower():
            return True

    # more readable version
    def detectCapitalUse(self, word: str) -> bool:
        return word in (
            word.upper(),
            word.lower(),
            word.capitalize(),
        )