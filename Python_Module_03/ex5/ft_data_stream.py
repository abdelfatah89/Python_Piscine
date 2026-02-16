def get_events(game_data):
    """Yields the event type for
    each game data entry sequentially."""
    for id in range(len(game_data)):
        yield game_data[id].get("event_type")


def get_players(game_data):
    """Yields the player name
    for each game data entry sequentially."""
    for id in range(len(game_data)):
        yield game_data[id].get("player")


def get_data_level(game_data):
    """Yields the player level from
    the nested data structure."""
    for id in range(len(game_data)):
        yield game_data[id].get("data").get("level")


def gen_fibonacci(limit):
    """Generates a sequence of Fibonacci
    numbers up to the specified limit."""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


def is_prime(number) -> bool:
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def gen_primes(number):
    """Generates prime numbers sequentially up
    to a given maximum."""
    for num in range(2, number):
        if is_prime(num):
            yield num


def stream_data_game(game_data) -> None:
    """Processes and prints game events in
    real-time using generator streams."""
    print("=== Game Data Stream Processor ===\n")
    events = get_events(game_data)
    players = get_players(game_data)
    level_data = get_data_level(game_data)

    print(f"Processing {len(game_data)} game events...\n")
    for id in range(1, len(game_data) + 1):
        print("Event {}: Player {} (level {}) {}".format(
            id, next(players), next(level_data), next(events)))


def stream_analyse(game_data) -> None:
    """Analyzes the data stream to count
    specific events and high-level players."""
    print("\n=== Stream Analytics ===")
    events_iter = iter(get_events(game_data))
    level_iter = iter(get_data_level(game_data))
    total_level_up = 0
    total_treasure = 0
    High_players = 0

    for id in range(len(game_data)):
        current_event = next(events_iter)
        current_level = next(level_iter)

        if current_event == "treasure":
            total_treasure += 1
        if current_event == "level_up":
            total_level_up += 1
        if current_level > 10:
            High_players += 1

    print(f"Total events processed: {len(game_data)}")
    print(f"High-level players (10+): {High_players}")
    print(f"Treasure events: {total_treasure}")
    print(f"Level-up events: {total_level_up}")


def generator_demo() -> None:
    """Demonstrates generator usage with
    Fibonacci and prime number sequences."""
    print("\n=== Generator Demonstration ===")

    fibonacci = gen_fibonacci(10)
    primes = gen_primes(100)
    fibonacci_string = "Fibonacci sequence (first 10): "
    prime_string = "Prime numbers (first 5): "
    is_first = True
    for i in range(10):
        if is_first is False:
            fibonacci_string += ", "
        fibonacci_string += f"{next(fibonacci)}"
        is_first = False
    print(fibonacci_string)

    is_first = True
    for i in range(5):
        if is_first is False:
            prime_string += ", "
        prime_string += f"{next(primes)}"
        is_first = False
    print(prime_string)


def ft_data_stream(game_data) -> None:
    stream_data_game(game_data)
    stream_analyse(game_data)
    generator_demo()


if __name__ == "__main__":
    sample_data = [
        {"event_type": "killed monster",
         "player": "alice", "data": {"level": 5}},
        {"event_type": "treasure", "player": "bob", "data": {"level": 12}},
        {"event_type": "level_up", "player": "charlie", "data": {"level": 8}}
    ]
    ft_data_stream(sample_data)
