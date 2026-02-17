# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 11:11:53 by stmaire         #+#    #+#               #
#  Updated: 2026/02/17 14:41:08 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_achievement_tracker_system() -> None:
    """Analyze achievement collections across players"""

    players_data: list[tuple[str, set[str]]] = [
        ('alice', {'first_kill', 'level_10',
                   'treasure_hunter', 'speed_demon'}),
        ('bob', {'first_kill', 'level_10',
                 'boss_slayer', 'collector'}),
        ('charlie', {'level_10', 'treasure_hunter',
                     'boss_slayer', 'speed_demon', 'perfectionist'})
    ]

    print("===  Achievement Tracker System ===\n")

    for name, achievements in players_data:
        print(f"Player {name} achievements: {achievements}")

    print("\n=== Achievement Analytics ===")
    alice_set = players_data[0][1]
    bob_set = players_data[1][1]
    charlie_set = players_data[2][1]

    unique_achievements = alice_set.union(bob_set.union(charlie_set))
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}\n")

    common = alice_set.intersection(bob_set.intersection(charlie_set))
    print(f"Common to all players: {common}")

    alice_rare = alice_set.difference(bob_set.union(charlie_set))
    bob_rare = bob_set.difference(alice_set.union(charlie_set))
    charlie_rare = charlie_set.difference(alice_set.union(bob_set))
    rare_achievements = alice_rare.union(bob_rare.union(charlie_rare))
    print(f"Rare achievements (1 player): {rare_achievements}\n")

    print(f"Alice vs Bob common: {alice_set.intersection(bob_set)}")
    print(f"Alice unique: {alice_set.difference(bob_set)}")
    print(f"Bob unique: {bob_set.difference(alice_set)}")


if __name__ == "__main__":
    ft_achievement_tracker_system()
