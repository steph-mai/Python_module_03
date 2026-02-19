# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 10:54:39 by stmaire         #+#    #+#               #
#  Updated: 2026/02/19 13:57:23 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Generator
import time


def generate_events(n: int) -> Generator[dict[str, int | str], None, None]:
    """Generate event dictionaries"""

    players = [
        "alice",
        "bob",
        "charlie",
        "frank",
        "diana",
        "stephanie",
        "mike"]

    actions = [
        "killed monster",
        "found treasure",
        "leveled up", "death",
        "leveled up", "capture",
        "leveled up"
        ]

    for i in range(0, n):
        event: dict[str, int | str] = {
            "id": i + 1,
            "player": players[i % len(players)],
            "level": i * 7 % 17 + 1,
            "action": actions[i % len(actions)]
        }
        yield event


def ft_data_stream_processor() -> None:
    """Explore data from generator"""

    print("=== Game Data Stream Processor ===\n")
    total_events: int = 1000
    print(f"Processing {total_events} game events...\n")

    start_time = time.time()

    high_level_players = 0
    treasure_events = 0
    level_up_events = 0

    for event in generate_events(total_events):
        if int(event["id"]) <= 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")
        if int(event["level"]) >= 10:
            high_level_players += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        if event["action"] == "leveled up":
            level_up_events += 1
    print("...")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {elapsed_time:.3f} seconds\n")


def fibonacci() -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    while True:
        yield a
        a, b = b, a + b


def prime_numbers() -> Generator[int, None, None]:
    a = 2
    while True:
        i = 2
        while i < a:
            if (a % i) == 0:
                break
            i += 1
        else:
            yield a
        a += 1


def ft_generator_demo() -> None:
    """Displays two generator examples :

    Fibonacci sequence and prime numbers
    """
    print("=== Generator Demonstration ===")
    gen = fibonacci()
    print("Fibonacci sequence (first 10): ", end="")
    for _ in range(9):
        print(f"{next(gen)}, ", end="")
    print(next(gen))

    gen = prime_numbers()
    print("Prime numbers (first 5): ", end="")
    for _ in range(4):
        print(f"{next(gen)}, ", end="")
    print(next(gen))


if __name__ == "__main__":
    ft_data_stream_processor()
    ft_generator_demo()
