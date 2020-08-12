from ways import info
from BestFirstSearch import best_first_search
from ways import graph


# return travel time in minutes
def w(roads, u_index, v_index):
    u = roads.get(u_index)
    for link in u.links:
        if link.target == v_index:
            max_speed = info.SPEED_RANGES[link.highway_type][1]
            return 60 * (link.distance / (1000 * max_speed))


def h(roads, u_index, v_index):
    return 0


def find_ucs_route(source_id, target_id):
    roads = graph.load_map_from_csv()
    return best_first_search(roads, source_id, target_id, w, h)
