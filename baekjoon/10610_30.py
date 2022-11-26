N = input()
res = []
cnt_zero = 0
digit_sum = 0
for i in range(len(N)):
    if int(N[i]) == 0:
        cnt_zero += 1
    else:
        res.append(N[i])
    digit_sum += int(N[i])
if cnt_zero == 0 or digit_sum % 3:
    print(-1)
else:
    res.sort(reverse=True)
    print(''.join(res) + '0' * cnt_zero)
