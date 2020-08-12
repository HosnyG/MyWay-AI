from time import clock
import zlib
from math import acos, radians, pi
from numpy import ones, cos, array, sin

DB_DIRNAME = 'db/'
SEED = 0x23587643


def dhash(*data):
    return abs(zlib.adler32(bytes(str(data), 'UTF-8'))*100) * SEED % 0xffffffff


def dbopen(fname, *args, **kwargs):
    if not fname.startswith(DB_DIRNAME):
        fname = DB_DIRNAME + fname
    return open(fname, *args, **kwargs)


def float2dms(decimal_degrees):
    degrees = int(decimal_degrees)
    minutes = int(60 * (decimal_degrees - degrees))
    seconds = int(3600 * (decimal_degrees - degrees - minutes / 60))
    return degrees, minutes, seconds


def dms2float(degrees, minutes, seconds=0):
    return degrees + minutes / 60 + seconds / 3600


# compute distance in KM
def compute_distance(lat1, lon1, lat2, lon2):
    if (lat1, lon1) == (lat2, lon2):
        return 0.0
    if max(abs(lat1 - lat2), abs(lon1 - lon2)) < 0.00001:
        return 0.001
    phi1 = radians(90 - lat1)
    phi2 = radians(90 - lat2)
    meter_units_factor = 40000 / (2 * pi)
    arc = acos(sin(phi1) * sin(phi2) * cos(radians(lon1) - radians(lon2))
               + cos(phi1) * cos(phi2))
    return arc * meter_units_factor


class Everything(object):
    def __contains__(self, val):
        return True


def base_traffic_pattern():
        base_pattern = ones(60*24)
        base_pattern[(60*6):(10*60)] += cos(((array(range(4*60))/(4*60))-0.5)*pi)
        base_pattern[(15*60):(19*60)] += base_pattern[(60*6):(10*60)]
        return list(base_pattern)


def generate_traffic_noise_params(seed1, seed2):

    wavelength_cos = 60 + 20*(dhash(seed1+seed2)/0xffffffff) - 10
    wavelength_sin = 60 + 20*(dhash(seed1*seed2)/0xffffffff) - 10
    return wavelength_cos, wavelength_sin


def generate_slowdown_multiplier(road_length, road_maxspeed, base_val, param1, param2, time):
    multiplier = (cos(time*pi/param1) + sin(time*pi/param2))/2 + base_val + 1
    km_per_minute = road_maxspeed/60
    if (km_per_minute/road_length) < 0.06:
        multiplier = multiplier*km_per_minute/(0.06*road_length)
    return max(1, multiplier)


def timed(f):
    def wrap(*x, **d):
        start = clock()
        res = f(*x, **d)
        print(f.__name__, ':', clock() - start)
        return res
    return wrap


if __name__ == '__main__':
    for i in range(100):
        print(dhash(i))
