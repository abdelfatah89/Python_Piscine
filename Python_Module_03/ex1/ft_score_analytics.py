import sys


def store_score() -> list:
    """Extracts valid integer scores from
    command-line arguments into a list."""
    scores_list = []
    i = 1
    if len(sys.argv) == 1:
        raise ValueError("Usage: python3 ft_score_analytics.py \
<score1> <score2> ...")
    while i < len(sys.argv):
        try:
            scores_list.append(int(sys.argv[i]))
        except ValueError:
            pass
        i += 1
    return scores_list


def ft_score_analytics() -> None:
    """Calculates and displays comprehensive statistical insights
    from the collected scores."""
    print("=== Player Score Analytics ===")
    try:
        scores_list = store_score()
        if not scores_list:
            print("No scores provided.")
            return

        print(f"Scores processed: {scores_list}")
        print(f"Total players: {len(scores_list)}")
        print(f"Total score: {sum(scores_list)}")
        if len(scores_list) > 0:
            avg = sum(scores_list) / len(scores_list)
        else:
            avg = 0
        print(f"Average score: {avg:.1f}")
        print(f"High score: {max(scores_list)}")
        print(f"Low score: {min(scores_list)}")
        print(f"Score range: {max(scores_list) - min(scores_list)}")
    except ValueError as e:
        print(f"No scores provided. {e}")


if __name__ == "__main__":
    ft_score_analytics()
