from typing import List, Dict


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    """Sorts artifacts by 'power' level in descending order"""
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    """Filters mages that have power >= min_power"""
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    """Adds '*' prefix and '*' suffix to spell names"""
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: List[Dict]) -> Dict:
    """Calculates max, min, and average power levels"""
    powers = list(map(lambda x: x['power'], mages))

    return {
        'max_power': max(powers, key=lambda x: x) if powers else 0,
        'min_power': min(powers, key=lambda x: x) if powers else 0,
        'avg_power': round(sum(powers) / len(powers), 2) if powers else 0.0
    }


def main() -> None:
    print("\nTesting artifact sorter...")
    artifacts = [
        {"name": "Fire Staff",
         "power": 92,
         "type": "legendary"},
        {"name": "Crystal Orb",
         "power": 85,
         "type": "legendary"}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} "
          f"power) comes before {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)\n")

    print("Testing spell transformer...")
    spells = ["fireball", "heal", "shield"]
    new_spells = spell_transformer(spells)
    for spell in new_spells:
        print(f"{spell} ", end="")


if __name__ == "__main__":
    main()
