# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 14:49:43 by stmaire         #+#    #+#               #
#  Updated: 2026/02/16 17:51:26 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math
import sys

def calculate_distance(point1: tuple, point2: tuple) -> float:
     """Calculate distance between 3D coordinates"""
     x1, y1, z1 = point1
     x2, y2, z2 = point2
     distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
     return distance

def parsing_coordinates(data: str) -> tuple:
    """Check the input and return a data tuple"""
    elements = data.split(",")
    
    if len(elements) != 3:
        print("Invalid input:"
              "Usage: python3 ft_coordinate_system.py \"int1, int2, int3\" ...")
        return None
        
    try:   
        x = int(elements[0])
        y = int(elements[1])
        z = int(elements[2])
        return (x, y, z)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        # print(f"Error details - Type: {type(e).__name__}, Args: {e.args}") 
        print(f"Error details - Type: ValueError, Args: {e.args}")
        return None

def display_coordinate_system() -> None:
    """Handle command line input and demo mode"""
    print("=== Game Coordinate System ===")
    
    if len(sys.argv) > 1:
        origin = (0, 0, 0)
        data_input = sys.argv[1]
        print(f"Input received: \"{data_input}\"")
        
        coordinate = parsing_coordinates(data_input)
        
        if coordinate is not None:
            print(f"Parsed position: {coordinate}")
            distance = calculate_distance(origin, coordinate)
            print(f"Distance between {origin} and {coordinate}: {distance:.2f}")   
        
    else:
        print("No argument provided, running demo mode")
        print ("=== Game Coordinate System ===\n")
        
        data = [
             (0, 0, 0),
             (10, 20, 5),
             "3, 4, 0", 
             "abc,def,ghi"
        ]
        
        print(f"Position created: {data[1]}")
        distance = calculate_distance(data[0], data[1])
        print(f"Distance between {data[0]} and {data[1]}: {distance:.2f}\n")
        
        print(f'Parsing coordinates: "{data[2]}"')
        parsed_coord = parsing_coordinates(data[2])
        print(f"Parsed position: {parsed_coord(data[2])}")
        distance = calculate_distance(data[0], parsed_coord(data[2]))
        print(f"Distance between {data[0]} and {parsed_coord(data[2])}: {distance:.2f}\n")

        print(f'Parsing invalid coordinates: "{data[3]}"')
        parsing_coordinates(data[3])
        

if __name__ == "__main__":
    display_coordinate_system()