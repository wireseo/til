# knowledge: [<whatever definition needs to go in the list>], you can multiply by boolean in python!
# concepts: generating continuous list
# comment: utilize list definition in python to generate easily!!!
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def fizzBuzz(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]