#!/usr/bin/env python3

import math


def print_distance(position: tuple[int, int, int],
                   zero: tuple[int, int, int]) -> None:
    total = 0
    for i in range(3):
        total += (position[i] - zero[i])**2
    print(f"Distance between {zero} and {position}: {math.sqrt(total):.2f}")


def parse_position(new_pos: str,
                   position: tuple[int, int, int]
                   ) -> tuple[int, int, int] | None:
    try:
        new_pos_list = new_pos.split(",")
        position_list = list(position)
        for i in range(3):
            position_list[i] = int(new_pos_list[i])
        print(f"Parsed position: {tuple(position_list)}")
        return (position_list[0], position_list[1], position_list[2])
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details: - Type {type(e).__name__}, Args: ({e})")


def game_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print()
    position = (10, 20, 5)
    zero = (0, 0, 0)
    print(f"Position created: {position}")
    print_distance(position, zero)
    print()
    new_pos = "3,4,0"
    print(f"Parsing coordinates: \"{new_pos}\"")
    position = parse_position(new_pos, position)
    if position is not None:
        print_distance(position, zero)
    print()
    invalid_pos = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{invalid_pos}\"")
    if position is not None:
        parse_position(invalid_pos, position)
    print()
    print("Unpacking demonstration:")
    if position is not None:
        print(f"Player at x={position[0]}, y={position[1]}, z={position[2]}")
        print(f"Coordinates:  X={position[0]}, "
              f"Y={position[1]}, Z={position[2]}")


game_coordinate_system()
