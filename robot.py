"""
Name - Suveer Dhawan

This program contains the Robot class and its functionality to move around Mars
and explore geological features. Robot also has the funcionality to transform
into a drone or an AUV.
"""

import geo_features
import math


class Robot:
    """ 
    The Robot class that is here to explore Mars

    Instance Variables:
        map_list: list of lists containing geological features of locations
        length (int): Length of the grid
        width (int): Width of the grid
        
        location (tuple): Position of the robot on the map
        explored_diary (list): list to track features explored on Mars by the Robot 
        journey (list): log to record the robot's journey
        total_days (int): tracker for number of days 
        r_type : default type for Robot class instance as robot

    Class Variables:
        speed_dict (dictionary): dictionary of dictionaries recording geological features 
            and different exploration speeds based on type of robot 
        r_types (list): List containing different transformation types that Robot can become 
    """

    r_types = ["robot", "drone", "auv"]

    speed_dict = {
        "robot": {"mountain": 6, "lake": 8, "crater": 10},
        "drone": {"mountain": 12, "lake": 6, "crater": 8},
        "auv": {"mountain": 2, "lake": 12, "crater": 6}
    }
    
    def __init__(self, map_list):
        """ 
        Creates a new Robot instance
        
        Arguments-
            map_list: list of lists containing geological features of locations
        """
        self.map_list = map_list
        self.length = len(map_list)
        self.width = len(map_list[0])
        
        self.location = (0,0)
        self.explored_diary = []
        self.journey = []
        self.total_days = 0
        self.r_type = Robot.r_types[0]
        self.mission_log = []

    def mission_explore(self, explore_list):
        """
        Method for the robot to complete missions on Mars. Updates the mission log. 

        Arguments:
            explore_list: List of features to explore in the mission
        """
        # Finding best form for the mission
        mission_form = self.best_form(explore_list)

        # Checking for transformation and updating robot type for the mission
        if mission_form != self.r_type:
            self.r_type = mission_form
            if mission_form == "drone":
                self.mission_log.append("transform into a drone")
            else:
                self.mission_log.append("transform into an AUV")

        else:
            self.mission_log.append("no transformation")

        # Looping through features in the list
        for feature in explore_list:

            # Loading current location of robot for mission start
            initial_loc = self.location

            # Checking if movememnt is required, then moving towards feature and exploring
            if initial_loc != feature.location:
                
                self.move(feature.location)
                self.explore(feature)
                
                self.mission_log.append(f"move from {geo_features.Location(*initial_loc)} to {geo_features.Location(*feature.location)} then explore {str(feature)} {feature.name}")
                
            # no movememnt required
            else:
                self.explore(feature)
                self.mission_log.append(f"same location, explore {str(feature)} {feature.name}")
        
        # Setting back to default at the end of the mission
        self.r_type = Robot.r_types[0]

    
    def move(self, target_loc):
        """
        Method to move the Robot on Mars, while updating the robot's location and computing 
        time taken for movement. Appends to journey and logs movemement.
        
        Arguments:
            target_loc (tuple): intended target location for robot
        """
        # Unpacking current and target location
        init_row, init_col = self.location
        final_row, final_col = target_loc

        # Initializing move start day and movement string 
        # Using geo_features.Location for formatting
        start_day = self.total_days
        move_string = f"move {geo_features.Location(*self.location)}"

        # Preference for Horizontal Movement
        if init_col != final_col:
            
            # Computing number of moves
            horizontal = self.move_calculator(init_col, final_col, self.width)

            # Looping through list of moves
            for move in horizontal:

                # Using % for wrapping
                init_col = (init_col + move) % self.width 
                
                # Updating class variables and concatenating to movement string
                self.total_days += 1
                self.location = (init_row, init_col)          
                move_string += f" -> {geo_features.Location(*self.location)}"

        # Then looking at Vertical movemement with same logic
        if init_row != final_row:
            vertical = self.move_calculator(init_row, final_row, self.length)
            
            for move in vertical:

                init_row = (init_row + move) % self.length
                
                self.total_days += 1
                self.location = (init_row, init_col)
                move_string += f" -> {geo_features.Location(*self.location)}"

        # Updating journey log
        travel_time = self.total_days - start_day

        if travel_time > 1:
            self.journey.append(f"Day {start_day + 1}-{self.total_days}: {move_string}") 

        else:
            self.journey.append(f"Day {self.total_days}: {move_string}")


    def move_calculator(self, start, finish, wrapping):
        """
        Calculates the number of moves from start to finish point (horizontal or vertical)

        Arguments- 
            start (int): starting position (row/column)
            finish (int): end position (row/column)
            wrapping (int): max length/width of grid

        Returns-
            move_list: List of moves denoted by +1 or -1 for forward or backward steps 
            taken by Robbie
        """
        # Computing forward or backward movements accounting for wrapping
        forward_moves = (finish - start) % wrapping
        back_moves = (start - finish) % wrapping

        # Prioritizing shortest distance
        if forward_moves < back_moves:
            move_list = [1] * forward_moves

        elif forward_moves > back_moves:
            move_list = [-1] * back_moves

        # Prioritizing wrapping when paths are equal by forcing movememnt 
        # in the direction of starting value
        else:
            if start < finish:
                move_list = [-1] * back_moves
            else:
                move_list = [1] * forward_moves

        return move_list


    def explore(self, feature):
        """
        Method to explore a geological feature and compute time taken to explore. Appends to journey 
        and logs exploration. Also updates exploration speeds and explored_diary

        Arguments- 
            feature: object of the geological feature to explore
        """
        # Initializing exploration start day
        start_day = self.total_days
        
        # Computing exploration time for the feature, based on current type/state of robot
        days = self.explore_time(self.r_type, feature, self.explored_diary, Robot.speed_dict)

        # Appending feature to diary and updating exploration speed after exploring 
        self.explored_diary.append(feature)
        for r_type in self.r_types:
            self.speed_dict[r_type][str(feature)] *= 1.2

        # using the ceiling function to account for rest time after exploration
        self.total_days += (days)

        # Updating journey log 
        if days > 1:
            self.journey.append(
                f"Day {start_day + 1}-{self.total_days}: explore {str(feature)} {feature.name}") 
        
        else:
            self.journey.append(f"Day {self.total_days}: explore {str(feature)} {feature.name}") 

    
    def best_form(self, explore_list):
        """
        Helps us determine what will be the best form for the robot, given a particular mission

        Arguments-
            explore_list: List of features to explore in the mission

        Returns-
            fastest(str): best form of the robot for this mission (robot, drone or auv)
        """    
        type_time = {}

        #Looping through different robot types to compute total time taken for each transformation
        for r_type in self.r_types:

            # Creating a copy of explored_diary for testing
            simulated_diary = self.explored_diary[:]
            
            # Manually creating a deepcopy of speed dict to be used for simulation best form testing
            simulated_dict = {}
            
            for robot in self.r_types:
                simulated_dict[robot] = self.speed_dict[robot].copy()
            
            total_days = 0
            
            # Using explpre_time to compute total duration for the mission
            for feature in explore_list:
                total_days += self.explore_time(r_type, feature, simulated_diary, simulated_dict)
                
                # Appending feature to simulated diary and updating exploration speed after exploring 
                simulated_diary.append(feature)
                
                for robot_type in self.r_types:
                    simulated_dict[robot_type][str(feature)] *= 1.2

            type_time[r_type] = total_days

        # finding fastest transformation type, preference: robot > drone > auv
        fastest = min(type_time, key=type_time.get)

        return fastest


    def explore_time(self, r_type, feature, diary, speed_dict):
        """
        Computes exploration time of a feature based on the type of transformation

        Arguments-
            r_type: transformation state of the robot
            feature: object of the geological feature to explore

        Returns-
            days (int): number of days taken to explore the feature
        """
        feature_type = str(feature)
                
        # Check if feature has previously been explored to determine exploration speed
        if feature_type not in diary:
            speed = speed_dict[r_type][feature_type]

        else:
            speed = speed_dict[r_type][feature_type] * 1.2
        
        days = math.ceil(feature.get_size()/speed)     
        return days

    
    def get_journey(self):
        """
        Getter method that returns the log of the journey so far
        """
        return self.journey

    def get_mission_log(self):
        """
        Getter method that returns the log of the mission and initializes it again
        """
        log = self.mission_log
        self.mission_log = []

        return log
