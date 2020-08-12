from ways.SearchTools import PriorityQueue
from ways.SearchTools import Node
from ways.SearchTools import get_path
from ways.SearchTools import successors
from ways import tools


# @tools.timed
def best_first_search(roads, source_id, target_id, w, h):
    result = best_first_search_algorithm(roads, source_id, target_id, w, h)
    if result == -1:
        print('there is no Path from source to dist')
        return -1
    else:
        # print('time in minutes : [', result.get_g(), ']')
        # return get_path(result), result.get_g()
        return get_path(result)


def best_first_search_algorithm(roads, source_id, target_id, w, h):
    open_list = PriorityQueue()
    open_list.insert(Node(source_id, 0), 0)
    closed_list = set()
    while not open_list.is_empty():
        current = open_list.pop()
        current_id = current.get_id()
        if current.get_id() == target_id:
            return current
        closed_list.add(current_id)
        for v in successors(roads, current_id):
            in_closed_list = v in closed_list
            if in_closed_list:
                continue
            path_cost = current.get_g() + w(roads, current_id, v)
            in_open_list, child = open_list.find(v)
            if not in_closed_list and not in_open_list:
                as_node = Node(v, path_cost)
                as_node._parent = current
                open_list.insert(as_node, path_cost + h(roads, v, target_id))
            elif open_list and child.get_g() > path_cost:
                open_list.remove(v)
                child._g = path_cost
                child._parent = current
                open_list.insert(child, path_cost + h(roads, v, target_id))
    return -1
