def solution(phone_number):
    num = len(phone_number)
    lst_phone = list(phone_number)
    for i in range(num - 4):
        lst_phone[i] = '*'
    return ''.join(lst_phone)
