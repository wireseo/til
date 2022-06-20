# knowledge: X
# concepts: in-place array manipulation, two pass
# comment: reverse, duplicate zeros, two-pass necessary
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        
        for i in range(n-1, -1, -1): # backward from last element to first element?
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0: 
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0