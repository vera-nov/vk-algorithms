def isSubsequence(a: str, b: str) -> bool:
    pa, pb = 0, 0
    while pa < len(a) and pb < len(b):
        if a[pa] == b[pb]:
            pa += 1
        pb += 1
    return pa == len(a)