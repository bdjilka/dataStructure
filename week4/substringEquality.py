# python3
import random
import sys
# import re


class Solver:
    _prime1 = 1000000007
    _prime2 = 1000000013

    _x1 = random.randint(1, 1000000000)
    _x2 = random.randint(1, 1000000000)

    def __init__(self, s):
        # self.s = re.sub('[^a-z]', '', s)
        self.s = s
        self.text_size = len(self.s)
        self.hashes1 = [0 for _ in range(self.text_size + 1)]
        self.hashes2 = [0 for _ in range(self.text_size + 1)]
        self.computeHashes()

    def computeHashes(self):
        """
        Pre computing hashes of all prefixes of string s
        """
        for i in range(1, self.text_size + 1):
            self.hashes1[i] = (self._x1 * self.hashes1[i - 1] + ord(self.s[i - 1])) % self._prime1
            self.hashes2[i] = (self._x2 * self.hashes2[i - 1] + ord(self.s[i - 1])) % self._prime2

    def ask(self, a, b, l):
        """
        For given two substring say are they equal or not.
        To implement such and algorithm used precomputed hashed value of all prefixes of given input string. Based on
        polynomial hash function properties, hash values of any substring can be computed with the help on two hash
        values of prefixes, so this gives constant time to compute hash of substring.

        To practically totally reduce collisions we use two polynomial hash functions, the probability of collision is
        about 10**-18.
        :param a: start index of first substring
        :param b: start index of second substring
        :param l: length of substrings
        :return: are they equal or not
        """
        if l == 1:
            return self.s[a] == self.s[b]
        if a == b:
            return True

        ha1 = (self.hashes1[a + l] - pow(self._x1, l, self._prime1) * self.hashes1[a]) % self._prime1
        hb1 = (self.hashes1[b + l] - pow(self._x1, l, self._prime1) * self.hashes1[b]) % self._prime1

        if ha1 == hb1:
            ha2 = (self.hashes2[a + l] - pow(self._x2, l, self._prime2) * self.hashes2[a]) % self._prime2
            hb2 = (self.hashes2[b + l] - pow(self._x2, l, self._prime2) * self.hashes2[b]) % self._prime2
            return ha2 == hb2

        return False


"""
Example
Input:
    trololo     // string s, 1 <= len(s) <= 500 000
    4           // number of queries q, 1 <= q <= 100 000
    0 0 7       // query: a - b - l, 0 <= a,b <= len(s) - l, indexes of start and length
    2 4 3
    3 5 1
    1 3 2
Output:
    Yes         // trololo = trololo
    Yes         // olo = olo
    Yes         // l = l
    No          // ro != lo
"""
s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if solver.ask(a, b, l) else "No")
