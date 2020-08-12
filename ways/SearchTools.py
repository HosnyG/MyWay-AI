from ways import info
from ways import tools
import heapq


class Node:
    def __init__(self, _id, g):
        self._id = _id
        self._g = g
        self._parent = None

    def get_id(self):
        return self._id

    def get_g(self):
        return self._g

    def get_parent(self):
        return self._parent


def successors(roads, u):
    return [k[1] for k in roads.get(u).links]


def get_path(node):
    path = []
    j = node
    while j is not None:
        path.append(j.get_id())
        j = j.get_parent()
    path.reverse()
    return path


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0

    def find(self, i):
        for item in self._queue:
            if item[2].get_id() == i:
                return True, item[2]
        return False, -1

    def remove(self, i):
        for item in self._queue:
            if item[2].get_id() == i:
                self._queue.remove(item)
