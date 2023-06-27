def MassVote(N, Votes):
    total_votes = sum(Votes)
    max_votes = max(Votes)
    max_index = Votes.index(max_votes) + 1
    percentage = (max_votes / total_votes) * 100

    if Votes.count(max_votes) > 1:
        return "no winner"
    elif percentage > 50:
        return f"majority winner {max_index}"
    elif percentage <= 50 and max_votes != 0:
        return f"minority winner {max_index}"
    else:
        return "no winner"
