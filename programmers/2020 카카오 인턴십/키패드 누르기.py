def solution(numbers, hand):
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    answer = ''
    left_loc, right_loc = keypad['*'], keypad['#']
    for num in numbers:
        num_loc = keypad[num]
        if num in [1, 4, 7]:
            answer += 'L'
            left_loc = num_loc
        elif num in [3, 6, 9]:
            answer += 'R'
            right_loc = num_loc
        else:
            l_distance = 0
            r_distance = 0
            for l, r, n in zip(left_loc, right_loc, num_loc):
                l_distance += abs(l - n)
                r_distance += abs(r - n)
            if l_distance < r_distance:
                answer += 'L'
                left_loc = num_loc
            elif l_distance > r_distance:
                answer += 'R'
                right_loc = num_loc
            else:
                if hand == 'left':
                    answer += 'L'
                    left_loc = num_loc
                else:
                    answer += 'R'
                    right_loc = num_loc
    return answer
