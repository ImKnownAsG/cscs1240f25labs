class RabinKarpHash:
    def __init__(self, s):
        self.mod = 9999991
        self.base = 31
        n = len(s)
        self.hash = [0] * n
        self.power = [0] * n

        # convert character to int 
        # ('a' = 1, ..., 'z' = 26)
        def charToInt(c):
            return ord(c) - ord('a') + 1

        self.hash[0] = charToInt(s[0])
        self.power[0] = 1

        for i in range(1, n):
            self.hash[i] = (self.hash[i - 1] * self.base \
                            + charToInt(s[i])) % self.mod
            
                            
            self.power[i] = (self.power[i - 1] * self.base)\
                                                % self.mod
        
        print(f'The hash of {s} is:')
        print(*self.hash)
        print(f'The powers of {s} are:')
        print(*self.power)
        
    # get hash of substring s[l...r] in O(1)
    def getSubHash(self, l, r):
        h = self.hash[r]
        if l > 0:
            h = (h - self.hash[l - 1] * self.power[r - l + 1]) % self.mod
            if h < 0:
                h += self.mod
        return h


# Rabin-Karp search using hash class
def searchPattern(text, pattern):
    n, m = len(text), len(pattern)
    textHash = RabinKarpHash(text)
    patHash = RabinKarpHash(pattern)

    patternHash = patHash.getSubHash(0, m - 1)
    print(f'patternhash is: {patternHash}')
    result = []

    for i in range(n - m + 1):
        subHash = textHash.getSubHash(i, i + m - 1)
        print(f'subHash of indexes {i + m - 1} and {i} is: {subHash}')
        if subHash == patternHash:
            print(f'found a match at index {i}')
            result.append(i)

    return result


if __name__ == "__main__":
#    txt = "geeksforgeeks"
#    pat = "geek"
    txt = "ababdabacdababcabab"
    pat = "ababcabab"
    positions = searchPattern(txt, pat)
    print(*positions)