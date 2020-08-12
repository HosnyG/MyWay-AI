from collections import namedtuple
from . import tools
from . import info
import sys

Link_traffic_params = namedtuple('Link_traffic_params', ['cos_frequency', 'sin_frequency', ])
Link = namedtuple('Link', ['source', 'target', 'distance', 'highway_type', 'link_params', ])
Junction = namedtuple('Junction', ['index', 'lat', 'lon',  'links', ])


# junction_id -> Junction
class Roads(dict):
    def junctions(self):
        return list(self.values())
    
    def __init__(self, junction_list):
        super(Roads, self).__init__(junction_list)
        self.generation = 0
        self.base_traffic = tools.base_traffic_pattern()
        tmp = [(n.lat, n.lon) for n in junction_list.values()]
        self.mean_lat_lon = (sum([i[0] for i in tmp])/len(tmp), sum([i[1] for i in tmp])/len(tmp))

    def link_speed_history(self, link, time=0):
        time = int(time)
        _, top = info.SPEED_RANGES[link.highway_type]
        return int(top/tools.generate_slowdown_multiplier(link.distance, top, self.base_traffic[time], *link.link_params, time=time))
        
    def realtime_link_speed(self, link, time=0):
        time = int(time)
        _, top = info.SPEED_RANGES[link.highway_type]
        _a = 40/60  # speed in km/minute
        _delta_dist = tools.compute_distance(self.mean_lat_lon[0], self.mean_lat_lon[1], self[link.source].lat, self[link.source].lon)
        multiplier = (tools.cos((time*_a + _delta_dist)*tools.pi/(15*2))/3)+1
        return int(min(top, self.link_speed_history(link, time)*multiplier))
        
    def return_focus(self, start):
        found = set()
        start_node = self[start]
        _next = {l for l in start_node.links}
        while len(_next) > 0:
            _next_next = {l for k in _next for l in self[k.target].links if l not in found}
            found |= _next
            _next = _next_next
            if len(found) > 15:
                break
        return found
                    
    def iterlinks(self):
        return (link for j in self.values() for link in j.links)

    def get_lat_lon(self, junction_id):
        junction = self.get(junction_id)
        return junction.lat, junction.lon


def _make_link(i, link_string):
    link_params = [int(x) for x in link_string.split("@")]
    return Link(i, *(link_params+[Link_traffic_params(*tools.generate_traffic_noise_params(i,link_params[0]))]))


def _make_junction(i_str, lat_str, lon_str, *link_row):
    i, lat, lon = int(i_str), float(lat_str), float(lon_str)
    try:
        links = tuple(_make_link(i, lnk) for lnk in link_row)
        links = tuple(filter(lambda lnk: lnk.distance > 0, links))
    except ValueError:
        links = []
    return Junction(i, lat, lon, links)


@tools.timed
def load_map_from_csv(filename='israel.csv', start=0, count=sys.maxsize):
    import csv
    from itertools import islice
    with tools.dbopen(filename, 'rt') as f:
        it = islice(f, start, min(start+count, sys.maxsize))
        lst = {int(row[0]): _make_junction(*row) for row in csv.reader(it)}
        if count < sys.maxsize:
            lst = {i: Junction(i, j.lat, j.lon, tuple(lnk for lnk in j.links if lnk.target in lst))
                   for i, j in lst.items()}
    return Roads(lst)
