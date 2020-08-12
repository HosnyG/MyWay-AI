# this file should be runnable to print map_statistics using python stats.py
from collections import namedtuple
from ways import load_map_from_csv
from collections import Counter
import sys


def roads_info(roads):
    sum_links = 0
    max_branching = 0
    min_branching = sys.maxsize
    sum_distances = 0
    max_distance = 0
    min_distance = sys.maxsize
    counter = Counter()
    for junction in roads.values():
        sum_links += len(junction.links)
        if max_branching < len(junction.links):
            max_branching = len(junction.links)
        if min_branching > len(junction.links):
            min_branching = len(junction.links)

        for link in junction.links:
            counter[link.highway_type] += 1
            sum_distances += link.distance
            if max_distance < link.distance:
                max_distance = link.distance
            if min_distance > link.distance:
                min_distance = link.distance

    return sum_links, max_branching, min_branching, sum_distances, max_distance, min_distance, counter


# return a dictionary containing the desired information
def map_statistics(roads):
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    t = roads_info(roads)
    return {
        'Number of junctions': len(roads),
        'Number of links': t[0],
        'Outgoing branching factor': Stat(max=[t[1]], min=t[2], avg=t[0] / len(roads)),
        'Link distance': Stat(max=t[4], min=t[5], avg=t[3] / t[0]),
        'Link type histogram': t[6],  # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    from sys import argv
    assert len(argv) == 1
    print_stats()
