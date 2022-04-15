def solution(n, arr1, arr2):
    answer = []
    lst1 = []
    lst2 = []
    for i in range(n):
        bin_tmp1 = bin(arr1[i])[2:]
        bin_tmp2 = bin(arr2[i])[2:]
        while len(bin_tmp1) < n:
            bin_tmp1 = '0' + bin_tmp1
        while len(bin_tmp2) < n:
            bin_tmp2 = '0' + bin_tmp2
        lst1.append(bin_tmp1)
        lst2.append(bin_tmp2)
    for r in range(n):
        tmp = ''
        for c in range(n):
            if lst1[r][c] == '0' and lst2[r][c] == '0':
                tmp += ' '
            else:
                tmp += '#'
        answer.append(tmp)
    return answer
