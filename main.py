import UCS
import AStar
import IDAStar


def find_ucs_rout(source, target):
    return UCS.find_ucs_route(source, target)


def find_astar_route(source, target):
    return AStar.find_astar_route(source, target)


def find_idastar_route(source, target):
    return IDAStar.find_idastar_route(source, target)


def dispatch(argv):
    from sys import argv
    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'ucs':
        path = find_ucs_rout(source, target)
    elif argv[1] == 'astar':
        path = find_astar_route(source, target)
    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
    print(' '.join(str(j) for j in path))


if __name__ == '__main__':
    from sys import argv
    dispatch(argv)
