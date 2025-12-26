#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age_day):
        self.name = name
        self.height = height
        self.age_day = age_day

    def display_info(self):
        print(f"{self.name}: {self.height}cm, {self.age_day} days old")

    def grow(self):
        self.height += 1

    def age(self):
        self.age_day += 1


def main():
    rose = Plant("Rose", 25, 30)
    days = 6
    old_height = rose.height
    print("=== Day 1 ===")
    rose.display_info()
    for day in range(days):
        rose.grow()
        rose.age()
    print("=== Day 7 ===")
    rose.display_info()
    print(f"Growth this week: +{rose.height - old_height}cm")


if __name__ == "__main__":
    main()
