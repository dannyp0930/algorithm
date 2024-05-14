from heapq import heappush, heappop

def solution(book_time):
    times = []
    for time in book_time:
        start = list(map(int, time[0].split(":")))
        end = list(map(int, time[1].split(":")))
        start_time = start[0] * 60 + start[1]
        end_time = end[0] * 60 + end[1] + 10
        heappush(times, [start_time, end_time])
    rooms = []
    while times:
        s, e = heappop(times)
        if not len(rooms):
            rooms.append([e, s])
        else:
            room = heappop(rooms)
            if room[0] > s:
                heappush(rooms, room)
            heappush(rooms, [e, s])
    return len(rooms)