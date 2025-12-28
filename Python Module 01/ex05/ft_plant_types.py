#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def print_info(self):
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days,"
              f" {self.color} color")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides {self.trunk_diameter * 1.56:.2f} "
              f"square meters of shade")

    def print_info(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter} diameter")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season}")
        print(f"{self.name} is rich in {self.nutritional_value}")


def main():
    flower1 = Flower("Rose", 25, 30, "red")
    flower2 = Flower("Sunflower", 120, 40, "yellow")
    tree1 = Tree("Oak", 500, 1825, 50)
    tree2 = Tree("Bamboo", 250, 200, 5)
    vege1 = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin c")
    vege2 = Vegetable("Cucumber", 70, 70, "warm-season", "vitamin-k")

    print("=== Garden Plant Types ===")
    print()
    flower1.print_info()
    flower1.bloom()
    print()
    flower2.print_info()
    flower2.bloom()
    print()
    tree1.print_info()
    tree1.produce_shade()
    print()
    tree2.print_info()
    tree2.produce_shade()
    print()
    vege1.print_info()
    print()
    vege2.print_info()


if __name__ == "__main__":
    main()
