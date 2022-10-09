def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    cam_pos = -30000
    for r_s, r_e in routes:
        if cam_pos < r_s:
            cam_pos = r_e
            answer += 1
    return answer
