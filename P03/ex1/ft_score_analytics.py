#!/usr/bin/env python3

import sys


def parse_scores(args):
    """Parse command line arguments to extract scores."""
    scores = []
    for arg in args:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Warning: '{arg}' is not a valid score"
                  " and will be ignored.")
    return scores


def compute_stats(scores):
    total_player = len(scores)
    total_score = sum(scores)
    average = total_score / total_player
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    stats = {
        "Total player:": total_player,
        "Total score:": total_score,
        "Average:": average,
        "High score:": high_score,
        "Low score:": low_score,
        "Score range:": score_range
    }

    return stats


def print_results(scores, stats):
    print(f"Scores processed: [{scores}]")
    for key, value in stats.items():
        print(key, value)


if __name__ == "__main__":
    args = sys.argv[1:]
    scores = parse_scores(args)
    if not scores:
        print("No scores provided. Usage:"
              " python3 ft_score_analytics.py <score1> <score2> ...")
        sys.exit(0)
    stats = compute_stats(scores)
    print("=== Player Score Analytics ===")
    print_results(scores, stats)
