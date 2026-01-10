#!/usr/bin/env python3
test_mode = "value"


def garden_operations():
    if test_mode == "value":
        int("abc")
    elif test_mode == "division":
        10/0
    elif test_mode == "file":
        open("missing.txt")
    elif test_mode == "key":
        dct = {"a": 2}
        dct["missing plant"]


def test_error_types():
    global test_mode
    print("=== Garden Error Types Demo ===")
    print()
    test_modes = ["value", "division", "file", "key"]
    for i in test_modes:
        test_mode = i
        try:
            garden_operations()
        except (ValueError, ZeroDivisionError, FileNotFoundError,
                KeyError) as e:
            print(f"Testing {type(e).__name__}...")
            print(f"Caught an {type(e).__name__}: {e}")
            print()
    print("Testing multiple errors together...")
    try:
        garden_operations()
    except (ValueError, ZeroDivisionError, FileNotFoundError,
            KeyError):
        print("Caught an error, but program continues!")
        print()
    print("All error types tested succesfully!")


test_error_types()
