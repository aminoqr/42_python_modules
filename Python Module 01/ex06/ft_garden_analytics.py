#!/usr/bin/env python3

class Plant():
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
        print(f"{self.color} flowers (blooming)", end='')


class PrizeFlower(FlowerPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points


class GardenManager():
    def __init__(self):
        self.gardens = {}
        self.total_growth_records = {}

    @staticmethod
    def is_valid_height(height):
        if (height < 0):
            return False
        else:
            return True

    @classmethod
    def create_garden_network(cls):
        instance = cls()
        return instance

    def garden_report(self, garden_name):
        print(f"=== {garden_name.capitalize()}'s Garden Report ===")
        print("Plants in garden")
        for plant in self.gardens[garden_name]:
            print(f"{plant.name}: {plant.height}cm", end='')
            if isinstance(plant, PrizeFlower):
                plant.bloom()
                print(f" Prize points: {plant.prize_points}", end='')
            elif isinstance(plant, FlowerPlant):
                plant.bloom()
            print()

        print("-" * 30)
        num_plants = len(self.gardens[garden_name])
        growth = self.total_growth_records[garden_name]

        print(f"Plants added: {num_plants}, Total growth: {growth}cm")

        stats = self.GardenStats(self.gardens[garden_name])
        stats.count_types()
        print("=" * 30)

    def add_plant(self, garden_name, plant):
        if garden_name not in self.gardens:
            self.gardens[garden_name] = []
            self.total_growth_records[garden_name] = 0
        self.gardens[garden_name].append(plant)
        print(f"Added {plant.name} to {garden_name}")

    class GardenStats():
        def __init__(self, plants):
            self.plants = plants

        def count_types(self):
            plant_count = 0
            flowerplant_count = 0
            prizeflower_count = 0
            for plant in self.plants:
                if isinstance(plant, PrizeFlower):
                    prizeflower_count += 1
                elif isinstance(plant, FlowerPlant):
                    flowerplant_count += 1
                elif isinstance(plant, Plant):
                    plant_count += 1
            print(f"{plant_count} regular, {flowerplant_count} flowering,"
                  f" {prizeflower_count} prize flowers")

    def grow_garden(self, garden_name):
        print(f"{garden_name} is helping all plants grow.")
        for plant in self.gardens[garden_name]:
            plant.grow()
            self.total_growth_records[garden_name] += 1


if __name__ == "__main__":
    # 1. Use the class method to create the manager
    manager = GardenManager.create_garden_network()

    # 2. Use the static method to check a height
    initial_height = 10
    if GardenManager.is_valid_height(initial_height):
        # 3. Create different types of plants
        p1 = Plant("Oak", initial_height)
        p2 = FlowerPlant("Rose", 5, "Red")
        p3 = PrizeFlower("Orchid", 8, "Purple", 50)

        # 4. Add them to Alice's garden
        manager.add_plant("Alice", p1)
        manager.add_plant("Alice", p2)
        manager.add_plant("Alice", p3)

        # 5. Make the garden grow
        print("\n--- Morning Care ---")
        manager.grow_garden("Alice")

        # 6. Generate the final report
        print("\n--- End of Day ---")
        manager.garden_report("Alice")
