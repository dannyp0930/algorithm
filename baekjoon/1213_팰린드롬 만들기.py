def solution(name):
    dic = [0] * 26
    for ch in name:
        dic[ord(ch) - 65] += 1
    odd = 0
    odd_ch = ''
    ans = ''
    for i in range(26):
        if not dic[i]:
            continue
        if dic[i] % 2:
            if odd:
                return "I'm Sorry Hansoo"
            odd += 1
            dic[i] -= 1
            odd_ch = chr(i + 65)
        ans += chr(i + 65) * (dic[i] // 2)
    return ans + odd_ch + ans[::-1]


name = input()
print(solution(name))
