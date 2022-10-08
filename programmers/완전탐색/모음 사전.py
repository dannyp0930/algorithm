def solution(word):
    dic = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    num = [781, 156, 31, 6, 1]
    ans = 0
    for i, ch in enumerate(word):
        ans += dic[ch] * num[i] + 1
    return ans
