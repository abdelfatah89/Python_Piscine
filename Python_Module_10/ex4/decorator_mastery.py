from time import time
from functools import wraps
from typing import Any


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def timer(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Spell completed in  {end_time - start_time} seconds")
        return result
    return timer


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(self, spell_name: str, power: int,
                    *args, **kwargs) -> Any:
            if power < min_power:
                return "Insufficient power for this spell"
            return func(self, spell_name, power, *args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for n in range(1, max_attempts + 1):
                try:
                    func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying..."
                          f"(attempt {n}/{max_attempts})")

                    if n == max_attempts:
                        return "Spell casting failed after"
                    f"{max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        v = len(name) > 3 and (all(c.isalpha() or c.isspace() for c in name))
        return v

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


def main():
    print("Testing spell_timer...")

    @spell_timer
    def slow_fireball():
        import time
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {slow_fireball()}")
    print("\n")

    print("Testing retry_spell...")
    attempts = 0

    @retry_spell(max_attempts=2)
    def fail_spell():
        nonlocal attempts
        attempts += 1
        raise Exception("Failure")
    print(f"Result: {fail_spell()}\n")

    print("Testing MageGuild...")
    name1 = "Alex"
    name2 = "A1"
    print(f"{MageGuild.validate_mage_name(name1)}")
    print(f"{MageGuild.validate_mage_name(name2)}")

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))


if __name__ == "__main__":
    main()
