#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager():
    def __init__(self):
        self.plants = {}

    def add_plant(self, name):
        try:
            if name is None or not name.strip():
                raise PlantError("Plant name cannot be empty!")
            self.plants[name] = {"water": 0, "sunlight": 8}
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        print("Watering plants...")
        print("Opening watering system")
        try:
            for key, value in self.plants.items():
                value["water"] += 1
                print(f"Watering {key} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self):
        print("Checking plant health...")
        for key, value in self.plants.items():
            try:
                if value["water"] < 1:
                    raise WaterError(f"Water level {value['water']}"
                                     f" is too low (min 1)")
                elif value["water"] > 10:
                    raise WaterError(f"Water level {value['water']} "
                                     f"is too high (max 10)")
                if value['sunlight'] < 2:
                    raise PlantError(f"Sunlight hours {value['sunlight']} "
                                     "is too low (min 2)")
                elif value['sunlight'] > 12:
                    raise PlantError(f"Sunlight hours {value['sunlight']} "
                                     "is too high (max 12)")
                print(f"{key}: healthy (water: {value['water']},"
                      f" sun : {value['sunlight']})")
            except GardenError as e:
                print(f"Error checking {key}: {e}")


print("=== Garden Management System ===")
print()
manager = GardenManager()
print("Adding plants to garden...")
manager.add_plant("tomato")
manager.plants["tomato"]["water"] = 4
manager.add_plant("lettuce")
manager.plants["lettuce"]["water"] = 14
manager.add_plant("   ")
print()
manager.water_plants()
print()
manager.check_health()
print()
print("Testing error recovery...")
try:
    raise GardenError("Not enough water in tank")
except GardenError as e:
    print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
print()
print("Garden management system test complete!")
