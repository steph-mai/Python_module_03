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

if __name__ == "__main__":
    data_players = [
    {"name": "alice", "score": 2300, "hours": 45, "region": "north", "achievements": ["first_kill", "level_10"]},
    {"name": "bob", "score": 1800, "hours": 20, "region": "east", "achievements": ["first_kill"]},
    {"name": "charlie", "score": 2150, "hours": 38, "region": "north", "achievements": ["boss_slayer", "level_10"]},
    {"name": "diana", "score": 2050, "hours": 50, "region": "central", "achievements": ["first_kill", "boss_slayer", "marathoner"]},
    {"name": "eve", "score": 900, "hours": 10, "region": "east", "achievements": []},
    {"name": "frank", "score": 2800, "hours": 60, "region": "north", "achievements": ["boss_slayer", "mvp"]}
]

print("=== Game Analytics Dashboard ===")

print("\n=== List Comprehension Examples ===")
high_scores: list = [x["name"] for x in data_players if x["score"] > 2000]
print (f"High scorers (>2000): {high_scores}")
scores_doubled: list = [x["score"] * 2 for x in data_players]
print (f"Scores doubled: {scores_doubled}")
active_players: list = [x["name"] for x in data_players if x["hours"] >= 40]
print (f"Active players: {active_players}")

print("\n=== Dict Comprehension Examples ===")
active_players_scores: dict = {x["name"]: x["score"] for x in data_players if x["hours"] >= 40}
print (f"Player scores: {active_players_scores}")
# TODO Score categories
achievements_counts: dict = {x["name"]: len(x["achievements"]) for x in data_players if x["hours"] >= 40}
print (f"Achievement counts: {achievements_counts}")