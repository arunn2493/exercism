import re


def score(word):
    scores = {
        1: re.sub(",", "", "A, E, I, O, U, L, N, R, S, T").split(),
        2: re.sub(",", "", "D, G").split(),
        3: re.sub(",", "", "B, C, M, P").split(),
        4: re.sub(",", "", "F, H, V, W, Y").split(),
        5: "K",
        8: re.sub(",", "", "J, X").split(),
        10: re.sub(",", "", "Q, Z").split()
    }

    word = word.upper().strip()
    start = 0
    keys = scores.keys()

    if word:
        for i in word:
            for j in keys:
                if i in scores[j]:
                    start = start + j
                    break

        return start
    else:
        return 0
