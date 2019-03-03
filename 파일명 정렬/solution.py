import re


def solution(files):
    answer = []
    p = re.compile('(\D+)(\d+)(\D+\w+.\w+|\s+\w+|)')
    # p = re.compile('(\D+)(\d+)(.*)')

    split_files = []
    for idx, file in enumerate(files):
        k = p.findall(file)
        temp = (k[0][0].lower(), int(k[0][1]), k[0][2], idx)
        split_files.append(temp)

    split_files = [file for file in sorted(split_files, key=lambda x: (x[0], x[1]))]

    for file in split_files:
        answer.append(files[file[3]])

    print(answer)
    return answer