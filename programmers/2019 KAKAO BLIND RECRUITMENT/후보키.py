from itertools import combinations


def solution(relation):
    # key의 개수
    N = len(relation[0])
    # 후보키
    candidate_keys = []
    for i in range(1, N + 1):
        for keys in combinations(range(N), i):
            tuples = []
            for rel in relation:
                t = [rel[k] for k in keys]
                # 유일성 판별
                if t in tuples:
                    break
                else:
                    tuples.append(t)
            else:
                # 최소성 판별
                for ck in candidate_keys:
                    if set(ck).issubset(keys):
                        break
                else:
                     candidate_keys.append(keys)
    return len(candidate_keys)
