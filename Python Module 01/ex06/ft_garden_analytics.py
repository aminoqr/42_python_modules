#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, amount=1):
        self.height += amount
        print(f"{self.name} grew {amount}cm")


class FlowerPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def bloom(self):
        print(f", {self.color.lower()} flowers (blooming)", end='')


class PrizeFlower(FlowerPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points


class GardenManager:
    total_gardens = 0

    def __init__(self):
        self.gardens = {}
        self.total_growth_records = {}
        GardenManager.total_gardens += 1

    @staticmethod
    def is_valid_height(height):
        return height >= 0

    @classmethod
    def create_garden_network(cls):
        return cls()

    def add_plant(self, garden_name, plant):
        if garden_name not in self.gardens:
            self.gardens[garden_name] = []
            self.total_growth_records[garden_name] = 0
        self.gardens[garden_name].append(plant)
        print(f"Added {plant.name} to {garden_name}'s garden")

    def grow_garden(self, garden_name):
        print(f"{garden_name} is helping all plants grow...")
        for plant in self.gardens[garden_name]:
            plant.grow()
            self.total_growth_records[garden_name] += 1
        print()

    def garden_report(self, garden_name):
        print(f"=== {garden_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.gardens[garden_name]:
            print(f"- {plant.name}: {plant.height}cm", end='')
            if isinstance(plant, PrizeFlower):
                plant.bloom()
                print(f", Prize points: {plant.prize_points}", end='')
            elif isinstance(plant, FlowerPlant):
                plant.bloom()
            print()
        print()
        num_plants = len(self.gardens[garden_name])
        growth = self.total_growth_records[garden_name]
        print(f"Plants added: {num_plants}, Total growth: {growth}cm")

        stats = self.GardenStats(self.gardens[garden_name])
        stats.count_types()

    class GardenStats:
        def __init__(self, plants):
            self.plants = plants

        def count_types(self):
            p, f, pf = 0, 0, 0
            for plant in self.plants:
                if isinstance(plant, PrizeFlower):
                    pf += 1
                elif isinstance(plant, FlowerPlant):
                    f += 1
                else:
                    p += 1
            print(f"Plant types: {p} regular, {f} flowering, {pf} prize"
                  "flowers")


def calculate_score(manager, garden_name):
    return sum(p.height for p in manager.gardens[garden_name])


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()
    mgr = GardenManager.create_garden_network()

    mgr.add_plant("Alice", Plant("Oak Tree", 100))
    mgr.add_plant("Alice", FlowerPlant("Rose", 25, "red"))
    mgr.add_plant("Alice", PrizeFlower("Sunflower", 50, "yellow", 10))
    mgr.add_plant("Bob", Plant("Bush", 91))
    print()
    mgr.grow_garden("Alice")
    mgr.garden_report("Alice")
    print()
    print(f"Height validation test: {GardenManager.is_valid_height(10)}")
    alice_score = calculate_score(mgr, "Alice")
    bob_score = calculate_score(mgr, "Bob")
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")