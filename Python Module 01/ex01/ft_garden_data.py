#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    garden = [p1, p2, p3]
    print("=== Garden Plant Registry ===")
    for plant in garden:
        plant.display_info()


if __name__ == "__main__":
    main()
