#!/usr/bin/env python3

def water_plants(plant_list):
    is_successful = True
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        is_successful = False
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")
        if is_successful:
            print("Watering completed successfully!")


def test_watering_system():
    good_list = ["tomato", "lettuce", "carrots"]
    bad_list = ["tomato", None]
    print("=== Garden Water System ===")
    print()
    print("Testing normal watering...")
    water_plants(good_list)
    print()
    print("Testing with error...")
    water_plants(bad_list)
    print()
    print("Cleanup always happens, even with errors!")


test_watering_system()
