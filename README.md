# 🚀 Robbie the Explorer: Autonomous Planetary Exploration System 🚀

This repository presents a sophisticated Python-based simulation of Robbie, an autonomous robot designed for planetary exploration. The project meticulously models geological features, advanced robot movement (including map wrapping), dynamic exploration mechanics with skill acquisition, and a **strategic robot transformation system** to optimize mission efficiency. Developed with a strong focus on object-oriented design and algorithmic problem-solving, this system demonstrates robust capabilities essential for complex, real-world robotic applications.

---
## Table of Contents

* [Project Overview](#project-overview)
* [Key Features & Design Principles](#key-features--design-principles)
    * [Geological Feature Management (`geo_features.py`)](#geological-feature-management-geo_featurespy)
    * [Advanced Robot Operations (`robot.py`)](#advanced-robot-operations-robotpy)
    * [Interactive Mission Control (`user_explore.py`)](#interactive-mission-control-user_explorepy)
* [Technical Implementation Highlights](#technical-implementation-highlights)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation & Setup](#installation--setup)
    * [Running the Application](#running-the-application)
* [File Structure](#file-structure)
* [Author](#author)

---
## Key Features & Design Principles

This project demonstrates robust software engineering practices through its modular design and intricate logic:

### Geological Feature Management (`geo_features.py`)

* **Abstract Base Class (`GeoFeature`):** Establishes a common interface for all geological features, ensuring consistency across `Mountain`, `Lake`, and `Crater` types.
* **Specialized Feature Data:** Each feature subclass (e.g., `Mountain`, `Lake`, `Crater`) correctly stores its unique characteristic (height, depth, perimeter) and provides methods to retrieve specific details.
* **Efficient Map Data Loading:** The `load_map_data` function effectively parses the `geo_features.txt` file, extracting map dimensions and populating a structured map of features, ready for Robbie's exploration.

### Advanced Robot Operations (`robot.py`)

This module houses Robbie's sophisticated movement and exploration capabilities:

* **Intelligent Pathfinding:** The `move_to` method uses a **Breadth-First Search (BFS)** algorithm to calculate the shortest path between any two points on the map. This includes clever handling of **map wrapping** (moving off one edge brings Robbie onto the opposite) and ensures **non-diagonal movements** only.
* **Dynamic Exploration Mechanics:** Robbie's `explore_feature` method calculates the exact time needed for exploration (rounding up to full days for resting). Critically, Robbie's **exploration speed for a specific feature type permanently increases by 20%** after each successful exploration of that type, reflecting gained experience.
* **Strategic Robot Transformation:**
    * Robbie can transform **only once per mission** into a `Drone` or an `AUV`, each with different initial exploration speeds for various feature types.
    * The `calculate_mission_time` function effectively simulates a mission for any robot type (`Robot`, `Drone`, `AUV`) without affecting Robbie's actual state.
    * The `execute_mission` method intelligently **determines the optimal robot type** (prioritizing no transformation, then Drone, then AUV if mission times are equal) to complete a given list of features in the shortest possible duration.
    * Crucially, Robbie's **gained skills persist** across transformations, ensuring his experience always contributes to mission efficiency. After each mission, Robbie automatically reverts to his base `Robot` form.
    * The base exploration speeds for each robot type are:

        | Robot Type         | Mountain (height unit/day) | Lake (depth unit/day) | Crater (perimeter unit/day) |
        | :----------------- | :------------------------- | :-------------------- | :-------------------------- |
        | Robbie the Robot   | 6                          | 8                     | 10                          |
        | Robbie the Drone   | 12                         | 6                     | 8                           |
        | Robbie the AUV     | 2                          | 12                    | 6                           |


### Interactive Mission Control (`user_explore.py`)

This is the command-line interface that brings Robbie's mission to life:

* **Comprehensive Command Set:** Supports commands from all tasks, including:
    * `show map`: Visualizes the Martian terrain.
    * `info <Y> <X>`: Retrieves detailed information about features at a specific location.
    * `moveto <Y> <X>`: Commands Robbie to navigate to a new location.
    * `explore`: Initiates exploration of a geological feature at Robbie's current location.
    * `display journey`: Shows a chronological log of Robbie's movements and explorations.
    * `mission <list of features>`: Initiates an automated mission to explore a sequence of features, leveraging Robbie's transformation optimization.
* **Seamless Integration:** Efficiently coordinates interactions between the `Robot` and `GeoFeature` modules, translating user commands into Robbie's actions.

---
## Technical Implementation Highlights

* **Object-Oriented Design:** The project is built on a strong OOP foundation, with classes like `GeoFeature` and `Robot` encapsulating data and behavior, which promotes modularity and maintainability for this complex system.
* **Algorithmic Problem-Solving:** The core movement logic leverages efficient **Breadth-First Search (BFS)** for shortest pathfinding, demonstrating effective application of graph algorithms in a grid-based environment.
* **Dynamic State Management:** The robot's skills and exploration speeds are dynamically updated and persist correctly, even across temporary transformations for mission planning, showcasing robust state management.
* **Modular Architecture:** By separating concerns into `geo_features.py` (data models), `robot.py` (core logic), and `user_explore.py` (interface), the codebase remains clean, scalable, and easy to navigate.

---
## Getting Started

To get Robbie's exploration system up and running on your local machine, follow these simple steps.

### Prerequisites

* Python 3.x

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/suveer-dhawan/robot-explorer.git](https://github.com/suveer-dhawan/robot-explorer.git)
    cd robot-explorer
    ```
2.  **Ensure you have a `geo_features.txt` file** in the root directory. You can create one based on the example format:
    ```
    4,5
    1,1,mountain,olympus mons,21
    2,4,lake,eridania,10
    3,2,crater,huygens,45
    ```

### Running the Application

Execute the `user_explore.py` file to start the interactive command-line interface:

```bash
python user_explore.py
```
Once running, you'll see a prompt (```>```) where you can enter commands like ```show map```, ```info 1 1```, ```moveto 3 2```, ```explore```, ```display journey```, ```mission olympus mons,eridania```, or ```quit```.

## File Structure

The project is organized with a clear and logical file structure:

```
.
├── geo_features.py             # Defines geological feature classes (GeoFeature, Mountain, Lake, Crater) and map loading.
├── robot.py                    # Implements the Robot's core logic: movement, exploration, and transformation.
├── user_explore.py             # The main application script for user interaction and mission control.
├── geo_features.txt            # Example file containing map dimensions and geological features.
└── README.md                   # This documentation file.
```
---

## Author

* **Suveer Dhawan** - [GitHub Profile](https://github.com/suveer-dhawan)