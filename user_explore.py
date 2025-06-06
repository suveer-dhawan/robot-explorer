"""
Name - Suveer Dhawan

This module is created for user interaction with Robbie the robot. The user has options
to see the map of Mars, gather info for any location on the map, move Robbie to a location, 
explore the location if a feature exists there, and view Robbie's journey. The user can also
assign a list of missions for Robbie to explore features on Mars.
"""

import geo_features
import robot

def create_map(ref_file):
    """
    The function takes a file as input, opens and reads the file and creates a map_list, which 
    is a list of lists containing locations and their geological features

    Parameters:
        ref_file (CSV file): CSV file containing location data for the map

    Returns:
        map_list: list of lists containing geological features of locations
    """
    
    # opening and reading CSV file, and taking out header as size of the map
    with open(ref_file, 'r') as loc_file:
        lines = loc_file.readlines()
        header = lines[0].strip().split(",")
        map_size = geo_features.Size(int(header[0]), int(header[1]))
        map_height = map_size.height
        map_width = map_size.width

        # creating a list of lists initialized with None values
        map_list = []

        for row in range(map_height):
            
            map_row = []
            for col in range(map_width):
                
                # Initializing entire map_list with None
                map_row.append(None)
            
            map_list.append(map_row)

        # reading through remaining lines and unpacking data 
        for line in lines[1:]:

            data = line.strip().split(",")

            loc_row = int(data[0])
            loc_col = int(data[1])

            location = (loc_row, loc_col)
            geo_type = data[2]
            geo_name = data[3]
            geo_dimension = int(data[4])

            # Using conditional statements, to create corresponding child class and update
            # Map list
            if geo_type == "mountain":
                geo = geo_features.Mountain(location, geo_name, geo_dimension)

            elif geo_type == "lake":
                geo = geo_features.Lake(location, geo_name, geo_dimension)
                
            elif geo_type == "crater":
                geo = geo_features.Crater(location, geo_name, geo_dimension)

            else:
                continue

            map_list[loc_row][loc_col] = geo 

        # replacing None values with GeoFeature base class
        for row in range(map_height):
            for col in range(map_width):

                if map_list[row][col] is None:
                    map_list[row][col] = geo_features.Location(row, col)

                    map_list[row][col] = geo_features.GeoFeature(location)

    return map_list
                

def show_map(map_list):
    """
    Takes map_list as input and prints the map in a graphical form to show the user

    Parameters:
        map_list: list of lists containing geological features of locations
    """
    
    # Looping through nested list and displaying output to user
    for row in map_list:
        
        for geo in row:
            print(geo.get_representation(), end='')
        
        print()

def robot_move(robot_object, target_loc):
    """
    Moves the Robot on Mars by invoking the move method of Robot class

    Parameters
        robot_object: Robot object
        target_loc (tuple): intended target location for robot 

    Returns
        string - output displaying robot's movemement or lack thereof
    """
    
    #Initializing starting location and ensuring new location is different before moving Robbie
    start_loc = robot_object.location    
    
    if start_loc == target_loc:
        return "same location"

    robot_object.move(target_loc)

    return f"move from {geo_features.Location(*start_loc)} to {geo_features.Location(*target_loc)}"

def robot_explore(robot_object, map_list):
    """
    Helps the Robot explore features on Mars by invoking the explore method of Robot class

    Parameters
        robot_object: Robot object
        map_list: list of lists containing geological features of locations

    Returns
        string - output displaying robot's exploration of a feature or lack thereof
    """

    row, col = robot_object.location
    feature = map_list[row][col]
    
    if str(feature) != "GeoFeature":
        
        robot_object.explore(feature)
        return f"explore {feature} {feature.name}"

    else:
        return "nothing to explore"

def robot_mission(robot_object, map_list, mission_list):
    """
    Function for the Robot to go on exploration missions. Calls the mission_explore method 
    and uses get_mission_log to display output to the user. 

    Parameters- 
        robot_object: Robot object
        map_list: list of lists containing geological features of locations
        mission_list: list of features/locations to explore in the mission
    """
    # Initializing a feature list and mission object list
    feature_list = []
    mission_object_list = []

    # Taking out features from the map
    for row in map_list:
        for feature in row:
            
            # Ensuring we only add features, not empty locations
            if str(feature) != "GeoFeature":
                feature_list.append(feature)
    
    for mission in mission_list:
        for feature in feature_list:
                
            # Adding corresponding names to new list
            if feature.name == mission:
                mission_object_list.append(feature)
    
    robot_object.mission_explore(mission_object_list)
        
    # Getting mission log and printing for user
    mission_log = robot_object.get_mission_log()

    if mission_log:
        for entry in mission_log:
            print(entry)
    
    else:
        print ()


def display_journey(robot_object):
    """
    Function to display the journey of the Robot so far, by calling the get_journey() method of the 
    Robot class and printing it to display output to the user.

    Parameters- 
        robot_object: Robot object
    """

    journey_log = robot_object.get_journey()

    if journey_log:
        for entry in journey_log:
            print(entry)
    
    else:
        print ()
  

if __name__ == "__main__":
    
    # Creating map using geo_features.txt and initializing Robbie
    map_list = create_map("geo_features.txt")

    robbie = robot.Robot(map_list)

    while True:

        #Taking user input and making it lowercase
        user_input = input("> ")
        lower_input = user_input.strip().lower()

        # Using if else conditionals for different possible user inputs 
        if lower_input == "quit":
            print("goodbye")
            break

        elif lower_input == "show map":
            
            # calling show map to display map to user
            show_map(map_list)

        elif lower_input.startswith("info "):
            
            # unpacking user input into location data and calling get_info to display 
            # location info to user
            loc_data = user_input.strip().split()
            loc_row = int(loc_data[1])
            loc_col = int(loc_data[2])

            feature = map_list[loc_row][loc_col]

            print(feature.get_info())

        elif lower_input.startswith("moveto "):

            # Unpacking user input and gathering target location for movemement
            move_input = user_input.strip().split()
            target_loc = (int(move_input[1]), int(move_input[2]))

            output = robot_move(robbie, target_loc)
            print(output)

        elif lower_input == "explore":
            
            output = robot_explore(robbie, map_list)
            print(output)

        elif lower_input == "display journey":

            display_journey(robbie)

        elif lower_input.startswith("mission "):
            
            prefix_len = len("mission ")
            mission_input = user_input[prefix_len:].strip()

            mission_list = [mission.strip() for mission in mission_input.split(",")]

            robot_mission(robbie, map_list, mission_list)