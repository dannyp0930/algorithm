def possible(ban, user, l):
    user_l = len(user)
    if user_l != l:
        return False
    for i in range(l):
        if ban[i] != '*' and ban[i] != user[i]:
            return False
    return True


def solution(user_id, banned_id):
    arr = []
    for ban in banned_id:
        l = len(ban)
        tmp = [ban, []]
        for user in user_id:
            if possible(ban, user, l):
                tmp[1].append(user)
        arr.append(tmp)
    stack = [[[user], 0] for user in arr[0][1]]
    res = []
    while stack:
        tmp = stack.pop()
        if tmp[1] == len(banned_id) - 1:
            tmp[0].sort()
            res.append(tuple(tmp[0]))
        else:
            for e in arr[tmp[1] + 1][1]:
                if e not in tmp[0]:
                    lst = tmp[0][:]
                    lst.append(e)
                    stack.append([lst, tmp[1] + 1])
    return len(set(res))
