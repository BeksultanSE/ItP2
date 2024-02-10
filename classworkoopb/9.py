def ones_threes_nines(n):
    nines = n // 9
    n %= 9
    threes = n // 3
    n %= 3
    ones = n
    return f"nines:{nines}, threes:{threes}, ones:{ones}"

test_cases = [10, 15, 22]
results = [ones_threes_nines(tc) for tc in test_cases]
results
