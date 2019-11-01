# python3
import datetime


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    """
    Thw goal is to implement a simple phone book manager, that is able to process the following types of user's
    queries: add -number- -name-, del -number-, find -number-.

    Length of phone number is maximum 7 digits, total number of queries lies in interval [1, 10**5].

    This task is solved by using hash table based on direct addressing scheme. Keys are integer representation of
    phone number, value is name of corresponding person.
    The implementation of such structure will be array of length 10**7, the index is equal to the phone number.
    Value of sell is None, is there is no such pair (phone number, name), person name in other case.

    :param queries: sequence of mentioned operations
    :return: sequence of responses for find operations
    """
    # list of responses for find operation
    result = list()

    # Keep list of all existing numbers. contacts[i] = None is number i is not in phone book.
    contacts = [None for _ in range(10000000)]

    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            contacts[cur_query.number] = cur_query.name

        elif cur_query.type == 'del':
            contacts[cur_query.number] = None

        else:
            name = contacts[cur_query.number]
            if name:
                result.append(name)
            else:
                result.append('not found')
    return result


if __name__ == '__main__':
    """
    Example:
    Input:
        12                      // number of queries
        add 911 police
        add 76213 Mom
        add 17239 Bob
        find 76213
        find 910
        find 911
        del 910
        del 911
        find 911
        find 76213
        add 76213 daddy
        find 76213
    Output: 
        Mom
        not found
        police
        not found
        Mom
        daddy
    """
    # t1 = datetime.datetime.now()
    write_responses(process_queries(read_queries()))
    # print(datetime.datetime.now() - t1)
