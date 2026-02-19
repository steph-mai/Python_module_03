# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 15:53:20 by stmaire         #+#    #+#               #
#  Updated: 2026/02/18 17:57:06 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# if __name__ == "__main__":
#     data_players: list[dict[str, str | list[str] | int]] = [
#     {"name": "alice", "score": 2300, "hours": 45, "region": "north", "achievements": ["first_kill", "level_10"]},
#     {"name": "bob", "score": 1800, "hours": 20, "region": "east", "achievements": ["first_kill", "pacifist"]},
#     {"name": "charlie", "score": 2150, "hours": 38, "region": "north", "achievements": ["boss_slayer", "level_10"]},
#     {"name": "diana", "score": 2050, "hours": 50, "region": "central", "achievements": ["first_kill", "boss_slayer", "marathoner"]},
#     {"name": "eve", "score": 900, "hours": 10, "region": "east", "achievements": ["first_kill", "pacifist", "world_traveler"]},
#     {"name": "frank", "score": 2800, "hours": 60, "region": "north", "achievements": ["boss_slayer", "mvp"]}
# ]

# print("=== Game Analytics Dashboard ===")

# print("\n=== List Comprehension Examples ===")

# high_scores: list[str] = [x["name"] for x in data_players if x["score"] > 2000]
# print (f"High scorers (>2000): {sorted(high_scores)}")
# scores_doubled: list[int] = [x["score"] * 2 for x in data_players]
# print (f"Scores doubled: {scores_doubled}")
# active_players: list[str]= [x["name"] for x in data_players if x["hours"] >= 40]
# print (f"Active players: {sorted(active_players)}")

# print("\n=== Dict Comprehension Examples ===")

# active_players_scores: dict[str, int] = {x["name"]: x["score"] for x in data_players if x["hours"] >= 40}
# print (f"Player scores: {active_players_scores}")
# score_categories: dict[str, int] = {
#     "high": sum(1 for x in data_players if x["score"] > 2000),
#     "medium": sum(1 for x in data_players if 1500 <= x["score"] <= 2000),
#     "low": sum(1 for x in data_players if x["score"] < 1500)
# }
# print (f"Score categories: {score_categories}")
# achievements_counts: dict[str, int] = {x["name"]: len(x["achievements"]) for x in data_players if x["hours"] >= 40}
# print (f"Achievement counts: {achievements_counts}")

# print("\n=== Set Comprehension Examples ===")

# unique_players: set[str] = {x["name"] for x in data_players}
# print (f"Unique players: {(unique_players)}")
# all_achievements: list[str] = [ach for x in data_players for ach in x["achievements"]]
# unique_achievements: set[str] = {
#     ach for ach in all_achievements
#     if sum(1 for x in all_achievements if x == ach) == 1
#     }
# print (f"Unique achievements: {unique_achievements}")
# active_regions: set[str] = {x["region"] for x in data_players if x["hours"] >= 40}
# print (f"Active regions: {active_regions}")

# print("\n=== Combined Analysis ===")

# print (f"Total players: {len(data_players)}")
# print (f"Total unique achievements: {len({ach for x in data_players for ach in x['achievements']})}")
# total_score = sum(x['score'] for x in data_players)
# count = len(data_players)
# average = sum(x['score'] for x in data_players) / len(data_players) if data_players else 0.0
# print(f"Average score: {average:.1f}")
# ranked_players = sorted([(x["score"], x["name"], x["achievements"]) for x in data_players])
# # les tuples contiennent le score en premier car la fonction sorted compare les 1ers elements s il s agit d'un tuple
# # puis le nom, puis l'ensemble des donnees relatives au joueur
# best_score, top_name, top_ach = ranked_players[-1] #unpacking : on deballe les donnees du dernier joueur [-1]
# print(f"Top performer: {top_name} ({best_score} points, {len(top_ach)} achievements)")


def get_high_scores(players: list[dict]) -> list[str]:
    high_scores: list[str] = [
        x["name"] for x in players if x["score"] > 2000
    ]
    return sorted(high_scores)


def get_scores_doubled(players: list[dict]) -> list[int]:
    return [x["score"] * 2 for x in players]


def get_active_players(players: list[dict]) -> list[str]:
    active_players: list[str] = [
        x["name"] for x in players if x["hours"] >= 40
    ]
    return sorted(active_players)


def get_active_players_scores(players: list[dict]) -> dict:
    return {x["name"]: x["score"] for x in players if x["hours"] >= 40}


def get_score_categories(players: list[dict]) -> dict:
    return {
        "high": sum(1 for x in players if x["score"] > 2000),
        "medium": sum(1 for x in players if 1500 <= x["score"] <= 2000),
        "low": sum(1 for x in players if x["score"] < 1500)
    }


def get_achievements_counts(players: list[dict]) -> dict:
    return {
        x["name"]: len(x["achievements"])
        for x in players if x["hours"] >= 40
    }


def get_unique_players(players: list[dict]) -> set:
    return {x["name"] for x in players}


def get_unique_achievements(players: list[dict]) -> set:
    all_achievements: list = [
        ach for x in players for ach in x["achievements"]
    ]
    return {
        ach for ach in all_achievements
        if sum(1 for x in all_achievements if x == ach) == 1
    }


def get_active_regions(players: list[dict]) -> set:
    return {x["region"] for x in players if x["hours"] >= 40}


def run_combined_analysis(players: list[dict]) -> None:
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
    data_players: list[dict] = [
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
    print(f"High scorers (>2000): {get_high_scores(data_players)}")
    print(f"Scores doubled: {get_scores_doubled(data_players)}")
    print(f"Active players: {get_active_players(data_players)}")

    print("\n=== Dict Comprehension Examples ===")
    print(f"Player scores: {get_active_players_scores(data_players)}")
    print(f"Score categories: {get_score_categories(data_players)}")
    print(f"Achievement counts: {get_achievements_counts(data_players)}")

    print("\n=== Set Comprehension Examples ===")
    print(f"Unique players: {get_unique_players(data_players)}")
    print(f"Unique achievements: {get_unique_achievements(data_players)}")
    print(f"Active regions: {get_active_regions(data_players)}")

    run_combined_analysis(data_players)
