def latest(scores):
    score = scores[-1]
    return score


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    return sorted(scores, reverse=True)[:3]
