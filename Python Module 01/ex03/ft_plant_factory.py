#!/usr/bin/env python3

class Plant:
    def __init__(self, name, starting_height, starting_age):
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age

    def created(self):
        print(f"Created: {self.name} ({self.starting_height}cm, "
              f"{self.starting_age} days)")


def main():
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Oak", 200, 365)
    p3 = Plant("Cactus", 5, 90)
    p4 = Plant("Sunflower", 80, 45)
    p5 = Plant("Fern", 15, 120)
    plants = [p1, p2, p3, p4, p5]
    count = 0
    print("=== Plant Factoru Output")
    for plant in plants:
        plant.created()
        count += 1
    print()
    print(f"Total plants created: {count}")


if __name__ == "__main__":
    main()
