import sys

inventory = {}
ac = len(sys.argv)

for i in range(1, ac):
    if ':' not in sys.argv[i]:
        print("Invalid input!")
    else:
        lst = sys.argv[i].split(':')
        inventory[lst[0]] = int(lst[1])

total_items = 0
for v in inventory.values():
    total_items += int(v)
unique_item_types = len(inventory)

item_names = list(inventory.keys())
most_abundant = item_names[0]
least_abundant = item_names[0]
moderate_items = {}
scarce_items = {}
restock_needed = []
for k, v in inventory.items():
    if v > inventory[most_abundant]:
        most_abundant = k
    if v < inventory[least_abundant]:
        least_abundant = k
    if v >= 5:
        moderate_items[k] = v
    else:
        scarce_items[k] = v
    if v < 2:
        restock_needed.append(k)

print("=== Inventory System Analysis ===")
print(f"total items in inventory: {total_items}")
print(f"Unique item types: {unique_item_types}")
print()
print("=== Current Inventory ===")
for k, v in inventory.items():
    perc = (int(v)*100)/total_items
    print(f"{k}: {v} units ({perc:.1f}%)")
print()
print("=== Inventory Statistics ===")
print(f"Most abundant: {most_abundant} ({inventory[most_abundant]} units)")
print(f"Least abundant: {least_abundant} ({inventory[least_abundant]} units)")
print()
print("=== Item Catagories ===")
print(f"Moderate: {moderate_items}")
print(f"Scarce: {scarce_items}")
print()
print("=== Management Suggestions ===")
print(f"Restock needed: {restock_needed}")
print()
print("=== Dictionary Properties Demo ===")
print(f"Dictionary keys: {list(inventory.keys())}")
print(f"Dictionary values: {list(inventory.values())}")
if 'sword' in inventory:
    print("Sample lookup - 'sword' in inventory: True")
else:
    print("Sample lookup = 'sword' in inventory: False")
