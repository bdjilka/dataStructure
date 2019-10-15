# python3
import sys


class StackWithMax():
    """
    Naive realization of stack with find maximum method. Disadvantage - linear time of search
    """
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return max(self.__stack)


class StackOfMax():
    """
    Auxiliary stack structure, that replicates operation of main stack, but saves only maximum value for each step.
    So, on each iteration, last element is maximum, that helps achieve constant time access to maximum.
    Disadvantage - cost of storing additional stack
    """
    def __init__(self):
        self.stack = list()

    def Push(self, a):
        if len(self.stack) == 0:
            self.stack.append(a)
        else:
            prev_max = self.stack[-1]
            if a > prev_max:
                self.stack.append(a)
            else:
                self.stack.append(prev_max)

    def Top(self):
        if len(self.stack):
            return self.stack[-1]
        else:
            return

    def Pop(self):
        assert (len(self.stack))
        self.stack.pop()


if __name__ == '__main__':
    # stack = StackWithMax()
    maxStack = StackOfMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            # stack.Push(int(query[1]))
            maxStack.Push(int(query[1]))
        elif query[0] == "pop":
            # stack.Pop()
            maxStack.Pop()
        elif query[0] == "max":
            # print(stack.Max())
            print(maxStack.Top())
        else:
            assert (0)
