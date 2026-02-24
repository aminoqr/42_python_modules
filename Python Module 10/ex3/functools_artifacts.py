from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import List, Callable, Dict


def spell_reducer(spells: List[int], operation: str) -> int:
    """Reduce spell powers using a specified operation."""
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    op_func = ops.get(operation)

    if not spells:
        return 0

    return reduce(op_func, spells)


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    """Creates specialized enchantment functions with power set to 50."""
    return {
        'fire_enchant': partial(base_enchantment, 50, 'fire'),
        'ice_enchant': partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': partial(base_enchantment, 50, 'lightning')
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Calculates nth Fibonacci number using a cache for performance."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    """Creates a spell system that handles different input types."""
    @singledispatch
    def base_spell(arg):
        return "Unknown magic type"

    @base_spell.register(int)
    def _(damage):
        return f"Cast damage spell: {damage} power"

    @base_spell.register(str)
    def _(name):
        return f"Cast enchantment: {name}"

    @base_spell.register(list)
    def _(spells):
        return f"Multi-cast: {len(spells)} spells"

    return base_spell


def main():
    # 1. Testing spell_reducer
    print("\nTesting spell reducer...")
    spell_powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")

    # # 2. Testing partial_enchanter
    # print("\nTesting partial enchanter...")
    # def base_enchant(power, element, target):
    #     return f"{element.capitalize()} {target} with {power} power"
    # enchanters = partial_enchanter(base_enchant)
    # print(enchanters['fire_enchant']("Sword"))
    # print(enchanters['ice_enchant']("Shield"))

    # 3. Testing memoized_fibonacci
    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    # # 4. Testing spell_dispatcher
    # print("\nTesting spell dispatcher...")
    # dispatch = spell_dispatcher()
    # print(dispatch(100))        # Testing int
    # print(dispatch("Fireball")) # Testing str
    # print(dispatch([1, 2, 3]))  # Testing list


if __name__ == "__main__":
    main()
