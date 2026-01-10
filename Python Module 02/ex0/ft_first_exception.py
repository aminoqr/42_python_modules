#!/usr/bin/env python3

def check_temperature(temp_str):
    print(f"Testing temperature: {temp_str}")
    try:
        try:
            tmp = int(temp_str)
        except ValueError:
            print(f"Error: '{temp_str}' is not a valid number")
            return None
        if tmp > 40:
            raise ValueError(f"Error: {tmp}°C is too hot for plants "
                             f"(max 40°C)")
        elif tmp < 0:
            raise ValueError(f"Error: {tmp}°C is too cold for plants "
                             f"(min 0°C)")
        print(f"Temperature {tmp}°C is perfect for plants!")
        return tmp
    except ValueError as e:
        print(e)


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    print()
    inputs = ["25", "abc", "100", "-50"]

    for i in inputs:
        check_temperature(i)
        print()
    print("All tests completed - program didn't crash")


test_temperature_input()
