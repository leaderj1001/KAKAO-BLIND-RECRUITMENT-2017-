def convert(n, base):
    num_str = "0123456789ABCDEF"
    # n과 base를 나눈 몫과 나머지를 tuple로 return한다.
    q, r = divmod(n, base)
    if q == 0:
        return num_str[r]
    else:
        return convert(q, base) + num_str[r]


def solution(n, t, m, p):
    answer = ''

    count = 0
    current = ''
    location = 0
    number = 0
    while (count < t):
        # 이진수에서 0, 1, 10이 들어오게 되는데 10이 들어왔을 때 1, 0으로 쪼개져야 하기 때문에 string length를 보고 더 받을지 말지를 결정한다.
        if location == len(current):
            current += convert(int(number), n)
            number += 1

        if location % m == p - 1:
            count += 1
            answer += current[location]

        location += 1
    return answer