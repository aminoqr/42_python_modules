#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name, height=0, age=0):
        self._name = name
        self._height = height if height >= 0 else 0
        self._age = age if age >= 0 else 0

    def set_height(self, new_height):
        if new_height < 0:
            print(f"Invalid operation attempted: height "
                  f"{new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, new_age):
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} days"
                  f" [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def print_info(self):
        print(f"Current plant: {self._name} ({self.get_height()}cm,"
              f" {self.get_age()} days)")


def main():
    print("=== Garden Security System ===")
    p1 = SecurePlant("Rose", 20, 10)
    print("Plant created: Rose")
    p1.set_height(25)
    p1.set_age(30)
    print()
    p1.set_height(-5)
    print()
    p1.print_info()


if __name__ == "__main__":
    main()
