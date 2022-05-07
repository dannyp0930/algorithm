def solution(m, musicinfos):
    answer = '(None)'
    playtime = 0
    # 메이저 코드를 소문자로
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    for music in musicinfos:
        start, end, title, code = music.split(',')
        code = code.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

        # 시간 계산
        startH, startM = map(int, start.split(':'))
        endH, endM = map(int, end.split(':'))
        startTime, endTime = startH * 60 + startM, endH * 60 + endM
        time = endTime - startTime

        # 재생 길이에 따른 음악 코드
        if time < len(code):
            code = code[:time]
        else:
            q, r = divmod(time, len(code))
            code = code * q + code[:r]

        # 코드가 발견되면
        if m in code:
            if playtime < time:
                answer = title
                playtime = time
    return answer
