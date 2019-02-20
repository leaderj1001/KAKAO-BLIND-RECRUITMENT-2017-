def solution(str1, str2):
    answer = 0

    list1 = []
    list2 = []

    # 대문자 소문자 관계 없다고 했기 때문에 대문자로 바꿔서 2글자씩 잘라서 넣어준다.
    for i in range(0, len(str1) - 1):
        if str1[i:i + 2].isalpha():
            word1 = str1[i:i + 2].upper()
            list1.append(word1)

    for i in range(0, len(str2) - 1):
        if str2[i:i + 2].isalpha():
            word2 = str2[i:i + 2].upper()
            list2.append(word2)

    # 첫 번째 집합에서 중복되는 원소를 뺀 후 remove_list에 append해줘서 교집합 쌍을 찾는다.
    remove_list = []
    for i in range(len(list1)):
        if list1[i] in list2:
            list2.remove(list1[i])
            remove_list.append(list1[i])

    if len(list1) + len(list2) == 0:
        answer = 65536
    else:
        answer = len(remove_list) / (len(list1) + len(list2))
        answer *= 65536

    return int(answer)
