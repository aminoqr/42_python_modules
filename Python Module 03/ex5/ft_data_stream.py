from typing import Generator
from random import randint, choice
from time import time

event_count = 1000


def primes() -> Generator[int, None, None]:
    a = 3
    yield 2
    while True:
        for i in range(2, a):
            if a % i == 0:
                break
            if i == a-1:
                yield a
        a += 1


def fibonacci_seq() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


def event_generator(count: int) -> Generator[str, None, None]:
    players = ["Alice", "Bob", "Charlie"]
    actions = ["killed monster.", "found treasure", "leveled up"]
    for i in range(1, event_count+1):
        lvl = randint(1, 15)
        name = choice(players)
        action = choice(actions)

        yield f"Event {i}: Player {name} (level {lvl}) {action}"


print("=== Game Data Stream Processor ===")
print()
print(f"Processing {event_count} game events...")
print()
high_lvl_players = 0
treasure_events = 0
lvlup_events = 0
total = 0

stream = event_generator(1000)
start_time = time()
for i in stream:
    if total < 3:
        print(i)
        total += 1
    elif total == 3:
        print("...")
        total += 1
    if "(level 10)" in i or "(level 11)" in i or "(level 12)" in i or\
       "(level 13)" in i or "(level 14)" in i or "(level 15)" in i:
        high_lvl_players += 1
    if "found treasure" in i:
        treasure_events += 1
    if "leveled up" in i:
        lvlup_events += 1
finish_time = time()
duration = finish_time - start_time
print("\n=== Stream Analytics ===")
print(f"Total events processed : {event_count}")
print(f"High-level players (10+): {high_lvl_players}")
print(f"Treasure events: {treasure_events}")
print(f"Level-up events: {lvlup_events}")
print()
print("Memory usage: Constant (streaming)")
print(f"Processing time: {duration:.3f} seconds.")
print()
print("=== Generator Demonstration ===")
fib_gen = fibonacci_seq()
print("Fibonacci sequence (first 10): ", end="")
for i in range(10):
    print(next(fib_gen), end="")
    if i < 9:
        print(", ", end="")
print("\nPrime numbers (first 5): ", end="")
prime_gen = primes()
for i in range(5):
    print(next(prime_gen), end="")
    if i < 4:
        print(", ", end="")
