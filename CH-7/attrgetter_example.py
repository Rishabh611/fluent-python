metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
]
from collections import namedtuple

LatLon = namedtuple("Latlon", "lat lon")

Metropolis = namedtuple("Metropolis", "name cc pop coord")

metro_area = [Metropolis(name, cc, pop, LatLon(lat, lon)) for name, cc, pop, (lat, lon) in metro_data]

print(metro_area[0])

print(metro_area[0].coord.lat)

from operator import attrgetter

name_lat = attrgetter('name', 'coord.lat')

for city in sorted(metro_area, key=attrgetter('coord.lat')):
    print(name_lat(city))