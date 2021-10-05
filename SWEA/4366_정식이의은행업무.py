import sys
sys.stdin = open('4366.txt', 'r')


for T in range(1, int(input()) + 1):
    binary = input()
    ternary = input()
    binary_list = []
    ternary_list = []
    for i in range(len(binary)):
        tmp = list(binary)
        if tmp[i] == '1':
            tmp[i] = '0'
        else:
            tmp[i] = '1'
        binary_list.append(int(''.join(tmp), 2))
    for j in range(len(ternary)):
        tmp = list(ternary)
        if tmp[j] == '0':
            tmp[j] = '1'
            ternary_list.append(int(''.join(tmp), 3))
            tmp[j] = '2'
            ternary_list.append(int(''.join(tmp), 3))
        elif tmp[j] == '1':
            tmp[j] = '0'
            ternary_list.append(int(''.join(tmp), 3))
            tmp[j] = '2'
            ternary_list.append(int(''.join(tmp), 3))
        else:
            tmp[j] = '0'
            ternary_list.append(int(''.join(tmp), 3))
            tmp[j] = '1'
            ternary_list.append(int(''.join(tmp), 3))
    for bin_num in binary_list:
        for ter_num in ternary_list:
            if bin_num == ter_num:
                print('#{} {}'.format(T, bin_num))
                break
