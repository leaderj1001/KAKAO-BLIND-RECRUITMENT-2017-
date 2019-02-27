def timeToMinute(time1, time2):
    minute_time1 = int(time1[:2]) * 60 + int(time1[3:5])
    minute_time2 = int(time2[:2]) * 60 + int(time2[3:5])

    return abs(minute_time1 - minute_time2)


def solution(m, musicinfos):
    answer = ''

    # C#과 같이 #이 포함된 음에 대해서 소문자로 처리해줌. C# -> c
    word = ''
    for i in range(0, len(m)):
        if m[i] == '#':
            word = word[:-1]
            word += m[i - 1].lower()
        else:
            word += m[i]
    m = word

    # 위에서 C# -> c 처리와 split을 통해서 input 자르기
    split_infos = []
    for info in musicinfos:
        temp = info.split(',')
        word = ''
        for i in range(0, len(temp[3])):
            if temp[3][i] == '#':
                word = word[:-1]
                word += temp[3][i - 1].lower()
            else:
                word += temp[3][i]
        temp.pop()
        temp.append(word)
        split_infos.append(temp)

    # 1분에 1개의 음이라고 했으므로 음악이 지속된 시간을 계산하고,
    # 그 시간에 맞게 음을 이어붙여주는 과정
    handling_strs = []
    for split_info in split_infos:
        # 시간 계산
        interval = timeToMinute(split_info[0], split_info[1])

        # 음 이어 붙이기
        word = ''
        for i in range(0, interval):
            if i >= len(split_info[3]):
                word += split_info[3][i % len(split_info[3])]
            else:
                word += split_info[3][i]
        handling_strs.append([word, split_info[2]])

    # 음 길이가 가장 큰 순서로 sorting
    handling_strs = [handling_str for handling_str in sorted(handling_strs, key=lambda x: len(x[0]), reverse=True)]

    # m이 각각의 이어붙인 음 안에 있는지 판단
    for handling_str in handling_strs:
        if m in handling_str[0]:
            answer += handling_str[1]
            break

    if len(answer) == 0:
        answer += '(None)'
    print(answer)
    return answer