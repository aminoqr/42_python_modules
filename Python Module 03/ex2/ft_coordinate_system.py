#!/usr/bin/env python3

import math


def print_distance(position, zero):
    total = 0
    for i in range(3):
        total += (position[i] - zero[i])**2
    print(f"Distance betweem {zero} and {position}: {math.sqrt(total):.2f}")


def parse_position(new_pos, position):
    try:
        new_pos = new_pos.split(",")
        position = list(position)
        for i in range(3):
            position[i] = int(new_pos[i])
        print(f"Parsed position: {tuple(position)}")
        return tuple(position)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details: - Type {type(e).__name__}, Args: ({e})")


def game_coordinate_system():
    print("=== Game Coordiante System ===")
    print()
    position = (10, 20, 5)
    zero = (0, 0, 0)
    print(f"Position created: {position}")
    print_distance(position, zero)
    print()
    new_pos = "3,4,0"
    print(f"Parsing coordinates: \"{new_pos}\"")
    position = parse_position(new_pos, position)
    print_distance(position, zero)
    print()
    invalid_pos = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{invalid_pos}\"")
    parse_position(invalid_pos, position)
    print()
    print("Unpacking demonstration:")
    print(f"Plater at x={position[0]}, y={position[1]}, z={position[2]}")
    print(f"Coordinates:  X={position[0]}, Y={position[1]}, Z={position[2]}")


game_coordinate_system()
