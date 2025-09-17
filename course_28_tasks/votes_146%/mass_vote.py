def MassVote(N: int, Votes: list[int]) -> str:
    total_votes: int = sum(Votes)
    max_votes: int = max(Votes)
    max_index: int = Votes.index(max_votes) + 1
    percentage: float = (max_votes / total_votes) * 100

    if Votes.count(max_votes) > 1:
        return "no winner"
    elif percentage > 50:
        return f"majority winner {max_index}"
    elif percentage <= 50 and max_votes != 0:
        return f"minority winner {max_index}"
    else:
        return "no winner"
