def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x.get("power"), reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x.get("power") >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x.get("power"))
    min_power = min(mages, key=lambda x: x.get("power"))
    avg_power = round(sum(map(lambda x: x.get("power"),
                              mages)) / len(mages), 2)
    return {
        'max_power': max_power['power'],
        'min_power': min_power['power'],
        'avg_power': avg_power
    }


def main() -> None:
    artifacts = [
        {'name': 'Earth Shield', 'power': 110, 'type': 'accessory'},
        {'name': 'Ice Wand', 'power': 101, 'type': 'accessory'},
        {'name': 'Lightning Rod', 'power': 81, 'type': 'relic'},
        {'name': 'Storm Crown', 'power': 65, 'type': 'relic'}]

    mages = [
        {'name': 'Morgan', 'power': 85, 'element': 'earth'},
        {'name': 'Ash', 'power': 92, 'element': 'light'},
        {'name': 'Kai', 'power': 58, 'element': 'fire'},
        {'name': 'Nova', 'power': 75, 'element': 'ice'},
        {'name': 'Storm', 'power': 98, 'element': 'fire'}]

    spells = ['earthquake', 'shield', 'heal', 'flash']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    if len(sorted_artifacts) >= 2:
        print(f"{sorted_artifacts[0]['name']}"
              f"({sorted_artifacts[0]['power']} power) "
              f"comes before {sorted_artifacts[1]['name']}"
              f"({sorted_artifacts[1]['power']} power)")

    print("\nTesting power filter...")
    min_p = 80
    filtered_mages = power_filter(mages, min_p)
    print(f"Mages with power >= {min_p}: {[m['name']
          for m in filtered_mages]}")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max Power: {stats['max_power']}")
    print(f"Min Power: {stats['min_power']}")
    print(f"Average Power: {stats['avg_power']}")


if __name__ == "__main__":
    main()
