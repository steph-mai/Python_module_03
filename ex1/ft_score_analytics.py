# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 09:44:48 by stmaire         #+#    #+#               #
#  Updated: 2026/02/17 08:49:23 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def ft_score_analytics() -> None:
    """Display analytics"""

    print("=== Player Score Analytics ===")

    if len(sys.argv) < 2:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores = []
    try:
        for i in range(1, (len(sys.argv))):
            score = int(sys.argv[i])
            scores += [score]
    except ValueError:
        print(f"Error: '{sys.argv[i]}' is not a valid number")
        return
    print("Scores processed: [", end="")
    for i in range(0, (len(scores))):
        print(f"{scores[i]}", end="")
        if i < len(scores) - 1:
            print(", ", end="")
    print("]")

    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / (len(scores))}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    ft_score_analytics()
