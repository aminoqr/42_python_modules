import time
from functools import wraps
from typing import Callable, Any


def spell_timer(func: Callable) -> Callable:
    """Decorator that measures function execution time"""
    @wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory that validates power levels"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, spell_name: str, power: int, *args, **kwargs) -> Any:
            # Check if the power argument is >= min_power
            if power >= min_power:
                return func(self, spell_name, power, *args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator that retries failed spells"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """Demonstrates staticmethod and decorated instance methods"""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Validates name: letters/spaces and at least 3 chars"""
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Successfully casts a spell if power is sufficient"""
        return f"Successfully cast {spell_name} with {power} power"


def main():
    """Main function to test all Tower artifacts."""
    # 1. Testing spell_timer
    print("\nTesting spell timer...")

    @spell_timer
    def slow_spell():
        time.sleep(0.1)
        return "Fireball cast!"
    print(f"Result: {slow_spell()}")

    # 2. Testing MageGuild
    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(f"{guild.validate_mage_name('Alex')}")
    print(f"{guild.validate_mage_name('Jo')}")

    # Testing decorated cast_spell
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fire", 5))

    # # 3. Testing retry_spell
    # print("\nTesting retry spell...")
    # @retry_spell(max_attempts=3)
    # def unstable_spell():
    #     raise Exception("Mana leak!")
    # print(unstable_spell())


if __name__ == "__main__":
    main()
