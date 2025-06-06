"""
Name - Suveer Dhawan

This program contains the base class and subclasses for geological features.
"""

from abc import ABC
from dataclasses import dataclass

@dataclass
class Location:
    Y: int = 0
    X: int = 0

    def __str__(self):
        return f"({self.Y},{self.X})"

@dataclass
class Size:
    height: int = 0
    width: int = 0


class GeoFeature(ABC):
    """ 
    The overarching abstract base class for all geological features.

    Instance Variables:
        location (Location): Position of the feature on the map

    Class Variables:
        info (string): Details of Geological feature at the location, else 
            "no information found"
        representation(string): Map representation, "." for no feature, "m" 
            for mountaint, "l" for lake, "c" for crater
    """

    info = "no information found"
    representation = "."

    def __init__(self, location):
        """ 
        Create a new Geological feature.

        Arguments:
            location: Position of the feature on the map
        """
        self.location = location

    def get_info(self):
        """
        Returns information about the geological feature at the specific location.

        Returns:
            string: information about the geological feature
        """
        return self.info

    def get_representation(self):
        """
        Returns information about the geological feature at the specific location.

        Returns:
            string: Graphical representation of the geological feature for the map
        """
        return GeoFeature.representation

    def __str__(self):
        """
        Cleaner representation of object
        """
        return "GeoFeature"


class Mountain(GeoFeature):
    """
    Creating the Mountain class that inherits from GeoFeature

    Additional Arguments:
        name(str): name of the mountain
        height(int): height of the mountain
    """
    
    info = "mountain"
    representation = "m"

    def __init__(self, location, name, height):
        super().__init__(location)
        self.name = name
        self.height = height

    def get_info(self):
        return f"{Mountain.info} {self.name}, height {self.height}"

    def get_representation(self):
        return Mountain.representation

    def get_size(self):
        """
        Getter method to get the height of the mountain

        Returns:
            height(int): height value of the mountain  
        """
        return self.height

    def __str__(self):
        return "mountain"


class Lake(GeoFeature):
    """
    Creating the Lake class that inherits from GeoFeature

    Additional Arguments:
        name(str): name of the lake
        depth(int): depth of the lake
    """
    
    info = "lake"
    representation = "l"

    def __init__(self, location, name, depth):
        super().__init__(location)
        self.name = name
        self.depth = depth

    def get_info(self):
        return f"{Lake.info} {self.name}, depth {self.depth}"

    def get_representation(self):
        return Lake.representation

    def get_size(self):
        """
        Getter method to get the depth of the lake

        Returns:
            depth(int): depth value of the lake  
        """
        return self.depth

    def __str__(self):
        return "lake"


class Crater(GeoFeature):
    """
    Creating the Crater class that inherits from GeoFeature

    Additional Arguments:
        name(str): name of the crater
        perimeter(int): perimeter of the crater
    """
    
    info = "crater"
    representation = "c"

    def __init__(self, location, name, perimeter):
        super().__init__(location)
        self.name = name
        self.perimeter = perimeter

    def get_info(self):
        return f"{Crater.info} {self.name}, perimeter {self.perimeter}"

    def get_representation(self):
        return Crater.representation

    def get_size(self):
        """
        Getter method to get the perimeter of the crater

        Returns:
            perimeter(int): perimeter value of the crater  
        """
        return self.perimeter

    def __str__(self):
        return "crater"