# python3

import datetime
from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request, r, w, finish_time):
        """
        Analyze packet: can it be added to buffer or not.
        If there is no empty space, packet - dropped down. Else we add packet to buffer and remembers its finish time.
        Before analyzing ability of addition, we delete from buffer completed tasks and free memory.
        :param request: named tuple Request
        :param r: initial index of record in finish_time list
        :param w: first place to write in finish_time list
        :param finish_time: array, representing vacant and occupied places in buffer, values are time when task will
        be finished
        :return: new values of r, w, finish_time and instance of named tuple Response, that contains information about
        if it dropped down and start time of execution
        """
        while finish_time[r] <= request.arrived_at and r != w:
            finish_time[r] = 0
            r = (r + 1) % (self.size + 1)

        # write your code here
        if r == w:
            # buffer is empty starting to execute immediately
            finish_time[r] = request.arrived_at + request.time_to_process
            w = (w + 1) % (self.size + 1)
            return r, w, finish_time, Response(False, request.arrived_at)
        else:
            if (w + 1) % (self.size + 1) == r:
                return r, w, finish_time, Response(True, -1)
            else:
                start = finish_time[(w - 1) % (self.size + 1)]
                finish_time[w] = start + request.time_to_process
                w = (w + 1) % (self.size + 1)
                return r, w, finish_time, Response(False, start)


def process_requests(requests, buffer, buffer_size):
    """
    For given sequence of packets calculate start time of each packet with given size of buffer. If some request is
    dropped down indicate it with value -1
    :param buffer_size: size of buffer
    :param requests: list of request(arrival_time, processing_time)
    :param buffer: buffer of size n
    :return: list of responses
    """
    responses = []
    r = 0
    w = 0
    finish_time = [0 for _ in range(buffer_size + 1)]

    # t1 = datetime.datetime.now()

    for request in requests:
        r, w, finish_time, response = buffer.process(request, r, w, finish_time)
        responses.append(response)

    # t2 = datetime.datetime.now()
    # print(t2 - t1)

    return responses


def main():
    """
    Input sample:

    1 2         // size of buffer is 1, number of packets is 2
    0 1         // first packet: arrived at time 0, time to process is 1
    0 1         // second packet: arrived at time 0, time to process is 1

    Output:
    0           // time of processing start oof first packet
    -1          // second packet was dropped
    """
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer, buffer_size)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
