from ways import info
from BestFirstSearch import best_first_search
from ways.tools import compute_distance
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
    distance = compute_distance(u_lat, u_lon, v_lat, v_lon)
    travel_time = distance/110
    return travel_time*60


def find_astar_route(source_id, target_id):
    roads = graph.load_map_from_csv()
    return best_first_search(roads, source_id, target_id, w, h)
