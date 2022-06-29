# knowledge: X
# concepts: X
# comment: easy question, close to brute force
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        people = num_people * [0]
        toGive = 0
        while candies > 0:
            people[toGive % num_people] += min(candies, toGive + 1)
            toGive += 1
            candies -= toGive
        return people