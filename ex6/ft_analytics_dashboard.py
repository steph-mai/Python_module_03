# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 15:53:20 by stmaire         #+#    #+#               #
#  Updated: 2026/02/19 13:58:10 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import List, Dict, Any


def get_high_scores(players: List[Dict[str, Any]]) -> list[str]:
    high_scores: list[str] = [
        x["name"] for x in players if x["score"] > 2000
    ]
    return sorted(high_scores)


def get_scores_doubled(players: List[Dict[str, Any]]) -> list[int]:
    return [x["score"] * 2 for x in players]


def get_active_players(players: List[Dict[str, Any]]) -> list[str]:
    active_players: list[str] = [
        x["name"] for x in players if x["hours"] >= 40
    ]
    return sorted(active_players)


def get_active_players_scores(players: List[Dict[str, Any]]) -> dict[str, int]:
    return {x["name"]: x["score"] for x in players if x["hours"] >= 40}


def get_score_categories(players: List[Dict[str, Any]]) -> dict[str, int]:
    return {
        "high": sum(1 for x in players if x["score"] > 2000),
        "medium": sum(1 for x in players if 1500 <= x["score"] <= 2000),
        "low": sum(1 for x in players if x["score"] < 1500)
    }


def get_achievements_counts(players: List[Dict[str, Any]]) -> dict[str, int]:
    return {
        x["name"]: len(x["achievements"])
        for x in players if x["hours"] >= 40
    }


def get_unique_players(players: List[Dict[str, Any]]) -> set[str]:
    return {x["name"] for x in players}


def get_unique_achievements(players: List[Dict[str, Any]]) -> set[str]:
    all_achievements: list[str] = [
        ach for x in players for ach in x["achievements"]
    ]
    return {
        ach for ach in all_achievements
        if sum(1 for x in all_achievements if x == ach) == 1
    }


def get_active_regions(players: List[Dict[str, Any]]) -> set[str]:
    return {x["region"] for x in players if x["hours"] >= 40}


def run_combined_analysis(players: List[Dict[str, Any]]) -> None:
    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(players)}")

    unique_ach_all = {ach for x in players for ach in x["achievements"]}
    print(f"Total unique achievements: {len(unique_ach_all)}")

    count = len(players)
    average = sum(x['score'] for x in players) / count if count > 0 else 0.0
    print(f"Average score: {average:.1f}")

    ranked_players = sorted([
        (x["score"], x["name"], x["achievements"]) for x in players
    ])
    best_score, top_name, top_ach = ranked_players[-1]
    print(
        f"Top performer: {top_name} ({best_score} points, "
        f"{len(top_ach)} achievements)"
    )


if __name__ == "__main__":
    players: List[Dict[str, Any]] = [
        {
            "name": "alice", "score": 2300, "hours": 45, "region": "north",
            "achievements": ["first_kill", "level_10", "speedrunner"]
        },
        {
            "name": "bob", "score": 1800, "hours": 20, "region": "east",
            "achievements": ["first_kill", "world_traveler"]
        },
        {
            "name": "charlie", "score": 2150, "hours": 38, "region": "north",
            "achievements": ["boss_slayer", "level_10"]
        },
        {
            "name": "diana", "score": 2050, "hours": 50, "region": "central",
            "achievements": ["first_kill", "boss_slayer", "marathoner"]
        },
        {
            "name": "eve", "score": 900, "hours": 10, "region": "east",
            "achievements": ["first_kill", "speedrunner"]
        },
        {
            "name": "frank", "score": 2800, "hours": 60, "region": "north",
            "achievements": ["boss_slayer", "mvp"]
        }
    ]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {get_high_scores(players)}")
    print(f"Scores doubled: {get_scores_doubled(players)}")
    print(f"Active players: {get_active_players(players)}")

    print("\n=== Dict Comprehension Examples ===")
    print(f"Player scores: {get_active_players_scores(players)}")
    print(f"Score categories: {get_score_categories(players)}")
    print(f"Achievement counts: {get_achievements_counts(players)}")

    print("\n=== Set Comprehension Examples ===")
    print(f"Unique players: {get_unique_players(players)}")
    print(f"Unique achievements: {get_unique_achievements(players)}")
    print(f"Active regions: {get_active_regions(players)}")

    run_combined_analysis(players)
