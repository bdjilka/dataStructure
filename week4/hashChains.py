# python3


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.hashes = dict()

    def _hash_func(self, s):
        """
        Hash polynomial function
        """
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        """
        In this task goal is to implement a hash table with lists chaining. Already given the number of buckets m and
        a polynomial hash function, where is used the ASCII code of the i-th symbol of hashing string S.
        p = 1 000 000 007 and x = 263.
        Program supports the following kinds of queries:
            ∙ add string — insert string into the table. If there is already such string in the hash table, then just
            ignore the query.
            ∙ del string — remove string from the table. If there is no such string in the hash table, then just ignore
            the query.
            ∙ find string — output “yes" or “no" (without quotes) depending on whether the table contains string or not.
            ∙ check i — output the content of the i-th list in the table. Use spaces to separate the elements of the
            list. If i-th list is empty, output a blank line.

        :param query: sequence of operations
        :return: nothing
        """
        if query.type == "check":
            text_list = self.hashes.get(query.ind, None)
            if text_list is None:
                print('')
            else:
                # use reverse order, because we simulate append strings to the end
                self.write_chain(text for text in reversed(text_list))
        else:
            text_hash = self._hash_func(query.s)
            text_list = self.hashes.get(text_hash, None)
            try:
                if text_list is None:
                    ind = -1
                else:
                    ind = text_list.index(query.s)
            except ValueError:
                ind = -1

            if query.type == 'find':
                self.write_search_result(text_list is not None and ind != -1)
            elif query.type == 'add':
                if text_list is None:
                    self.hashes[text_hash] = [query.s]
                elif ind == -1:
                    self.hashes[text_hash].append(query.s)
            else:
                if text_list is not None and ind > -1:
                    self.hashes[text_hash].remove(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    """
    Example:
    Input:
        5               // the number of buckets - m, N/5 <= m <= N
        12              // number of queries - N, 1 <= N <= 10**5
        add world
        add HellO
        check 4
        find World
        find world
        del world
        check 4
        del HellO
        add luck
        add GooD
        check 2
        del good
    Output:
        HellO world
        no
        yes
        HellO
        GooD luck
    """
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
