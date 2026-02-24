from typing import List, Callable, Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Returns a function that calls both spells and
       returns a tuple of results."""
    def combined(*args, **kwargs) -> tuple:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Returns a function that multiplies the base spell's result."""
    def amplified(*args, **kwargs) -> Any:
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Returns a function that only casts if the condition is True."""
    def cast_if_valid(*args, **kwargs) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return cast_if_valid


def spell_sequence(spells: List[Callable]) -> Callable:
    """Returns a function that casts all spells in order."""
    def sequence(*args, **kwargs) -> List[Any]:
        # Return a list of all spell results
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


def main():
    # Basic spells for testing
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def simple_damage(target: str) -> int:
        return 10

    # 1. Testing spell_combiner
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined('Dragon')[0]}, "
          f"{combined('Dragon')[1]}")

    # 2. Testing power_amplifier
    print("\nTesting power amplifier...")
    amplified_damage = power_amplifier(simple_damage, 3)
    original = simple_damage("Goblin")
    amplified = amplified_damage("Goblin")
    print(f"Original: {original}, Amplified: {amplified}")

    # # 3. Testing conditional_caster
    # print("\nTesting conditional caster...")
    # is_dragon = lambda target: target == "Dragon"
    # dragon_slayer = conditional_caster(is_dragon, fireball)

    # print(f"Casting on Dragon: {dragon_slayer('Dragon')}")
    # print(f"Casting on Goblin: {dragon_slayer('Goblin')}")

    # # 4. Testing spell_sequence
    # print("\nTesting spell sequence...")
    # party_buff = spell_sequence([fireball, heal])
    # print(f"Sequence results: {party_buff('Knight')}")


if __name__ == "__main__":
    main()
