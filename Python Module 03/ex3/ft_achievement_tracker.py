alice_ach = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob_ach = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie_ach = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}

all_unique_ach = alice_ach.union(bob_ach, charlie_ach)
total_uniqe_ach = len(all_unique_ach)

common = alice_ach.intersection(bob_ach, charlie_ach)
alice_rare = alice_ach.difference(bob_ach, charlie_ach)
bob_rare = bob_ach.difference(alice_ach, charlie_ach)
charlie_rare = charlie_ach.difference(alice_ach, bob_ach)
all_rare = alice_rare.union(bob_rare, charlie_rare)

alice_bob_common = alice_ach.intersection(bob_ach)
alice_unique_bob = alice_ach.difference(bob_ach)
bob_unique_alice = bob_ach.difference(alice_ach)

print("=== Achievements Tracker System ===")
print()
print(f"Player alice achievements: {alice_ach}")
print(f"Player bob achievements: {bob_ach}")
print(f"Player charlie achievements: {charlie_ach}")
print()
print("=== Achievement Analytics ====")
print(f"All unique achievements: {all_unique_ach}")
print(f"Total unique achievements: {total_uniqe_ach}")
print()
print(f"Common to all players: {common}")
print(f"Rare achievements (1 player): {all_rare}")
print()
print(f"Alice vs Bob common: {alice_bob_common}")
print(f"Alice unique: {alice_unique_bob}")
print(f"Bob unique: {bob_unique_alice}")
