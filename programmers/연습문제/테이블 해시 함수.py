from functools import reduce


def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    arr = [reduce(lambda acc, cur: acc + cur % (i + 1), data[i], 0)
           for i in range(row_begin - 1, row_end)]
    return reduce(lambda acc, cur: acc ^ cur, arr)
