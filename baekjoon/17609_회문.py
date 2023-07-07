def check(string, s, e):
    while s < e:
        if string[s] == string[e]:
            s += 1
            e -= 1
        else:
            if remove(string, s + 1, e) or remove(string, s, e - 1):
                return 1
            return 2
    return 0


def remove(string, s, e):
    while s < e:
        if string[s] == string[e]:
            s += 1
            e -= 1
        else:
            return False
    return True


for _ in range(t := int(input())):
    print(check(string := input(), 0, len(string) - 1))
