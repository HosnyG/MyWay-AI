from ways import info
import sys
from ways import SearchTools
from ways import tools
from ways import graph

# return travel time in minutes
def w(roads, u_index, v_index):
    u = roads.get(u_index)
    for link in u.links:
        if link.target == v_index:
            max_speed = info.SPEED_RANGES[link.highway_type][1]
            return 60 * (link.distance / (1000 * max_speed))


# return travel time in minutes
def h(roads, u_index, v_index):
    u_lat, u_lon = roads.get_lat_lon(u_index)
    v_lat, v_lon = roads.get_lat_lon(v_index)
    distance = tools.compute_distance(u_lat, u_lon, v_lat, v_lon)
    travel_time = distance/110
    return travel_time*60


new_limit = -1


# @tools.timed
def find_idastar_route(source_id, target_id):
    roads = graph.load_map_from_csv()
    global new_limit
    new_limit = h(roads, source_id, target_id)
    while True:
        path = [source_id]
        f_limit = new_limit
        new_limit = sys.maxsize
        solution, time = dfs_f(roads, source_id, 0, path, f_limit, target_id)
        if solution is not None:
            # return solution, time
            return solution


def dfs_f(roads, u, g, path, f_limit, target_id):
    global new_limit
    new_f = g + h(roads, u, target_id)
    if new_f > f_limit:
        new_limit = min(new_limit, new_f)
        return None, -1
    if u == target_id:
        return path, g
    for v in SearchTools.successors(roads, u):
        path1 = []
        for i in path:
            path1.append(i)
        path1.append(v)
        sol, time = dfs_f(roads, v, g+w(roads, u, v), path1, f_limit, target_id)
        if sol is not None:
            return sol, time
    return None, -1
