
def count_words(s):
    import re

    s = s.lower()
    words = re.findall(r"((?<!')[a-z0-9]+'[a-z0-9]+(?!')|[a-z0-9]+)", s)
    outd = {}
    for word in words:
        outd[word] = words.count(word)
    return outd
