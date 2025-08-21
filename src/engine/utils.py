def match_score(a: str, b: str) -> int:
    ta = set(a.lower().split())
    tb = set(b.lower().split())
    return len(ta.intersection(tb))

def pick(seq, i):
    return seq[i % len(seq)]
