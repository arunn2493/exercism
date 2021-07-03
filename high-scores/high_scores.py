def latest(scores):
    return scores.pop()


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    return(sorted(scores,reverse=True)[:3])
    

scores = [20, 10, 30]
print(personal_top_three(scores))