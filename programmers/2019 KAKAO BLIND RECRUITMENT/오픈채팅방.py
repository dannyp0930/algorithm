def solution(record):
    answer = []
    id_nickname = dict()
    for command in record:
        command = command.split(' ')
        if command[0] == 'Enter' or command[0] == 'Change':
            id_nickname[command[1]] = command[2]
    for command in record:
        command = command.split(' ')
        if command[0] == 'Enter':
            answer.append(f'{id_nickname[command[1]]}님이 들어왔습니다.')
        elif command[0] == 'Leave':
            answer.append(f'{id_nickname[command[1]]}님이 나갔습니다.')
    return answer
