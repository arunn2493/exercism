def is_isogram(string):
    alpha = [i for i in string.lower() if i.isalpha()]
    print(alpha)
    return len(alpha) == len(set(alpha))
