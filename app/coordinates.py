"""app.coordinates.py"""

class Latitude:
    """
    A numeric representation of a latitudinal position north or south of the Earth's equator, to track Coronavirus spread nation to nation latitudinally.
    """
    def __init__(self, value: float):
        self.data = value

    def sum(other: Latitude):
        self.data += other.data

    def merge(other: Longitude):
        return Coordinates(self, other)

class Longitude:
    """
    A numeric representation of a longitudinal position measuring east to west, to track Coronavirus spread nation to nation longitudinally
    """
    def __init__(self, value: float):
        self.data = value

    def sum(other: Longitude):
        self.data += other.data
    
    def merge(other: Latitude):
        return Coordinates(self, other)

class Coordinates:
    """
    A position on earth using decimal coordinates (latitude and longitude).
    """

    def __init__(self, latitude: Latitude, longitude:Longitude):
        self.latitude = latitude
        self.longitude = longitude

    def serialize(self):
        """
        Serializes the coordinates into a dict.
        :returns: The serialized coordinates.
        :rtype: dict
        """
        return {"latitude": self.latitude.data, "longitude": self.longitude.data}

    def __str__(self):
        return "lat: %s, long: %s" % (self.latitude.data, self.longitude.data)
