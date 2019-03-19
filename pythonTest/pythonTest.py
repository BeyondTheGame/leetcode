def suffix(pattern: str, pattern_len: int):
    shift = [0] * (pattern_len + 1)
    bPos = [None] * (pattern_len + 1)
    i, j = pattern_len, pattern_len + 1
    bPos[i] = j
    while i > 0:
        while j <= pattern_len and pattern[i - 1] != pattern[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            j = bPos[j]
        i -= 1
        j -= 1
        """
        if border[i-1] = j-1 then border[i] = j
        """
        bPos[i] = j  # bPos[pattern_len-1] =  pattern_len

    j = bPos[0]
    for i in range(pattern_len + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = bPos[j]
    return bPos, shift
P = "ABBABAB"
bPos, shift = suffix(P, len(P))
print(bPos, shift)