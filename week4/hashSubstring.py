# python3
import random


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def poly_hash(s, p, x):
    """
    Computes value of polynomial hash function for some string.
    :param s: target string
    :param p: prime value
    :param x: random number no more then p - 1
    :return: integer value of hash
    """
    hash_value = 0
    for i in range(len(s) - 1, -1, -1):
        hash_value = (hash_value * x + ord(s[i])) % p
    return hash_value


def precompute_hashes(t, pat_len, p, x):
    """
    Pre computes hash values for all substrings of length of pattern length. Used to decrease total running time of
    Rabin-Karp's algorithm.
    :param t: input text
    :param pat_len: length of pattern
    :param p: prime value
    :param x: random number no more then p - 1
    :return: list of hashes
    """
    h = [0 for _ in range(len(t) - pat_len + 1)]
    s = t[len(t) - pat_len: len(t)]
    h[len(t) - pat_len] = poly_hash(s, p, x)
    y = 1
    for i in range(1, pat_len + 1):
        y = (y * x) % p
    for i in range(len(t) - pat_len - 1, -1, -1):
        h[i] = (x * h[i + 1] + ord(t[i]) - y * ord(t[i + pat_len])) % p
    return h


def get_occurrences(pattern, text):
    """
    Realization of Rabin-Karp's algorithm to find positions of all occurrences of some pattern in text.

    1 <= len(pattern) <= len(text) <= 5 * 10**5, the total length of all occurrences of pattern in the text doesn't
    exceed 10**8.
    Pattern and text consists only of latin letters.
    Comparision is case sensitive.
    :param pattern: string
    :param text: string
    :return: list of integers representing indexes of occurrences
    """
    p = 500019
    x = random.randint(1, p-1)
    result = list()

    p_hash = poly_hash(pattern, p, x)
    h = precompute_hashes(text, len(pattern), p, x)

    for i in range(len(text) - len(pattern) + 1):
        if p_hash == h[i] and text[i: i + len(pattern)] == pattern:
            result.append(i)

    return result


if __name__ == '__main__':
    """
    Example
    Input:
        aaaaa           // pattern
        baaaaaaa        // text
    Output: 
        1 2 3
    """
    print_occurrences(get_occurrences(*read_input()))
