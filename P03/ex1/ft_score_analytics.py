#!/usr/bin/env python3

import sys


def parse_scores(args: list[str]) -> list[str]:
    """Parse command line arguments to extract scores."""
    scores: list = []
    for arg in args:
        try:
            score: int = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Warning: '{arg}' is not a valid score"
                  " and will be ignored.")
    return scores


def compute_stats(scores: list[str]) -> dict[str]:
    total_player: int = len(scores)
    total_score: int = sum(scores)
    average: float = total_score / total_player
    high_score: int = max(scores)
    low_score: int = min(scores)
    score_range: int = high_score - low_score

    stats: dict[str] = {
        "Total players:": total_player,
        "Total score:": total_score,
        "Average score:": average,
        "High score:": high_score,
        "Low score:": low_score,
        "Score range:": score_range
    }

    return stats


def print_results(scores: list[str], stats: dict[str]) -> None:
    print(f"Scores processed: {scores}")
    for key, value in stats.items():
        print(key, value)


if __name__ == "__main__":
    args: list[str] = sys.argv[1:]
    scores: list[str] = parse_scores(args)
    if not scores:
        print("No scores provided. Usage:"
              " python3 ft_score_analytics.py <score1> <score2> ...")
        sys.exit(0)
    stats: dict[str] = compute_stats(scores)
    print("=== Player Score Analytics ===")
    print_results(scores, stats)
