# python3

from collections import namedtuple


Element = namedtuple("Element", ["value", "max"])


class StackOfMax():
    """
    Stack structure, that saves not only value, but maximum value for each step.
    So, on each iteration, last element contains maximum, that helps achieve constant time access to maximum.
    """
    def __init__(self):
        self.stack = list()

    def Push(self, a):
        if len(self.stack) == 0:
            self.stack.append(Element(a, a))
        else:
            prev = self.stack[-1]
            if a > prev.max:
                self.stack.append(Element(a, a))
            else:
                self.stack.append(Element(a, prev.max))

    def Top(self):
        if len(self.stack):
            return self.stack[-1]
        else:
            return

    def Pop(self):
        assert (len(self.stack))
        return self.stack.pop()


def max_sliding_window_naive(sequence, m):
    """
    Given a sequence [A1, ..., An] of integers and an integer m ≤ n, find the maximum among {Ai , ..., Ai+m−1 }
    for very 1 ≤ i ≤ n − m + 1. A naive O(nm) algorithm for solving this problem scans each window separately.
    :param sequence: array of integers
    :param m: length of window
    :return: array of maximums for all windows
    """
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


def max_sliding_window(sequence, m):
    """
    Optimized method of finding maximums. It uses two stack, that store maximum for some subsequences, such two stacks
    in pair represents structure of queue.

    Goal of O(n) complexity not achieved.

    :param sequence: array of integers
    :param m: length of window
    :return: array of maximums for all windows
    """
    stack1 = StackOfMax()
    stack2 = StackOfMax()
    k = 2

    for i in range(m):
        stack1.Push(sequence[i])

    maximums = list()
    maximums.append(stack1.Top().max)

    for i in range(0, len(sequence) - m):
        for _ in range(m - 1):
            el = stack1.Pop()
            stack2.Push(el.value)
        stack1.Pop()
        for _ in range(m - 1):
            el = stack2.Pop()
            stack1.Push(el.value)
        stack1.Push(sequence[i + m])
        maximums.append(stack1.Top().max)
    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    # print(*max_sliding_window_naive(input_sequence, window_size))
    print(*max_sliding_window(input_sequence, window_size))
