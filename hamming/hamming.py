def distance(strand_a, strand_b):
    length_a = len(strand_a)
    length_b = len(strand_b)

    if length_a == length_b:
        hamming_distance = 0
        for i in range(length_a):
            if strand_a[i] != strand_b[i]:
                hamming_distance = hamming_distance+1
            else:
                continue
    else:
        raise ValueError("DNA strand must be of the same length")

    return hamming_distance
