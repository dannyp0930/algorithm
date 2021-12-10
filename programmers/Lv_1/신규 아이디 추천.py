def solution(new_id):
    # 1단계
    first = []
    for ch in new_id:
        if 65 <= ord(ch) <= 90:
            ascii_num = ord(ch) + 32
            first.append(chr(ascii_num))
        else:
            first.append(ch)

    # 2단계
    second = []
    for ch in first:
        if 97 <= ord(ch) <= 122 or 48 <= ord(ch) <= 57 or ord(ch) == 45 or ord(ch) == 46 or ord(ch) == 95:
            second.append(ch)

    # 3단계
    third = []
    for ch in second:
        if third and third[-1] == '.' and ch == '.':
            continue
        third.append(ch)

    # 4단계
    fourth = []
    for ch in third:
        if not fourth and ch == '.':
            continue
        fourth.append(ch)
    while 1:
        if not fourth or fourth[-1] != '.':
            break
        fourth.pop()

    # 5단계
    fifth = fourth[:]
    if not fifth:
        fifth = ['a']

    # 6단계
    sixth = fifth[:]
    while len(sixth) > 15:
        sixth.pop()
    if sixth[-1] == '.':
        sixth.pop()

    # 7단계
    seventh = sixth[:]
    while len(seventh) < 3:
        seventh.append(seventh[-1])

    answer = ''.join(seventh)
    return answer
