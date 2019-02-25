def time_calculate(time1, time2, mark):
    timeToMinute1 = 0
    timeToMinute2 = 0

    timeToMinute1 += (int(time1[:2]) * 60 + int(time1[3:5]))
    timeToMinute2 += (int(time2[:2]) * 60 + int(time2[3:5]))

    total_time = 0
    if mark == '+':
        total_time = timeToMinute1 + timeToMinute2
    elif mark == '-':
        total_time = timeToMinute1 - timeToMinute2

    # zfill 함수,
    # string에 0을 채우는 함수

    return '%02d:%02d' % (total_time // 60, total_time % 60)


def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()

    t = '%02d:%02d' % (t // 60, t % 60)

    start_time = '09:00'
    current_location = 0
    for i in range(1, n + 1):
        m_count = 0
        if i == n:
            for j in range(current_location, len(timetable)):
                if start_time >= timetable[j]:
                    if m_count == m - 1:
                        answer = time_calculate(timetable[j], "00:01", '-')
                        break
                    m_count += 1
                answer = start_time
        else:
            for j in range(current_location, len(timetable)):
                if start_time >= timetable[j]:
                    if m_count < m:
                        m_count += 1
            start_time = time_calculate(start_time, str(t), '+')
        current_location += m_count
    return answer