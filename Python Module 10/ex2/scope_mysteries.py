from typing import Dict, Callable, Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Returns a function that accumulates power over time."""
    current_power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal current_power
        current_power += amount
        return current_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    """Returns a function that applies the specified enchantment."""
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> Dict[str, Callable]:
    """Creates a private storage system using closures."""
    vault = {}

    def store(key: str, value: Any) -> None:
        """Stores a value in the private vault."""
        vault[key] = value

    def recall(key: str) -> Any:
        """Retrieves a value or returns a failure message."""
        return vault.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


def main():
    print("\nTesting mage counter...")
    my_counter = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {my_counter()}")

    print("\nTesting enchanment factory...")
    my_enchantment1 = enchantment_factory("Flaming")
    my_enchantment2 = enchantment_factory("Frozen")
    print(my_enchantment1("Sword"))
    print(my_enchantment2("Shield"))

    # print("\nTesting spell accumulator...")
    # current_power = 10
    # my_accumulator = spell_accumulator(current_power)
    # print(f"Current power: {current_power}, accumulated:{my_accumulator(5)}")


if __name__ == "__main__":
    main()
