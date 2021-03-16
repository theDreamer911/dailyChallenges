import numpy as np
from geopy.geocoders import Nominatim
geolocator = Nominatim()


def geolocate(city=None, country=None):
    if city != None:
        try:
            loc = geolocator.geocode(str(city+','+country))
            return (loc.latitude, loc.longitude)
        except:
            return np.nan
    else:
        try:
            loc = geolocator.geocode(country)
            return (loc.latitude, loc.longitude)
        except:
            return np.nan


geolocate(country='USA')
