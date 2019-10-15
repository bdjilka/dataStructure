# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    """
    For given text sequence it is required to check if usage of brackets is right. Right using of brackets need all
    brackets to be closed and it right order.
    Right usage: [], {[]}, []{}
    Error usage: []), }{, {{}
    :param text: string of length from 1 to 10**5 that contains consists of big and small latin letters, digits,
    punctuation marks and brackets from the set []{}().
    :return: 'SUCCESS' if there is no error or position of first problematic bracket.
    """
    opening_brackets_stack = []
    length = 0

    for i, value in enumerate(text):
        if value in "([{":
            opening_brackets_stack.append(Bracket(value, i))
            length += 1

        if value in ")]}":
            if length == 0 and i == 0:
                return 1
            if length > 0 and are_matching(opening_brackets_stack[length - 1].char, value):
                del opening_brackets_stack[-1]
                length -= 1
            else:
                return i + 1

    if length == 0:
        return 'Success'
    else:
        return opening_brackets_stack[-1].position + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
