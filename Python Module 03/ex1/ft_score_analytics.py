#!/usr/bin/env python3

import sys


def score_analytics() -> None:
    print("=== Player Score Analytics ===")
    ac = len(sys.argv)
    if ac == 1:
        print("No scores provided. Usage: python3"
              " ft_score_analytics.py <score1> <score2> ...")
        return
    score_list = []
    for i in range(1, ac):
        try:
            score_list.append(int(sys.argv[i]))
        except ValueError:
            print(f"{sys.argv[i]} is not a valid score")
    if len(score_list) == 0:
        print("No valid score was given!")
        return
    print(f"Scores processed: {score_list}")
    print(f"Total players: {len(score_list)}")
    print(f"Total score: {sum(score_list)}")
    print(f"Average score: {sum(score_list)/len(score_list):.1f}")
    print(f"High score: {max(score_list)}")
    print(f"Low score: {min(score_list)}")
    print(f"Score Range: {max(score_list) - min(score_list)}")
    print()


score_analytics()
