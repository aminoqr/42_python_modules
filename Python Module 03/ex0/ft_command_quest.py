#!/usr/bin/env python3

import sys

print("=== Command Quest ===")
ac = len(sys.argv)
if ac == 1:
    print("No arguments provided!")
print(f"Program name: {sys.argv[0]}")
if ac > 1:
    print(f"Arguments received: {ac-1}")
    for i in range(1, ac):
        print(f"Argument {i}: {sys.argv[i]}")

print(f"Total arguments: {ac}")
print()
