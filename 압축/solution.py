def solution(msg):
    answer = []
    dictionary = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1, 27)))

    location = 0
    while (location < len(msg)):

        word = msg[location]
        init = word
        while (word in dictionary):
            location += 1
            if location >= len(msg):
                answer.append(dictionary[init])
                break
            word += msg[location]
            if word not in dictionary:
                answer.append(dictionary[init])
            init = word

        dictionary[word] = len(dictionary) + 1

    print(answer)
    return answer