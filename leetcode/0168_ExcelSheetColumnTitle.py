# knowledge: ord(), string.ascii_upercase[]
# concepts: binary/hexadecimal/26-cimal
# comment: subtract 1 from columnNumber to utilize ascii uppercase array
# runtime: X, not mine
# memory usage: X, not mine

def convertToTitle(self, columnNumber: int) -> str:
    result = []
    while columnNumber > 0:
        result.append(string.ascii_uppercase[(columnNumber - 1) % 26])
        columnNumber = (columnNumber - 1) // 26
        
    return "".join(reversed(result))