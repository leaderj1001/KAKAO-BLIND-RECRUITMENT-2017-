def solution(cacheSize, cities):
    answer = 0

    cache = []
    location = 0
    for i in range(0, len(cities)):
        if cacheSize == 0:
            answer += 5
        else:
            if cities[i].lower() in cache:
                cache.remove(cities[i].lower())
                cache.append(cities[i].lower())
                answer += 1
            else:
                if len(cache) == cacheSize:
                    cache.pop(0)
                    cache.append(cities[i].lower())
                else:
                    cache.append(cities[i].lower())
                answer += 5

    # print(answer)
    return answer