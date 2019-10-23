# python3


class Database:
    """
    Class representing set of tables. Each table i contains Ri rows. For given sequence of merges of table count on
    each step largest number of rows among all tables.
    To merge two tables, we need to merge root tables, append to first one all rows from the second, and make link that
    first table now is root.

    For realization used disjoint sets implemented as trees, also used union by rank and path compression approaches.

    More detailed info about conditions, output ind input data is in file week3/assignment.pdf: task 3
    """
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        if self.ranks[dst_parent] > self.ranks[src_parent]:
            self.parents[src_parent] = dst_parent
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            self.row_counts[src_parent] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[dst_parent])
        else:
            self.parents[dst_parent] = src_parent
            self.row_counts[src_parent] += self.row_counts[dst_parent]
            self.row_counts[dst_parent] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[src_parent])
            if self.ranks[dst_parent] == self.ranks[src_parent]:
                self.ranks[src_parent] += 1

        # self.parents[src_parent] = dst_parent
        # self.ranks[dst_parent] += self.ranks[src_parent]
        # self.ranks[src_parent] = 0
        # self.max_row_count = max(self.max_row_count, self.ranks[dst_parent])
        return True

    def get_parent(self, table):
        if self.parents[table] != table:
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
