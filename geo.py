from geopy.geocoders import Nominatim
def position(pname):
    geolocator = Nominatim()
    location = geolocator.geocode(pname)
    if location is None:
        return None
    print((location.latitude,location.longitude))
    strs=str(location.longitude)+':'+str(location.latitude)
    return strs
