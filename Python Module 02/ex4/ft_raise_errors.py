#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if plant_name is None:
            raise ValueError("Plant name cannot be empty!")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             f"is too low (min 2)")
        elif sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             f"is too high (max 12)")
        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")
    print()
    print("Testing good values...")
    check_plant_health("tomato", 5, 5)
    print()
    print("Testing empty plant name...")
    check_plant_health(None, 5, 5)
    print()
    print("Testing bad water level...")
    check_plant_health("tomato", 15, 3)
    print()
    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 5, 0)
    print()
    print("All error raising tests completed!")


test_plant_checks()
