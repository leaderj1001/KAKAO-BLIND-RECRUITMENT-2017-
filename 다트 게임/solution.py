import re


def solution(dartResult):
    answer = 0
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)

    stack = []
    for i in range(1, len(dartResult)):
        print(i, ' ', dartResult[i - 1], ' ', dartResult[i])

        if dartResult[i - 1] == '1' and dartResult[i] == '0':
            if dartResult[i + 1] == 'S':
                stack.append(10 ** 1)
            elif dartResult[i + 1] == 'D':
                stack.append(10 ** 2)
            elif dartResult[i + 1] == 'T':
                stack.append(10 ** 3)
            continue
        elif dartResult[i - 1] >= '0' and dartResult[i - 1] <= '9':
            stack.append(int(dartResult[i - 1]))

        if dartResult[i].isalpha():
            if len(stack) != 0:
                temp_num = stack.pop()
                if dartResult[i] == 'S':
                    stack.append(temp_num ** 1)
                elif dartResult[i] == 'D':
                    stack.append(temp_num ** 2)
                elif dartResult[i] == 'T':
                    stack.append(temp_num ** 3)
        print(stack)

        if dartResult[i] == '*':
            check = 0
            temp = []
            while (len(stack) > 0):
                number = (stack.pop() * 2)
                temp.append(number)
                check += 1
                if check == 2:
                    break
            while (len(temp) > 0):
                t = temp.pop()
                stack.append(t)

        elif dartResult[i] == '#':
            num = stack.pop()
            stack.append(-num)

    while (len(stack) > 0):
        answer += (stack.pop())
    print(answer)

    return answer