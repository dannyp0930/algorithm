# 백트래킹


def select(k):
    for i in range(k):
        min_index = i
        for j in range(i + 1, C):
            if ord(chars[min_index]) > ord(chars[j]):
                min_index = j
        chars[i], chars[min_index] = chars[min_index], chars[i]
    return


def comb(k, idx):
    if k == L:
        cnt_vowel = 0
        cnt_consonants = 0
        for ch in lst:
            if ch in vowel:
                cnt_vowel += 1
            else:
                cnt_consonants += 1
        if cnt_vowel < 1 or cnt_consonants < 2:
            return
        print(''.join(lst))
        return
    for i in range(idx, C):
        lst.append(chars[i])
        comb(k + 1, i + 1)
        lst.pop()


vowel = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, input().split())
chars = list(map(str, input().split()))
select(C)
lst = []
comb(0, 0)
