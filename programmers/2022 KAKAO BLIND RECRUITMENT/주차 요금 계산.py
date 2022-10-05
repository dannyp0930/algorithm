import math


def time_to_minute(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m
    

def solution(fees, records):
    ans = []
    cars = dict()
    for record in records:
        time, car, in_out = record.split()
        if car in cars:
            cars[car].append([time_to_minute(time), in_out])
        else:
            cars[car] = [[time_to_minute(time), in_out]]
    cars = sorted(cars.items())
    for car in cars:
        t = 0
        for r in car[1]:
            if r[1] == 'IN':
                t -= r[0]
            else:
                t += r[0]
        if car[1][-1][1] == 'IN':
            t += time_to_minute('23:59')
        fee = fees[1]
        if t > fees[0]:
            fee += math.ceil((t - fees[0]) / fees[2]) * fees[3]
        ans.append(fee)
    return ans