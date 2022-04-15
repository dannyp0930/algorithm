def solution(cacheSize, cities):
    cities = [city.upper() for city in cities]
    answer = 0
    cache = []

    # 캐시 사이즈가 0인경우 cache miss 발생
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        # 도시가 없는경우 cache miss
        if not city in cache:
            # 현재 캐시 크기가 작을경우 바로 삽입
            if len(cache) < cacheSize:
                cache.append(city)
            # 현재 캐시 크기가 클 경우 선입 선출
            else:
                cache.pop(0)
                cache.append(city)
            answer += 5
        # 도시가 있는경우 cache hit
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1
    return answer
