# python3
import random
import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')


class StringComparator:
    """
    In the longest common substring problem one is given two strings s and t and the goal is to find a string w of
    maximal length that is a substring of both s and t.
    """
    _prime1 = 1000000007
    _prime2 = 1000000113

    _mult1 = random.randint(1, 1000000000)
    _mult2 = random.randint(1, 1000000000)

    def __init__(self, s, t):
        self.s = s
        self.t = t
        self.lower_bound = 0
        self.upper_bound = min(len(s), len(t))
        self.pivot = self.upper_bound // 2
        self.s_ind = None
        self.t_ind = None
        self.found_len = None
        self.hashes = None
        self.hashes_add = None
        self.thashes = None
        self.thashes_add = None

    def solve(self):
        """
        For every pair of strings s and t, used binary search to find the length of the longest common substring.
        To check whether two strings have a common substring of length k used function check_match, also used pre
        computed hashes for all prefixes of strings s and t.
        """
        self.compute_hashes()

        while self.lower_bound != self.upper_bound and self.lower_bound != self.pivot and self.upper_bound != self.pivot:
            has_match = self.check_match()
            if has_match:
                self.lower_bound = self.pivot
            else:
                self.upper_bound = self.pivot
            self.pivot = (self.lower_bound + self.upper_bound) // 2

        self.hashes = None
        self.hashes_add = None
        self.thashes = None
        self.thashes_add = None

        return Answer(self.s_ind, self.t_ind, self.found_len)

    def compute_hashes(self):
        self.hashes = [0 for _ in range(len(self.s) + 1)]
        self.hashes_add = [0 for _ in range(len(self.s) + 1)]

        for i in range(1, len(self.s) + 1):
            self.hashes[i] = (self._mult1 * self.hashes[i - 1] + ord(self.s[i - 1])) % self._prime1
            self.hashes_add[i] = (self._mult2 * self.hashes_add[i - 1] + ord(self.s[i - 1])) % self._prime2

        self.thashes = [0 for _ in range(len(self.t) + 1)]
        self.thashes_add = [0 for _ in range(len(self.t) + 1)]

        for i in range(1, len(self.t) + 1):
            self.thashes[i] = (self._mult1 * self.thashes[i - 1] + ord(self.t[i - 1])) % self._prime1
            self.thashes_add[i] = (self._mult2 * self.thashes_add[i - 1] + ord(self.t[i - 1])) % self._prime2

    def check_match(self):
        """
        The algorithm is following:
        - pre compute hash values of all substrings of length k of only s string
        - use two hash functions to reduce the probability of collision
        - not to store hash values of string t
        :return: True is natch is found, else in other way
        """
        k = self.pivot

        s_subs = [0 for _ in range(len(self.s) - k + 1)]
        s_subs_add = [0 for _ in range(len(self.s) - k + 1)]
        for i in range(len(self.s) - k + 1):
            s_subs[i] = (self.hashes[i + k] - pow(self._mult1, k, self._prime1) * self.hashes[i]) % self._prime1
            s_subs_add[i] = (self.hashes_add[i + k] - pow(self._mult2, k, self._prime2) * self.hashes_add[i]) % self._prime2

        for i in range(len(self.t) - k + 1):
            sub = (self.thashes[i + k] - pow(self._mult1, k, self._prime1) * self.thashes[i]) % self._prime1

            try:
                index = s_subs.index(sub)
            except ValueError:
                index = -1

            if index >= 0:
                sub_add = (self.thashes_add[i + k] - pow(self._mult2, k, self._prime2) * self.thashes_add[i]) % self._prime2
                if sub_add == s_subs_add[index]:
                    self.s_ind = index
                    self.t_ind = i
                    self.found_len = k
                    del s_subs, s_subs_add
                    return True

        del s_subs, s_subs_add
        return False


"""
Example
Input:
    cool toolbox          // pair of strings
    aaa bb
    aabaa babbaab
Output:
    -index in fisrt string- -index in second- -length-
    1 1 3                 // longest common substring is 'ool'
    0 1 0                 // no common substring, any indexes can be applied
    0 4 3                 // answer is 'aab', indexes can be (2, 3) and (0, 4)
"""
for line in sys.stdin.readlines():
    s, t = line.split()
    comparator = StringComparator(s, t)
    ans = comparator.solve()
    if ans.len:
        print(ans.i, ans.j, ans.len)
    else:
        print(0, 0, 0)
